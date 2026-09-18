# IRON Trends


<details>
<summary>iron/operators/axpy</summary>


### test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (-12.80%)</td><td>0.04 (-5.26%)</td><td>0.04 (-4.82%)</td><td>0.03 (+6.74%)</td><td>0.00 <b>(-53.75%)</b></td><td>186.10 (-6.29%)</td><td>169.88 (+3.51%)</td><td>167.70 (+5.08%)</td><td>148.80 (+14.73%)</td><td>14.18 <b>(-51.19%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>198.60 (n/a)</td><td>164.12 (n/a)</td><td>159.60 (n/a)</td><td>129.70 (n/a)</td><td>29.05 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (-7.24%)</td><td>0.04 (-5.91%)</td><td>0.04 (-0.51%)</td><td>0.02 <b>(-25.67%)</b></td><td>0.01 (+16.33%)</td><td>247.00 <b>(+34.53%)</b></td><td>176.42 (+8.55%)</td><td>170.40 (+0.53%)</td><td>132.20 (+7.83%)</td><td>43.06 <b>(+76.53%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>183.60 (n/a)</td><td>162.52 (n/a)</td><td>169.50 (n/a)</td><td>122.60 (n/a)</td><td>24.39 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (-3.95%)</td><td>0.03 (-8.97%)</td><td>0.03 (-13.04%)</td><td>0.03 (-16.92%)</td><td>0.01 <b>(+45.77%)</b></td><td>221.80 <b>(+20.35%)</b></td><td>182.26 (+11.80%)</td><td>195.20 (+14.96%)</td><td>144.10 (+4.04%)</td><td>33.99 <b>(+78.71%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>184.30 (n/a)</td><td>163.02 (n/a)</td><td>169.80 (n/a)</td><td>138.50 (n/a)</td><td>19.02 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 <b>(+38.75%)</b></td><td>0.04 <b>(+24.18%)</b></td><td>0.04 <b>(+21.73%)</b></td><td>0.03 <b>(+23.55%)</b></td><td>0.01 <b>(+109.21%)</b></td><td>188.30 (-19.08%)</td><td>163.52 (-18.44%)</td><td>161.30 (-17.87%)</td><td>126.70 <b>(-27.89%)</b></td><td>25.52 <b>(+22.36%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>232.70 (n/a)</td><td>200.48 (n/a)</td><td>196.40 (n/a)</td><td>175.70 (n/a)</td><td>20.85 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (-18.55%)</td><td>0.03 (-17.19%)</td><td>0.03 (-9.98%)</td><td>0.02 <b>(-32.00%)</b></td><td>0.01 (+4.91%)</td><td>300.70 <b>(+47.04%)</b></td><td>220.58 <b>(+22.71%)</b></td><td>202.40 (+11.09%)</td><td>178.00 <b>(+22.76%)</b></td><td>47.91 <b>(+93.59%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>204.50 (n/a)</td><td>179.76 (n/a)</td><td>182.20 (n/a)</td><td>145.00 (n/a)</td><td>24.75 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (-12.04%)</td><td>0.04 (+3.52%)</td><td>0.04 (+5.88%)</td><td>0.03 (+7.45%)</td><td>0.00 <b>(-41.60%)</b></td><td>196.50 (-6.92%)</td><td>171.00 (-5.41%)</td><td>174.00 (-5.54%)</td><td>142.20 (+13.76%)</td><td>21.24 <b>(-36.37%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>211.10 (n/a)</td><td>180.78 (n/a)</td><td>184.20 (n/a)</td><td>125.00 (n/a)</td><td>33.37 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (+15.97%)</td><td>0.04 (+14.95%)</td><td>0.04 (+4.96%)</td><td>0.03 <b>(+26.30%)</b></td><td>0.01 (+6.06%)</td><td>218.20 <b>(-20.80%)</b></td><td>178.18 (-13.75%)</td><td>174.70 (-4.74%)</td><td>142.10 (-13.72%)</td><td>34.01 <b>(-27.62%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>275.50 (n/a)</td><td>206.58 (n/a)</td><td>183.40 (n/a)</td><td>164.70 (n/a)</td><td>46.99 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (-7.99%)</td><td>0.04 (+14.81%)</td><td>0.04 <b>(+25.51%)</b></td><td>0.03 <b>(+35.47%)</b></td><td>0.01 <b>(-44.80%)</b></td><td>198.20 <b>(-26.21%)</b></td><td>166.42 (-17.45%)</td><td>163.60 <b>(-20.31%)</b></td><td>130.40 (+8.67%)</td><td>25.09 <b>(-54.23%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>268.60 (n/a)</td><td>201.60 (n/a)</td><td>205.30 (n/a)</td><td>120.00 (n/a)</td><td>54.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.10 <b>(+21.69%)</b></td><td>0.08 (+12.24%)</td><td>0.07 (-2.83%)</td><td>0.07 <b>(+31.13%)</b></td><td>0.01 (+14.43%)</td><td>186.40 <b>(-23.73%)</b></td><td>160.48 (-11.37%)</td><td>173.80 (+2.90%)</td><td>127.70 (-17.82%)</td><td>25.95 <b>(-29.52%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>244.40 (n/a)</td><td>181.06 (n/a)</td><td>168.90 (n/a)</td><td>155.40 (n/a)</td><td>36.82 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.11 <b>(+57.67%)</b></td><td>0.08 <b>(+43.41%)</b></td><td>0.08 <b>(+28.24%)</b></td><td>0.07 <b>(+33.48%)</b></td><td>0.02 <b>(+132.50%)</b></td><td>188.90 <b>(-25.07%)</b></td><td>150.90 <b>(-28.90%)</b></td><td>154.70 <b>(-22.03%)</b></td><td>116.60 <b>(-36.56%)</b></td><td>30.04 (+8.00%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>252.10 (n/a)</td><td>212.24 (n/a)</td><td>198.40 (n/a)</td><td>183.80 (n/a)</td><td>27.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.10 (+7.53%)</td><td>0.07 (-4.12%)</td><td>0.07 (-0.09%)</td><td>0.05 <b>(-20.97%)</b></td><td>0.02 <b>(+81.11%)</b></td><td>237.20 <b>(+26.51%)</b></td><td>181.70 (+8.52%)</td><td>177.40 (+0.11%)</td><td>124.60 (-7.01%)</td><td>45.81 <b>(+118.46%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>187.50 (n/a)</td><td>167.44 (n/a)</td><td>177.20 (n/a)</td><td>134.00 (n/a)</td><td>20.97 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.08 (+11.20%)</td><td>0.07 (+3.61%)</td><td>0.07 (+1.06%)</td><td>0.06 (+9.74%)</td><td>0.01 (+7.06%)</td><td>210.10 (-8.89%)</td><td>178.62 (-3.62%)</td><td>179.80 (-1.05%)</td><td>145.30 (-10.09%)</td><td>23.04 (-14.90%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>230.60 (n/a)</td><td>185.32 (n/a)</td><td>181.70 (n/a)</td><td>161.60 (n/a)</td><td>27.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.10 (-11.05%)</td><td>0.08 (+15.01%)</td><td>0.08 <b>(+27.12%)</b></td><td>0.06 (+8.00%)</td><td>0.01 <b>(-32.31%)</b></td><td>190.30 (-7.40%)</td><td>153.62 (-15.37%)</td><td>154.50 <b>(-21.37%)</b></td><td>126.90 (+12.50%)</td><td>27.16 <b>(-29.99%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>205.50 (n/a)</td><td>181.52 (n/a)</td><td>196.50 (n/a)</td><td>112.80 (n/a)</td><td>38.80 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.09 <b>(-28.35%)</b></td><td>0.07 (-7.48%)</td><td>0.07 (+7.68%)</td><td>0.05 (+0.01%)</td><td>0.02 <b>(-43.02%)</b></td><td>250.00 (+0.00%)</td><td>182.94 (+3.29%)</td><td>168.20 (-7.17%)</td><td>140.60 <b>(+39.48%)</b></td><td>45.15 (-17.17%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>250.00 (n/a)</td><td>177.12 (n/a)</td><td>181.20 (n/a)</td><td>100.80 (n/a)</td><td>54.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.11 (+19.45%)</td><td>0.08 <b>(+21.58%)</b></td><td>0.07 <b>(+23.34%)</b></td><td>0.06 (+12.17%)</td><td>0.02 (+18.13%)</td><td>206.80 (-10.86%)</td><td>166.58 (-17.74%)</td><td>176.50 (-18.93%)</td><td>111.80 (-16.25%)</td><td>34.93 (-14.41%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>232.00 (n/a)</td><td>202.50 (n/a)</td><td>217.70 (n/a)</td><td>133.50 (n/a)</td><td>40.80 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.08 (-19.07%)</td><td>0.06 (+2.66%)</td><td>0.07 <b>(+36.82%)</b></td><td>0.04 (-18.80%)</td><td>0.02 (-10.77%)</td><td>283.70 <b>(+23.13%)</b></td><td>204.88 (-1.72%)</td><td>166.40 <b>(-26.92%)</b></td><td>161.10 <b>(+23.54%)</b></td><td>58.18 <b>(+33.16%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>230.40 (n/a)</td><td>208.46 (n/a)</td><td>227.70 (n/a)</td><td>130.40 (n/a)</td><td>43.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.20 <b>(+40.38%)</b></td><td>0.17 <b>(+28.88%)</b></td><td>0.18 <b>(+32.54%)</b></td><td>0.15 (+16.51%)</td><td>0.02 <b>(+185.02%)</b></td><td>168.80 (-14.18%)</td><td>144.16 <b>(-21.70%)</b></td><td>138.70 <b>(-24.54%)</b></td><td>123.60 <b>(-28.80%)</b></td><td>17.42 <b>(+76.26%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>196.70 (n/a)</td><td>184.12 (n/a)</td><td>183.80 (n/a)</td><td>173.60 (n/a)</td><td>9.88 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.19 (-6.02%)</td><td>0.15 (-6.12%)</td><td>0.14 (-4.97%)</td><td>0.10 (-18.44%)</td><td>0.04 <b>(+21.20%)</b></td><td>234.60 <b>(+22.63%)</b></td><td>174.20 (+8.86%)</td><td>178.60 (+5.24%)</td><td>130.50 (+6.36%)</td><td>42.90 <b>(+54.15%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>191.30 (n/a)</td><td>160.02 (n/a)</td><td>169.70 (n/a)</td><td>122.70 (n/a)</td><td>27.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.17 (+10.03%)</td><td>0.14 (+7.00%)</td><td>0.14 (+1.53%)</td><td>0.11 (+6.20%)</td><td>0.02 <b>(+29.42%)</b></td><td>216.70 (-5.82%)</td><td>175.16 (-5.96%)</td><td>179.70 (-1.48%)</td><td>141.80 (-9.10%)</td><td>29.24 (+7.65%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>230.10 (n/a)</td><td>186.26 (n/a)</td><td>182.40 (n/a)</td><td>156.00 (n/a)</td><td>27.17 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.19 <b>(+35.88%)</b></td><td>0.16 <b>(+27.22%)</b></td><td>0.16 <b>(+26.39%)</b></td><td>0.13 (+16.97%)</td><td>0.02 <b>(+59.68%)</b></td><td>188.80 (-14.53%)</td><td>154.88 <b>(-20.95%)</b></td><td>151.40 <b>(-20.90%)</b></td><td>127.60 <b>(-26.41%)</b></td><td>21.91 (+0.86%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>220.90 (n/a)</td><td>195.92 (n/a)</td><td>191.40 (n/a)</td><td>173.40 (n/a)</td><td>21.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.20 <b>(+22.62%)</b></td><td>0.16 <b>(+20.56%)</b></td><td>0.16 (+14.15%)</td><td>0.13 <b>(+30.74%)</b></td><td>0.03 (+15.92%)</td><td>191.70 <b>(-23.50%)</b></td><td>156.32 (-17.47%)</td><td>155.80 (-12.37%)</td><td>122.50 (-18.50%)</td><td>26.25 <b>(-29.90%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>250.60 (n/a)</td><td>189.42 (n/a)</td><td>177.80 (n/a)</td><td>150.30 (n/a)</td><td>37.44 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.18 (-17.93%)</td><td>0.15 (+7.70%)</td><td>0.15 (+17.43%)</td><td>0.14 <b>(+59.31%)</b></td><td>0.02 <b>(-65.77%)</b></td><td>176.90 <b>(-37.25%)</b></td><td>160.40 (-14.53%)</td><td>161.30 (-14.84%)</td><td>134.10 <b>(+21.80%)</b></td><td>16.34 <b>(-73.80%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>281.90 (n/a)</td><td>187.66 (n/a)</td><td>189.40 (n/a)</td><td>110.10 (n/a)</td><td>62.38 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.19 (+13.87%)</td><td>0.13 (+8.99%)</td><td>0.13 (+16.24%)</td><td>0.09 <b>(+22.24%)</b></td><td>0.04 (+2.20%)</td><td>288.50 (-18.18%)</td><td>200.92 (-10.17%)</td><td>191.30 (-13.98%)</td><td>130.00 (-12.16%)</td><td>60.94 <b>(-25.11%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>352.60 (n/a)</td><td>223.66 (n/a)</td><td>222.40 (n/a)</td><td>148.00 (n/a)</td><td>81.36 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.17 (-13.93%)</td><td>0.13 (+8.42%)</td><td>0.13 (+18.64%)</td><td>0.08 (+6.96%)</td><td>0.03 <b>(-23.30%)</b></td><td>289.80 (-6.49%)</td><td>196.50 (-9.98%)</td><td>184.80 (-15.73%)</td><td>147.30 (+16.17%)</td><td>57.05 (-11.91%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>309.90 (n/a)</td><td>218.28 (n/a)</td><td>219.30 (n/a)</td><td>126.80 (n/a)</td><td>64.76 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.36 <b>(+25.95%)</b></td><td>0.31 (+18.35%)</td><td>0.29 (+8.40%)</td><td>0.27 (+18.49%)</td><td>0.04 <b>(+89.83%)</b></td><td>182.50 (-15.63%)</td><td>159.36 (-14.75%)</td><td>167.00 (-7.79%)</td><td>135.60 <b>(-20.61%)</b></td><td>22.02 <b>(+23.08%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.02 (n/a)</td><td>216.30 (n/a)</td><td>186.94 (n/a)</td><td>181.10 (n/a)</td><td>170.80 (n/a)</td><td>17.89 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.44 <b>(+45.29%)</b></td><td>0.34 <b>(+25.24%)</b></td><td>0.31 (+12.16%)</td><td>0.24 (+1.14%)</td><td>0.08 <b>(+230.57%)</b></td><td>206.60 (-1.10%)</td><td>152.10 (-16.64%)</td><td>156.70 (-10.81%)</td><td>112.20 <b>(-31.21%)</b></td><td>38.41 <b>(+116.91%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.03 (n/a)</td><td>208.90 (n/a)</td><td>182.46 (n/a)</td><td>175.70 (n/a)</td><td>163.10 (n/a)</td><td>17.71 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.34 (+10.88%)</td><td>0.32 (+11.70%)</td><td>0.33 (+9.58%)</td><td>0.27 <b>(+24.03%)</b></td><td>0.03 <b>(-24.16%)</b></td><td>180.10 (-19.35%)</td><td>156.02 (-11.28%)</td><td>150.80 (-8.77%)</td><td>144.40 (-9.81%)</td><td>14.56 <b>(-45.48%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>223.30 (n/a)</td><td>175.86 (n/a)</td><td>165.30 (n/a)</td><td>160.10 (n/a)</td><td>26.70 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.31 (-6.03%)</td><td>0.28 (-3.97%)</td><td>0.27 (-5.67%)</td><td>0.24 (-9.18%)</td><td>0.03 (+3.07%)</td><td>207.50 (+10.08%)</td><td>179.50 (+4.31%)</td><td>182.80 (+6.03%)</td><td>158.80 (+6.43%)</td><td>19.92 (+17.07%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.33 (n/a)</td><td>0.29 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.03 (n/a)</td><td>188.50 (n/a)</td><td>172.08 (n/a)</td><td>172.40 (n/a)</td><td>149.20 (n/a)</td><td>17.01 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.32 (+4.48%)</td><td>0.25 (+9.79%)</td><td>0.27 (+3.98%)</td><td>0.17 <b>(+35.59%)</b></td><td>0.06 (-12.36%)</td><td>282.70 <b>(-26.25%)</b></td><td>206.90 (-12.73%)</td><td>180.70 (-3.83%)</td><td>156.00 (-4.29%)</td><td>55.63 <b>(-38.69%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.26 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>383.30 (n/a)</td><td>237.08 (n/a)</td><td>187.90 (n/a)</td><td>163.00 (n/a)</td><td>90.73 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.27 <b>(-23.91%)</b></td><td>0.20 <b>(-28.03%)</b></td><td>0.20 <b>(-26.52%)</b></td><td>0.13 <b>(-40.39%)</b></td><td>0.05 (-7.72%)</td><td>380.00 <b>(+67.77%)</b></td><td>260.82 <b>(+42.51%)</b></td><td>250.70 <b>(+36.10%)</b></td><td>185.30 <b>(+31.42%)</b></td><td>72.32 <b>(+111.56%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.35 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.05 (n/a)</td><td>226.50 (n/a)</td><td>183.02 (n/a)</td><td>184.20 (n/a)</td><td>141.00 (n/a)</td><td>34.18 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.35 <b>(+30.10%)</b></td><td>0.26 (+6.17%)</td><td>0.26 (+9.26%)</td><td>0.15 <b>(-33.69%)</b></td><td>0.08 <b>(+442.17%)</b></td><td>317.40 <b>(+50.78%)</b></td><td>205.14 (+2.51%)</td><td>187.90 (-8.52%)</td><td>139.40 <b>(-23.15%)</b></td><td>71.92 <b>(+528.67%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.01 (n/a)</td><td>210.50 (n/a)</td><td>200.12 (n/a)</td><td>205.40 (n/a)</td><td>181.40 (n/a)</td><td>11.44 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.35 <b>(+23.01%)</b></td><td>0.29 <b>(+32.03%)</b></td><td>0.28 <b>(+34.47%)</b></td><td>0.26 <b>(+45.82%)</b></td><td>0.04 (-8.72%)</td><td>190.00 <b>(-31.41%)</b></td><td>170.88 <b>(-25.25%)</b></td><td>172.80 <b>(-25.65%)</b></td><td>140.30 (-18.71%)</td><td>20.16 <b>(-48.11%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>277.00 (n/a)</td><td>228.60 (n/a)</td><td>232.40 (n/a)</td><td>172.60 (n/a)</td><td>38.85 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/dequant</summary>


### test_dequant[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.02 (-14.58%)</td><td>0.02 (-1.45%)</td><td>0.01 (-5.56%)</td><td>0.01 <b>(+26.83%)</b></td><td>0.00 <b>(-49.28%)</b></td><td>188.80 <b>(-21.14%)</b></td><td>170.20 (-1.97%)</td><td>177.20 (+5.85%)</td><td>142.30 (+17.12%)</td><td>19.75 <b>(-53.23%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>239.40 (n/a)</td><td>173.62 (n/a)</td><td>167.40 (n/a)</td><td>121.50 (n/a)</td><td>42.22 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.02 (+7.61%)</td><td>0.02 (+3.38%)</td><td>0.02 (+12.01%)</td><td>0.01 <b>(-33.97%)</b></td><td>0.01 <b>(+60.22%)</b></td><td>321.80 <b>(+51.44%)</b></td><td>180.96 (+5.34%)</td><td>157.80 (-10.70%)</td><td>119.20 (-7.09%)</td><td>81.33 <b>(+139.91%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>212.50 (n/a)</td><td>171.78 (n/a)</td><td>176.70 (n/a)</td><td>128.30 (n/a)</td><td>33.90 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.02 (+0.11%)</td><td>0.02 (+12.35%)</td><td>0.02 <b>(+28.83%)</b></td><td>0.01 (+2.36%)</td><td>0.00 (+7.02%)</td><td>188.20 (-2.34%)</td><td>144.62 (-10.70%)</td><td>135.00 <b>(-22.37%)</b></td><td>118.60 (-0.08%)</td><td>30.16 (+3.57%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>192.70 (n/a)</td><td>161.94 (n/a)</td><td>173.90 (n/a)</td><td>118.70 (n/a)</td><td>29.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.02 (+18.96%)</td><td>0.02 (+4.17%)</td><td>0.01 (-9.66%)</td><td>0.01 (-4.04%)</td><td>0.01 <b>(+44.34%)</b></td><td>228.70 (+4.24%)</td><td>173.28 (-0.71%)</td><td>196.40 (+10.65%)</td><td>108.80 (-15.92%)</td><td>50.08 <b>(+25.53%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>219.40 (n/a)</td><td>174.52 (n/a)</td><td>177.50 (n/a)</td><td>129.40 (n/a)</td><td>39.90 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.02 (+5.98%)</td><td>0.02 (-0.59%)</td><td>0.01 (-17.37%)</td><td>0.01 <b>(+27.78%)</b></td><td>0.00 <b>(-24.74%)</b></td><td>201.10 <b>(-21.72%)</b></td><td>175.12 (-2.69%)</td><td>185.40 <b>(+21.02%)</b></td><td>129.60 (-5.68%)</td><td>27.88 <b>(-45.36%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>256.90 (n/a)</td><td>179.96 (n/a)</td><td>153.20 (n/a)</td><td>137.40 (n/a)</td><td>51.03 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.02 (+6.43%)</td><td>0.02 (+8.30%)</td><td>0.02 (+1.91%)</td><td>0.01 <b>(+23.49%)</b></td><td>0.00 <b>(-22.25%)</b></td><td>190.30 (-19.02%)</td><td>167.08 (-9.62%)</td><td>172.80 (-1.87%)</td><td>130.00 (-6.07%)</td><td>23.21 <b>(-42.85%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>235.00 (n/a)</td><td>184.86 (n/a)</td><td>176.10 (n/a)</td><td>138.40 (n/a)</td><td>40.62 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.02 <b>(+32.24%)</b></td><td>0.01 (-6.34%)</td><td>0.01 (-19.39%)</td><td>0.01 <b>(-28.26%)</b></td><td>0.01 <b>(+238.27%)</b></td><td>287.70 <b>(+39.39%)</b></td><td>221.02 (+16.51%)</td><td>244.40 <b>(+24.06%)</b></td><td>120.70 <b>(-24.37%)</b></td><td>66.03 <b>(+248.13%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>206.40 (n/a)</td><td>189.70 (n/a)</td><td>197.00 (n/a)</td><td>159.60 (n/a)</td><td>18.97 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.01 (-7.18%)</td><td>0.01 (+0.30%)</td><td>0.01 (+0.34%)</td><td>0.01 (+8.30%)</td><td>0.00 <b>(-40.94%)</b></td><td>234.20 (-7.65%)</td><td>211.86 (-1.17%)</td><td>212.40 (-0.38%)</td><td>189.80 (+7.72%)</td><td>16.20 <b>(-40.89%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>253.60 (n/a)</td><td>214.36 (n/a)</td><td>213.20 (n/a)</td><td>176.20 (n/a)</td><td>27.41 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (-2.32%)</td><td>0.04 <b>(+21.91%)</b></td><td>0.04 <b>(+31.68%)</b></td><td>0.04 <b>(+28.79%)</b></td><td>0.00 <b>(-63.09%)</b></td><td>149.60 <b>(-22.33%)</b></td><td>140.00 (-19.69%)</td><td>143.30 <b>(-24.02%)</b></td><td>131.20 (+2.34%)</td><td>7.98 <b>(-70.78%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>192.60 (n/a)</td><td>174.32 (n/a)</td><td>188.60 (n/a)</td><td>128.20 (n/a)</td><td>27.32 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (-2.08%)</td><td>0.04 (+15.32%)</td><td>0.04 (+16.70%)</td><td>0.03 <b>(+66.31%)</b></td><td>0.00 <b>(-62.35%)</b></td><td>163.30 <b>(-39.87%)</b></td><td>143.96 (-19.67%)</td><td>148.10 (-14.29%)</td><td>127.90 (+2.16%)</td><td>14.53 <b>(-76.07%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>271.60 (n/a)</td><td>179.22 (n/a)</td><td>172.80 (n/a)</td><td>125.20 (n/a)</td><td>60.69 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (-1.94%)</td><td>0.03 (+15.21%)</td><td>0.04 <b>(+35.46%)</b></td><td>0.03 <b>(+59.63%)</b></td><td>0.00 <b>(-49.42%)</b></td><td>188.00 <b>(-37.35%)</b></td><td>156.26 (-19.72%)</td><td>147.40 <b>(-26.19%)</b></td><td>130.00 (+1.96%)</td><td>23.32 <b>(-66.26%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>300.10 (n/a)</td><td>194.64 (n/a)</td><td>199.70 (n/a)</td><td>127.50 (n/a)</td><td>69.12 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (+12.47%)</td><td>0.03 (+4.50%)</td><td>0.03 (+2.32%)</td><td>0.03 <b>(+23.77%)</b></td><td>0.01 (-11.66%)</td><td>172.80 (-19.18%)</td><td>153.14 (-5.55%)</td><td>159.30 (-2.27%)</td><td>118.60 (-11.09%)</td><td>20.64 <b>(-37.10%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>213.80 (n/a)</td><td>162.14 (n/a)</td><td>163.00 (n/a)</td><td>133.40 (n/a)</td><td>32.81 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 <b>(+21.01%)</b></td><td>0.04 (+18.28%)</td><td>0.04 (+9.43%)</td><td>0.03 <b>(+30.46%)</b></td><td>0.01 (-2.99%)</td><td>167.80 <b>(-23.34%)</b></td><td>142.42 (-17.23%)</td><td>149.90 (-8.60%)</td><td>104.20 (-17.37%)</td><td>25.59 <b>(-40.57%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>218.90 (n/a)</td><td>172.06 (n/a)</td><td>164.00 (n/a)</td><td>126.10 (n/a)</td><td>43.06 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (+14.68%)</td><td>0.03 (+0.33%)</td><td>0.03 (-13.28%)</td><td>0.02 (+2.83%)</td><td>0.01 <b>(+49.86%)</b></td><td>212.60 (-2.79%)</td><td>174.74 (+0.97%)</td><td>184.30 (+15.33%)</td><td>136.30 (-12.80%)</td><td>32.25 <b>(+23.35%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.70 (n/a)</td><td>173.06 (n/a)</td><td>159.80 (n/a)</td><td>156.30 (n/a)</td><td>26.15 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (-6.49%)</td><td>0.03 (+7.66%)</td><td>0.03 (+12.65%)</td><td>0.03 (+4.20%)</td><td>0.01 <b>(-26.49%)</b></td><td>190.80 (-4.02%)</td><td>154.14 (-8.39%)</td><td>153.30 (-11.23%)</td><td>127.50 (+6.96%)</td><td>24.08 <b>(-22.74%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>198.80 (n/a)</td><td>168.26 (n/a)</td><td>172.70 (n/a)</td><td>119.20 (n/a)</td><td>31.16 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (-1.60%)</td><td>0.03 (-8.72%)</td><td>0.03 (-7.63%)</td><td>0.02 (-7.64%)</td><td>0.00 <b>(+27.16%)</b></td><td>240.20 (+8.30%)</td><td>210.06 (+10.19%)</td><td>204.60 (+8.25%)</td><td>171.30 (+1.60%)</td><td>26.80 <b>(+37.84%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.80 (n/a)</td><td>190.64 (n/a)</td><td>189.00 (n/a)</td><td>168.60 (n/a)</td><td>19.44 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.08 (-3.05%)</td><td>0.07 (-1.91%)</td><td>0.06 (-11.10%)</td><td>0.06 (+18.01%)</td><td>0.01 (-17.53%)</td><td>190.30 (-15.23%)</td><td>159.00 (-0.10%)</td><td>168.60 (+12.47%)</td><td>126.00 (+3.19%)</td><td>30.64 <b>(-28.02%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>224.50 (n/a)</td><td>159.16 (n/a)</td><td>149.90 (n/a)</td><td>122.10 (n/a)</td><td>42.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.10 (+8.73%)</td><td>0.07 (+1.00%)</td><td>0.06 (+3.35%)</td><td>0.05 <b>(-22.15%)</b></td><td>0.02 <b>(+55.12%)</b></td><td>226.10 <b>(+28.47%)</b></td><td>163.18 (+2.60%)</td><td>164.40 (-3.24%)</td><td>109.80 (-8.04%)</td><td>42.92 <b>(+85.03%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>176.00 (n/a)</td><td>159.04 (n/a)</td><td>169.90 (n/a)</td><td>119.40 (n/a)</td><td>23.19 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.09 (-2.84%)</td><td>0.06 (-12.41%)</td><td>0.06 <b>(-20.64%)</b></td><td>0.05 (-9.25%)</td><td>0.01 (+18.20%)</td><td>207.90 (+10.23%)</td><td>176.44 (+15.52%)</td><td>189.40 <b>(+26.01%)</b></td><td>122.90 (+2.93%)</td><td>32.57 <b>(+29.93%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>188.60 (n/a)</td><td>152.74 (n/a)</td><td>150.30 (n/a)</td><td>119.40 (n/a)</td><td>25.06 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.08 (+12.87%)</td><td>0.07 (+10.01%)</td><td>0.06 (+0.29%)</td><td>0.05 <b>(+24.55%)</b></td><td>0.01 (+6.15%)</td><td>208.90 (-19.72%)</td><td>165.56 (-9.95%)</td><td>168.80 (-0.30%)</td><td>129.70 (-11.41%)</td><td>34.09 <b>(-26.72%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>260.20 (n/a)</td><td>183.86 (n/a)</td><td>169.30 (n/a)</td><td>146.40 (n/a)</td><td>46.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.08 (-14.79%)</td><td>0.06 (-9.07%)</td><td>0.07 (-1.37%)</td><td>0.05 (+5.78%)</td><td>0.01 <b>(-31.45%)</b></td><td>199.90 (-5.44%)</td><td>166.82 (+7.83%)</td><td>156.20 (+1.43%)</td><td>134.40 (+17.38%)</td><td>29.09 <b>(-21.80%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>211.40 (n/a)</td><td>154.70 (n/a)</td><td>154.00 (n/a)</td><td>114.50 (n/a)</td><td>37.20 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.09 (+16.22%)</td><td>0.06 (-7.70%)</td><td>0.06 (-15.87%)</td><td>0.04 <b>(-36.95%)</b></td><td>0.02 <b>(+141.17%)</b></td><td>284.00 <b>(+58.57%)</b></td><td>182.82 (+16.59%)</td><td>179.50 (+18.87%)</td><td>114.90 (-14.00%)</td><td>62.50 <b>(+232.09%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>179.10 (n/a)</td><td>156.80 (n/a)</td><td>151.00 (n/a)</td><td>133.60 (n/a)</td><td>18.82 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 (-1.66%)</td><td>0.06 (-10.76%)</td><td>0.07 (-8.73%)</td><td>0.04 <b>(-30.46%)</b></td><td>0.01 <b>(+131.71%)</b></td><td>239.50 <b>(+43.76%)</b></td><td>173.32 (+15.56%)</td><td>159.30 (+9.56%)</td><td>142.70 (+1.71%)</td><td>39.60 <b>(+243.59%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>166.60 (n/a)</td><td>149.98 (n/a)</td><td>145.40 (n/a)</td><td>140.30 (n/a)</td><td>11.53 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (-0.26%)</td><td>0.06 (-1.24%)</td><td>0.06 (+0.46%)</td><td>0.04 (-9.23%)</td><td>0.01 <b>(+29.90%)</b></td><td>251.30 (+10.17%)</td><td>194.10 (+2.21%)</td><td>187.60 (-0.48%)</td><td>168.60 (+0.24%)</td><td>33.30 <b>(+44.08%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>228.10 (n/a)</td><td>189.90 (n/a)</td><td>188.50 (n/a)</td><td>168.20 (n/a)</td><td>23.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.14 (-12.52%)</td><td>0.12 (-14.51%)</td><td>0.12 (-19.95%)</td><td>0.10 (-13.62%)</td><td>0.02 (-13.01%)</td><td>205.00 (+15.75%)</td><td>176.98 (+16.93%)</td><td>182.50 <b>(+24.91%)</b></td><td>147.50 (+14.25%)</td><td>23.46 (+13.50%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>177.10 (n/a)</td><td>151.36 (n/a)</td><td>146.10 (n/a)</td><td>129.10 (n/a)</td><td>20.67 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.15 (-1.27%)</td><td>0.12 (-2.96%)</td><td>0.12 (+6.10%)</td><td>0.10 (-3.71%)</td><td>0.02 (-17.59%)</td><td>211.90 (+3.87%)</td><td>178.18 (+2.13%)</td><td>180.40 (-5.75%)</td><td>136.90 (+1.26%)</td><td>27.13 (-15.43%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>204.00 (n/a)</td><td>174.46 (n/a)</td><td>191.40 (n/a)</td><td>135.20 (n/a)</td><td>32.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.13 <b>(-26.87%)</b></td><td>0.12 (-15.16%)</td><td>0.12 (-9.05%)</td><td>0.09 (-9.60%)</td><td>0.02 <b>(-50.00%)</b></td><td>232.50 (+10.61%)</td><td>181.50 (+14.53%)</td><td>171.70 (+9.92%)</td><td>158.50 <b>(+36.76%)</b></td><td>29.90 <b>(-22.46%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>210.20 (n/a)</td><td>158.48 (n/a)</td><td>156.20 (n/a)</td><td>115.90 (n/a)</td><td>38.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.14 (+18.87%)</td><td>0.11 (+12.92%)</td><td>0.11 (+9.54%)</td><td>0.10 <b>(+23.73%)</b></td><td>0.01 (+7.09%)</td><td>210.70 (-19.18%)</td><td>188.06 (-11.74%)</td><td>192.30 (-8.73%)</td><td>155.50 (-15.85%)</td><td>20.12 <b>(-30.39%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>260.70 (n/a)</td><td>213.08 (n/a)</td><td>210.70 (n/a)</td><td>184.80 (n/a)</td><td>28.90 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.15 (-1.34%)</td><td>0.11 (-9.08%)</td><td>0.11 (-14.73%)</td><td>0.08 <b>(-24.24%)</b></td><td>0.03 <b>(+48.66%)</b></td><td>273.10 <b>(+32.00%)</b></td><td>199.24 (+15.34%)</td><td>195.50 (+17.28%)</td><td>136.40 (+1.34%)</td><td>60.09 <b>(+90.43%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>206.90 (n/a)</td><td>172.74 (n/a)</td><td>166.70 (n/a)</td><td>134.60 (n/a)</td><td>31.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.13 <b>(-24.58%)</b></td><td>0.12 (-13.02%)</td><td>0.12 (-8.67%)</td><td>0.09 (+3.48%)</td><td>0.02 <b>(-36.50%)</b></td><td>223.20 (-3.38%)</td><td>184.88 (+12.48%)</td><td>171.00 (+9.55%)</td><td>155.90 <b>(+32.57%)</b></td><td>32.90 <b>(-20.25%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>231.00 (n/a)</td><td>164.36 (n/a)</td><td>156.10 (n/a)</td><td>117.60 (n/a)</td><td>41.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.19 <b>(+58.92%)</b></td><td>0.13 <b>(+22.59%)</b></td><td>0.12 (+5.69%)</td><td>0.11 <b>(+51.20%)</b></td><td>0.03 <b>(+64.66%)</b></td><td>199.20 <b>(-33.86%)</b></td><td>168.28 (-18.23%)</td><td>173.20 (-5.36%)</td><td>109.50 <b>(-37.11%)</b></td><td>34.83 <b>(-35.53%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>301.20 (n/a)</td><td>205.80 (n/a)</td><td>183.00 (n/a)</td><td>174.10 (n/a)</td><td>54.02 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.12 (+14.80%)</td><td>0.10 (+10.90%)</td><td>0.10 (+6.81%)</td><td>0.09 <b>(+31.36%)</b></td><td>0.01 (-18.46%)</td><td>234.80 <b>(-23.87%)</b></td><td>210.40 (-11.02%)</td><td>210.20 (-6.37%)</td><td>174.50 (-12.88%)</td><td>22.68 <b>(-47.54%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>308.40 (n/a)</td><td>236.46 (n/a)</td><td>224.50 (n/a)</td><td>200.30 (n/a)</td><td>43.24 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/elementwise_add</summary>


### test_elementwise_add[input_length_1024-num_aie_columns_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>190.20 (n/a)</td><td>145.56 (n/a)</td><td>135.70 (n/a)</td><td>106.30 (n/a)</td><td>31.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_1024-num_aie_columns_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>172.30 (n/a)</td><td>154.42 (n/a)</td><td>149.70 (n/a)</td><td>142.10 (n/a)</td><td>12.14 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_1024-num_aie_columns_4-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>256.60 (n/a)</td><td>189.90 (n/a)</td><td>191.00 (n/a)</td><td>150.40 (n/a)</td><td>42.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_1024-num_aie_columns_8-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>207.70 (n/a)</td><td>185.96 (n/a)</td><td>182.90 (n/a)</td><td>173.40 (n/a)</td><td>12.85 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>220.50 (n/a)</td><td>166.30 (n/a)</td><td>165.70 (n/a)</td><td>118.50 (n/a)</td><td>43.73 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>172.80 (n/a)</td><td>146.06 (n/a)</td><td>146.20 (n/a)</td><td>112.10 (n/a)</td><td>22.15 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>211.50 (n/a)</td><td>169.10 (n/a)</td><td>155.60 (n/a)</td><td>138.80 (n/a)</td><td>33.05 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>184.10 (n/a)</td><td>152.86 (n/a)</td><td>152.20 (n/a)</td><td>132.50 (n/a)</td><td>21.53 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_4096-num_aie_columns_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>182.30 (n/a)</td><td>155.00 (n/a)</td><td>157.70 (n/a)</td><td>116.20 (n/a)</td><td>25.79 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_4096-num_aie_columns_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>245.40 (n/a)</td><td>180.34 (n/a)</td><td>193.00 (n/a)</td><td>125.90 (n/a)</td><td>47.16 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_4096-num_aie_columns_4-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>228.40 (n/a)</td><td>168.92 (n/a)</td><td>175.40 (n/a)</td><td>123.00 (n/a)</td><td>44.30 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_4096-num_aie_columns_8-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>213.20 (n/a)</td><td>187.72 (n/a)</td><td>186.40 (n/a)</td><td>167.20 (n/a)</td><td>17.54 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_8192-num_aie_columns_1-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.37 (+3.78%)</td><td>0.30 (+0.98%)</td><td>0.30 (-6.60%)</td><td>0.24 (+3.78%)</td><td>0.06 <b>(+24.26%)</b></td><td>208.10 (-3.66%)</td><td>167.46 (-0.02%)</td><td>166.00 (+7.10%)</td><td>133.30 (-3.68%)</td><td>34.68 (+11.52%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.36 (n/a)</td><td>0.30 (n/a)</td><td>0.32 (n/a)</td><td>0.23 (n/a)</td><td>0.05 (n/a)</td><td>216.00 (n/a)</td><td>167.50 (n/a)</td><td>155.00 (n/a)</td><td>138.40 (n/a)</td><td>31.10 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_8192-num_aie_columns_2-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.02 (n/a)</td><td>191.50 (n/a)</td><td>175.72 (n/a)</td><td>171.80 (n/a)</td><td>167.00 (n/a)</td><td>10.54 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_8192-num_aie_columns_4-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.41 (n/a)</td><td>0.32 (n/a)</td><td>0.33 (n/a)</td><td>0.24 (n/a)</td><td>0.06 (n/a)</td><td>206.70 (n/a)</td><td>158.92 (n/a)</td><td>149.10 (n/a)</td><td>121.00 (n/a)</td><td>31.76 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_8192-num_aie_columns_8-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>223.20 (n/a)</td><td>192.74 (n/a)</td><td>192.70 (n/a)</td><td>149.60 (n/a)</td><td>28.71 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/elementwise_mul</summary>


### test_elementwise_mul[input_length_1024-num_aie_columns_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>193.50 (n/a)</td><td>165.68 (n/a)</td><td>162.80 (n/a)</td><td>129.70 (n/a)</td><td>24.53 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_1024-num_aie_columns_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>193.30 (n/a)</td><td>150.58 (n/a)</td><td>146.60 (n/a)</td><td>114.30 (n/a)</td><td>28.75 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_1024-num_aie_columns_4-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>215.70 (n/a)</td><td>194.96 (n/a)</td><td>189.00 (n/a)</td><td>178.50 (n/a)</td><td>17.54 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_1024-num_aie_columns_8-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>286.20 (n/a)</td><td>209.02 (n/a)</td><td>195.20 (n/a)</td><td>166.90 (n/a)</td><td>49.11 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>197.30 (n/a)</td><td>168.80 (n/a)</td><td>172.80 (n/a)</td><td>146.80 (n/a)</td><td>20.39 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>196.00 (n/a)</td><td>171.20 (n/a)</td><td>183.10 (n/a)</td><td>129.20 (n/a)</td><td>28.65 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>228.10 (n/a)</td><td>183.48 (n/a)</td><td>177.00 (n/a)</td><td>155.10 (n/a)</td><td>31.08 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>216.70 (n/a)</td><td>200.06 (n/a)</td><td>205.50 (n/a)</td><td>179.80 (n/a)</td><td>14.28 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_4096-num_aie_columns_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>209.20 (n/a)</td><td>172.74 (n/a)</td><td>182.70 (n/a)</td><td>134.10 (n/a)</td><td>32.35 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_4096-num_aie_columns_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>191.60 (n/a)</td><td>162.08 (n/a)</td><td>166.00 (n/a)</td><td>126.40 (n/a)</td><td>26.47 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_4096-num_aie_columns_4-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>222.10 (n/a)</td><td>178.14 (n/a)</td><td>176.10 (n/a)</td><td>139.80 (n/a)</td><td>29.33 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_4096-num_aie_columns_8-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>312.70 (n/a)</td><td>219.58 (n/a)</td><td>195.60 (n/a)</td><td>178.50 (n/a)</td><td>54.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_8192-num_aie_columns_2-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.38 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.06 (n/a)</td><td>219.70 (n/a)</td><td>173.30 (n/a)</td><td>156.80 (n/a)</td><td>130.90 (n/a)</td><td>38.96 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_8192-num_aie_columns_4-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.37 (n/a)</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.06 (n/a)</td><td>192.60 (n/a)</td><td>164.02 (n/a)</td><td>173.10 (n/a)</td><td>134.00 (n/a)</td><td>28.16 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_8192-num_aie_columns_8-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>224.50 (n/a)</td><td>193.58 (n/a)</td><td>186.90 (n/a)</td><td>165.80 (n/a)</td><td>23.46 (n/a)</td>
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


### test_gemm[M_1024-K_10240-N_2560-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>15.36 (+4.82%)</td><td>14.31 (+1.77%)</td><td>14.39 (+0.60%)</td><td>13.04 (-1.57%)</td><td>0.83 <b>(+45.49%)</b></td><td>4270.80 (+1.59%)</td><td>3904.76 (-1.60%)</td><td>3870.40 (-0.60%)</td><td>3626.30 (-4.60%)</td><td>231.43 <b>(+41.95%)</b></td><td>14804.78 (+4.82%)</td><td>13786.70 (+1.77%)</td><td>13871.06 (+0.60%)</td><td>12570.64 (-1.57%)</td><td>795.37 <b>(+45.49%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>14.66 (n/a)</td><td>14.06 (n/a)</td><td>14.31 (n/a)</td><td>13.25 (n/a)</td><td>0.57 (n/a)</td><td>4203.80 (n/a)</td><td>3968.22 (n/a)</td><td>3893.70 (n/a)</td><td>3801.00 (n/a)</td><td>163.04 (n/a)</td><td>14124.61 (n/a)</td><td>13547.26 (n/a)</td><td>13788.20 (n/a)</td><td>12771.06 (n/a)</td><td>546.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_1024-K_2048-N_2048-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>14.66 (-10.58%)</td><td>12.93 (-6.85%)</td><td>13.21 (-10.09%)</td><td>9.79 (+8.49%)</td><td>1.86 <b>(-33.99%)</b></td><td>1339.00 (-7.83%)</td><td>1034.08 (+4.76%)</td><td>992.20 (+11.23%)</td><td>893.90 (+11.84%)</td><td>175.60 <b>(-33.38%)</b></td><td>9609.80 (-10.58%)</td><td>8471.71 (-6.85%)</td><td>8657.82 (-10.09%)</td><td>6415.14 (+8.49%)</td><td>1218.99 <b>(-33.99%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>16.40 (n/a)</td><td>13.88 (n/a)</td><td>14.69 (n/a)</td><td>9.02 (n/a)</td><td>2.82 (n/a)</td><td>1452.70 (n/a)</td><td>987.08 (n/a)</td><td>892.00 (n/a)</td><td>799.30 (n/a)</td><td>263.58 (n/a)</td><td>10747.08 (n/a)</td><td>9094.27 (n/a)</td><td>9629.90 (n/a)</td><td>5912.98 (n/a)</td><td>1846.80 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_1024-K_2560-N_10240-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>14.24 (+1.23%)</td><td>13.88 (+4.35%)</td><td>13.97 (+8.12%)</td><td>13.52 (+6.12%)</td><td>0.29 <b>(-52.41%)</b></td><td>4119.40 (-5.77%)</td><td>4014.00 (-4.30%)</td><td>3986.30 (-7.51%)</td><td>3913.00 (-1.21%)</td><td>84.37 <b>(-55.53%)</b></td><td>13720.26 (+1.23%)</td><td>13379.72 (+4.35%)</td><td>13467.90 (+8.12%)</td><td>13032.89 (+6.12%)</td><td>280.51 <b>(-52.41%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>14.06 (n/a)</td><td>13.30 (n/a)</td><td>12.92 (n/a)</td><td>12.74 (n/a)</td><td>0.61 (n/a)</td><td>4371.50 (n/a)</td><td>4194.14 (n/a)</td><td>4310.00 (n/a)</td><td>3961.10 (n/a)</td><td>189.74 (n/a)</td><td>13553.42 (n/a)</td><td>12821.77 (n/a)</td><td>12456.43 (n/a)</td><td>12281.06 (n/a)</td><td>589.43 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_1024-K_2560-N_2560-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>15.57 (-0.97%)</td><td>13.26 (-13.19%)</td><td>13.45 (-11.98%)</td><td>11.30 <b>(-24.24%)</b></td><td>1.93 <b>(+544.79%)</b></td><td>1580.00 <b>(+32.01%)</b></td><td>1370.42 (+17.15%)</td><td>1328.10 (+13.61%)</td><td>1147.30 (+0.98%)</td><td>201.00 <b>(+783.48%)</b></td><td>11698.42 (-0.97%)</td><td>9963.57 (-13.19%)</td><td>10106.01 (-11.98%)</td><td>8494.75 <b>(-24.24%)</b></td><td>1450.37 <b>(+544.79%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>15.72 (n/a)</td><td>15.27 (n/a)</td><td>15.28 (n/a)</td><td>14.92 (n/a)</td><td>0.30 (n/a)</td><td>1196.90 (n/a)</td><td>1169.78 (n/a)</td><td>1169.00 (n/a)</td><td>1136.20 (n/a)</td><td>22.75 (n/a)</td><td>11812.74 (n/a)</td><td>11477.25 (n/a)</td><td>11481.67 (n/a)</td><td>11213.34 (n/a)</td><td>224.94 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_10240-N_2560-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>11.26 (+5.30%)</td><td>10.84 (+3.02%)</td><td>10.73 (+1.57%)</td><td>10.50 (+2.10%)</td><td>0.33 <b>(+97.88%)</b></td><td>7798.80 (-2.06%)</td><td>7559.92 (-2.88%)</td><td>7634.40 (-1.55%)</td><td>7276.50 (-5.03%)</td><td>227.80 <b>(+83.86%)</b></td><td>14756.25 (+5.30%)</td><td>14213.48 (+3.02%)</td><td>14064.46 (+1.57%)</td><td>13768.02 (+2.10%)</td><td>431.62 <b>(+97.88%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>10.69 (n/a)</td><td>10.53 (n/a)</td><td>10.56 (n/a)</td><td>10.29 (n/a)</td><td>0.17 (n/a)</td><td>7962.80 (n/a)</td><td>7783.86 (n/a)</td><td>7754.30 (n/a)</td><td>7662.00 (n/a)</td><td>123.90 (n/a)</td><td>14013.79 (n/a)</td><td>13797.24 (n/a)</td><td>13847.08 (n/a)</td><td>13484.44 (n/a)</td><td>218.13 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_2048-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>15.25 (-3.28%)</td><td>12.67 (-13.87%)</td><td>11.13 <b>(-22.47%)</b></td><td>10.98 <b>(-20.85%)</b></td><td>2.23 <b>(+191.52%)</b></td><td>1957.40 <b>(+26.35%)</b></td><td>1737.18 (+18.60%)</td><td>1932.10 <b>(+28.98%)</b></td><td>1409.10 (+3.39%)</td><td>286.68 <b>(+283.78%)</b></td><td>12191.97 (-3.28%)</td><td>10124.35 (-13.87%)</td><td>8891.63 <b>(-22.47%)</b></td><td>8776.76 <b>(-20.85%)</b></td><td>1778.80 <b>(+191.52%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>15.77 (n/a)</td><td>14.71 (n/a)</td><td>14.35 (n/a)</td><td>13.88 (n/a)</td><td>0.76 (n/a)</td><td>1549.20 (n/a)</td><td>1464.70 (n/a)</td><td>1498.00 (n/a)</td><td>1362.90 (n/a)</td><td>74.70 (n/a)</td><td>12605.81 (n/a)</td><td>11754.11 (n/a)</td><td>11468.31 (n/a)</td><td>11089.24 (n/a)</td><td>610.18 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2560-N_10240-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>10.90 (-0.48%)</td><td>10.54 (-1.61%)</td><td>10.43 (-2.92%)</td><td>10.39 (+0.15%)</td><td>0.22 (-15.29%)</td><td>7886.10 (-0.15%)</td><td>7775.24 (+1.62%)</td><td>7850.80 (+3.01%)</td><td>7515.70 (+0.48%)</td><td>157.08 (-14.71%)</td><td>14286.69 (-0.48%)</td><td>13814.38 (-1.61%)</td><td>13676.78 (-2.92%)</td><td>13615.70 (+0.15%)</td><td>284.50 (-15.29%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>10.95 (n/a)</td><td>10.71 (n/a)</td><td>10.75 (n/a)</td><td>10.37 (n/a)</td><td>0.26 (n/a)</td><td>7897.80 (n/a)</td><td>7650.96 (n/a)</td><td>7621.60 (n/a)</td><td>7480.00 (n/a)</td><td>184.17 (n/a)</td><td>14354.93 (n/a)</td><td>14040.57 (n/a)</td><td>14088.14 (n/a)</td><td>13595.41 (n/a)</td><td>335.85 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>3.59 (-6.23%)</td><td>3.12 (-0.97%)</td><td>3.05 (-0.93%)</td><td>2.74 (-0.14%)</td><td>0.31 <b>(-28.92%)</b></td><td>502.10 (+0.14%)</td><td>444.16 (+0.30%)</td><td>450.90 (+0.94%)</td><td>383.30 (+6.62%)</td><td>43.39 <b>(-24.90%)</b></td><td>700.27 (-6.23%)</td><td>609.11 (-0.97%)</td><td>595.32 (-0.93%)</td><td>534.65 (-0.14%)</td><td>60.90 <b>(-28.92%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>3.83 (n/a)</td><td>3.15 (n/a)</td><td>3.08 (n/a)</td><td>2.74 (n/a)</td><td>0.44 (n/a)</td><td>501.40 (n/a)</td><td>442.82 (n/a)</td><td>446.70 (n/a)</td><td>359.50 (n/a)</td><td>57.78 (n/a)</td><td>746.79 (n/a)</td><td>615.10 (n/a)</td><td>600.89 (n/a)</td><td>535.38 (n/a)</td><td>85.68 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>3.88 <b>(-20.11%)</b></td><td>3.74 (-2.87%)</td><td>3.80 (+3.15%)</td><td>3.52 (+2.87%)</td><td>0.16 <b>(-72.41%)</b></td><td>391.40 (-2.81%)</td><td>368.44 (+1.55%)</td><td>362.50 (-3.05%)</td><td>354.70 <b>(+25.16%)</b></td><td>15.87 <b>(-65.53%)</b></td><td>756.85 <b>(-20.11%)</b></td><td>729.63 (-2.87%)</td><td>740.53 (+3.15%)</td><td>685.76 (+2.87%)</td><td>30.84 <b>(-72.41%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>4.86 (n/a)</td><td>3.85 (n/a)</td><td>3.68 (n/a)</td><td>3.42 (n/a)</td><td>0.57 (n/a)</td><td>402.70 (n/a)</td><td>362.82 (n/a)</td><td>373.90 (n/a)</td><td>283.40 (n/a)</td><td>46.04 (n/a)</td><td>947.33 (n/a)</td><td>751.20 (n/a)</td><td>717.91 (n/a)</td><td>666.61 (n/a)</td><td>111.79 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>6.27 (-9.55%)</td><td>4.11 (-3.43%)</td><td>3.60 (-0.53%)</td><td>3.46 (+0.66%)</td><td>1.21 (-19.04%)</td><td>397.80 (-0.65%)</td><td>353.00 (+1.67%)</td><td>381.80 (+0.55%)</td><td>219.50 (+10.52%)</td><td>75.64 (-9.53%)</td><td>1222.79 (-9.55%)</td><td>800.98 (-3.43%)</td><td>703.12 (-0.53%)</td><td>674.87 (+0.66%)</td><td>236.87 (-19.04%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>6.93 (n/a)</td><td>4.25 (n/a)</td><td>3.62 (n/a)</td><td>3.44 (n/a)</td><td>1.50 (n/a)</td><td>400.40 (n/a)</td><td>347.20 (n/a)</td><td>379.70 (n/a)</td><td>198.60 (n/a)</td><td>83.62 (n/a)</td><td>1351.92 (n/a)</td><td>829.46 (n/a)</td><td>706.89 (n/a)</td><td>670.41 (n/a)</td><td>292.56 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>5.91 (+2.55%)</td><td>4.39 (-8.52%)</td><td>3.75 <b>(-31.72%)</b></td><td>3.63 (+5.61%)</td><td>1.03 (-7.55%)</td><td>379.50 (-5.31%)</td><td>326.08 (+8.37%)</td><td>366.90 <b>(+46.47%)</b></td><td>232.90 (-2.47%)</td><td>67.96 (-11.58%)</td><td>1152.81 (+2.55%)</td><td>856.63 (-8.52%)</td><td>731.67 <b>(-31.73%)</b></td><td>707.35 (+5.61%)</td><td>200.91 (-7.55%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>5.76 (n/a)</td><td>4.80 (n/a)</td><td>5.49 (n/a)</td><td>3.43 (n/a)</td><td>1.11 (n/a)</td><td>400.80 (n/a)</td><td>300.90 (n/a)</td><td>250.50 (n/a)</td><td>238.80 (n/a)</td><td>76.86 (n/a)</td><td>1124.13 (n/a)</td><td>936.42 (n/a)</td><td>1071.66 (n/a)</td><td>669.80 (n/a)</td><td>217.32 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_1024-epilogue_sigmoid-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>5.26 (+10.86%)</td><td>3.79 (+7.63%)</td><td>3.37 (-0.29%)</td><td>3.13 (+4.25%)</td><td>0.88 <b>(+22.96%)</b></td><td>439.00 (-4.09%)</td><td>376.56 (-6.31%)</td><td>408.10 (+0.29%)</td><td>261.70 (-9.82%)</td><td>72.30 (+6.68%)</td><td>1025.58 (+10.86%)</td><td>738.86 (+7.63%)</td><td>657.82 (-0.29%)</td><td>611.46 (+4.25%)</td><td>170.72 <b>(+22.95%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>4.74 (n/a)</td><td>3.52 (n/a)</td><td>3.38 (n/a)</td><td>3.01 (n/a)</td><td>0.71 (n/a)</td><td>457.70 (n/a)</td><td>401.94 (n/a)</td><td>406.90 (n/a)</td><td>290.20 (n/a)</td><td>67.77 (n/a)</td><td>925.15 (n/a)</td><td>686.48 (n/a)</td><td>659.77 (n/a)</td><td>586.51 (n/a)</td><td>138.84 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>3.34 (-14.49%)</td><td>3.14 (-4.73%)</td><td>3.05 (-4.15%)</td><td>3.01 (-1.64%)</td><td>0.16 <b>(-54.86%)</b></td><td>457.00 (+1.69%)</td><td>438.60 (+4.35%)</td><td>451.00 (+4.33%)</td><td>411.90 (+16.95%)</td><td>21.26 <b>(-45.21%)</b></td><td>651.73 (-14.49%)</td><td>613.20 (-4.73%)</td><td>595.16 (-4.15%)</td><td>587.44 (-1.64%)</td><td>30.29 <b>(-54.86%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>3.91 (n/a)</td><td>3.30 (n/a)</td><td>3.18 (n/a)</td><td>3.06 (n/a)</td><td>0.34 (n/a)</td><td>449.40 (n/a)</td><td>420.30 (n/a)</td><td>432.30 (n/a)</td><td>352.20 (n/a)</td><td>38.81 (n/a)</td><td>762.17 (n/a)</td><td>643.62 (n/a)</td><td>620.90 (n/a)</td><td>597.26 (n/a)</td><td>67.10 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_1024-epilogue_silu-clamp_None-rounding_floor]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>3.11 <b>(-30.56%)</b></td><td>3.04 (-13.64%)</td><td>3.06 (-2.28%)</td><td>2.97 (-0.86%)</td><td>0.06 <b>(-90.98%)</b></td><td>463.70 (+0.87%)</td><td>452.74 (+12.75%)</td><td>450.30 (+2.34%)</td><td>443.00 <b>(+44.02%)</b></td><td>9.04 <b>(-87.13%)</b></td><td>605.93 <b>(-30.56%)</b></td><td>593.10 (-13.64%)</td><td>596.14 (-2.28%)</td><td>578.88 (-0.86%)</td><td>11.82 <b>(-90.98%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>4.47 (n/a)</td><td>3.52 (n/a)</td><td>3.13 (n/a)</td><td>2.99 (n/a)</td><td>0.67 (n/a)</td><td>459.70 (n/a)</td><td>401.56 (n/a)</td><td>440.00 (n/a)</td><td>307.60 (n/a)</td><td>70.23 (n/a)</td><td>872.63 (n/a)</td><td>686.76 (n/a)</td><td>610.04 (n/a)</td><td>583.92 (n/a)</td><td>131.00 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>1.70 (-2.18%)</td><td>1.32 (-8.38%)</td><td>1.26 (-13.74%)</td><td>0.99 (-9.83%)</td><td>0.28 (+7.07%)</td><td>405.20 (+10.89%)</td><td>316.64 (+10.04%)</td><td>319.40 (+15.93%)</td><td>235.90 (+2.25%)</td><td>67.04 <b>(+20.77%)</b></td><td>142.25 (-2.18%)</td><td>109.94 (-8.38%)</td><td>105.06 (-13.74%)</td><td>82.81 (-9.83%)</td><td>23.70 (+7.07%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>1.74 (n/a)</td><td>1.44 (n/a)</td><td>1.46 (n/a)</td><td>1.10 (n/a)</td><td>0.26 (n/a)</td><td>365.40 (n/a)</td><td>287.76 (n/a)</td><td>275.50 (n/a)</td><td>230.70 (n/a)</td><td>55.51 (n/a)</td><td>145.43 (n/a)</td><td>120.00 (n/a)</td><td>121.80 (n/a)</td><td>91.84 (n/a)</td><td>22.13 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>6.36 (+6.83%)</td><td>5.07 (-0.06%)</td><td>4.80 (-2.32%)</td><td>4.42 (-3.30%)</td><td>0.75 <b>(+36.22%)</b></td><td>437.40 (+3.43%)</td><td>386.96 (+0.73%)</td><td>403.10 (+2.39%)</td><td>304.20 (-6.40%)</td><td>50.37 <b>(+28.92%)</b></td><td>1323.69 (+6.83%)</td><td>1056.83 (-0.06%)</td><td>998.95 (-2.32%)</td><td>920.62 (-3.30%)</td><td>156.67 <b>(+36.22%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>5.95 (n/a)</td><td>5.08 (n/a)</td><td>4.91 (n/a)</td><td>4.57 (n/a)</td><td>0.55 (n/a)</td><td>422.90 (n/a)</td><td>384.14 (n/a)</td><td>393.70 (n/a)</td><td>325.00 (n/a)</td><td>39.07 (n/a)</td><td>1239.06 (n/a)</td><td>1057.48 (n/a)</td><td>1022.64 (n/a)</td><td>952.05 (n/a)</td><td>115.01 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>19.50 (+15.00%)</td><td>12.84 (-1.99%)</td><td>11.23 (-2.55%)</td><td>9.57 (-11.64%)</td><td>3.90 <b>(+40.71%)</b></td><td>575.30 (+13.18%)</td><td>454.72 (+4.71%)</td><td>490.10 (+2.62%)</td><td>282.20 (-13.06%)</td><td>109.53 <b>(+30.35%)</b></td><td>7608.80 (+15.00%)</td><td>5010.09 (-1.99%)</td><td>4381.60 (-2.55%)</td><td>3732.77 (-11.64%)</td><td>1520.95 <b>(+40.71%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>16.96 (n/a)</td><td>13.10 (n/a)</td><td>11.53 (n/a)</td><td>10.83 (n/a)</td><td>2.77 (n/a)</td><td>508.30 (n/a)</td><td>434.28 (n/a)</td><td>477.60 (n/a)</td><td>324.60 (n/a)</td><td>84.03 (n/a)</td><td>6616.23 (n/a)</td><td>5111.75 (n/a)</td><td>4496.05 (n/a)</td><td>4224.69 (n/a)</td><td>1080.93 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_512-K_1024-N_2048-epilogue_silu-clamp_(-4.0, 4.0)-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>8.28 (-2.83%)</td><td>7.10 (-12.54%)</td><td>7.74 (-3.87%)</td><td>3.97 <b>(-49.57%)</b></td><td>1.76 <b>(+628.13%)</b></td><td>1385.30 <b>(+98.30%)</b></td><td>836.56 <b>(+23.24%)</b></td><td>711.10 (+4.02%)</td><td>665.20 (+2.91%)</td><td>307.48 <b>(+1457.04%)</b></td><td>3228.25 (-2.83%)</td><td>2768.85 (-12.54%)</td><td>3020.14 (-3.87%)</td><td>1550.23 <b>(-49.57%)</b></td><td>687.80 <b>(+628.13%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>8.52 (n/a)</td><td>8.12 (n/a)</td><td>8.05 (n/a)</td><td>7.88 (n/a)</td><td>0.24 (n/a)</td><td>698.60 (n/a)</td><td>678.82 (n/a)</td><td>683.60 (n/a)</td><td>646.40 (n/a)</td><td>19.75 (n/a)</td><td>3322.27 (n/a)</td><td>3165.74 (n/a)</td><td>3141.57 (n/a)</td><td>3073.81 (n/a)</td><td>94.46 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_512-K_1536-N_1536-epilogue_silu-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>10.43 (-8.67%)</td><td>8.35 (-9.63%)</td><td>8.77 (-1.39%)</td><td>4.82 <b>(-40.61%)</b></td><td>2.10 <b>(+65.93%)</b></td><td>1203.90 <b>(+68.38%)</b></td><td>746.36 (+17.31%)</td><td>661.10 (+1.41%)</td><td>556.00 (+9.49%)</td><td>259.93 <b>(+238.91%)</b></td><td>4345.26 (-8.67%)</td><td>3477.27 (-9.63%)</td><td>3654.35 (-1.39%)</td><td>2006.74 <b>(-40.61%)</b></td><td>875.30 <b>(+65.93%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>11.42 (n/a)</td><td>9.24 (n/a)</td><td>8.90 (n/a)</td><td>8.11 (n/a)</td><td>1.27 (n/a)</td><td>715.00 (n/a)</td><td>636.24 (n/a)</td><td>651.90 (n/a)</td><td>507.80 (n/a)</td><td>76.70 (n/a)</td><td>4757.84 (n/a)</td><td>3847.79 (n/a)</td><td>3705.73 (n/a)</td><td>3378.95 (n/a)</td><td>527.52 (n/a)</td>
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


### test_gemm_tile_options[tn128-ma16]

_No metrics available._


### test_gemm_tile_options[tn128-ma32]

_No metrics available._


### test_gemm_tile_options[tn128-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn16-ma16]

_No metrics available._


### test_gemm_tile_options[tn16-ma32]

_No metrics available._


### test_gemm_tile_options[tn16-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn32-ma16]

_No metrics available._


### test_gemm_tile_options[tn32-ma32]

_No metrics available._


### test_gemm_tile_options[tn32-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn64-ma16]

_No metrics available._


### test_gemm_tile_options[tn64-ma32-default]

_No metrics available._


### test_gemm_tile_options[tn64-ma64]

_No metrics available._


</details>


<details>
<summary>iron/operators/flm/mm_prebuilt</summary>


### test_mm_prebuilt[M_256-K_512-N_1024-epilogue_gelu-clamp_None]

_No metrics available._


### test_mm_prebuilt[M_256-K_512-N_1024-epilogue_none-clamp_None]

_No metrics available._


### test_mm_prebuilt[M_256-K_512-N_1024-epilogue_silu-clamp_None]

_No metrics available._


### test_mm_prebuilt[M_256-K_512-N_1280-epilogue_none-clamp_None]

_No metrics available._


### test_mm_prebuilt[M_256-K_512-N_640-epilogue_none-clamp_None]

_No metrics available._


### test_mm_prebuilt[M_512-K_1024-N_2048-epilogue_none-clamp_None]

_No metrics available._


### test_mm_prebuilt_epilogue_matches_accumulator[epilogue_gelu-clamp_None]

_No metrics available._


### test_mm_prebuilt_epilogue_matches_accumulator[epilogue_none-clamp_(-2.0, 2.0)]

_No metrics available._


### test_mm_prebuilt_epilogue_matches_accumulator[epilogue_sigmoid-clamp_None]

_No metrics available._


### test_mm_prebuilt_epilogue_matches_accumulator[epilogue_silu-clamp_None]

_No metrics available._


</details>


<details>
<summary>iron/operators/gelu</summary>


### test_gelu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>248.40 (n/a)</td><td>162.18 (n/a)</td><td>155.70 (n/a)</td><td>118.00 (n/a)</td><td>52.44 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>243.50 (n/a)</td><td>181.88 (n/a)</td><td>163.50 (n/a)</td><td>150.30 (n/a)</td><td>37.76 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>232.90 (n/a)</td><td>162.56 (n/a)</td><td>145.20 (n/a)</td><td>129.50 (n/a)</td><td>41.10 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>244.80 (n/a)</td><td>179.80 (n/a)</td><td>182.40 (n/a)</td><td>129.70 (n/a)</td><td>43.85 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>224.80 (n/a)</td><td>161.48 (n/a)</td><td>149.60 (n/a)</td><td>132.40 (n/a)</td><td>37.98 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>195.00 (n/a)</td><td>168.60 (n/a)</td><td>159.50 (n/a)</td><td>150.90 (n/a)</td><td>20.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>215.90 (n/a)</td><td>160.32 (n/a)</td><td>153.10 (n/a)</td><td>121.50 (n/a)</td><td>36.68 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>262.20 (n/a)</td><td>190.80 (n/a)</td><td>167.80 (n/a)</td><td>155.10 (n/a)</td><td>43.69 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>173.70 (n/a)</td><td>158.28 (n/a)</td><td>156.80 (n/a)</td><td>146.50 (n/a)</td><td>10.04 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.70 (n/a)</td><td>173.74 (n/a)</td><td>187.70 (n/a)</td><td>128.20 (n/a)</td><td>35.98 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.20 (n/a)</td><td>153.80 (n/a)</td><td>154.90 (n/a)</td><td>126.30 (n/a)</td><td>22.14 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>186.40 (n/a)</td><td>156.84 (n/a)</td><td>151.20 (n/a)</td><td>145.80 (n/a)</td><td>16.74 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>320.30 (n/a)</td><td>181.34 (n/a)</td><td>161.80 (n/a)</td><td>122.90 (n/a)</td><td>81.30 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>300.40 (n/a)</td><td>196.10 (n/a)</td><td>174.70 (n/a)</td><td>161.10 (n/a)</td><td>58.94 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.40 (n/a)</td><td>201.30 (n/a)</td><td>214.00 (n/a)</td><td>142.40 (n/a)</td><td>34.43 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>343.50 (n/a)</td><td>236.64 (n/a)</td><td>196.70 (n/a)</td><td>175.80 (n/a)</td><td>70.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>248.10 (n/a)</td><td>181.48 (n/a)</td><td>187.90 (n/a)</td><td>139.60 (n/a)</td><td>44.17 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>242.90 (n/a)</td><td>175.82 (n/a)</td><td>166.00 (n/a)</td><td>122.60 (n/a)</td><td>45.77 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>237.40 (n/a)</td><td>193.90 (n/a)</td><td>183.50 (n/a)</td><td>173.20 (n/a)</td><td>25.30 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>249.90 (n/a)</td><td>209.64 (n/a)</td><td>205.20 (n/a)</td><td>166.40 (n/a)</td><td>30.64 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>348.90 (n/a)</td><td>208.26 (n/a)</td><td>180.90 (n/a)</td><td>159.90 (n/a)</td><td>79.19 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>222.70 (n/a)</td><td>194.66 (n/a)</td><td>194.30 (n/a)</td><td>170.20 (n/a)</td><td>20.93 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>328.00 (n/a)</td><td>226.48 (n/a)</td><td>210.60 (n/a)</td><td>174.40 (n/a)</td><td>58.94 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>269.90 (n/a)</td><td>223.56 (n/a)</td><td>223.90 (n/a)</td><td>170.20 (n/a)</td><td>35.90 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>210.90 (n/a)</td><td>176.50 (n/a)</td><td>172.40 (n/a)</td><td>138.70 (n/a)</td><td>32.74 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>218.90 (n/a)</td><td>184.84 (n/a)</td><td>191.80 (n/a)</td><td>138.30 (n/a)</td><td>31.55 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>178.80 (n/a)</td><td>158.22 (n/a)</td><td>166.30 (n/a)</td><td>121.00 (n/a)</td><td>22.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>241.60 (n/a)</td><td>188.64 (n/a)</td><td>186.90 (n/a)</td><td>124.50 (n/a)</td><td>46.03 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>181.50 (n/a)</td><td>157.16 (n/a)</td><td>159.20 (n/a)</td><td>122.00 (n/a)</td><td>24.97 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>215.80 (n/a)</td><td>172.14 (n/a)</td><td>160.10 (n/a)</td><td>142.20 (n/a)</td><td>31.43 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>187.80 (n/a)</td><td>166.40 (n/a)</td><td>161.80 (n/a)</td><td>142.50 (n/a)</td><td>19.36 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>233.10 (n/a)</td><td>200.20 (n/a)</td><td>207.30 (n/a)</td><td>161.90 (n/a)</td><td>33.19 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/gemm</summary>


### test_gemm[M_1024-K_2560-N_10240-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>4.12 (-1.66%)</td><td>4.10 (-0.18%)</td><td>4.11 (+0.02%)</td><td>4.07 (+0.25%)</td><td>0.02 <b>(-56.51%)</b></td><td>19329.50 (-0.25%)</td><td>19159.20 (+0.17%)</td><td>19122.80 (-0.02%)</td><td>19109.80 (+1.69%)</td><td>95.43 <b>(-55.80%)</b></td><td>2809.40 (-1.66%)</td><td>2802.21 (-0.18%)</td><td>2807.50 (+0.02%)</td><td>2777.47 (+0.25%)</td><td>13.86 <b>(-56.51%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>4.19 (n/a)</td><td>4.11 (n/a)</td><td>4.11 (n/a)</td><td>4.06 (n/a)</td><td>0.05 (n/a)</td><td>19378.60 (n/a)</td><td>19127.00 (n/a)</td><td>19126.50 (n/a)</td><td>18791.70 (n/a)</td><td>215.93 (n/a)</td><td>2856.96 (n/a)</td><td>2807.16 (n/a)</td><td>2806.95 (n/a)</td><td>2770.43 (n/a)</td><td>31.88 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>4.79 (+10.34%)</td><td>4.18 (+3.18%)</td><td>4.18 (-0.61%)</td><td>3.70 (+3.89%)</td><td>0.41 <b>(+26.25%)</b></td><td>2542.90 (-3.74%)</td><td>2268.90 (-2.89%)</td><td>2250.80 (+0.62%)</td><td>1963.00 (-9.37%)</td><td>214.97 (+9.40%)</td><td>1884.53 (+10.34%)</td><td>1642.56 (+3.18%)</td><td>1643.62 (-0.61%)</td><td>1454.77 (+3.89%)</td><td>160.15 <b>(+26.25%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>4.34 (n/a)</td><td>4.05 (n/a)</td><td>4.20 (n/a)</td><td>3.56 (n/a)</td><td>0.32 (n/a)</td><td>2641.80 (n/a)</td><td>2336.34 (n/a)</td><td>2237.00 (n/a)</td><td>2166.00 (n/a)</td><td>196.50 (n/a)</td><td>1707.93 (n/a)</td><td>1591.92 (n/a)</td><td>1653.75 (n/a)</td><td>1400.31 (n/a)</td><td>126.85 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>1.44 (+14.75%)</td><td>1.11 (+7.80%)</td><td>1.03 (-8.49%)</td><td>0.89 <b>(+39.58%)</b></td><td>0.22 (-11.97%)</td><td>249.70 <b>(-28.35%)</b></td><td>205.32 (-10.18%)</td><td>214.80 (+9.26%)</td><td>153.20 (-12.86%)</td><td>38.09 <b>(-46.40%)</b></td><td>61.61 (+14.75%)</td><td>47.36 (+7.80%)</td><td>43.93 (-8.49%)</td><td>37.80 <b>(+39.58%)</b></td><td>9.49 (-11.97%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>1.26 (n/a)</td><td>1.03 (n/a)</td><td>1.13 (n/a)</td><td>0.63 (n/a)</td><td>0.25 (n/a)</td><td>348.50 (n/a)</td><td>228.60 (n/a)</td><td>196.60 (n/a)</td><td>175.80 (n/a)</td><td>71.07 (n/a)</td><td>53.69 (n/a)</td><td>43.93 (n/a)</td><td>48.01 (n/a)</td><td>27.08 (n/a)</td><td>10.78 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>1.30 <b>(+27.36%)</b></td><td>1.04 <b>(+26.36%)</b></td><td>1.11 <b>(+46.99%)</b></td><td>0.63 (-1.46%)</td><td>0.26 <b>(+43.40%)</b></td><td>349.90 (+1.48%)</td><td>227.20 (-18.75%)</td><td>199.20 <b>(-31.99%)</b></td><td>169.60 <b>(-21.48%)</b></td><td>71.70 <b>(+22.64%)</b></td><td>55.65 <b>(+27.36%)</b></td><td>44.24 <b>(+26.36%)</b></td><td>47.37 <b>(+46.99%)</b></td><td>26.97 (-1.46%)</td><td>10.91 <b>(+43.40%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>1.02 (n/a)</td><td>0.82 (n/a)</td><td>0.76 (n/a)</td><td>0.64 (n/a)</td><td>0.18 (n/a)</td><td>344.80 (n/a)</td><td>279.64 (n/a)</td><td>292.90 (n/a)</td><td>216.00 (n/a)</td><td>58.46 (n/a)</td><td>43.69 (n/a)</td><td>35.01 (n/a)</td><td>32.22 (n/a)</td><td>27.37 (n/a)</td><td>7.61 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.53 (-0.00%)</td><td>0.53 (-0.08%)</td><td>0.53 (-0.04%)</td><td>0.52 (-0.19%)</td><td>0.00 <b>(+144.83%)</b></td><td>47948.30 (+0.19%)</td><td>47849.84 (+0.08%)</td><td>47824.30 (+0.04%)</td><td>47779.80 (+0.00%)</td><td>71.02 <b>(+145.33%)</b></td><td>359.56 (-0.00%)</td><td>359.04 (-0.08%)</td><td>359.23 (-0.04%)</td><td>358.30 (-0.19%)</td><td>0.53 <b>(+144.79%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47856.30 (n/a)</td><td>47809.32 (n/a)</td><td>47806.80 (n/a)</td><td>47779.70 (n/a)</td><td>28.95 (n/a)</td><td>359.56 (n/a)</td><td>359.34 (n/a)</td><td>359.36 (n/a)</td><td>358.99 (n/a)</td><td>0.22 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_8-k_16-n_32-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.21 (+1.01%)</td><td>0.21 (+0.66%)</td><td>0.21 (+0.70%)</td><td>0.21 (+0.13%)</td><td>0.00 <b>(+76.15%)</b></td><td>119249.70 (-0.13%)</td><td>118235.84 (-0.65%)</td><td>118464.20 (-0.70%)</td><td>117098.80 (-1.00%)</td><td>858.86 <b>(+74.02%)</b></td><td>146.71 (+1.01%)</td><td>145.31 (+0.66%)</td><td>145.02 (+0.70%)</td><td>144.07 (+0.13%)</td><td>1.06 <b>(+76.16%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>119400.20 (n/a)</td><td>119013.32 (n/a)</td><td>119297.10 (n/a)</td><td>118284.00 (n/a)</td><td>493.55 (n/a)</td><td>145.24 (n/a)</td><td>144.35 (n/a)</td><td>144.01 (n/a)</td><td>143.88 (n/a)</td><td>0.60 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.92 (+0.99%)</td><td>0.90 (-0.08%)</td><td>0.90 (-0.35%)</td><td>0.89 (-1.05%)</td><td>0.01 <b>(+225.21%)</b></td><td>28237.20 (+1.06%)</td><td>27846.82 (+0.09%)</td><td>27896.80 (+0.35%)</td><td>27464.30 (-0.98%)</td><td>287.10 <b>(+225.49%)</b></td><td>625.53 (+0.99%)</td><td>616.99 (-0.08%)</td><td>615.84 (-0.35%)</td><td>608.41 (-1.05%)</td><td>6.36 <b>(+225.20%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.00 (n/a)</td><td>27941.60 (n/a)</td><td>27823.14 (n/a)</td><td>27798.20 (n/a)</td><td>27735.40 (n/a)</td><td>88.21 (n/a)</td><td>619.42 (n/a)</td><td>617.47 (n/a)</td><td>618.02 (n/a)</td><td>614.85 (n/a)</td><td>1.96 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_32-k_32-n_128-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>3.63 (-0.80%)</td><td>3.58 (+1.64%)</td><td>3.61 (+0.78%)</td><td>3.48 (+4.71%)</td><td>0.06 <b>(-55.06%)</b></td><td>7241.90 (-4.49%)</td><td>7033.40 (-1.72%)</td><td>6967.80 (-0.77%)</td><td>6930.40 (+0.81%)</td><td>129.02 <b>(-56.72%)</b></td><td>2478.93 (-0.80%)</td><td>2443.27 (+1.64%)</td><td>2465.62 (+0.78%)</td><td>2372.29 (+4.71%)</td><td>44.15 <b>(-55.06%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>3.66 (n/a)</td><td>3.52 (n/a)</td><td>3.58 (n/a)</td><td>3.32 (n/a)</td><td>0.14 (n/a)</td><td>7582.70 (n/a)</td><td>7156.22 (n/a)</td><td>7021.90 (n/a)</td><td>6875.00 (n/a)</td><td>298.14 (n/a)</td><td>2498.89 (n/a)</td><td>2403.96 (n/a)</td><td>2446.62 (n/a)</td><td>2265.66 (n/a)</td><td>98.24 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_False-m_128-k_32-n_32-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>2.90 (-9.30%)</td><td>2.85 (-3.75%)</td><td>2.88 (+0.29%)</td><td>2.70 (-3.13%)</td><td>0.08 <b>(-51.67%)</b></td><td>9323.70 (+3.24%)</td><td>8844.08 (+3.69%)</td><td>8750.10 (-0.29%)</td><td>8666.00 (+10.26%)</td><td>270.37 <b>(-44.57%)</b></td><td>1982.44 (-9.30%)</td><td>1943.93 (-3.75%)</td><td>1963.39 (+0.29%)</td><td>1842.61 (-3.13%)</td><td>57.19 <b>(-51.67%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>3.20 (n/a)</td><td>2.96 (n/a)</td><td>2.87 (n/a)</td><td>2.79 (n/a)</td><td>0.17 (n/a)</td><td>9031.50 (n/a)</td><td>8529.04 (n/a)</td><td>8775.40 (n/a)</td><td>7859.70 (n/a)</td><td>487.78 (n/a)</td><td>2185.83 (n/a)</td><td>2019.69 (n/a)</td><td>1957.72 (n/a)</td><td>1902.22 (n/a)</td><td>118.33 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>3.33 (-0.01%)</td><td>3.24 (+0.58%)</td><td>3.23 (+1.26%)</td><td>3.16 (+1.81%)</td><td>0.06 <b>(-28.33%)</b></td><td>7952.90 (-1.78%)</td><td>7765.06 (-0.61%)</td><td>7780.30 (-1.25%)</td><td>7558.20 (+0.01%)</td><td>154.20 <b>(-29.42%)</b></td><td>2273.00 (-0.01%)</td><td>2213.15 (+0.58%)</td><td>2208.11 (+1.26%)</td><td>2160.19 (+1.81%)</td><td>44.09 <b>(-28.33%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>3.33 (n/a)</td><td>3.22 (n/a)</td><td>3.19 (n/a)</td><td>3.11 (n/a)</td><td>0.09 (n/a)</td><td>8097.20 (n/a)</td><td>7812.64 (n/a)</td><td>7878.70 (n/a)</td><td>7557.60 (n/a)</td><td>218.49 (n/a)</td><td>2273.20 (n/a)</td><td>2200.37 (n/a)</td><td>2180.56 (n/a)</td><td>2121.71 (n/a)</td><td>61.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.80 (+0.46%)</td><td>0.80 (+0.07%)</td><td>0.80 (-0.01%)</td><td>0.80 (-0.05%)</td><td>0.00 <b>(+1171.68%)</b></td><td>94864.50 (+0.05%)</td><td>94715.22 (-0.07%)</td><td>94791.10 (+0.01%)</td><td>94338.70 (-0.46%)</td><td>213.00 <b>(+1166.26%)</b></td><td>728.43 (+0.46%)</td><td>725.54 (+0.07%)</td><td>724.96 (-0.01%)</td><td>724.40 (-0.05%)</td><td>1.64 <b>(+1171.33%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94814.20 (n/a)</td><td>94785.24 (n/a)</td><td>94780.30 (n/a)</td><td>94770.20 (n/a)</td><td>16.82 (n/a)</td><td>725.12 (n/a)</td><td>725.00 (n/a)</td><td>725.04 (n/a)</td><td>724.78 (n/a)</td><td>0.13 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.73 (-0.34%)</td><td>0.73 (-0.08%)</td><td>0.73 (+0.01%)</td><td>0.73 (-0.13%)</td><td>0.00 <b>(-50.37%)</b></td><td>103514.50 (+0.13%)</td><td>103346.48 (+0.08%)</td><td>103325.40 (-0.01%)</td><td>103267.40 (+0.34%)</td><td>97.26 <b>(-50.11%)</b></td><td>665.45 (-0.34%)</td><td>664.94 (-0.08%)</td><td>665.08 (+0.01%)</td><td>663.86 (-0.13%)</td><td>0.63 <b>(-50.36%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103375.40 (n/a)</td><td>103261.64 (n/a)</td><td>103338.50 (n/a)</td><td>102914.60 (n/a)</td><td>194.95 (n/a)</td><td>667.73 (n/a)</td><td>665.49 (n/a)</td><td>664.99 (n/a)</td><td>664.76 (n/a)</td><td>1.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.69 (+0.25%)</td><td>0.69 (+0.06%)</td><td>0.69 (-0.09%)</td><td>0.69 (+0.19%)</td><td>0.00 <b>(+21.17%)</b></td><td>110003.60 (-0.19%)</td><td>109750.64 (-0.06%)</td><td>109922.60 (+0.09%)</td><td>109298.80 (-0.25%)</td><td>298.54 <b>(+20.64%)</b></td><td>628.73 (+0.25%)</td><td>626.15 (+0.06%)</td><td>625.16 (-0.09%)</td><td>624.70 (+0.19%)</td><td>1.71 <b>(+21.17%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>110213.70 (n/a)</td><td>109818.34 (n/a)</td><td>109822.10 (n/a)</td><td>109576.30 (n/a)</td><td>247.46 (n/a)</td><td>627.14 (n/a)</td><td>625.76 (n/a)</td><td>625.73 (n/a)</td><td>623.51 (n/a)</td><td>1.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2560-N_10240-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>2.80 (+0.06%)</td><td>2.80 (+0.10%)</td><td>2.80 (+0.00%)</td><td>2.79 (+0.50%)</td><td>0.00 <b>(-63.74%)</b></td><td>37542.80 (-0.49%)</td><td>37506.10 (-0.10%)</td><td>37511.70 (-0.00%)</td><td>37441.00 (-0.06%)</td><td>38.76 <b>(-63.95%)</b></td><td>2867.82 (+0.06%)</td><td>2862.85 (+0.10%)</td><td>2862.42 (+0.00%)</td><td>2860.05 (+0.50%)</td><td>2.96 <b>(-63.74%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>2.80 (n/a)</td><td>2.79 (n/a)</td><td>2.80 (n/a)</td><td>2.78 (n/a)</td><td>0.01 (n/a)</td><td>37729.10 (n/a)</td><td>37542.98 (n/a)</td><td>37512.90 (n/a)</td><td>37463.20 (n/a)</td><td>107.53 (n/a)</td><td>2866.12 (n/a)</td><td>2860.05 (n/a)</td><td>2862.32 (n/a)</td><td>2845.92 (n/a)</td><td>8.17 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>7.65 (+0.80%)</td><td>6.01 (-17.32%)</td><td>6.43 (-14.54%)</td><td>4.55 <b>(-31.90%)</b></td><td>1.30 <b>(+212.54%)</b></td><td>1959.00 <b>(+46.83%)</b></td><td>1543.06 <b>(+25.40%)</b></td><td>1386.30 (+17.01%)</td><td>1165.40 (-0.79%)</td><td>343.16 <b>(+372.60%)</b></td><td>460.66 (+0.80%)</td><td>361.73 (-17.32%)</td><td>387.27 (-14.54%)</td><td>274.05 <b>(-31.90%)</b></td><td>78.25 <b>(+212.54%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>7.59 (n/a)</td><td>7.26 (n/a)</td><td>7.52 (n/a)</td><td>6.68 (n/a)</td><td>0.42 (n/a)</td><td>1334.20 (n/a)</td><td>1230.52 (n/a)</td><td>1184.80 (n/a)</td><td>1174.70 (n/a)</td><td>72.61 (n/a)</td><td>457.02 (n/a)</td><td>437.48 (n/a)</td><td>453.15 (n/a)</td><td>402.40 (n/a)</td><td>25.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>7.14 (-0.84%)</td><td>6.81 (+8.70%)</td><td>6.80 (+1.29%)</td><td>6.36 <b>(+52.51%)</b></td><td>0.32 <b>(-73.24%)</b></td><td>1401.00 <b>(-34.43%)</b></td><td>1311.34 (-11.39%)</td><td>1309.80 (-1.27%)</td><td>1247.90 (+0.85%)</td><td>63.01 <b>(-83.04%)</b></td><td>430.22 (-0.84%)</td><td>410.16 (+8.70%)</td><td>409.90 (+1.29%)</td><td>383.20 <b>(+52.51%)</b></td><td>19.44 <b>(-73.24%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>7.20 (n/a)</td><td>6.26 (n/a)</td><td>6.72 (n/a)</td><td>4.17 (n/a)</td><td>1.21 (n/a)</td><td>2136.70 (n/a)</td><td>1479.84 (n/a)</td><td>1326.60 (n/a)</td><td>1237.40 (n/a)</td><td>371.56 (n/a)</td><td>433.88 (n/a)</td><td>377.32 (n/a)</td><td>404.68 (n/a)</td><td>251.26 (n/a)</td><td>72.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>7.16 (+6.54%)</td><td>6.12 (+1.55%)</td><td>6.28 (+0.53%)</td><td>4.67 (-2.13%)</td><td>0.93 <b>(+24.19%)</b></td><td>1908.30 (+2.18%)</td><td>1486.78 (-0.88%)</td><td>1419.00 (-0.53%)</td><td>1244.20 (-6.14%)</td><td>253.86 (+19.06%)</td><td>431.48 (+6.54%)</td><td>368.66 (+1.55%)</td><td>378.34 (+0.53%)</td><td>281.34 (-2.13%)</td><td>55.90 <b>(+24.19%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>6.72 (n/a)</td><td>6.03 (n/a)</td><td>6.25 (n/a)</td><td>4.77 (n/a)</td><td>0.75 (n/a)</td><td>1867.60 (n/a)</td><td>1499.92 (n/a)</td><td>1426.50 (n/a)</td><td>1325.60 (n/a)</td><td>213.22 (n/a)</td><td>405.01 (n/a)</td><td>363.03 (n/a)</td><td>376.35 (n/a)</td><td>287.47 (n/a)</td><td>45.01 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>8.59 (+1.79%)</td><td>8.04 (-0.47%)</td><td>8.13 (+1.97%)</td><td>7.39 (-6.98%)</td><td>0.44 <b>(+107.06%)</b></td><td>4720.20 (+7.50%)</td><td>4345.32 (+0.66%)</td><td>4290.90 (-1.93%)</td><td>4059.00 (-1.76%)</td><td>241.43 <b>(+120.30%)</b></td><td>529.06 (+1.79%)</td><td>495.40 (-0.47%)</td><td>500.48 (+1.97%)</td><td>454.96 (-6.98%)</td><td>26.88 <b>(+107.06%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>8.44 (n/a)</td><td>8.08 (n/a)</td><td>7.97 (n/a)</td><td>7.94 (n/a)</td><td>0.21 (n/a)</td><td>4390.80 (n/a)</td><td>4316.78 (n/a)</td><td>4375.40 (n/a)</td><td>4131.90 (n/a)</td><td>109.59 (n/a)</td><td>519.74 (n/a)</td><td>497.73 (n/a)</td><td>490.80 (n/a)</td><td>489.08 (n/a)</td><td>12.98 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>7.82 (+2.75%)</td><td>7.52 (+3.20%)</td><td>7.62 (+3.11%)</td><td>6.84 (-0.50%)</td><td>0.39 (+14.10%)</td><td>5094.70 (+0.51%)</td><td>4647.76 (-3.05%)</td><td>4574.60 (-3.01%)</td><td>4459.20 (-2.68%)</td><td>254.83 (+12.83%)</td><td>481.58 (+2.75%)</td><td>463.09 (+3.20%)</td><td>469.44 (+3.11%)</td><td>421.52 (-0.50%)</td><td>23.83 (+14.10%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>7.61 (n/a)</td><td>7.29 (n/a)</td><td>7.39 (n/a)</td><td>6.88 (n/a)</td><td>0.34 (n/a)</td><td>5069.00 (n/a)</td><td>4794.10 (n/a)</td><td>4716.70 (n/a)</td><td>4582.10 (n/a)</td><td>225.85 (n/a)</td><td>468.67 (n/a)</td><td>448.73 (n/a)</td><td>455.29 (n/a)</td><td>423.65 (n/a)</td><td>20.88 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>7.52 (-1.72%)</td><td>7.25 (-2.13%)</td><td>7.44 (+0.52%)</td><td>6.92 (-5.00%)</td><td>0.30 <b>(+101.17%)</b></td><td>5041.80 (+5.26%)</td><td>4814.44 (+2.28%)</td><td>4685.70 (-0.52%)</td><td>4636.90 (+1.75%)</td><td>200.65 <b>(+116.58%)</b></td><td>463.13 (-1.72%)</td><td>446.66 (-2.13%)</td><td>458.31 (+0.52%)</td><td>425.94 (-5.00%)</td><td>18.35 <b>(+101.17%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>7.65 (n/a)</td><td>7.41 (n/a)</td><td>7.40 (n/a)</td><td>7.28 (n/a)</td><td>0.15 (n/a)</td><td>4789.80 (n/a)</td><td>4707.06 (n/a)</td><td>4710.20 (n/a)</td><td>4557.10 (n/a)</td><td>92.64 (n/a)</td><td>471.24 (n/a)</td><td>456.37 (n/a)</td><td>455.93 (n/a)</td><td>448.35 (n/a)</td><td>9.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.80 (+0.00%)</td><td>0.80 (+0.01%)</td><td>0.80 (-0.01%)</td><td>0.80 (+0.06%)</td><td>0.00 <b>(-44.15%)</b></td><td>94095.60 (-0.06%)</td><td>94056.70 (-0.01%)</td><td>94056.40 (+0.01%)</td><td>94018.10 (-0.00%)</td><td>29.09 <b>(-44.22%)</b></td><td>730.92 (+0.00%)</td><td>730.62 (+0.01%)</td><td>730.62 (-0.01%)</td><td>730.32 (+0.06%)</td><td>0.23 <b>(-44.14%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94153.40 (n/a)</td><td>94068.22 (n/a)</td><td>94048.90 (n/a)</td><td>94020.50 (n/a)</td><td>52.14 (n/a)</td><td>730.90 (n/a)</td><td>730.53 (n/a)</td><td>730.68 (n/a)</td><td>729.87 (n/a)</td><td>0.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.74 (-0.01%)</td><td>0.74 (-0.01%)</td><td>0.74 (-0.07%)</td><td>0.73 (+0.08%)</td><td>0.00 <b>(-43.60%)</b></td><td>102775.70 (-0.08%)</td><td>102679.78 (+0.01%)</td><td>102676.50 (+0.07%)</td><td>102576.70 (+0.01%)</td><td>71.23 <b>(-43.64%)</b></td><td>669.93 (-0.01%)</td><td>669.26 (-0.01%)</td><td>669.28 (-0.07%)</td><td>668.64 (+0.08%)</td><td>0.46 <b>(-43.60%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>102858.60 (n/a)</td><td>102670.58 (n/a)</td><td>102606.70 (n/a)</td><td>102568.40 (n/a)</td><td>126.38 (n/a)</td><td>669.99 (n/a)</td><td>669.32 (n/a)</td><td>669.74 (n/a)</td><td>668.10 (n/a)</td><td>0.82 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.71 (-0.11%)</td><td>0.71 (-0.11%)</td><td>0.71 (-0.11%)</td><td>0.71 (+0.01%)</td><td>0.00 <b>(-21.80%)</b></td><td>106182.40 (-0.01%)</td><td>106046.26 (+0.11%)</td><td>106070.70 (+0.11%)</td><td>105790.20 (+0.11%)</td><td>150.42 <b>(-21.74%)</b></td><td>649.58 (-0.11%)</td><td>648.02 (-0.11%)</td><td>647.86 (-0.11%)</td><td>647.18 (+0.01%)</td><td>0.92 <b>(-21.80%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.00 (n/a)</td><td>106190.50 (n/a)</td><td>105933.24 (n/a)</td><td>105951.30 (n/a)</td><td>105669.30 (n/a)</td><td>192.21 (n/a)</td><td>650.33 (n/a)</td><td>648.71 (n/a)</td><td>648.60 (n/a)</td><td>647.13 (n/a)</td><td>1.18 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>4.34 (-0.87%)</td><td>3.72 (+3.03%)</td><td>3.86 (+5.29%)</td><td>3.04 (+0.83%)</td><td>0.56 (-2.02%)</td><td>2650.80 (-0.83%)</td><td>2209.68 (-3.04%)</td><td>2089.90 (-5.03%)</td><td>1857.40 (+0.87%)</td><td>344.90 (-3.50%)</td><td>1138.10 (-0.87%)</td><td>974.96 (+3.03%)</td><td>1011.48 (+5.29%)</td><td>797.47 (+0.83%)</td><td>146.97 (-2.02%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>4.38 (n/a)</td><td>3.61 (n/a)</td><td>3.66 (n/a)</td><td>3.02 (n/a)</td><td>0.57 (n/a)</td><td>2672.90 (n/a)</td><td>2278.98 (n/a)</td><td>2200.50 (n/a)</td><td>1841.30 (n/a)</td><td>357.41 (n/a)</td><td>1148.08 (n/a)</td><td>946.30 (n/a)</td><td>960.66 (n/a)</td><td>790.87 (n/a)</td><td>149.99 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.35 (+3.62%)</td><td>0.33 (+5.87%)</td><td>0.32 (+1.14%)</td><td>0.31 (+7.59%)</td><td>0.02 (-3.40%)</td><td>4023.60 (-7.05%)</td><td>3799.98 (-5.61%)</td><td>3917.80 (-1.13%)</td><td>3528.30 (-3.49%)</td><td>242.48 (-14.88%)</td><td>19.02 (+3.62%)</td><td>17.72 (+5.87%)</td><td>17.13 (+1.14%)</td><td>16.68 (+7.59%)</td><td>1.15 (-3.40%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.34 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.02 (n/a)</td><td>4329.00 (n/a)</td><td>4025.78 (n/a)</td><td>3962.60 (n/a)</td><td>3655.90 (n/a)</td><td>284.86 (n/a)</td><td>18.36 (n/a)</td><td>16.74 (n/a)</td><td>16.94 (n/a)</td><td>15.50 (n/a)</td><td>1.19 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>6.22 <b>(+24.55%)</b></td><td>4.85 (+7.13%)</td><td>4.80 (+0.93%)</td><td>3.48 (+1.79%)</td><td>1.00 <b>(+56.96%)</b></td><td>1911.10 (-1.76%)</td><td>1421.76 (-5.06%)</td><td>1387.00 (-0.92%)</td><td>1069.90 (-19.71%)</td><td>312.45 <b>(+22.92%)</b></td><td>1920.92 <b>(+24.55%)</b></td><td>1498.84 (+7.13%)</td><td>1481.81 (+0.93%)</td><td>1075.41 (+1.79%)</td><td>309.46 <b>(+56.96%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>4.99 (n/a)</td><td>4.53 (n/a)</td><td>4.75 (n/a)</td><td>3.42 (n/a)</td><td>0.64 (n/a)</td><td>1945.40 (n/a)</td><td>1497.58 (n/a)</td><td>1399.90 (n/a)</td><td>1332.60 (n/a)</td><td>254.19 (n/a)</td><td>1542.23 (n/a)</td><td>1399.06 (n/a)</td><td>1468.15 (n/a)</td><td>1056.46 (n/a)</td><td>197.15 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>13.51 (n/a)</td><td>12.32 (n/a)</td><td>12.34 (n/a)</td><td>10.98 (n/a)</td><td>1.19 (n/a)</td><td>13.50 (n/a)</td><td>12.31 (n/a)</td><td>12.33 (n/a)</td><td>10.98 (n/a)</td><td>1.19 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>25.18 (+0.25%)</td><td>24.78 (+0.57%)</td><td>24.96 (+0.63%)</td><td>24.21 (+0.60%)</td><td>0.42 (-6.50%)</td><td>25.16 (+0.25%)</td><td>24.77 (+0.57%)</td><td>24.95 (+0.63%)</td><td>24.19 (+0.60%)</td><td>0.42 (-6.50%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>25.12 (n/a)</td><td>24.64 (n/a)</td><td>24.81 (n/a)</td><td>24.06 (n/a)</td><td>0.45 (n/a)</td><td>25.10 (n/a)</td><td>24.63 (n/a)</td><td>24.79 (n/a)</td><td>24.05 (n/a)</td><td>0.45 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>43.69 (+4.96%)</td><td>41.41 (+3.37%)</td><td>40.90 (+2.76%)</td><td>40.34 (+3.15%)</td><td>1.33 <b>(+35.22%)</b></td><td>43.67 (+4.96%)</td><td>41.39 (+3.37%)</td><td>40.87 (+2.76%)</td><td>40.32 (+3.15%)</td><td>1.33 <b>(+35.22%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>41.63 (n/a)</td><td>40.06 (n/a)</td><td>39.80 (n/a)</td><td>39.11 (n/a)</td><td>0.98 (n/a)</td><td>41.60 (n/a)</td><td>40.04 (n/a)</td><td>39.77 (n/a)</td><td>39.08 (n/a)</td><td>0.98 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>45.74 (-2.66%)</td><td>44.28 (+4.20%)</td><td>44.18 (+5.59%)</td><td>42.84 (+7.89%)</td><td>1.20 <b>(-59.87%)</b></td><td>45.71 (-2.66%)</td><td>44.25 (+4.20%)</td><td>44.15 (+5.59%)</td><td>42.82 (+7.89%)</td><td>1.20 <b>(-59.87%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>46.99 (n/a)</td><td>42.49 (n/a)</td><td>41.84 (n/a)</td><td>39.71 (n/a)</td><td>2.98 (n/a)</td><td>46.96 (n/a)</td><td>42.46 (n/a)</td><td>41.81 (n/a)</td><td>39.68 (n/a)</td><td>2.98 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>13.50 (n/a)</td><td>13.17 (n/a)</td><td>13.39 (n/a)</td><td>12.72 (n/a)</td><td>0.40 (n/a)</td><td>13.49 (n/a)</td><td>13.16 (n/a)</td><td>13.38 (n/a)</td><td>12.71 (n/a)</td><td>0.40 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>24.96 (-0.72%)</td><td>24.59 (-0.15%)</td><td>24.68 (+0.07%)</td><td>24.14 (+0.64%)</td><td>0.31 <b>(-30.30%)</b></td><td>24.94 (-0.72%)</td><td>24.58 (-0.15%)</td><td>24.66 (+0.07%)</td><td>24.12 (+0.64%)</td><td>0.31 <b>(-30.30%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>25.14 (n/a)</td><td>24.63 (n/a)</td><td>24.66 (n/a)</td><td>23.99 (n/a)</td><td>0.44 (n/a)</td><td>25.13 (n/a)</td><td>24.62 (n/a)</td><td>24.65 (n/a)</td><td>23.97 (n/a)</td><td>0.44 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>42.42 (+1.10%)</td><td>41.16 (+0.78%)</td><td>40.89 (-0.73%)</td><td>39.54 (+1.41%)</td><td>1.22 (+4.51%)</td><td>42.39 (+1.10%)</td><td>41.13 (+0.78%)</td><td>40.87 (-0.73%)</td><td>39.52 (+1.41%)</td><td>1.22 (+4.51%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>41.96 (n/a)</td><td>40.84 (n/a)</td><td>41.19 (n/a)</td><td>38.99 (n/a)</td><td>1.17 (n/a)</td><td>41.93 (n/a)</td><td>40.81 (n/a)</td><td>41.16 (n/a)</td><td>38.97 (n/a)</td><td>1.17 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>44.52 (-2.92%)</td><td>43.96 (-1.09%)</td><td>43.77 (-2.47%)</td><td>43.37 (+3.37%)</td><td>0.48 <b>(-67.83%)</b></td><td>44.49 (-2.92%)</td><td>43.93 (-1.09%)</td><td>43.74 (-2.47%)</td><td>43.34 (+3.37%)</td><td>0.48 <b>(-67.83%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>45.86 (n/a)</td><td>44.44 (n/a)</td><td>44.88 (n/a)</td><td>41.96 (n/a)</td><td>1.48 (n/a)</td><td>45.83 (n/a)</td><td>44.42 (n/a)</td><td>44.85 (n/a)</td><td>41.93 (n/a)</td><td>1.48 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>9.98 (-0.21%)</td><td>9.30 (+2.81%)</td><td>9.31 (+2.23%)</td><td>8.53 (+6.33%)</td><td>0.55 <b>(-23.77%)</b></td><td>9.96 (-0.21%)</td><td>9.28 (+2.81%)</td><td>9.29 (+2.23%)</td><td>8.51 (+6.33%)</td><td>0.55 <b>(-23.77%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>10.00 (n/a)</td><td>9.04 (n/a)</td><td>9.10 (n/a)</td><td>8.02 (n/a)</td><td>0.72 (n/a)</td><td>9.98 (n/a)</td><td>9.03 (n/a)</td><td>9.09 (n/a)</td><td>8.00 (n/a)</td><td>0.72 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>1.03 (-4.15%)</td><td>0.89 (-8.61%)</td><td>0.93 (-0.49%)</td><td>0.75 (-15.53%)</td><td>0.11 <b>(+24.39%)</b></td><td>1.01 (-4.15%)</td><td>0.88 (-8.61%)</td><td>0.92 (-0.49%)</td><td>0.74 (-15.53%)</td><td>0.11 <b>(+24.39%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>1.07 (n/a)</td><td>0.98 (n/a)</td><td>0.94 (n/a)</td><td>0.89 (n/a)</td><td>0.09 (n/a)</td><td>1.05 (n/a)</td><td>0.96 (n/a)</td><td>0.92 (n/a)</td><td>0.87 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>1.51 (+8.43%)</td><td>1.32 (+4.66%)</td><td>1.30 (+1.60%)</td><td>1.10 (-2.86%)</td><td>0.16 <b>(+40.25%)</b></td><td>1.50 (+8.43%)</td><td>1.30 (+4.66%)</td><td>1.28 (+1.60%)</td><td>1.09 (-2.86%)</td><td>0.15 <b>(+40.25%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>1.40 (n/a)</td><td>1.26 (n/a)</td><td>1.28 (n/a)</td><td>1.13 (n/a)</td><td>0.11 (n/a)</td><td>1.38 (n/a)</td><td>1.24 (n/a)</td><td>1.26 (n/a)</td><td>1.12 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>17.85 (-9.02%)</td><td>16.59 (-5.35%)</td><td>16.73 (-9.55%)</td><td>13.99 (+5.34%)</td><td>1.57 <b>(-38.96%)</b></td><td>17.64 (-9.02%)</td><td>16.40 (-5.35%)</td><td>16.54 (-9.55%)</td><td>13.83 (+5.34%)</td><td>1.55 <b>(-38.96%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>19.62 (n/a)</td><td>17.53 (n/a)</td><td>18.50 (n/a)</td><td>13.28 (n/a)</td><td>2.57 (n/a)</td><td>19.39 (n/a)</td><td>17.33 (n/a)</td><td>18.29 (n/a)</td><td>13.13 (n/a)</td><td>2.54 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>14.09 (-0.29%)</td><td>13.58 (-0.76%)</td><td>13.60 (-0.31%)</td><td>12.66 (-5.02%)</td><td>0.58 <b>(+84.47%)</b></td><td>13.84 (-0.29%)</td><td>13.35 (-0.76%)</td><td>13.36 (-0.31%)</td><td>12.44 (-5.02%)</td><td>0.57 <b>(+84.47%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>14.13 (n/a)</td><td>13.69 (n/a)</td><td>13.64 (n/a)</td><td>13.33 (n/a)</td><td>0.31 (n/a)</td><td>13.88 (n/a)</td><td>13.45 (n/a)</td><td>13.40 (n/a)</td><td>13.10 (n/a)</td><td>0.31 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>9.85 (+3.26%)</td><td>8.38 (+4.17%)</td><td>7.92 (+5.87%)</td><td>7.61 <b>(+21.00%)</b></td><td>0.93 <b>(-33.81%)</b></td><td>9.68 (+3.26%)</td><td>8.23 (+4.17%)</td><td>7.78 (+5.87%)</td><td>7.48 <b>(+21.00%)</b></td><td>0.91 <b>(-33.81%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>9.54 (n/a)</td><td>8.04 (n/a)</td><td>7.48 (n/a)</td><td>6.29 (n/a)</td><td>1.40 (n/a)</td><td>9.37 (n/a)</td><td>7.90 (n/a)</td><td>7.35 (n/a)</td><td>6.18 (n/a)</td><td>1.38 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>6.14 (-11.02%)</td><td>5.30 (-15.43%)</td><td>4.98 (-19.80%)</td><td>4.53 (-17.06%)</td><td>0.78 <b>(+29.24%)</b></td><td>6.04 (-11.02%)</td><td>5.22 (-15.43%)</td><td>4.90 (-19.80%)</td><td>4.46 (-17.06%)</td><td>0.77 <b>(+29.24%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>6.90 (n/a)</td><td>6.27 (n/a)</td><td>6.21 (n/a)</td><td>5.46 (n/a)</td><td>0.60 (n/a)</td><td>6.79 (n/a)</td><td>6.17 (n/a)</td><td>6.11 (n/a)</td><td>5.38 (n/a)</td><td>0.59 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>13.14 (n/a)</td><td>12.40 (n/a)</td><td>12.19 (n/a)</td><td>12.04 (n/a)</td><td>0.45 (n/a)</td><td>13.13 (n/a)</td><td>12.39 (n/a)</td><td>12.18 (n/a)</td><td>12.04 (n/a)</td><td>0.45 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>13.17 (n/a)</td><td>12.59 (n/a)</td><td>12.67 (n/a)</td><td>11.84 (n/a)</td><td>0.60 (n/a)</td><td>13.16 (n/a)</td><td>12.58 (n/a)</td><td>12.66 (n/a)</td><td>11.84 (n/a)</td><td>0.60 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/layer_norm</summary>


### test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>170.90 (n/a)</td><td>133.02 (n/a)</td><td>126.40 (n/a)</td><td>117.10 (n/a)</td><td>21.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>159.50 (n/a)</td><td>144.26 (n/a)</td><td>147.10 (n/a)</td><td>121.10 (n/a)</td><td>14.10 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>190.40 (n/a)</td><td>152.26 (n/a)</td><td>147.60 (n/a)</td><td>124.70 (n/a)</td><td>28.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>185.40 (n/a)</td><td>161.10 (n/a)</td><td>154.10 (n/a)</td><td>147.00 (n/a)</td><td>16.51 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>180.20 (n/a)</td><td>157.62 (n/a)</td><td>159.00 (n/a)</td><td>132.10 (n/a)</td><td>20.55 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>177.00 (n/a)</td><td>160.18 (n/a)</td><td>157.50 (n/a)</td><td>138.70 (n/a)</td><td>15.89 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>207.90 (n/a)</td><td>167.82 (n/a)</td><td>153.80 (n/a)</td><td>134.30 (n/a)</td><td>35.84 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>238.50 (n/a)</td><td>205.10 (n/a)</td><td>204.50 (n/a)</td><td>179.70 (n/a)</td><td>25.72 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>184.80 (n/a)</td><td>166.40 (n/a)</td><td>174.10 (n/a)</td><td>123.40 (n/a)</td><td>24.71 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>149.10 (n/a)</td><td>132.58 (n/a)</td><td>129.30 (n/a)</td><td>116.80 (n/a)</td><td>14.67 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.30 (n/a)</td><td>148.54 (n/a)</td><td>128.80 (n/a)</td><td>124.40 (n/a)</td><td>30.06 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.30 (n/a)</td><td>164.76 (n/a)</td><td>169.70 (n/a)</td><td>127.10 (n/a)</td><td>36.64 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.00 (n/a)</td><td>150.72 (n/a)</td><td>131.60 (n/a)</td><td>126.80 (n/a)</td><td>32.22 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>246.20 (n/a)</td><td>194.48 (n/a)</td><td>191.50 (n/a)</td><td>133.30 (n/a)</td><td>47.84 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>274.40 (n/a)</td><td>192.06 (n/a)</td><td>185.80 (n/a)</td><td>134.60 (n/a)</td><td>58.24 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>286.50 (n/a)</td><td>215.42 (n/a)</td><td>205.50 (n/a)</td><td>168.10 (n/a)</td><td>49.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>212.70 (n/a)</td><td>161.94 (n/a)</td><td>162.30 (n/a)</td><td>126.20 (n/a)</td><td>35.19 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>178.30 (n/a)</td><td>138.72 (n/a)</td><td>131.60 (n/a)</td><td>117.90 (n/a)</td><td>23.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>174.00 (n/a)</td><td>167.82 (n/a)</td><td>173.70 (n/a)</td><td>147.30 (n/a)</td><td>11.58 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>203.20 (n/a)</td><td>161.08 (n/a)</td><td>168.70 (n/a)</td><td>114.00 (n/a)</td><td>32.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>223.40 (n/a)</td><td>162.60 (n/a)</td><td>163.60 (n/a)</td><td>116.40 (n/a)</td><td>44.03 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>197.70 (n/a)</td><td>170.02 (n/a)</td><td>172.90 (n/a)</td><td>146.70 (n/a)</td><td>20.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>281.70 (n/a)</td><td>194.68 (n/a)</td><td>170.50 (n/a)</td><td>156.60 (n/a)</td><td>50.96 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>312.20 (n/a)</td><td>231.22 (n/a)</td><td>221.00 (n/a)</td><td>191.90 (n/a)</td><td>46.88 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>186.60 (n/a)</td><td>154.80 (n/a)</td><td>152.80 (n/a)</td><td>120.40 (n/a)</td><td>24.19 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>323.90 (n/a)</td><td>187.12 (n/a)</td><td>170.50 (n/a)</td><td>116.20 (n/a)</td><td>82.33 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>233.70 (n/a)</td><td>183.94 (n/a)</td><td>196.90 (n/a)</td><td>123.80 (n/a)</td><td>47.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>201.20 (n/a)</td><td>156.12 (n/a)</td><td>136.20 (n/a)</td><td>126.70 (n/a)</td><td>33.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>250.20 (n/a)</td><td>187.98 (n/a)</td><td>184.20 (n/a)</td><td>146.10 (n/a)</td><td>39.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>184.20 (n/a)</td><td>162.00 (n/a)</td><td>163.50 (n/a)</td><td>133.50 (n/a)</td><td>19.64 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>198.00 (n/a)</td><td>164.24 (n/a)</td><td>169.40 (n/a)</td><td>122.90 (n/a)</td><td>31.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>227.00 (n/a)</td><td>197.78 (n/a)</td><td>191.50 (n/a)</td><td>174.20 (n/a)</td><td>23.30 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/leaky_relu</summary>


### test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (+0.97%)</td><td>0.02 (+9.43%)</td><td>0.02 (+7.28%)</td><td>0.02 <b>(+32.29%)</b></td><td>0.00 <b>(-57.71%)</b></td><td>175.80 <b>(-24.42%)</b></td><td>165.48 (-10.60%)</td><td>169.30 (-6.77%)</td><td>150.60 (-0.99%)</td><td>10.87 <b>(-67.68%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.60 (n/a)</td><td>185.10 (n/a)</td><td>181.60 (n/a)</td><td>152.10 (n/a)</td><td>33.62 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (+2.06%)</td><td>0.03 (-5.37%)</td><td>0.02 (-14.79%)</td><td>0.02 (+7.58%)</td><td>0.01 (+4.87%)</td><td>202.20 (-7.03%)</td><td>163.02 (+5.51%)</td><td>170.20 (+17.38%)</td><td>114.90 (-1.96%)</td><td>34.09 (-9.53%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>217.50 (n/a)</td><td>154.50 (n/a)</td><td>145.00 (n/a)</td><td>117.20 (n/a)</td><td>37.68 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (+0.50%)</td><td>0.02 (-7.64%)</td><td>0.02 (-11.11%)</td><td>0.02 (+2.54%)</td><td>0.00 (+6.38%)</td><td>204.50 (-2.48%)</td><td>174.28 (+8.49%)</td><td>174.50 (+12.51%)</td><td>129.80 (-0.54%)</td><td>30.37 (+1.35%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.70 (n/a)</td><td>160.64 (n/a)</td><td>155.10 (n/a)</td><td>130.50 (n/a)</td><td>29.97 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (-9.10%)</td><td>0.02 (-6.83%)</td><td>0.03 (+0.17%)</td><td>0.02 <b>(-25.61%)</b></td><td>0.00 <b>(+51.89%)</b></td><td>229.90 <b>(+34.37%)</b></td><td>170.14 (+9.56%)</td><td>157.70 (-0.19%)</td><td>143.30 (+9.98%)</td><td>35.21 <b>(+134.14%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>171.10 (n/a)</td><td>155.30 (n/a)</td><td>158.00 (n/a)</td><td>130.30 (n/a)</td><td>15.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (+10.63%)</td><td>0.02 (+3.76%)</td><td>0.03 (+3.52%)</td><td>0.02 (-0.31%)</td><td>0.00 <b>(+44.74%)</b></td><td>201.30 (+0.30%)</td><td>166.46 (-2.92%)</td><td>159.40 (-3.39%)</td><td>138.20 (-9.55%)</td><td>23.56 <b>(+30.12%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>200.70 (n/a)</td><td>171.46 (n/a)</td><td>165.00 (n/a)</td><td>152.80 (n/a)</td><td>18.11 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (-6.64%)</td><td>0.02 (-9.23%)</td><td>0.02 (-5.22%)</td><td>0.02 (-14.99%)</td><td>0.00 (+11.90%)</td><td>219.00 (+17.62%)</td><td>186.62 (+10.79%)</td><td>183.70 (+5.45%)</td><td>154.40 (+7.15%)</td><td>26.04 <b>(+40.65%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>186.20 (n/a)</td><td>168.44 (n/a)</td><td>174.20 (n/a)</td><td>144.10 (n/a)</td><td>18.51 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.02 (-2.23%)</td><td>0.02 (-1.24%)</td><td>0.02 (+1.18%)</td><td>0.02 (-6.06%)</td><td>0.00 (+17.69%)</td><td>211.40 (+6.45%)</td><td>191.04 (+1.42%)</td><td>189.30 (-1.15%)</td><td>172.90 (+2.25%)</td><td>14.73 <b>(+30.37%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>198.60 (n/a)</td><td>188.36 (n/a)</td><td>191.50 (n/a)</td><td>169.10 (n/a)</td><td>11.30 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 <b>(+55.93%)</b></td><td>0.02 (+4.05%)</td><td>0.02 (+12.78%)</td><td>0.01 <b>(-31.21%)</b></td><td>0.01 <b>(+1427.28%)</b></td><td>329.10 <b>(+45.36%)</b></td><td>234.50 (+8.08%)</td><td>190.80 (-11.34%)</td><td>135.60 <b>(-35.89%)</b></td><td>88.71 <b>(+1443.77%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>226.40 (n/a)</td><td>216.96 (n/a)</td><td>215.20 (n/a)</td><td>211.50 (n/a)</td><td>5.75 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 (+7.81%)</td><td>0.05 (-1.72%)</td><td>0.05 (-1.29%)</td><td>0.05 (-0.84%)</td><td>0.01 <b>(+25.75%)</b></td><td>178.90 (+0.85%)</td><td>157.44 (+2.41%)</td><td>161.00 (+1.32%)</td><td>118.20 (-7.29%)</td><td>23.45 (+15.05%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>177.40 (n/a)</td><td>153.74 (n/a)</td><td>158.90 (n/a)</td><td>127.50 (n/a)</td><td>20.38 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 <b>(+26.37%)</b></td><td>0.05 (+12.97%)</td><td>0.05 (-8.97%)</td><td>0.04 <b>(+64.08%)</b></td><td>0.01 (-8.86%)</td><td>189.90 <b>(-39.06%)</b></td><td>163.74 (-15.25%)</td><td>174.60 (+9.88%)</td><td>119.30 <b>(-20.84%)</b></td><td>28.59 <b>(-57.68%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>311.60 (n/a)</td><td>193.20 (n/a)</td><td>158.90 (n/a)</td><td>150.70 (n/a)</td><td>67.55 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 <b>(-24.77%)</b></td><td>0.05 (+1.00%)</td><td>0.05 (+8.55%)</td><td>0.05 <b>(+35.68%)</b></td><td>0.00 <b>(-82.80%)</b></td><td>172.10 <b>(-26.30%)</b></td><td>164.84 (-6.54%)</td><td>165.90 (-7.88%)</td><td>153.00 <b>(+32.93%)</b></td><td>7.79 <b>(-82.91%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.50 (n/a)</td><td>176.38 (n/a)</td><td>180.10 (n/a)</td><td>115.10 (n/a)</td><td>45.56 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (-18.50%)</td><td>0.05 (-13.67%)</td><td>0.05 (-8.28%)</td><td>0.04 (-16.37%)</td><td>0.01 <b>(-22.55%)</b></td><td>203.60 (+19.55%)</td><td>177.14 (+15.72%)</td><td>170.40 (+9.02%)</td><td>155.00 <b>(+22.63%)</b></td><td>19.43 (+16.63%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>170.30 (n/a)</td><td>153.08 (n/a)</td><td>156.30 (n/a)</td><td>126.40 (n/a)</td><td>16.66 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 <b>(+20.01%)</b></td><td>0.05 (-8.67%)</td><td>0.04 <b>(-25.27%)</b></td><td>0.02 <b>(-51.40%)</b></td><td>0.02 <b>(+378.81%)</b></td><td>348.40 <b>(+105.79%)</b></td><td>200.52 <b>(+30.02%)</b></td><td>209.10 <b>(+33.87%)</b></td><td>114.20 (-16.70%)</td><td>96.31 <b>(+649.50%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>169.30 (n/a)</td><td>154.22 (n/a)</td><td>156.20 (n/a)</td><td>137.10 (n/a)</td><td>12.85 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (-8.66%)</td><td>0.05 (-10.70%)</td><td>0.05 (-10.92%)</td><td>0.04 (-10.21%)</td><td>0.01 (-16.41%)</td><td>223.10 (+11.38%)</td><td>176.78 (+11.66%)</td><td>167.10 (+12.22%)</td><td>147.40 (+9.51%)</td><td>29.04 (+4.90%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.30 (n/a)</td><td>158.32 (n/a)</td><td>148.90 (n/a)</td><td>134.60 (n/a)</td><td>27.68 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (-6.74%)</td><td>0.04 (-6.59%)</td><td>0.04 (-14.40%)</td><td>0.04 (-6.76%)</td><td>0.01 (-12.08%)</td><td>227.70 (+7.20%)</td><td>193.88 (+6.76%)</td><td>200.50 (+16.84%)</td><td>158.10 (+7.26%)</td><td>27.33 (-2.72%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.40 (n/a)</td><td>181.60 (n/a)</td><td>171.60 (n/a)</td><td>147.40 (n/a)</td><td>28.09 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 <b>(+25.52%)</b></td><td>0.05 (-4.57%)</td><td>0.04 (-15.91%)</td><td>0.04 (-12.82%)</td><td>0.01 <b>(+173.14%)</b></td><td>222.40 (+14.70%)</td><td>192.72 (+10.08%)</td><td>212.40 (+18.92%)</td><td>116.70 <b>(-20.29%)</b></td><td>43.26 <b>(+146.11%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.90 (n/a)</td><td>175.08 (n/a)</td><td>178.60 (n/a)</td><td>146.40 (n/a)</td><td>17.58 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 <b>(-28.58%)</b></td><td>0.05 (-5.62%)</td><td>0.05 (+0.14%)</td><td>0.04 (+12.46%)</td><td>0.00 <b>(-74.26%)</b></td><td>194.80 (-11.09%)</td><td>176.36 (+1.19%)</td><td>170.20 (-0.18%)</td><td>162.10 <b>(+40.10%)</b></td><td>13.17 <b>(-67.72%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.10 (n/a)</td><td>174.28 (n/a)</td><td>170.50 (n/a)</td><td>115.70 (n/a)</td><td>40.81 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (-7.22%)</td><td>0.04 (-6.64%)</td><td>0.04 (-10.77%)</td><td>0.02 (-10.10%)</td><td>0.01 (-11.39%)</td><td>330.60 (+11.24%)</td><td>235.34 (+7.06%)</td><td>219.40 (+12.05%)</td><td>193.80 (+7.79%)</td><td>54.44 (+11.30%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>297.20 (n/a)</td><td>219.82 (n/a)</td><td>195.80 (n/a)</td><td>179.80 (n/a)</td><td>48.92 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.14 (+16.76%)</td><td>0.11 (-2.36%)</td><td>0.10 (-10.62%)</td><td>0.09 (+7.65%)</td><td>0.02 <b>(+27.91%)</b></td><td>179.80 (-7.13%)</td><td>154.70 (+2.85%)</td><td>158.10 (+11.89%)</td><td>115.30 (-14.34%)</td><td>23.83 (-3.55%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>193.60 (n/a)</td><td>150.42 (n/a)</td><td>141.30 (n/a)</td><td>134.60 (n/a)</td><td>24.70 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.12 (+2.45%)</td><td>0.11 (+7.24%)</td><td>0.10 (+6.57%)</td><td>0.10 (+13.15%)</td><td>0.01 (-19.92%)</td><td>166.70 (-11.66%)</td><td>152.02 (-7.33%)</td><td>158.50 (-6.16%)</td><td>133.30 (-2.42%)</td><td>14.64 <b>(-30.80%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>188.70 (n/a)</td><td>164.04 (n/a)</td><td>168.90 (n/a)</td><td>136.60 (n/a)</td><td>21.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.16 <b>(+26.61%)</b></td><td>0.11 (+0.83%)</td><td>0.10 (-12.47%)</td><td>0.09 (-2.46%)</td><td>0.03 <b>(+88.59%)</b></td><td>186.00 (+2.54%)</td><td>156.70 (+2.10%)</td><td>164.70 (+14.22%)</td><td>103.60 <b>(-21.04%)</b></td><td>33.60 <b>(+49.89%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>181.40 (n/a)</td><td>153.48 (n/a)</td><td>144.20 (n/a)</td><td>131.20 (n/a)</td><td>22.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.15 <b>(+22.12%)</b></td><td>0.10 (+9.32%)</td><td>0.09 (+0.33%)</td><td>0.07 (+13.69%)</td><td>0.03 <b>(+28.84%)</b></td><td>230.70 (-12.05%)</td><td>175.56 (-7.88%)</td><td>175.30 (-0.34%)</td><td>110.40 (-18.10%)</td><td>44.53 (-11.44%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>262.30 (n/a)</td><td>190.58 (n/a)</td><td>175.90 (n/a)</td><td>134.80 (n/a)</td><td>50.28 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.15 <b>(+46.20%)</b></td><td>0.11 (+14.07%)</td><td>0.12 <b>(+21.11%)</b></td><td>0.07 (-17.10%)</td><td>0.03 <b>(+507.32%)</b></td><td>221.10 <b>(+20.62%)</b></td><td>158.50 (-7.18%)</td><td>138.20 (-17.44%)</td><td>110.80 <b>(-31.56%)</b></td><td>44.00 <b>(+408.83%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.00 (n/a)</td><td>183.30 (n/a)</td><td>170.76 (n/a)</td><td>167.40 (n/a)</td><td>161.90 (n/a)</td><td>8.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.13 <b>(+28.88%)</b></td><td>0.09 (+3.32%)</td><td>0.09 (+1.45%)</td><td>0.07 (-9.00%)</td><td>0.02 <b>(+186.62%)</b></td><td>227.00 (+9.93%)</td><td>181.66 (+0.31%)</td><td>176.40 (-1.40%)</td><td>126.90 <b>(-22.39%)</b></td><td>39.49 <b>(+142.90%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>206.50 (n/a)</td><td>181.10 (n/a)</td><td>178.90 (n/a)</td><td>163.50 (n/a)</td><td>16.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.12 (+15.26%)</td><td>0.09 (+11.35%)</td><td>0.08 (-8.59%)</td><td>0.08 <b>(+40.72%)</b></td><td>0.02 (+0.40%)</td><td>218.10 <b>(-28.93%)</b></td><td>180.52 (-12.05%)</td><td>194.30 (+9.40%)</td><td>140.40 (-13.23%)</td><td>34.76 <b>(-41.23%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>306.90 (n/a)</td><td>205.26 (n/a)</td><td>177.60 (n/a)</td><td>161.80 (n/a)</td><td>59.14 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.10 (+1.32%)</td><td>0.07 (-9.88%)</td><td>0.07 (-8.26%)</td><td>0.05 <b>(-29.67%)</b></td><td>0.02 <b>(+70.68%)</b></td><td>341.80 <b>(+42.18%)</b></td><td>245.78 (+15.28%)</td><td>239.10 (+8.98%)</td><td>169.70 (-1.28%)</td><td>62.69 <b>(+146.79%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>240.40 (n/a)</td><td>213.20 (n/a)</td><td>219.40 (n/a)</td><td>171.90 (n/a)</td><td>25.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.28 (+1.66%)</td><td>0.19 (-10.52%)</td><td>0.20 (-8.47%)</td><td>0.10 (-9.08%)</td><td>0.07 (+5.21%)</td><td>336.60 (+9.96%)</td><td>197.26 (+13.20%)</td><td>167.10 (+9.29%)</td><td>116.20 (-1.61%)</td><td>83.59 (+10.90%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>306.10 (n/a)</td><td>174.26 (n/a)</td><td>152.90 (n/a)</td><td>118.10 (n/a)</td><td>75.37 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.28 (+17.16%)</td><td>0.21 (+1.75%)</td><td>0.20 (-1.41%)</td><td>0.15 (-7.44%)</td><td>0.05 <b>(+87.58%)</b></td><td>213.30 (+8.05%)</td><td>167.00 (+1.79%)</td><td>168.00 (+1.45%)</td><td>116.80 (-14.68%)</td><td>40.84 <b>(+75.18%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>197.40 (n/a)</td><td>164.06 (n/a)</td><td>165.60 (n/a)</td><td>136.90 (n/a)</td><td>23.31 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.20 (-15.80%)</td><td>0.19 (-4.90%)</td><td>0.19 (-1.31%)</td><td>0.18 (+14.40%)</td><td>0.01 <b>(-76.94%)</b></td><td>183.10 (-12.60%)</td><td>174.58 (+3.19%)</td><td>175.60 (+1.33%)</td><td>165.00 (+18.79%)</td><td>6.50 <b>(-76.09%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>209.50 (n/a)</td><td>169.18 (n/a)</td><td>173.30 (n/a)</td><td>138.90 (n/a)</td><td>27.17 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.21 <b>(-21.25%)</b></td><td>0.18 (-16.58%)</td><td>0.18 (-5.39%)</td><td>0.14 (-17.45%)</td><td>0.03 <b>(-41.73%)</b></td><td>239.90 <b>(+21.16%)</b></td><td>186.16 (+18.03%)</td><td>179.00 (+5.67%)</td><td>157.20 <b>(+26.98%)</b></td><td>31.73 (-2.81%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>198.00 (n/a)</td><td>157.72 (n/a)</td><td>169.40 (n/a)</td><td>123.80 (n/a)</td><td>32.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.22 (+8.04%)</td><td>0.16 (-7.90%)</td><td>0.17 (-1.97%)</td><td>0.12 <b>(-29.74%)</b></td><td>0.04 <b>(+116.41%)</b></td><td>283.40 <b>(+42.34%)</b></td><td>207.84 (+12.74%)</td><td>198.40 (+2.01%)</td><td>148.00 (-7.44%)</td><td>50.06 <b>(+185.09%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>199.10 (n/a)</td><td>184.36 (n/a)</td><td>194.50 (n/a)</td><td>159.90 (n/a)</td><td>17.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.20 <b>(-23.40%)</b></td><td>0.18 (-3.84%)</td><td>0.18 (+1.76%)</td><td>0.16 <b>(+20.12%)</b></td><td>0.02 <b>(-60.67%)</b></td><td>209.00 (-16.73%)</td><td>184.96 (+0.02%)</td><td>177.90 (-1.71%)</td><td>164.70 <b>(+30.61%)</b></td><td>19.40 <b>(-56.34%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>251.00 (n/a)</td><td>184.92 (n/a)</td><td>181.00 (n/a)</td><td>126.10 (n/a)</td><td>44.44 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.20 (+11.95%)</td><td>0.16 (+5.44%)</td><td>0.15 (-0.32%)</td><td>0.14 <b>(+34.18%)</b></td><td>0.03 (-12.70%)</td><td>236.40 <b>(-25.47%)</b></td><td>209.84 (-6.99%)</td><td>217.70 (+0.32%)</td><td>160.30 (-10.65%)</td><td>28.97 <b>(-46.04%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>317.20 (n/a)</td><td>225.62 (n/a)</td><td>217.00 (n/a)</td><td>179.40 (n/a)</td><td>53.69 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/mem_copy</summary>


### test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (-13.88%)</td><td>0.03 (-9.72%)</td><td>0.03 (-17.88%)</td><td>0.02 <b>(+21.29%)</b></td><td>0.00 <b>(-54.94%)</b></td><td>174.80 (-17.55%)</td><td>151.30 (+6.03%)</td><td>149.20 <b>(+21.80%)</b></td><td>129.10 (+16.10%)</td><td>17.51 <b>(-57.55%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>212.00 (n/a)</td><td>142.70 (n/a)</td><td>122.50 (n/a)</td><td>111.20 (n/a)</td><td>41.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (+8.47%)</td><td>0.03 (-2.32%)</td><td>0.02 (-10.33%)</td><td>0.02 (+11.30%)</td><td>0.01 (+7.46%)</td><td>191.10 (-10.16%)</td><td>161.30 (+2.17%)</td><td>168.20 (+11.54%)</td><td>116.20 (-7.78%)</td><td>29.39 (-13.59%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>212.70 (n/a)</td><td>157.88 (n/a)</td><td>150.80 (n/a)</td><td>126.00 (n/a)</td><td>34.01 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_False-tile_size_64]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4746217.00 (n/a)</td><td>4746129.75 (n/a)</td><td>4746129.75 (n/a)</td><td>4746042.50 (n/a)</td><td>123.39 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_True-tile_size_64]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.02 (+12.35%)</td><td>0.02 (+11.90%)</td><td>0.02 (+10.19%)</td><td>0.02 <b>(+30.42%)</b></td><td>0.00 <b>(-24.08%)</b></td><td>227.80 <b>(-23.33%)</b></td><td>202.60 (-12.06%)</td><td>202.00 (-9.25%)</td><td>168.30 (-10.95%)</td><td>22.30 <b>(-48.74%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>297.10 (n/a)</td><td>230.38 (n/a)</td><td>222.60 (n/a)</td><td>189.00 (n/a)</td><td>43.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (+2.80%)</td><td>0.02 (-4.83%)</td><td>0.02 (-17.61%)</td><td>0.02 (+7.73%)</td><td>0.00 <b>(-22.15%)</b></td><td>184.30 (-7.15%)</td><td>170.86 (+4.16%)</td><td>178.40 <b>(+21.36%)</b></td><td>139.00 (-2.73%)</td><td>18.18 <b>(-30.43%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>198.50 (n/a)</td><td>164.04 (n/a)</td><td>147.00 (n/a)</td><td>142.90 (n/a)</td><td>26.13 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (+15.70%)</td><td>0.03 <b>(+20.81%)</b></td><td>0.03 (+4.80%)</td><td>0.02 <b>(+88.05%)</b></td><td>0.01 (-12.43%)</td><td>194.80 <b>(-46.82%)</b></td><td>153.24 <b>(-23.84%)</b></td><td>151.70 (-4.53%)</td><td>114.30 (-13.61%)</td><td>36.43 <b>(-61.84%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>366.30 (n/a)</td><td>201.20 (n/a)</td><td>158.90 (n/a)</td><td>132.30 (n/a)</td><td>95.45 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (-10.09%)</td><td>0.03 (+3.99%)</td><td>0.03 (+7.32%)</td><td>0.02 (+16.63%)</td><td>0.00 <b>(-54.70%)</b></td><td>167.00 (-14.27%)</td><td>147.96 (-5.90%)</td><td>147.60 (-6.82%)</td><td>135.10 (+11.19%)</td><td>12.36 <b>(-56.49%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>194.80 (n/a)</td><td>157.24 (n/a)</td><td>158.40 (n/a)</td><td>121.50 (n/a)</td><td>28.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 <b>(+21.75%)</b></td><td>0.03 (+0.63%)</td><td>0.03 (+2.46%)</td><td>0.02 (-15.62%)</td><td>0.01 <b>(+202.73%)</b></td><td>204.10 (+18.52%)</td><td>159.58 (+2.49%)</td><td>153.90 (-2.41%)</td><td>118.30 (-17.90%)</td><td>33.13 <b>(+197.47%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>172.20 (n/a)</td><td>155.70 (n/a)</td><td>157.70 (n/a)</td><td>144.10 (n/a)</td><td>11.14 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_False-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (-1.32%)</td><td>0.02 (-3.68%)</td><td>0.02 (+1.40%)</td><td>0.02 (-4.09%)</td><td>0.01 (+13.36%)</td><td>259.30 (+4.26%)</td><td>192.84 (+5.04%)</td><td>179.10 (-1.43%)</td><td>148.80 (+1.36%)</td><td>47.97 (+18.04%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>248.70 (n/a)</td><td>183.58 (n/a)</td><td>181.70 (n/a)</td><td>146.80 (n/a)</td><td>40.64 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_True-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (-9.26%)</td><td>0.02 (-4.06%)</td><td>0.02 (-4.14%)</td><td>0.02 (+8.60%)</td><td>0.00 <b>(-30.13%)</b></td><td>214.10 (-7.95%)</td><td>184.78 (+2.99%)</td><td>181.30 (+4.32%)</td><td>160.30 (+10.25%)</td><td>22.34 <b>(-31.09%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.60 (n/a)</td><td>179.42 (n/a)</td><td>173.80 (n/a)</td><td>145.40 (n/a)</td><td>32.42 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_False-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (-15.34%)</td><td>0.02 (-10.81%)</td><td>0.02 (+0.01%)</td><td>0.02 <b>(-27.61%)</b></td><td>0.01 (+11.57%)</td><td>266.20 <b>(+38.14%)</b></td><td>189.30 (+15.16%)</td><td>169.40 (+0.00%)</td><td>143.40 (+18.12%)</td><td>51.04 <b>(+85.48%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>192.70 (n/a)</td><td>164.38 (n/a)</td><td>169.40 (n/a)</td><td>121.40 (n/a)</td><td>27.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_True-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (+1.51%)</td><td>0.02 (-8.19%)</td><td>0.02 (-11.84%)</td><td>0.02 <b>(-20.01%)</b></td><td>0.00 <b>(+107.95%)</b></td><td>229.40 <b>(+25.01%)</b></td><td>190.86 (+10.81%)</td><td>199.80 (+13.46%)</td><td>154.40 (-1.47%)</td><td>30.59 <b>(+151.17%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>183.50 (n/a)</td><td>172.24 (n/a)</td><td>176.10 (n/a)</td><td>156.70 (n/a)</td><td>12.18 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_False-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.02 (-17.83%)</td><td>0.02 (-5.20%)</td><td>0.02 (-15.50%)</td><td>0.02 <b>(+37.15%)</b></td><td>0.00 <b>(-66.13%)</b></td><td>234.40 <b>(-27.09%)</b></td><td>200.90 (-3.23%)</td><td>202.60 (+18.34%)</td><td>174.60 <b>(+21.67%)</b></td><td>23.27 <b>(-69.62%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>321.50 (n/a)</td><td>207.60 (n/a)</td><td>171.20 (n/a)</td><td>143.50 (n/a)</td><td>76.61 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_True-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (+11.95%)</td><td>0.02 (+9.83%)</td><td>0.02 (-7.08%)</td><td>0.02 (+10.40%)</td><td>0.01 <b>(+43.38%)</b></td><td>210.80 (-9.41%)</td><td>173.90 (-7.06%)</td><td>194.70 (+7.63%)</td><td>124.90 (-10.66%)</td><td>41.77 (+15.68%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.70 (n/a)</td><td>187.10 (n/a)</td><td>180.90 (n/a)</td><td>139.80 (n/a)</td><td>36.11 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_False-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (-1.61%)</td><td>0.02 (-4.80%)</td><td>0.02 (-10.93%)</td><td>0.02 (-10.70%)</td><td>0.00 <b>(+34.33%)</b></td><td>222.20 (+12.00%)</td><td>190.62 (+5.97%)</td><td>202.40 (+12.26%)</td><td>155.00 (+1.64%)</td><td>27.25 <b>(+52.11%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>198.40 (n/a)</td><td>179.88 (n/a)</td><td>180.30 (n/a)</td><td>152.50 (n/a)</td><td>17.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_True-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (-3.36%)</td><td>0.02 (+11.69%)</td><td>0.03 (+10.96%)</td><td>0.02 <b>(+23.24%)</b></td><td>0.00 <b>(-44.87%)</b></td><td>192.70 (-18.86%)</td><td>169.80 (-12.72%)</td><td>163.20 (-9.88%)</td><td>154.00 (+3.49%)</td><td>17.61 <b>(-55.86%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>237.50 (n/a)</td><td>194.54 (n/a)</td><td>181.10 (n/a)</td><td>148.80 (n/a)</td><td>39.90 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (-6.18%)</td><td>0.05 (-5.69%)</td><td>0.05 (+0.88%)</td><td>0.04 (-16.42%)</td><td>0.01 <b>(+26.98%)</b></td><td>213.50 (+19.67%)</td><td>175.10 (+7.82%)</td><td>169.60 (-0.88%)</td><td>135.60 (+6.60%)</td><td>34.44 <b>(+69.61%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.40 (n/a)</td><td>162.40 (n/a)</td><td>171.10 (n/a)</td><td>127.20 (n/a)</td><td>20.31 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_True-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 <b>(-27.35%)</b></td><td>0.05 (-12.50%)</td><td>0.04 (-12.11%)</td><td>0.04 (-0.99%)</td><td>0.00 <b>(-58.97%)</b></td><td>196.50 (+0.98%)</td><td>180.38 (+11.91%)</td><td>186.90 (+13.82%)</td><td>161.40 <b>(+37.71%)</b></td><td>16.48 <b>(-41.30%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.60 (n/a)</td><td>161.18 (n/a)</td><td>164.20 (n/a)</td><td>117.20 (n/a)</td><td>28.08 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 <b>(+46.19%)</b></td><td>0.04 <b>(+20.20%)</b></td><td>0.04 (+2.28%)</td><td>0.04 <b>(+40.44%)</b></td><td>0.01 <b>(+52.68%)</b></td><td>233.40 <b>(-28.80%)</b></td><td>198.38 (-16.61%)</td><td>209.50 (-2.19%)</td><td>140.40 <b>(-31.61%)</b></td><td>36.56 <b>(-28.66%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>327.80 (n/a)</td><td>237.88 (n/a)</td><td>214.20 (n/a)</td><td>205.30 (n/a)</td><td>51.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_True-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (+13.27%)</td><td>0.04 (-3.91%)</td><td>0.04 <b>(-21.61%)</b></td><td>0.03 (-2.80%)</td><td>0.01 <b>(+38.68%)</b></td><td>242.20 (+2.89%)</td><td>199.58 (+6.24%)</td><td>219.30 <b>(+27.57%)</b></td><td>130.80 (-11.68%)</td><td>45.58 <b>(+22.60%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.40 (n/a)</td><td>187.86 (n/a)</td><td>171.90 (n/a)</td><td>148.10 (n/a)</td><td>37.18 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (-12.92%)</td><td>0.05 (-11.00%)</td><td>0.05 (+1.71%)</td><td>0.03 <b>(-25.57%)</b></td><td>0.01 <b>(+23.48%)</b></td><td>241.00 <b>(+34.34%)</b></td><td>181.00 (+14.11%)</td><td>162.30 (-1.70%)</td><td>152.80 (+14.80%)</td><td>35.92 <b>(+94.66%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>179.40 (n/a)</td><td>158.62 (n/a)</td><td>165.10 (n/a)</td><td>133.10 (n/a)</td><td>18.45 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 <b>(-27.73%)</b></td><td>0.05 <b>(-23.58%)</b></td><td>0.05 <b>(-26.32%)</b></td><td>0.04 <b>(-21.51%)</b></td><td>0.01 <b>(-42.60%)</b></td><td>233.90 <b>(+27.40%)</b></td><td>185.56 <b>(+29.00%)</b></td><td>180.80 <b>(+35.74%)</b></td><td>156.80 <b>(+38.39%)</b></td><td>30.47 (+0.82%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.60 (n/a)</td><td>143.84 (n/a)</td><td>133.20 (n/a)</td><td>113.30 (n/a)</td><td>30.22 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 (+4.76%)</td><td>0.05 (-1.00%)</td><td>0.05 (-7.24%)</td><td>0.03 (-17.37%)</td><td>0.01 <b>(+64.01%)</b></td><td>245.40 <b>(+21.01%)</b></td><td>171.36 (+5.23%)</td><td>176.90 (+7.80%)</td><td>124.30 (-4.60%)</td><td>49.25 <b>(+81.90%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.80 (n/a)</td><td>162.84 (n/a)</td><td>164.10 (n/a)</td><td>130.30 (n/a)</td><td>27.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 (+6.55%)</td><td>0.05 (-1.58%)</td><td>0.04 (-2.19%)</td><td>0.03 (-8.95%)</td><td>0.01 <b>(+23.20%)</b></td><td>256.00 (+9.82%)</td><td>183.42 (+3.73%)</td><td>186.60 (+2.25%)</td><td>118.20 (-6.12%)</td><td>49.46 <b>(+25.77%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.10 (n/a)</td><td>176.82 (n/a)</td><td>182.50 (n/a)</td><td>125.90 (n/a)</td><td>39.33 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (-4.14%)</td><td>0.05 (+7.10%)</td><td>0.04 (+9.11%)</td><td>0.03 (-0.83%)</td><td>0.01 (+2.43%)</td><td>261.20 (+0.85%)</td><td>188.22 (-6.12%)</td><td>187.70 (-8.35%)</td><td>143.10 (+4.30%)</td><td>47.49 (+9.62%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>259.00 (n/a)</td><td>200.50 (n/a)</td><td>204.80 (n/a)</td><td>137.20 (n/a)</td><td>43.32 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (+2.13%)</td><td>0.04 (-7.43%)</td><td>0.05 (+2.34%)</td><td>0.02 <b>(-38.71%)</b></td><td>0.01 <b>(+89.79%)</b></td><td>354.60 <b>(+63.18%)</b></td><td>209.50 (+17.05%)</td><td>175.00 (-2.29%)</td><td>144.60 (-2.03%)</td><td>84.17 <b>(+219.93%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.30 (n/a)</td><td>178.98 (n/a)</td><td>179.10 (n/a)</td><td>147.60 (n/a)</td><td>26.31 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 <b>(+31.86%)</b></td><td>0.05 (+9.95%)</td><td>0.04 (+1.75%)</td><td>0.04 (+3.37%)</td><td>0.01 <b>(+127.92%)</b></td><td>200.20 (-3.29%)</td><td>174.08 (-6.19%)</td><td>184.10 (-1.71%)</td><td>114.80 <b>(-24.17%)</b></td><td>35.13 <b>(+68.00%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.00 (n/a)</td><td>185.56 (n/a)</td><td>187.30 (n/a)</td><td>151.40 (n/a)</td><td>20.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (-6.97%)</td><td>0.04 (-3.66%)</td><td>0.04 (-10.90%)</td><td>0.04 (+0.83%)</td><td>0.00 (-10.70%)</td><td>228.50 (-0.82%)</td><td>206.44 (+3.57%)</td><td>217.60 (+12.22%)</td><td>180.40 (+7.51%)</td><td>23.64 (-6.93%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.40 (n/a)</td><td>199.32 (n/a)</td><td>193.90 (n/a)</td><td>167.80 (n/a)</td><td>25.40 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (+17.41%)</td><td>0.05 (+15.22%)</td><td>0.05 <b>(+26.86%)</b></td><td>0.04 (+4.19%)</td><td>0.01 <b>(+54.76%)</b></td><td>213.50 (-4.00%)</td><td>172.04 (-12.22%)</td><td>159.10 <b>(-21.20%)</b></td><td>138.90 (-14.84%)</td><td>29.60 <b>(+29.25%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.40 (n/a)</td><td>196.00 (n/a)</td><td>201.90 (n/a)</td><td>163.10 (n/a)</td><td>22.90 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_True-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 <b>(-23.64%)</b></td><td>0.04 (-1.39%)</td><td>0.04 (-1.67%)</td><td>0.04 <b>(+71.84%)</b></td><td>0.00 <b>(-71.69%)</b></td><td>202.60 <b>(-41.80%)</b></td><td>185.22 (-9.01%)</td><td>191.40 (+1.70%)</td><td>160.20 <b>(+30.99%)</b></td><td>17.57 <b>(-79.51%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>348.10 (n/a)</td><td>203.56 (n/a)</td><td>188.20 (n/a)</td><td>122.30 (n/a)</td><td>85.72 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (-1.15%)</td><td>0.05 (+11.25%)</td><td>0.05 <b>(+29.28%)</b></td><td>0.04 <b>(+22.89%)</b></td><td>0.01 <b>(-32.19%)</b></td><td>216.60 (-18.63%)</td><td>184.48 (-12.44%)</td><td>177.60 <b>(-22.65%)</b></td><td>157.60 (+1.16%)</td><td>27.27 <b>(-42.46%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>266.20 (n/a)</td><td>210.68 (n/a)</td><td>229.60 (n/a)</td><td>155.80 (n/a)</td><td>47.39 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_True-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 (+10.52%)</td><td>0.06 <b>(+29.29%)</b></td><td>0.05 <b>(+30.18%)</b></td><td>0.05 <b>(+36.56%)</b></td><td>0.01 (-11.92%)</td><td>175.00 <b>(-26.78%)</b></td><td>148.48 <b>(-24.04%)</b></td><td>153.10 <b>(-23.18%)</b></td><td>123.20 (-9.48%)</td><td>23.07 <b>(-41.72%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.00 (n/a)</td><td>195.46 (n/a)</td><td>199.30 (n/a)</td><td>136.10 (n/a)</td><td>39.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_False-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.12 (-0.30%)</td><td>0.10 (+8.62%)</td><td>0.10 (+3.88%)</td><td>0.09 <b>(+22.39%)</b></td><td>0.01 <b>(-42.83%)</b></td><td>180.40 (-18.26%)</td><td>159.18 (-9.99%)</td><td>156.60 (-3.75%)</td><td>137.80 (+0.29%)</td><td>16.01 <b>(-54.05%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>220.70 (n/a)</td><td>176.84 (n/a)</td><td>162.70 (n/a)</td><td>137.40 (n/a)</td><td>34.85 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_True-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.13 (+7.96%)</td><td>0.10 (+8.22%)</td><td>0.11 (+12.47%)</td><td>0.07 (+5.41%)</td><td>0.03 <b>(+37.56%)</b></td><td>228.20 (-5.11%)</td><td>166.72 (-5.41%)</td><td>148.50 (-11.08%)</td><td>122.50 (-7.41%)</td><td>46.96 (+18.30%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>240.50 (n/a)</td><td>176.26 (n/a)</td><td>167.00 (n/a)</td><td>132.30 (n/a)</td><td>39.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_False-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.10 (-4.57%)</td><td>0.08 (+3.06%)</td><td>0.08 (+7.41%)</td><td>0.07 (+5.52%)</td><td>0.01 <b>(-31.93%)</b></td><td>251.50 (-5.24%)</td><td>204.34 (-5.39%)</td><td>208.10 (-6.89%)</td><td>162.10 (+4.78%)</td><td>33.06 <b>(-33.89%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>265.40 (n/a)</td><td>215.98 (n/a)</td><td>223.50 (n/a)</td><td>154.70 (n/a)</td><td>50.01 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_True-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.10 (+18.77%)</td><td>0.09 (+13.66%)</td><td>0.09 (+16.75%)</td><td>0.07 (+5.02%)</td><td>0.01 <b>(+45.04%)</b></td><td>219.60 (-4.81%)</td><td>183.60 (-11.54%)</td><td>175.70 (-14.33%)</td><td>156.20 (-15.80%)</td><td>24.17 (+16.89%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>230.70 (n/a)</td><td>207.56 (n/a)</td><td>205.10 (n/a)</td><td>185.50 (n/a)</td><td>20.68 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_False-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.14 (-2.70%)</td><td>0.10 (-5.56%)</td><td>0.10 (+2.33%)</td><td>0.08 (-14.50%)</td><td>0.02 (+7.97%)</td><td>211.70 (+16.96%)</td><td>164.72 (+6.85%)</td><td>162.10 (-2.29%)</td><td>120.60 (+2.81%)</td><td>32.87 <b>(+29.77%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>181.00 (n/a)</td><td>154.16 (n/a)</td><td>165.90 (n/a)</td><td>117.30 (n/a)</td><td>25.33 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_True-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.10 (-16.09%)</td><td>0.09 <b>(-20.08%)</b></td><td>0.08 (-18.32%)</td><td>0.08 (-17.90%)</td><td>0.01 (-19.75%)</td><td>217.90 <b>(+21.80%)</b></td><td>194.42 <b>(+25.01%)</b></td><td>195.30 <b>(+22.37%)</b></td><td>157.30 (+19.17%)</td><td>23.85 (+16.90%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>178.90 (n/a)</td><td>155.52 (n/a)</td><td>159.60 (n/a)</td><td>132.00 (n/a)</td><td>20.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_False-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.13 <b>(+30.33%)</b></td><td>0.10 <b>(+22.67%)</b></td><td>0.09 (+8.37%)</td><td>0.08 <b>(+32.00%)</b></td><td>0.02 <b>(+52.52%)</b></td><td>210.30 <b>(-24.27%)</b></td><td>166.80 (-17.89%)</td><td>177.00 (-7.72%)</td><td>128.70 <b>(-23.26%)</b></td><td>35.00 (-18.39%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>277.70 (n/a)</td><td>203.14 (n/a)</td><td>191.80 (n/a)</td><td>167.70 (n/a)</td><td>42.89 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_True-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.14 (+14.34%)</td><td>0.11 (+7.33%)</td><td>0.11 (+12.01%)</td><td>0.07 (-17.00%)</td><td>0.03 <b>(+101.60%)</b></td><td>227.10 <b>(+20.48%)</b></td><td>158.66 (-2.01%)</td><td>150.20 (-10.75%)</td><td>115.40 (-12.51%)</td><td>47.22 <b>(+106.39%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>188.50 (n/a)</td><td>161.92 (n/a)</td><td>168.30 (n/a)</td><td>131.90 (n/a)</td><td>22.88 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.13 (+1.68%)</td><td>0.10 (+18.80%)</td><td>0.10 <b>(+32.79%)</b></td><td>0.09 <b>(+30.40%)</b></td><td>0.02 <b>(-33.83%)</b></td><td>180.20 <b>(-23.32%)</b></td><td>159.24 (-18.45%)</td><td>159.50 <b>(-24.69%)</b></td><td>125.90 (-1.72%)</td><td>21.78 <b>(-49.23%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>235.00 (n/a)</td><td>195.26 (n/a)</td><td>211.80 (n/a)</td><td>128.10 (n/a)</td><td>42.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.14 <b>(+23.97%)</b></td><td>0.11 <b>(+23.34%)</b></td><td>0.11 <b>(+22.49%)</b></td><td>0.08 <b>(+20.34%)</b></td><td>0.02 <b>(+41.32%)</b></td><td>198.40 (-16.88%)</td><td>157.90 (-18.14%)</td><td>152.20 (-18.35%)</td><td>118.60 (-19.32%)</td><td>33.36 (-3.71%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>238.70 (n/a)</td><td>192.88 (n/a)</td><td>186.40 (n/a)</td><td>147.00 (n/a)</td><td>34.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.13 (+1.68%)</td><td>0.11 <b>(+27.53%)</b></td><td>0.12 <b>(+36.15%)</b></td><td>0.09 <b>(+85.63%)</b></td><td>0.02 <b>(-37.24%)</b></td><td>176.70 <b>(-46.13%)</b></td><td>146.28 <b>(-27.17%)</b></td><td>136.50 <b>(-26.53%)</b></td><td>123.60 (-1.67%)</td><td>23.93 <b>(-68.29%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>328.00 (n/a)</td><td>200.84 (n/a)</td><td>185.80 (n/a)</td><td>125.70 (n/a)</td><td>75.47 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.13 <b>(+25.26%)</b></td><td>0.10 (+2.46%)</td><td>0.09 (-1.10%)</td><td>0.07 <b>(-22.77%)</b></td><td>0.03 <b>(+293.14%)</b></td><td>250.10 <b>(+29.45%)</b></td><td>180.94 (+3.75%)</td><td>179.00 (+1.07%)</td><td>129.00 <b>(-20.12%)</b></td><td>51.77 <b>(+296.30%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>193.20 (n/a)</td><td>174.40 (n/a)</td><td>177.10 (n/a)</td><td>161.50 (n/a)</td><td>13.06 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.12 (-4.02%)</td><td>0.10 (-0.43%)</td><td>0.10 (+6.05%)</td><td>0.06 <b>(-28.57%)</b></td><td>0.02 <b>(+20.73%)</b></td><td>296.80 <b>(+40.00%)</b></td><td>182.18 (+4.54%)</td><td>160.60 (-5.70%)</td><td>135.00 (+4.17%)</td><td>65.00 <b>(+84.74%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>212.00 (n/a)</td><td>174.26 (n/a)</td><td>170.30 (n/a)</td><td>129.60 (n/a)</td><td>35.18 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.11 (-5.98%)</td><td>0.09 (-3.07%)</td><td>0.08 (-6.23%)</td><td>0.07 (-10.70%)</td><td>0.02 <b>(+27.49%)</b></td><td>249.00 (+12.01%)</td><td>200.06 (+5.45%)</td><td>207.70 (+6.68%)</td><td>151.20 (+6.33%)</td><td>46.52 <b>(+50.97%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>222.30 (n/a)</td><td>189.72 (n/a)</td><td>194.70 (n/a)</td><td>142.20 (n/a)</td><td>30.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.10 (-12.03%)</td><td>0.09 (-7.43%)</td><td>0.10 (-1.44%)</td><td>0.05 <b>(-24.93%)</b></td><td>0.02 (+12.77%)</td><td>325.40 <b>(+33.20%)</b></td><td>202.12 (+11.75%)</td><td>166.10 (+1.47%)</td><td>160.60 (+13.66%)</td><td>70.48 <b>(+70.22%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>244.30 (n/a)</td><td>180.86 (n/a)</td><td>163.70 (n/a)</td><td>141.30 (n/a)</td><td>41.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.13 <b>(+24.36%)</b></td><td>0.10 (+12.69%)</td><td>0.10 (+12.10%)</td><td>0.08 (+11.35%)</td><td>0.02 <b>(+59.65%)</b></td><td>215.70 (-10.20%)</td><td>173.00 (-9.44%)</td><td>159.70 (-10.78%)</td><td>122.70 (-19.59%)</td><td>39.44 (+18.19%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>240.20 (n/a)</td><td>191.04 (n/a)</td><td>179.00 (n/a)</td><td>152.60 (n/a)</td><td>33.37 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_False-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.23 (-9.84%)</td><td>0.19 (+5.98%)</td><td>0.18 (+8.37%)</td><td>0.16 (+19.45%)</td><td>0.03 <b>(-37.30%)</b></td><td>201.70 (-16.27%)</td><td>173.56 (-8.29%)</td><td>180.00 (-7.74%)</td><td>142.60 (+10.89%)</td><td>25.16 <b>(-40.94%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>240.90 (n/a)</td><td>189.24 (n/a)</td><td>195.10 (n/a)</td><td>128.60 (n/a)</td><td>42.60 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_True-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.26 (+10.22%)</td><td>0.21 (+17.43%)</td><td>0.20 (+2.30%)</td><td>0.18 <b>(+34.97%)</b></td><td>0.04 (+1.28%)</td><td>183.90 <b>(-25.91%)</b></td><td>156.30 (-15.87%)</td><td>166.10 (-2.24%)</td><td>127.40 (-9.26%)</td><td>26.91 <b>(-34.85%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>248.20 (n/a)</td><td>185.78 (n/a)</td><td>169.90 (n/a)</td><td>140.40 (n/a)</td><td>41.29 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.19 (-9.85%)</td><td>0.17 (-8.85%)</td><td>0.16 (-14.75%)</td><td>0.15 (-0.41%)</td><td>0.01 <b>(-35.65%)</b></td><td>218.40 (+0.41%)</td><td>198.74 (+8.95%)</td><td>202.60 (+17.31%)</td><td>174.50 (+10.93%)</td><td>16.81 <b>(-29.41%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>217.50 (n/a)</td><td>182.42 (n/a)</td><td>172.70 (n/a)</td><td>157.30 (n/a)</td><td>23.82 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.21 (-3.80%)</td><td>0.18 (-10.46%)</td><td>0.17 (-14.57%)</td><td>0.16 (-9.19%)</td><td>0.02 <b>(+26.65%)</b></td><td>204.40 (+10.13%)</td><td>186.08 (+12.26%)</td><td>195.40 (+17.08%)</td><td>153.10 (+3.94%)</td><td>21.13 <b>(+45.12%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>185.60 (n/a)</td><td>165.76 (n/a)</td><td>166.90 (n/a)</td><td>147.30 (n/a)</td><td>14.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_False-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.28 <b>(+37.52%)</b></td><td>0.21 (+9.74%)</td><td>0.21 (+2.55%)</td><td>0.15 (+9.68%)</td><td>0.05 <b>(+73.59%)</b></td><td>216.90 (-8.83%)</td><td>165.64 (-6.94%)</td><td>158.00 (-2.47%)</td><td>116.10 <b>(-27.30%)</b></td><td>38.15 (+13.30%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>237.90 (n/a)</td><td>178.00 (n/a)</td><td>162.00 (n/a)</td><td>159.70 (n/a)</td><td>33.67 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_True-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.23 (+10.34%)</td><td>0.21 (+4.63%)</td><td>0.22 (+8.76%)</td><td>0.19 (-6.38%)</td><td>0.02 <b>(+360.12%)</b></td><td>176.10 (+6.86%)</td><td>154.80 (-3.82%)</td><td>147.00 (-8.07%)</td><td>142.30 (-9.42%)</td><td>14.53 <b>(+346.80%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.00 (n/a)</td><td>164.80 (n/a)</td><td>160.94 (n/a)</td><td>159.90 (n/a)</td><td>157.10 (n/a)</td><td>3.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_False-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.29 (+12.68%)</td><td>0.25 <b>(+21.16%)</b></td><td>0.25 (+13.26%)</td><td>0.22 <b>(+92.12%)</b></td><td>0.03 <b>(-55.00%)</b></td><td>152.00 <b>(-47.96%)</b></td><td>132.42 <b>(-23.96%)</b></td><td>133.10 (-11.68%)</td><td>114.10 (-11.28%)</td><td>13.88 <b>(-79.61%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>292.10 (n/a)</td><td>174.14 (n/a)</td><td>150.70 (n/a)</td><td>128.60 (n/a)</td><td>68.05 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_True-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.29 (+13.01%)</td><td>0.23 (+9.02%)</td><td>0.24 (+11.34%)</td><td>0.17 (-6.16%)</td><td>0.04 <b>(+67.96%)</b></td><td>187.80 (+6.58%)</td><td>143.88 (-6.66%)</td><td>137.70 (-10.18%)</td><td>114.10 (-11.55%)</td><td>27.94 <b>(+63.17%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>176.20 (n/a)</td><td>154.14 (n/a)</td><td>153.30 (n/a)</td><td>129.00 (n/a)</td><td>17.13 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_False-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.26 (+0.86%)</td><td>0.22 <b>(+24.23%)</b></td><td>0.22 (+19.00%)</td><td>0.18 <b>(+105.68%)</b></td><td>0.03 <b>(-46.30%)</b></td><td>182.80 <b>(-51.38%)</b></td><td>154.74 <b>(-27.79%)</b></td><td>151.70 (-16.00%)</td><td>125.60 (-0.87%)</td><td>23.55 <b>(-75.36%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>376.00 (n/a)</td><td>214.30 (n/a)</td><td>180.60 (n/a)</td><td>126.70 (n/a)</td><td>95.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_True-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.26 (-1.13%)</td><td>0.22 (-2.03%)</td><td>0.20 (-3.25%)</td><td>0.17 (-16.84%)</td><td>0.04 <b>(+66.75%)</b></td><td>192.80 <b>(+20.20%)</b></td><td>154.86 (+3.95%)</td><td>161.60 (+3.32%)</td><td>126.70 (+1.12%)</td><td>28.24 <b>(+94.91%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>160.40 (n/a)</td><td>148.98 (n/a)</td><td>156.40 (n/a)</td><td>125.30 (n/a)</td><td>14.49 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_False-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.24 (-8.87%)</td><td>0.21 (-0.21%)</td><td>0.22 (+5.14%)</td><td>0.17 (-4.79%)</td><td>0.03 (-17.09%)</td><td>189.30 (+5.05%)</td><td>156.22 (-0.13%)</td><td>149.30 (-4.84%)</td><td>137.50 (+9.74%)</td><td>21.15 (-4.82%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>180.20 (n/a)</td><td>156.42 (n/a)</td><td>156.90 (n/a)</td><td>125.30 (n/a)</td><td>22.22 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_True-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.28 (+12.98%)</td><td>0.20 (-9.04%)</td><td>0.20 (-10.69%)</td><td>0.09 <b>(-48.41%)</b></td><td>0.08 <b>(+202.86%)</b></td><td>353.20 <b>(+93.85%)</b></td><td>198.16 <b>(+28.14%)</b></td><td>163.60 (+11.98%)</td><td>118.40 (-11.44%)</td><td>97.71 <b>(+401.37%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>182.20 (n/a)</td><td>154.64 (n/a)</td><td>146.10 (n/a)</td><td>133.70 (n/a)</td><td>19.49 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.23 (+18.27%)</td><td>0.20 (+11.76%)</td><td>0.21 (+16.16%)</td><td>0.15 (-3.03%)</td><td>0.03 <b>(+84.01%)</b></td><td>214.90 (+3.12%)</td><td>166.80 (-9.25%)</td><td>155.90 (-13.96%)</td><td>139.70 (-15.44%)</td><td>28.96 <b>(+64.94%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>208.40 (n/a)</td><td>183.80 (n/a)</td><td>181.20 (n/a)</td><td>165.20 (n/a)</td><td>17.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.21 (+7.32%)</td><td>0.18 (+1.16%)</td><td>0.19 (+3.94%)</td><td>0.14 (-13.12%)</td><td>0.03 <b>(+122.68%)</b></td><td>233.10 (+15.05%)</td><td>182.30 (+0.66%)</td><td>172.30 (-3.80%)</td><td>153.60 (-6.80%)</td><td>32.17 <b>(+136.70%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>202.60 (n/a)</td><td>181.10 (n/a)</td><td>179.10 (n/a)</td><td>164.80 (n/a)</td><td>13.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.25 (-0.57%)</td><td>0.22 (+8.93%)</td><td>0.23 (+12.06%)</td><td>0.15 (-3.28%)</td><td>0.04 (+2.68%)</td><td>212.90 (+3.40%)</td><td>154.36 (-7.81%)</td><td>142.80 (-10.75%)</td><td>128.60 (+0.55%)</td><td>33.36 (+11.99%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>205.90 (n/a)</td><td>167.44 (n/a)</td><td>160.00 (n/a)</td><td>127.90 (n/a)</td><td>29.79 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.22 (-15.54%)</td><td>0.19 (-13.30%)</td><td>0.19 (-14.51%)</td><td>0.16 (-11.78%)</td><td>0.02 (-13.58%)</td><td>204.00 (+13.33%)</td><td>174.40 (+15.31%)</td><td>173.10 (+16.96%)</td><td>151.70 (+18.42%)</td><td>21.59 (+13.98%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>180.00 (n/a)</td><td>151.24 (n/a)</td><td>148.00 (n/a)</td><td>128.10 (n/a)</td><td>18.94 (n/a)</td>
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


### test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_4-num_kv_heads_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.16 (-0.66%)</td><td>0.16 (-0.21%)</td><td>0.16 (-0.11%)</td><td>0.16 (-0.09%)</td><td>0.00 <b>(-75.35%)</b></td><td>52355.70 (+0.09%)</td><td>52312.58 (+0.21%)</td><td>52332.90 (+0.11%)</td><td>52254.70 (+0.67%)</td><td>41.29 <b>(-75.15%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.00 (n/a)</td><td>52310.90 (n/a)</td><td>52202.68 (n/a)</td><td>52274.80 (n/a)</td><td>51908.90 (n/a)</td><td>166.17 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.00 (n/a)</td><td>52330.20 (n/a)</td><td>52309.88 (n/a)</td><td>52315.10 (n/a)</td><td>52274.80 (n/a)</td><td>20.95 (n/a)</td>
</tr>
</tbody>
</table>


### test_mha[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.00 (n/a)</td><td>413340.00 (n/a)</td><td>413184.28 (n/a)</td><td>413251.10 (n/a)</td><td>412970.80 (n/a)</td><td>155.79 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.21 <b>(+21.39%)</b></td><td>0.19 <b>(+26.13%)</b></td><td>0.20 <b>(+35.61%)</b></td><td>0.14 (+16.46%)</td><td>0.03 (+14.79%)</td><td>169.70 (-14.16%)</td><td>134.62 <b>(-20.84%)</b></td><td>125.70 <b>(-26.28%)</b></td><td>115.80 (-17.64%)</td><td>21.58 (-18.44%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>197.70 (n/a)</td><td>170.06 (n/a)</td><td>170.50 (n/a)</td><td>140.60 (n/a)</td><td>26.45 (n/a)</td>
</tr>
</tbody>
</table>


### test_repeat[rows_4-cols_2048-repeat_2-transfer_size_None]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.39 (+0.89%)</td><td>0.33 (-7.78%)</td><td>0.34 (-8.68%)</td><td>0.26 (-16.27%)</td><td>0.06 <b>(+105.11%)</b></td><td>190.50 (+19.44%)</td><td>153.18 (+10.95%)</td><td>146.40 (+9.50%)</td><td>125.60 (-0.87%)</td><td>29.43 <b>(+134.09%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.39 (n/a)</td><td>0.36 (n/a)</td><td>0.37 (n/a)</td><td>0.31 (n/a)</td><td>0.03 (n/a)</td><td>159.50 (n/a)</td><td>138.06 (n/a)</td><td>133.70 (n/a)</td><td>126.70 (n/a)</td><td>12.57 (n/a)</td>
</tr>
</tbody>
</table>


### test_repeat[rows_8-cols_131072-repeat_4-transfer_size_64]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>13.44 (+0.65%)</td><td>13.08 (+10.70%)</td><td>13.43 (+3.95%)</td><td>12.47 <b>(+70.76%)</b></td><td>0.49 <b>(-80.89%)</b></td><td>840.90 <b>(-41.43%)</b></td><td>802.48 (-14.22%)</td><td>781.00 (-3.79%)</td><td>780.20 (-0.64%)</td><td>30.26 <b>(-89.21%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>13.35 (n/a)</td><td>11.82 (n/a)</td><td>12.92 (n/a)</td><td>7.30 (n/a)</td><td>2.54 (n/a)</td><td>1435.80 (n/a)</td><td>935.54 (n/a)</td><td>811.80 (n/a)</td><td>785.20 (n/a)</td><td>280.39 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.33 (-6.32%)</td><td>0.31 (+8.76%)</td><td>0.32 (+9.73%)</td><td>0.28 <b>(+37.98%)</b></td><td>0.02 <b>(-59.68%)</b></td><td>143.80 <b>(-27.48%)</b></td><td>133.34 (-10.43%)</td><td>128.60 (-8.86%)</td><td>125.10 (+6.74%)</td><td>9.37 <b>(-69.32%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.35 (n/a)</td><td>0.28 (n/a)</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>198.30 (n/a)</td><td>148.86 (n/a)</td><td>141.10 (n/a)</td><td>117.20 (n/a)</td><td>30.53 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (-3.41%)</td><td>0.04 (-1.71%)</td><td>0.04 (-9.11%)</td><td>0.03 (+4.69%)</td><td>0.00 (-19.97%)</td><td>162.40 (-4.47%)</td><td>142.44 (+1.08%)</td><td>146.00 (+10.02%)</td><td>121.00 (+3.51%)</td><td>16.26 <b>(-22.09%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>170.00 (n/a)</td><td>140.92 (n/a)</td><td>132.70 (n/a)</td><td>116.90 (n/a)</td><td>20.87 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/rms_norm</summary>


### test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (+11.68%)</td><td>0.03 (+12.46%)</td><td>0.03 (+6.71%)</td><td>0.02 <b>(+50.14%)</b></td><td>0.00 (-19.88%)</td><td>166.60 <b>(-33.39%)</b></td><td>149.90 (-13.90%)</td><td>155.20 (-6.28%)</td><td>112.90 (-10.47%)</td><td>21.26 <b>(-54.76%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>250.10 (n/a)</td><td>174.10 (n/a)</td><td>165.60 (n/a)</td><td>126.10 (n/a)</td><td>46.99 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (-8.21%)</td><td>0.04 (-10.69%)</td><td>0.04 <b>(-22.37%)</b></td><td>0.03 (+6.87%)</td><td>0.01 <b>(-24.42%)</b></td><td>225.40 (-6.43%)</td><td>171.76 (+8.19%)</td><td>173.50 <b>(+28.80%)</b></td><td>117.60 (+8.99%)</td><td>38.78 <b>(-26.59%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.90 (n/a)</td><td>158.76 (n/a)</td><td>134.70 (n/a)</td><td>107.90 (n/a)</td><td>52.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (+9.69%)</td><td>0.03 (-3.58%)</td><td>0.02 (-13.42%)</td><td>0.02 (+7.69%)</td><td>0.01 (+6.81%)</td><td>184.40 (-7.15%)</td><td>162.88 (+3.44%)</td><td>172.20 (+15.49%)</td><td>111.40 (-8.84%)</td><td>29.42 (-13.36%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>198.60 (n/a)</td><td>157.46 (n/a)</td><td>149.10 (n/a)</td><td>122.20 (n/a)</td><td>33.95 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (-6.90%)</td><td>0.04 <b>(+21.03%)</b></td><td>0.03 <b>(+32.30%)</b></td><td>0.03 <b>(+25.96%)</b></td><td>0.01 <b>(-40.75%)</b></td><td>181.30 <b>(-20.62%)</b></td><td>144.30 <b>(-22.54%)</b></td><td>146.50 <b>(-24.41%)</b></td><td>106.90 (+7.44%)</td><td>26.75 <b>(-49.20%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>228.40 (n/a)</td><td>186.28 (n/a)</td><td>193.80 (n/a)</td><td>99.50 (n/a)</td><td>52.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (-2.79%)</td><td>0.03 (+4.47%)</td><td>0.03 (+5.12%)</td><td>0.02 (+5.73%)</td><td>0.00 (-4.43%)</td><td>213.70 (-5.40%)</td><td>164.18 (-4.67%)</td><td>156.20 (-4.87%)</td><td>131.60 (+2.89%)</td><td>33.89 (-8.26%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>225.90 (n/a)</td><td>172.22 (n/a)</td><td>164.20 (n/a)</td><td>127.90 (n/a)</td><td>36.94 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 <b>(-23.49%)</b></td><td>0.03 (-14.15%)</td><td>0.03 (-17.88%)</td><td>0.02 (-6.64%)</td><td>0.00 <b>(-46.35%)</b></td><td>218.00 (+7.13%)</td><td>180.14 (+14.20%)</td><td>181.50 <b>(+21.81%)</b></td><td>153.80 <b>(+30.78%)</b></td><td>24.44 <b>(-24.86%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>203.50 (n/a)</td><td>157.74 (n/a)</td><td>149.00 (n/a)</td><td>117.60 (n/a)</td><td>32.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (-0.78%)</td><td>0.02 (-1.78%)</td><td>0.02 (+0.82%)</td><td>0.02 (-6.52%)</td><td>0.00 <b>(+24.86%)</b></td><td>209.50 (+6.94%)</td><td>172.68 (+2.60%)</td><td>172.40 (-0.86%)</td><td>145.30 (+0.76%)</td><td>27.52 <b>(+32.89%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>195.90 (n/a)</td><td>168.30 (n/a)</td><td>173.90 (n/a)</td><td>144.20 (n/a)</td><td>20.71 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.04 (+1.03%)</td><td>0.03 (+6.31%)</td><td>0.03 (+7.77%)</td><td>0.02 (+0.04%)</td><td>0.01 (-2.42%)</td><td>209.40 (-0.05%)</td><td>165.94 (-6.14%)</td><td>172.20 (-7.22%)</td><td>121.80 (-1.06%)</td><td>33.24 (-3.13%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>209.50 (n/a)</td><td>176.80 (n/a)</td><td>185.60 (n/a)</td><td>123.10 (n/a)</td><td>34.32 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (-6.64%)</td><td>0.03 (-5.25%)</td><td>0.02 (-4.95%)</td><td>0.02 (-11.76%)</td><td>0.00 (+4.79%)</td><td>204.00 (+13.33%)</td><td>166.32 (+5.99%)</td><td>168.80 (+5.17%)</td><td>138.50 (+7.12%)</td><td>25.01 <b>(+28.45%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>180.00 (n/a)</td><td>156.92 (n/a)</td><td>160.50 (n/a)</td><td>129.30 (n/a)</td><td>19.47 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (-4.82%)</td><td>0.03 (-1.19%)</td><td>0.03 (+3.57%)</td><td>0.02 (-1.36%)</td><td>0.00 <b>(-24.59%)</b></td><td>229.60 (+1.37%)</td><td>183.76 (-0.03%)</td><td>181.40 (-3.41%)</td><td>150.70 (+5.09%)</td><td>30.04 (-17.95%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>226.50 (n/a)</td><td>183.82 (n/a)</td><td>187.80 (n/a)</td><td>143.40 (n/a)</td><td>36.62 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (-5.65%)</td><td>0.02 (+4.87%)</td><td>0.02 (+5.42%)</td><td>0.02 (+14.29%)</td><td>0.00 <b>(-26.57%)</b></td><td>224.20 (-12.49%)</td><td>179.10 (-6.06%)</td><td>171.90 (-5.13%)</td><td>159.60 (+5.98%)</td><td>26.25 <b>(-33.27%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>256.20 (n/a)</td><td>190.66 (n/a)</td><td>181.20 (n/a)</td><td>150.60 (n/a)</td><td>39.34 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 <b>(+20.68%)</b></td><td>0.02 (+15.52%)</td><td>0.02 (+5.36%)</td><td>0.02 <b>(+37.67%)</b></td><td>0.00 (-8.56%)</td><td>215.50 <b>(-27.34%)</b></td><td>196.52 (-14.90%)</td><td>207.10 (-5.09%)</td><td>151.00 (-17.17%)</td><td>26.49 <b>(-45.59%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>296.60 (n/a)</td><td>230.92 (n/a)</td><td>218.20 (n/a)</td><td>182.30 (n/a)</td><td>48.68 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (+2.74%)</td><td>0.02 (+3.77%)</td><td>0.02 (-0.47%)</td><td>0.02 (-2.60%)</td><td>0.00 (+2.13%)</td><td>209.10 (+2.70%)</td><td>170.24 (-3.60%)</td><td>173.30 (+0.46%)</td><td>132.00 (-2.65%)</td><td>28.03 (-0.56%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.60 (n/a)</td><td>176.60 (n/a)</td><td>172.50 (n/a)</td><td>135.60 (n/a)</td><td>28.19 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 <b>(+23.52%)</b></td><td>0.02 (-0.54%)</td><td>0.02 (-14.44%)</td><td>0.01 (-5.93%)</td><td>0.01 <b>(+104.03%)</b></td><td>311.90 (+6.31%)</td><td>231.10 (+7.22%)</td><td>229.10 (+16.89%)</td><td>150.70 (-19.02%)</td><td>75.73 <b>(+71.38%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>293.40 (n/a)</td><td>215.54 (n/a)</td><td>196.00 (n/a)</td><td>186.10 (n/a)</td><td>44.19 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.02 (-10.53%)</td><td>0.02 (-18.11%)</td><td>0.02 (-0.79%)</td><td>0.01 <b>(-33.74%)</b></td><td>0.00 <b>(+58.46%)</b></td><td>351.10 <b>(+50.95%)</b></td><td>257.16 <b>(+28.79%)</b></td><td>213.00 (+0.80%)</td><td>188.30 (+11.75%)</td><td>78.08 <b>(+180.26%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.60 (n/a)</td><td>199.68 (n/a)</td><td>211.30 (n/a)</td><td>168.50 (n/a)</td><td>27.86 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 <b>(-27.88%)</b></td><td>0.05 (+9.20%)</td><td>0.05 (+12.06%)</td><td>0.05 <b>(+133.53%)</b></td><td>0.00 <b>(-84.95%)</b></td><td>181.70 <b>(-57.18%)</b></td><td>167.62 <b>(-31.07%)</b></td><td>170.30 (-10.79%)</td><td>153.70 <b>(+38.72%)</b></td><td>12.61 <b>(-91.22%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>424.30 (n/a)</td><td>243.16 (n/a)</td><td>190.90 (n/a)</td><td>110.80 (n/a)</td><td>143.65 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.10 (+7.67%)</td><td>0.08 (+9.48%)</td><td>0.08 (+10.55%)</td><td>0.07 <b>(+21.26%)</b></td><td>0.01 (-13.79%)</td><td>178.20 (-17.54%)</td><td>155.18 (-9.85%)</td><td>161.30 (-9.53%)</td><td>121.00 (-7.07%)</td><td>21.45 <b>(-35.06%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>216.10 (n/a)</td><td>172.14 (n/a)</td><td>178.30 (n/a)</td><td>130.20 (n/a)</td><td>33.03 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 <b>(-22.59%)</b></td><td>0.05 (-0.39%)</td><td>0.05 (-3.96%)</td><td>0.04 <b>(+45.29%)</b></td><td>0.00 <b>(-69.84%)</b></td><td>199.40 <b>(-31.17%)</b></td><td>179.80 (-7.02%)</td><td>180.00 (+4.11%)</td><td>154.40 <b>(+29.21%)</b></td><td>16.66 <b>(-73.67%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>289.70 (n/a)</td><td>193.38 (n/a)</td><td>172.90 (n/a)</td><td>119.50 (n/a)</td><td>63.26 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 (-14.55%)</td><td>0.06 (-6.58%)</td><td>0.06 (-5.71%)</td><td>0.05 (-8.95%)</td><td>0.01 (-14.74%)</td><td>200.20 (+9.88%)</td><td>172.24 (+6.99%)</td><td>176.50 (+6.01%)</td><td>138.80 (+17.03%)</td><td>28.30 (+14.47%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>182.20 (n/a)</td><td>160.98 (n/a)</td><td>166.50 (n/a)</td><td>118.60 (n/a)</td><td>24.72 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 <b>(-20.37%)</b></td><td>0.05 (-10.95%)</td><td>0.05 (-6.93%)</td><td>0.04 (-10.04%)</td><td>0.01 <b>(-37.63%)</b></td><td>199.50 (+11.20%)</td><td>176.56 (+11.13%)</td><td>180.80 (+7.49%)</td><td>148.70 <b>(+25.59%)</b></td><td>22.31 (-12.42%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>179.40 (n/a)</td><td>158.88 (n/a)</td><td>168.20 (n/a)</td><td>118.40 (n/a)</td><td>25.47 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 <b>(-28.46%)</b></td><td>0.06 (-11.66%)</td><td>0.06 (-9.60%)</td><td>0.05 (-1.43%)</td><td>0.01 <b>(-58.03%)</b></td><td>197.50 (+1.44%)</td><td>176.20 (+8.97%)</td><td>186.20 (+10.64%)</td><td>143.40 <b>(+39.77%)</b></td><td>22.08 <b>(-38.52%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>194.70 (n/a)</td><td>161.70 (n/a)</td><td>168.30 (n/a)</td><td>102.60 (n/a)</td><td>35.92 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (-16.14%)</td><td>0.05 (+2.72%)</td><td>0.05 (+13.44%)</td><td>0.04 (+15.37%)</td><td>0.01 <b>(-47.82%)</b></td><td>208.90 (-13.36%)</td><td>178.90 (-5.01%)</td><td>165.90 (-11.85%)</td><td>161.90 (+19.22%)</td><td>20.72 <b>(-45.50%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.10 (n/a)</td><td>188.34 (n/a)</td><td>188.20 (n/a)</td><td>135.80 (n/a)</td><td>38.02 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 <b>(-24.74%)</b></td><td>0.05 (-19.03%)</td><td>0.05 (-8.19%)</td><td>0.04 <b>(-25.04%)</b></td><td>0.01 <b>(-34.94%)</b></td><td>247.80 <b>(+33.37%)</b></td><td>194.80 <b>(+22.12%)</b></td><td>191.90 (+8.91%)</td><td>143.60 <b>(+32.84%)</b></td><td>37.11 (+13.55%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>185.80 (n/a)</td><td>159.52 (n/a)</td><td>176.20 (n/a)</td><td>108.10 (n/a)</td><td>32.68 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 <b>(-20.59%)</b></td><td>0.05 (-9.47%)</td><td>0.05 (-7.78%)</td><td>0.04 (-2.70%)</td><td>0.00 <b>(-51.14%)</b></td><td>205.90 (+2.80%)</td><td>183.08 (+8.43%)</td><td>177.50 (+8.43%)</td><td>158.40 <b>(+25.91%)</b></td><td>18.83 <b>(-36.43%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.30 (n/a)</td><td>168.84 (n/a)</td><td>163.70 (n/a)</td><td>125.80 (n/a)</td><td>29.61 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 (+1.25%)</td><td>0.05 (-7.92%)</td><td>0.05 (-2.19%)</td><td>0.03 <b>(-33.34%)</b></td><td>0.02 <b>(+58.32%)</b></td><td>304.30 <b>(+50.05%)</b></td><td>189.86 (+15.32%)</td><td>169.20 (+2.24%)</td><td>126.50 (-1.25%)</td><td>67.39 <b>(+150.92%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>202.80 (n/a)</td><td>164.64 (n/a)</td><td>165.50 (n/a)</td><td>128.10 (n/a)</td><td>26.86 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 (+0.93%)</td><td>0.04 (-0.42%)</td><td>0.04 (+4.77%)</td><td>0.03 (-6.28%)</td><td>0.01 (-3.85%)</td><td>309.80 (+6.68%)</td><td>212.54 (+0.45%)</td><td>208.50 (-4.58%)</td><td>148.00 (-0.94%)</td><td>60.29 (+6.47%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>290.40 (n/a)</td><td>211.58 (n/a)</td><td>218.50 (n/a)</td><td>149.40 (n/a)</td><td>56.63 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 <b>(+20.62%)</b></td><td>0.05 (+19.62%)</td><td>0.05 (+17.54%)</td><td>0.04 <b>(+38.87%)</b></td><td>0.01 (-0.67%)</td><td>209.80 <b>(-28.00%)</b></td><td>179.62 (-17.45%)</td><td>180.30 (-14.95%)</td><td>145.80 (-17.11%)</td><td>26.37 <b>(-41.41%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>291.40 (n/a)</td><td>217.58 (n/a)</td><td>212.00 (n/a)</td><td>175.90 (n/a)</td><td>45.01 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.06 <b>(+21.63%)</b></td><td>0.04 (+5.27%)</td><td>0.04 (-0.71%)</td><td>0.03 (+6.37%)</td><td>0.01 <b>(+36.06%)</b></td><td>238.20 (-6.00%)</td><td>193.58 (-3.41%)</td><td>206.70 (+0.68%)</td><td>127.30 (-17.76%)</td><td>45.95 (+8.18%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>253.40 (n/a)</td><td>200.42 (n/a)</td><td>205.30 (n/a)</td><td>154.80 (n/a)</td><td>42.48 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.07 <b>(+32.00%)</b></td><td>0.05 (+16.17%)</td><td>0.05 (+8.65%)</td><td>0.04 (+4.03%)</td><td>0.01 <b>(+132.88%)</b></td><td>222.40 (-3.85%)</td><td>182.82 (-11.42%)</td><td>193.20 (-7.96%)</td><td>130.00 <b>(-24.24%)</b></td><td>37.60 <b>(+73.04%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>231.30 (n/a)</td><td>206.40 (n/a)</td><td>209.90 (n/a)</td><td>171.60 (n/a)</td><td>21.73 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.05 (+6.84%)</td><td>0.04 (+5.84%)</td><td>0.04 (-3.95%)</td><td>0.03 <b>(+27.15%)</b></td><td>0.01 <b>(-22.85%)</b></td><td>242.90 <b>(-21.37%)</b></td><td>213.12 (-7.10%)</td><td>222.40 (+4.12%)</td><td>175.70 (-6.39%)</td><td>25.85 <b>(-45.46%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>308.90 (n/a)</td><td>229.42 (n/a)</td><td>213.60 (n/a)</td><td>187.70 (n/a)</td><td>47.39 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.11 (-7.23%)</td><td>0.09 (-12.20%)</td><td>0.09 (-14.08%)</td><td>0.08 (-10.72%)</td><td>0.01 (-10.29%)</td><td>205.10 (+12.02%)</td><td>182.58 (+13.80%)</td><td>182.50 (+16.39%)</td><td>147.20 (+7.76%)</td><td>22.50 (+5.12%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>183.10 (n/a)</td><td>160.44 (n/a)</td><td>156.80 (n/a)</td><td>136.60 (n/a)</td><td>21.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.21 <b>(+28.80%)</b></td><td>0.17 <b>(+31.70%)</b></td><td>0.16 <b>(+20.22%)</b></td><td>0.14 <b>(+71.85%)</b></td><td>0.03 (-14.01%)</td><td>177.90 <b>(-41.81%)</b></td><td>150.30 <b>(-26.96%)</b></td><td>155.50 (-16.80%)</td><td>117.00 <b>(-22.36%)</b></td><td>22.08 <b>(-63.33%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>305.70 (n/a)</td><td>205.78 (n/a)</td><td>186.90 (n/a)</td><td>150.70 (n/a)</td><td>60.23 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.13 <b>(+20.75%)</b></td><td>0.11 (+12.45%)</td><td>0.10 (+2.95%)</td><td>0.09 (+5.50%)</td><td>0.02 <b>(+126.83%)</b></td><td>178.80 (-5.25%)</td><td>156.00 (-9.99%)</td><td>167.40 (-2.84%)</td><td>128.60 (-17.19%)</td><td>21.57 <b>(+77.62%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>188.70 (n/a)</td><td>173.32 (n/a)</td><td>172.30 (n/a)</td><td>155.30 (n/a)</td><td>12.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.21 (+6.07%)</td><td>0.14 <b>(+28.66%)</b></td><td>0.13 <b>(+44.16%)</b></td><td>0.11 <b>(+48.08%)</b></td><td>0.04 <b>(-20.99%)</b></td><td>182.90 <b>(-32.46%)</b></td><td>152.24 <b>(-26.81%)</b></td><td>156.10 <b>(-30.62%)</b></td><td>99.50 (-5.78%)</td><td>32.73 <b>(-46.74%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>270.80 (n/a)</td><td>208.00 (n/a)</td><td>225.00 (n/a)</td><td>105.60 (n/a)</td><td>61.46 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.11 (-9.45%)</td><td>0.10 (+1.15%)</td><td>0.09 (-3.35%)</td><td>0.09 <b>(+40.45%)</b></td><td>0.01 <b>(-55.33%)</b></td><td>185.00 <b>(-28.82%)</b></td><td>170.64 (-5.69%)</td><td>181.10 (+3.43%)</td><td>144.30 (+10.41%)</td><td>17.73 <b>(-64.81%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>259.90 (n/a)</td><td>180.94 (n/a)</td><td>175.10 (n/a)</td><td>130.70 (n/a)</td><td>50.37 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.17 (-13.50%)</td><td>0.14 (+14.52%)</td><td>0.15 <b>(+36.56%)</b></td><td>0.11 <b>(+24.23%)</b></td><td>0.02 <b>(-47.25%)</b></td><td>184.50 (-19.50%)</td><td>147.92 (-17.82%)</td><td>138.80 <b>(-26.79%)</b></td><td>123.30 (+15.67%)</td><td>25.28 <b>(-51.87%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>229.20 (n/a)</td><td>180.00 (n/a)</td><td>189.60 (n/a)</td><td>106.60 (n/a)</td><td>52.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.11 <b>(-22.02%)</b></td><td>0.09 <b>(-20.18%)</b></td><td>0.09 (-11.16%)</td><td>0.06 <b>(-33.30%)</b></td><td>0.02 (-4.34%)</td><td>272.10 <b>(+49.92%)</b></td><td>198.72 <b>(+27.74%)</b></td><td>184.20 (+12.59%)</td><td>149.20 <b>(+28.18%)</b></td><td>49.16 <b>(+86.23%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>181.50 (n/a)</td><td>155.56 (n/a)</td><td>163.60 (n/a)</td><td>116.40 (n/a)</td><td>26.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.17 <b>(+37.04%)</b></td><td>0.13 (+17.61%)</td><td>0.11 (+7.98%)</td><td>0.09 (+2.15%)</td><td>0.03 <b>(+121.88%)</b></td><td>194.40 (-2.11%)</td><td>154.38 (-11.61%)</td><td>167.30 (-7.42%)</td><td>108.30 <b>(-27.02%)</b></td><td>38.47 <b>(+58.85%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>198.60 (n/a)</td><td>174.66 (n/a)</td><td>180.70 (n/a)</td><td>148.40 (n/a)</td><td>24.22 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.12 (-6.55%)</td><td>0.09 (-10.82%)</td><td>0.10 (-5.63%)</td><td>0.07 <b>(-23.21%)</b></td><td>0.02 <b>(+26.84%)</b></td><td>236.70 <b>(+30.20%)</b></td><td>178.04 (+14.07%)</td><td>170.10 (+5.98%)</td><td>141.30 (+7.05%)</td><td>36.58 <b>(+81.77%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>181.80 (n/a)</td><td>156.08 (n/a)</td><td>160.50 (n/a)</td><td>132.00 (n/a)</td><td>20.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.16 (+10.03%)</td><td>0.13 (+16.61%)</td><td>0.13 (+19.67%)</td><td>0.09 (+0.88%)</td><td>0.03 <b>(+33.68%)</b></td><td>205.00 (-0.87%)</td><td>146.90 (-12.69%)</td><td>139.40 (-16.48%)</td><td>112.30 (-9.14%)</td><td>37.38 <b>(+22.48%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>206.80 (n/a)</td><td>168.26 (n/a)</td><td>166.90 (n/a)</td><td>123.60 (n/a)</td><td>30.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.13 (+13.75%)</td><td>0.10 (+10.52%)</td><td>0.10 (-2.04%)</td><td>0.08 <b>(+37.81%)</b></td><td>0.02 <b>(-24.89%)</b></td><td>207.60 <b>(-27.44%)</b></td><td>164.78 (-13.01%)</td><td>163.60 (+2.06%)</td><td>130.10 (-12.09%)</td><td>28.52 <b>(-51.27%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>286.10 (n/a)</td><td>189.42 (n/a)</td><td>160.30 (n/a)</td><td>148.00 (n/a)</td><td>58.53 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.16 <b>(+47.44%)</b></td><td>0.10 (+5.31%)</td><td>0.10 (-1.39%)</td><td>0.05 <b>(-38.91%)</b></td><td>0.04 <b>(+253.80%)</b></td><td>348.70 <b>(+63.71%)</b></td><td>200.86 (+7.86%)</td><td>180.00 (+1.41%)</td><td>110.80 <b>(-32.19%)</b></td><td>89.71 <b>(+301.67%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>213.00 (n/a)</td><td>186.22 (n/a)</td><td>177.50 (n/a)</td><td>163.40 (n/a)</td><td>22.33 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.11 <b>(-27.03%)</b></td><td>0.09 (-9.73%)</td><td>0.08 (-7.46%)</td><td>0.07 (+18.23%)</td><td>0.02 <b>(-49.54%)</b></td><td>232.90 (-15.40%)</td><td>186.96 (+3.95%)</td><td>195.50 (+8.07%)</td><td>149.40 <b>(+37.06%)</b></td><td>35.07 <b>(-43.28%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>275.30 (n/a)</td><td>179.86 (n/a)</td><td>180.90 (n/a)</td><td>109.00 (n/a)</td><td>61.82 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.11 (-8.33%)</td><td>0.10 (+2.43%)</td><td>0.10 (+10.43%)</td><td>0.09 <b>(+31.31%)</b></td><td>0.01 <b>(-61.93%)</b></td><td>202.30 <b>(-23.86%)</b></td><td>183.64 (-5.84%)</td><td>178.60 (-9.43%)</td><td>164.50 (+9.08%)</td><td>14.86 <b>(-67.71%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>265.70 (n/a)</td><td>195.04 (n/a)</td><td>197.20 (n/a)</td><td>150.80 (n/a)</td><td>46.02 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.10 (+6.13%)</td><td>0.08 (+2.55%)</td><td>0.08 (-1.88%)</td><td>0.05 <b>(-24.48%)</b></td><td>0.02 <b>(+87.04%)</b></td><td>347.10 <b>(+32.43%)</b></td><td>225.02 (+2.61%)</td><td>217.80 (+1.87%)</td><td>169.10 (-5.79%)</td><td>72.29 <b>(+134.18%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>262.10 (n/a)</td><td>219.30 (n/a)</td><td>213.80 (n/a)</td><td>179.50 (n/a)</td><td>30.87 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.23 (+2.12%)</td><td>0.19 (+6.13%)</td><td>0.18 (+5.89%)</td><td>0.18 <b>(+25.83%)</b></td><td>0.02 <b>(-37.87%)</b></td><td>186.90 <b>(-20.54%)</b></td><td>172.06 (-7.48%)</td><td>177.70 (-5.53%)</td><td>145.10 (-2.03%)</td><td>16.43 <b>(-51.97%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>235.20 (n/a)</td><td>185.98 (n/a)</td><td>188.10 (n/a)</td><td>148.10 (n/a)</td><td>34.20 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.26 <b>(+37.02%)</b></td><td>0.20 (+14.43%)</td><td>0.19 (+5.99%)</td><td>0.15 (-5.23%)</td><td>0.04 <b>(+213.26%)</b></td><td>220.30 (+5.56%)</td><td>170.30 (-10.10%)</td><td>173.50 (-5.66%)</td><td>126.10 <b>(-26.98%)</b></td><td>34.20 <b>(+138.46%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>208.70 (n/a)</td><td>189.44 (n/a)</td><td>183.90 (n/a)</td><td>172.70 (n/a)</td><td>14.34 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.30 (-9.99%)</td><td>0.26 (+9.20%)</td><td>0.28 (+15.11%)</td><td>0.20 <b>(+27.61%)</b></td><td>0.05 <b>(-36.35%)</b></td><td>209.00 <b>(-21.63%)</b></td><td>163.22 (-12.90%)</td><td>145.60 (-13.18%)</td><td>135.40 (+11.07%)</td><td>31.88 <b>(-45.75%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.34 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>266.70 (n/a)</td><td>187.40 (n/a)</td><td>167.70 (n/a)</td><td>121.90 (n/a)</td><td>58.78 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.32 <b>(+58.33%)</b></td><td>0.21 <b>(+25.56%)</b></td><td>0.19 (+3.34%)</td><td>0.18 <b>(+28.39%)</b></td><td>0.06 <b>(+121.06%)</b></td><td>184.20 <b>(-22.11%)</b></td><td>160.40 (-18.31%)</td><td>175.00 (-3.21%)</td><td>104.00 <b>(-36.82%)</b></td><td>32.87 (+4.60%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>236.50 (n/a)</td><td>196.36 (n/a)</td><td>180.80 (n/a)</td><td>164.60 (n/a)</td><td>31.43 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.32 (-2.79%)</td><td>0.24 (-10.52%)</td><td>0.21 <b>(-27.03%)</b></td><td>0.20 (+10.85%)</td><td>0.05 (-2.18%)</td><td>203.80 (-9.82%)</td><td>173.34 (+11.09%)</td><td>194.60 <b>(+37.04%)</b></td><td>130.00 (+2.85%)</td><td>34.37 (-13.55%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.29 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>226.00 (n/a)</td><td>156.04 (n/a)</td><td>142.00 (n/a)</td><td>126.40 (n/a)</td><td>39.75 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.26 (+15.33%)</td><td>0.18 (+4.02%)</td><td>0.15 (-9.06%)</td><td>0.11 (-16.95%)</td><td>0.06 <b>(+57.26%)</b></td><td>292.50 <b>(+20.37%)</b></td><td>200.84 (+1.41%)</td><td>214.80 (+9.93%)</td><td>124.30 (-13.32%)</td><td>66.93 <b>(+55.45%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>243.00 (n/a)</td><td>198.04 (n/a)</td><td>195.40 (n/a)</td><td>143.40 (n/a)</td><td>43.06 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.27 (+12.98%)</td><td>0.22 (+7.95%)</td><td>0.22 (+1.66%)</td><td>0.21 <b>(+22.04%)</b></td><td>0.03 (+0.95%)</td><td>179.50 (-18.04%)</td><td>166.56 (-7.68%)</td><td>171.20 (-1.67%)</td><td>138.50 (-11.45%)</td><td>16.89 <b>(-28.59%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>219.00 (n/a)</td><td>180.42 (n/a)</td><td>174.10 (n/a)</td><td>156.40 (n/a)</td><td>23.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.23 (+2.76%)</td><td>0.20 (+8.71%)</td><td>0.21 (+11.06%)</td><td>0.16 (+15.43%)</td><td>0.03 <b>(-21.98%)</b></td><td>209.10 (-13.38%)</td><td>168.48 (-9.71%)</td><td>155.80 (-9.94%)</td><td>144.50 (-2.63%)</td><td>27.94 <b>(-33.88%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>241.40 (n/a)</td><td>186.60 (n/a)</td><td>173.00 (n/a)</td><td>148.40 (n/a)</td><td>42.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.29 (-7.14%)</td><td>0.24 (+14.75%)</td><td>0.24 <b>(+27.78%)</b></td><td>0.21 <b>(+20.45%)</b></td><td>0.03 <b>(-45.76%)</b></td><td>175.00 (-16.98%)</td><td>154.50 (-15.56%)</td><td>152.10 <b>(-21.76%)</b></td><td>129.00 (+7.77%)</td><td>18.59 <b>(-50.03%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>210.80 (n/a)</td><td>182.98 (n/a)</td><td>194.40 (n/a)</td><td>119.70 (n/a)</td><td>37.20 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.27 (-2.44%)</td><td>0.19 (-6.73%)</td><td>0.17 (-17.10%)</td><td>0.14 (-5.84%)</td><td>0.05 (-1.09%)</td><td>238.80 (+6.18%)</td><td>183.96 (+7.35%)</td><td>195.20 <b>(+20.64%)</b></td><td>122.70 (+2.51%)</td><td>45.15 (+3.81%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>224.90 (n/a)</td><td>171.36 (n/a)</td><td>161.80 (n/a)</td><td>119.70 (n/a)</td><td>43.49 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.20 <b>(-23.06%)</b></td><td>0.16 (-15.32%)</td><td>0.17 (-5.48%)</td><td>0.10 <b>(-40.46%)</b></td><td>0.04 (+4.71%)</td><td>359.00 <b>(+67.91%)</b></td><td>229.84 <b>(+22.62%)</b></td><td>201.70 (+5.77%)</td><td>177.70 <b>(+29.99%)</b></td><td>74.02 <b>(+144.67%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>213.80 (n/a)</td><td>187.44 (n/a)</td><td>190.70 (n/a)</td><td>136.70 (n/a)</td><td>30.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.23 (-13.41%)</td><td>0.20 (-0.28%)</td><td>0.20 (+11.51%)</td><td>0.15 (-3.53%)</td><td>0.03 <b>(-36.58%)</b></td><td>212.00 (+3.67%)</td><td>169.30 (-1.54%)</td><td>167.60 (-10.33%)</td><td>139.80 (+15.44%)</td><td>26.51 <b>(-21.85%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>204.50 (n/a)</td><td>171.94 (n/a)</td><td>186.90 (n/a)</td><td>121.10 (n/a)</td><td>33.93 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.21 (+13.18%)</td><td>0.18 (+6.49%)</td><td>0.18 (+4.57%)</td><td>0.15 (+1.99%)</td><td>0.03 <b>(+89.94%)</b></td><td>225.60 (-1.96%)</td><td>194.50 (-4.91%)</td><td>191.50 (-4.39%)</td><td>164.70 (-11.64%)</td><td>29.66 <b>(+65.40%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>230.10 (n/a)</td><td>204.54 (n/a)</td><td>200.30 (n/a)</td><td>186.40 (n/a)</td><td>17.93 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.19 (+1.50%)</td><td>0.17 (+11.31%)</td><td>0.17 <b>(+20.89%)</b></td><td>0.14 (+8.53%)</td><td>0.02 (-19.81%)</td><td>236.90 (-7.86%)</td><td>195.16 (-10.79%)</td><td>188.20 (-17.31%)</td><td>176.40 (-1.51%)</td><td>23.95 <b>(-24.55%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>257.10 (n/a)</td><td>218.76 (n/a)</td><td>227.60 (n/a)</td><td>179.10 (n/a)</td><td>31.75 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/rope</summary>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.16 (+7.91%)</td><td>0.13 (+0.97%)</td><td>0.13 (+1.46%)</td><td>0.10 (-12.09%)</td><td>0.02 <b>(+73.65%)</b></td><td>212.20 (+13.78%)</td><td>163.76 (+1.12%)</td><td>161.60 (-1.40%)</td><td>129.40 (-7.31%)</td><td>32.65 <b>(+82.90%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>186.50 (n/a)</td><td>161.94 (n/a)</td><td>163.90 (n/a)</td><td>139.60 (n/a)</td><td>17.85 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.15 <b>(+42.96%)</b></td><td>0.13 <b>(+22.59%)</b></td><td>0.13 <b>(+25.58%)</b></td><td>0.08 (-9.57%)</td><td>0.03 <b>(+360.78%)</b></td><td>241.80 (+10.56%)</td><td>168.94 (-15.23%)</td><td>157.00 <b>(-20.35%)</b></td><td>132.30 <b>(-30.07%)</b></td><td>42.24 <b>(+271.29%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>218.70 (n/a)</td><td>199.30 (n/a)</td><td>197.10 (n/a)</td><td>189.20 (n/a)</td><td>11.38 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.13 <b>(-27.83%)</b></td><td>0.11 (-19.73%)</td><td>0.11 (-14.87%)</td><td>0.09 <b>(-23.34%)</b></td><td>0.02 <b>(-38.35%)</b></td><td>236.00 <b>(+30.46%)</b></td><td>189.36 <b>(+23.23%)</b></td><td>194.90 (+17.48%)</td><td>154.70 <b>(+38.50%)</b></td><td>32.22 (+9.49%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>180.90 (n/a)</td><td>153.66 (n/a)</td><td>165.90 (n/a)</td><td>111.70 (n/a)</td><td>29.43 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.15 (-6.33%)</td><td>0.13 (+3.14%)</td><td>0.15 <b>(+26.98%)</b></td><td>0.09 (-7.35%)</td><td>0.03 (-8.74%)</td><td>233.70 (+7.94%)</td><td>164.94 (-3.12%)</td><td>141.00 <b>(-21.27%)</b></td><td>137.30 (+6.77%)</td><td>41.40 (+7.51%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>216.50 (n/a)</td><td>170.26 (n/a)</td><td>179.10 (n/a)</td><td>128.60 (n/a)</td><td>38.51 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.16 (-2.58%)</td><td>0.13 (+8.09%)</td><td>0.13 (+5.55%)</td><td>0.11 <b>(+46.99%)</b></td><td>0.02 <b>(-41.88%)</b></td><td>183.30 <b>(-31.99%)</b></td><td>156.22 (-12.45%)</td><td>154.50 (-5.27%)</td><td>129.90 (+2.69%)</td><td>23.52 <b>(-59.22%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>269.50 (n/a)</td><td>178.44 (n/a)</td><td>163.10 (n/a)</td><td>126.50 (n/a)</td><td>57.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.16 (+5.74%)</td><td>0.14 (+4.15%)</td><td>0.14 (-1.06%)</td><td>0.11 (-4.24%)</td><td>0.02 <b>(+22.88%)</b></td><td>182.70 (+4.46%)</td><td>145.62 (-3.41%)</td><td>143.00 (+1.06%)</td><td>125.90 (-5.41%)</td><td>23.26 (+19.90%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>174.90 (n/a)</td><td>150.76 (n/a)</td><td>141.50 (n/a)</td><td>133.10 (n/a)</td><td>19.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.16 (+9.19%)</td><td>0.12 (+3.93%)</td><td>0.11 (+6.68%)</td><td>0.10 (+0.24%)</td><td>0.02 (+14.61%)</td><td>204.00 (-0.24%)</td><td>176.56 (-3.47%)</td><td>189.40 (-6.24%)</td><td>132.00 (-8.40%)</td><td>28.53 (+0.87%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>204.50 (n/a)</td><td>182.90 (n/a)</td><td>202.00 (n/a)</td><td>144.10 (n/a)</td><td>28.28 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.16 (+10.71%)</td><td>0.12 (+5.59%)</td><td>0.13 (+2.77%)</td><td>0.08 (+13.48%)</td><td>0.03 (+7.49%)</td><td>246.10 (-11.89%)</td><td>176.14 (-5.84%)</td><td>162.30 (-2.64%)</td><td>130.90 (-9.66%)</td><td>43.89 (-17.19%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>279.30 (n/a)</td><td>187.06 (n/a)</td><td>166.70 (n/a)</td><td>144.90 (n/a)</td><td>53.00 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.15 <b>(-20.02%)</b></td><td>0.14 (-10.28%)</td><td>0.14 (-15.35%)</td><td>0.14 (+5.07%)</td><td>0.00 <b>(-81.37%)</b></td><td>178.40 (-4.80%)</td><td>171.76 (+9.00%)</td><td>172.70 (+18.13%)</td><td>162.40 <b>(+25.02%)</b></td><td>5.79 <b>(-78.67%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>187.40 (n/a)</td><td>157.58 (n/a)</td><td>146.20 (n/a)</td><td>129.90 (n/a)</td><td>27.16 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.17 (-10.76%)</td><td>0.16 (-0.44%)</td><td>0.17 (+0.43%)</td><td>0.14 (+7.48%)</td><td>0.01 <b>(-44.82%)</b></td><td>170.10 (-7.00%)</td><td>154.70 (-0.76%)</td><td>148.00 (-0.40%)</td><td>142.50 (+12.03%)</td><td>13.01 <b>(-42.97%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>182.90 (n/a)</td><td>155.88 (n/a)</td><td>148.60 (n/a)</td><td>127.20 (n/a)</td><td>22.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.20 (-2.23%)</td><td>0.14 (+1.21%)</td><td>0.15 (+14.52%)</td><td>0.09 (-12.63%)</td><td>0.04 (+2.19%)</td><td>272.30 (+14.46%)</td><td>190.64 (+0.00%)</td><td>166.20 (-12.71%)</td><td>125.40 (+2.28%)</td><td>57.54 (+19.19%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>237.90 (n/a)</td><td>190.64 (n/a)</td><td>190.40 (n/a)</td><td>122.60 (n/a)</td><td>48.27 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.19 (-0.88%)</td><td>0.17 (+14.13%)</td><td>0.17 (+9.84%)</td><td>0.13 <b>(+23.49%)</b></td><td>0.02 <b>(-32.65%)</b></td><td>186.90 (-19.02%)</td><td>149.28 (-14.64%)</td><td>146.00 (-8.98%)</td><td>128.90 (+0.86%)</td><td>22.46 <b>(-44.47%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>230.80 (n/a)</td><td>174.88 (n/a)</td><td>160.40 (n/a)</td><td>127.80 (n/a)</td><td>40.45 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.21 (+18.76%)</td><td>0.16 (+6.62%)</td><td>0.17 (+8.55%)</td><td>0.12 (-3.11%)</td><td>0.04 <b>(+84.77%)</b></td><td>208.40 (+3.22%)</td><td>161.90 (-3.49%)</td><td>147.10 (-7.89%)</td><td>119.70 (-15.82%)</td><td>37.79 <b>(+63.59%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>201.90 (n/a)</td><td>167.76 (n/a)</td><td>159.70 (n/a)</td><td>142.20 (n/a)</td><td>23.10 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.22 (-3.90%)</td><td>0.17 (+13.72%)</td><td>0.19 <b>(+33.95%)</b></td><td>0.13 (+16.17%)</td><td>0.04 (-19.31%)</td><td>190.30 (-13.93%)</td><td>148.16 (-14.19%)</td><td>132.00 <b>(-25.34%)</b></td><td>110.90 (+4.03%)</td><td>33.89 <b>(-24.27%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>221.10 (n/a)</td><td>172.66 (n/a)</td><td>176.80 (n/a)</td><td>106.60 (n/a)</td><td>44.75 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.23 <b>(+46.52%)</b></td><td>0.17 <b>(+40.46%)</b></td><td>0.16 <b>(+41.45%)</b></td><td>0.11 <b>(+24.20%)</b></td><td>0.04 <b>(+74.58%)</b></td><td>229.30 (-19.49%)</td><td>157.56 <b>(-27.06%)</b></td><td>154.90 <b>(-29.30%)</b></td><td>107.40 <b>(-31.77%)</b></td><td>45.23 (-2.21%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>284.80 (n/a)</td><td>216.00 (n/a)</td><td>219.10 (n/a)</td><td>157.40 (n/a)</td><td>46.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.19 (+17.40%)</td><td>0.12 (-13.96%)</td><td>0.11 <b>(-25.72%)</b></td><td>0.09 (-12.85%)</td><td>0.04 <b>(+73.68%)</b></td><td>265.20 (+14.71%)</td><td>213.16 <b>(+21.10%)</b></td><td>214.60 <b>(+34.63%)</b></td><td>131.50 (-14.83%)</td><td>54.09 <b>(+67.84%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>231.20 (n/a)</td><td>176.02 (n/a)</td><td>159.40 (n/a)</td><td>154.40 (n/a)</td><td>32.23 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.14 <b>(+20.86%)</b></td><td>0.13 (+19.04%)</td><td>0.14 <b>(+30.87%)</b></td><td>0.09 (-6.46%)</td><td>0.02 <b>(+130.23%)</b></td><td>208.00 (+6.94%)</td><td>152.40 (-13.69%)</td><td>132.80 <b>(-23.59%)</b></td><td>128.40 (-17.27%)</td><td>34.23 <b>(+97.40%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>194.50 (n/a)</td><td>176.58 (n/a)</td><td>173.80 (n/a)</td><td>155.20 (n/a)</td><td>17.34 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.15 <b>(+33.57%)</b></td><td>0.13 <b>(+29.60%)</b></td><td>0.14 <b>(+40.59%)</b></td><td>0.10 (+7.77%)</td><td>0.02 <b>(+153.16%)</b></td><td>186.90 (-7.20%)</td><td>146.46 <b>(-21.62%)</b></td><td>136.40 <b>(-28.88%)</b></td><td>124.30 <b>(-25.17%)</b></td><td>24.59 <b>(+81.11%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>201.40 (n/a)</td><td>186.86 (n/a)</td><td>191.80 (n/a)</td><td>166.10 (n/a)</td><td>13.58 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.14 (-13.36%)</td><td>0.11 (+1.72%)</td><td>0.12 (+16.41%)</td><td>0.08 (+0.85%)</td><td>0.02 <b>(-28.21%)</b></td><td>218.20 (-0.86%)</td><td>171.76 (-3.61%)</td><td>158.80 (-14.12%)</td><td>128.20 (+15.39%)</td><td>35.90 (-11.60%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>220.10 (n/a)</td><td>178.20 (n/a)</td><td>184.90 (n/a)</td><td>111.10 (n/a)</td><td>40.61 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.13 (-4.84%)</td><td>0.10 (-10.28%)</td><td>0.10 (-6.10%)</td><td>0.05 <b>(-31.61%)</b></td><td>0.03 <b>(+24.60%)</b></td><td>353.50 <b>(+46.26%)</b></td><td>207.56 (+18.12%)</td><td>180.80 (+6.48%)</td><td>137.70 (+5.11%)</td><td>84.16 <b>(+102.62%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>241.70 (n/a)</td><td>175.72 (n/a)</td><td>169.80 (n/a)</td><td>131.00 (n/a)</td><td>41.54 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.14 (+3.47%)</td><td>0.12 (+8.86%)</td><td>0.11 (+13.44%)</td><td>0.08 (-10.06%)</td><td>0.02 <b>(+25.02%)</b></td><td>228.90 (+11.22%)</td><td>165.84 (-6.62%)</td><td>165.80 (-11.81%)</td><td>128.50 (-3.38%)</td><td>39.25 <b>(+37.84%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>205.80 (n/a)</td><td>177.60 (n/a)</td><td>188.00 (n/a)</td><td>133.00 (n/a)</td><td>28.48 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.14 (-9.30%)</td><td>0.12 (+4.49%)</td><td>0.12 (+18.12%)</td><td>0.11 <b>(+23.35%)</b></td><td>0.01 <b>(-52.30%)</b></td><td>174.90 (-18.95%)</td><td>152.38 (-8.05%)</td><td>150.50 (-15.35%)</td><td>133.90 (+10.30%)</td><td>17.94 <b>(-55.93%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>215.80 (n/a)</td><td>165.72 (n/a)</td><td>177.80 (n/a)</td><td>121.40 (n/a)</td><td>40.70 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.11 (+1.50%)</td><td>0.10 (+0.58%)</td><td>0.10 (+1.21%)</td><td>0.09 (-0.68%)</td><td>0.01 (+2.52%)</td><td>212.50 (+0.71%)</td><td>190.58 (-0.55%)</td><td>188.30 (-1.15%)</td><td>162.20 (-1.52%)</td><td>19.10 (+0.40%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>211.00 (n/a)</td><td>191.64 (n/a)</td><td>190.50 (n/a)</td><td>164.70 (n/a)</td><td>19.02 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.11 (+9.91%)</td><td>0.10 (+3.81%)</td><td>0.10 (+6.04%)</td><td>0.08 (-8.74%)</td><td>0.01 <b>(+142.63%)</b></td><td>217.00 (+9.54%)</td><td>180.72 (-2.85%)</td><td>176.70 (-5.71%)</td><td>161.30 (-9.02%)</td><td>21.59 <b>(+147.80%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.00 (n/a)</td><td>198.10 (n/a)</td><td>186.02 (n/a)</td><td>187.40 (n/a)</td><td>177.30 (n/a)</td><td>8.71 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.60 (-4.06%)</td><td>0.55 (+6.82%)</td><td>0.55 (+5.36%)</td><td>0.48 (+9.36%)</td><td>0.05 <b>(-33.61%)</b></td><td>206.70 (-8.58%)</td><td>180.10 (-7.35%)</td><td>177.40 (-5.08%)</td><td>162.80 (+4.23%)</td><td>17.61 <b>(-37.60%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.63 (n/a)</td><td>0.51 (n/a)</td><td>0.53 (n/a)</td><td>0.43 (n/a)</td><td>0.08 (n/a)</td><td>226.10 (n/a)</td><td>194.38 (n/a)</td><td>186.90 (n/a)</td><td>156.20 (n/a)</td><td>28.22 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.69 (-12.81%)</td><td>0.55 (-13.99%)</td><td>0.54 (-14.95%)</td><td>0.46 (-18.50%)</td><td>0.09 (+6.05%)</td><td>213.50 <b>(+22.70%)</b></td><td>181.52 (+17.26%)</td><td>182.70 (+17.57%)</td><td>142.00 (+14.70%)</td><td>29.35 <b>(+53.27%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.79 (n/a)</td><td>0.64 (n/a)</td><td>0.63 (n/a)</td><td>0.57 (n/a)</td><td>0.09 (n/a)</td><td>174.00 (n/a)</td><td>154.80 (n/a)</td><td>155.40 (n/a)</td><td>123.80 (n/a)</td><td>19.15 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.76 (-0.44%)</td><td>0.60 (+7.25%)</td><td>0.67 <b>(+32.31%)</b></td><td>0.43 (-2.83%)</td><td>0.15 (+13.47%)</td><td>227.60 (+2.94%)</td><td>172.78 (-5.28%)</td><td>145.80 <b>(-24.42%)</b></td><td>128.50 (+0.39%)</td><td>47.85 <b>(+20.87%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.77 (n/a)</td><td>0.56 (n/a)</td><td>0.51 (n/a)</td><td>0.44 (n/a)</td><td>0.14 (n/a)</td><td>221.10 (n/a)</td><td>182.42 (n/a)</td><td>192.90 (n/a)</td><td>128.00 (n/a)</td><td>39.59 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.60 (-18.96%)</td><td>0.46 (-19.25%)</td><td>0.49 (-7.60%)</td><td>0.30 (-18.25%)</td><td>0.13 <b>(-21.18%)</b></td><td>322.40 <b>(+22.31%)</b></td><td>230.78 <b>(+23.86%)</b></td><td>201.40 (+8.22%)</td><td>162.80 <b>(+23.43%)</b></td><td>69.75 <b>(+26.29%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.75 (n/a)</td><td>0.57 (n/a)</td><td>0.53 (n/a)</td><td>0.37 (n/a)</td><td>0.16 (n/a)</td><td>263.60 (n/a)</td><td>186.32 (n/a)</td><td>186.10 (n/a)</td><td>131.90 (n/a)</td><td>55.23 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.59 <b>(+45.83%)</b></td><td>0.48 (+19.92%)</td><td>0.46 (+15.23%)</td><td>0.36 (-7.41%)</td><td>0.09 <b>(+1246.63%)</b></td><td>205.20 (+8.00%)</td><td>159.76 (-13.95%)</td><td>161.50 (-13.17%)</td><td>124.20 <b>(-31.46%)</b></td><td>32.03 <b>(+888.48%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.41 (n/a)</td><td>0.40 (n/a)</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.01 (n/a)</td><td>190.00 (n/a)</td><td>185.66 (n/a)</td><td>186.00 (n/a)</td><td>181.20 (n/a)</td><td>3.24 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.55 (+11.99%)</td><td>0.43 (+8.16%)</td><td>0.43 (+9.72%)</td><td>0.32 (+9.46%)</td><td>0.08 (+10.66%)</td><td>227.50 (-8.63%)</td><td>176.06 (-7.55%)</td><td>173.00 (-8.90%)</td><td>134.20 (-10.71%)</td><td>34.22 (-9.70%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.49 (n/a)</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.30 (n/a)</td><td>0.07 (n/a)</td><td>249.00 (n/a)</td><td>190.44 (n/a)</td><td>189.90 (n/a)</td><td>150.30 (n/a)</td><td>37.90 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.59 (-1.23%)</td><td>0.45 (+5.81%)</td><td>0.46 <b>(+23.43%)</b></td><td>0.28 (-14.54%)</td><td>0.12 (+12.55%)</td><td>263.30 (+17.02%)</td><td>175.74 (-3.29%)</td><td>159.90 (-19.00%)</td><td>125.20 (+1.21%)</td><td>55.28 <b>(+35.86%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.60 (n/a)</td><td>0.42 (n/a)</td><td>0.37 (n/a)</td><td>0.33 (n/a)</td><td>0.11 (n/a)</td><td>225.00 (n/a)</td><td>181.72 (n/a)</td><td>197.40 (n/a)</td><td>123.70 (n/a)</td><td>40.69 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.46 (-18.38%)</td><td>0.36 (-19.01%)</td><td>0.35 (-14.84%)</td><td>0.23 <b>(-39.91%)</b></td><td>0.09 (+13.92%)</td><td>323.20 <b>(+66.43%)</b></td><td>217.92 <b>(+28.01%)</b></td><td>212.50 (+17.40%)</td><td>161.00 <b>(+22.53%)</b></td><td>64.13 <b>(+130.47%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.56 (n/a)</td><td>0.44 (n/a)</td><td>0.41 (n/a)</td><td>0.38 (n/a)</td><td>0.08 (n/a)</td><td>194.20 (n/a)</td><td>170.24 (n/a)</td><td>181.00 (n/a)</td><td>131.40 (n/a)</td><td>27.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.28 (+11.19%)</td><td>0.24 (+7.93%)</td><td>0.23 (+7.43%)</td><td>0.20 (-1.44%)</td><td>0.03 <b>(+53.25%)</b></td><td>187.00 (+1.47%)</td><td>158.06 (-6.61%)</td><td>160.60 (-6.90%)</td><td>129.70 (-10.06%)</td><td>21.30 <b>(+41.97%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>184.30 (n/a)</td><td>169.24 (n/a)</td><td>172.50 (n/a)</td><td>144.20 (n/a)</td><td>15.00 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.24 (+1.08%)</td><td>0.20 (-0.17%)</td><td>0.21 (+3.03%)</td><td>0.17 (-6.27%)</td><td>0.04 <b>(+44.30%)</b></td><td>222.30 (+6.67%)</td><td>184.36 (+1.53%)</td><td>173.50 (-2.91%)</td><td>151.90 (-1.04%)</td><td>32.75 <b>(+54.15%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>208.40 (n/a)</td><td>181.58 (n/a)</td><td>178.70 (n/a)</td><td>153.50 (n/a)</td><td>21.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.22 <b>(-36.28%)</b></td><td>0.20 <b>(-21.24%)</b></td><td>0.21 (-13.18%)</td><td>0.18 (-8.14%)</td><td>0.02 <b>(-68.95%)</b></td><td>205.90 (+8.83%)</td><td>181.56 <b>(+23.54%)</b></td><td>172.30 (+15.17%)</td><td>170.40 <b>(+56.91%)</b></td><td>15.62 <b>(-47.01%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.34 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>189.20 (n/a)</td><td>146.96 (n/a)</td><td>149.60 (n/a)</td><td>108.60 (n/a)</td><td>29.48 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.28 (+4.53%)</td><td>0.23 (+0.70%)</td><td>0.22 (+1.12%)</td><td>0.19 (-0.63%)</td><td>0.03 (+10.03%)</td><td>190.70 (+0.63%)</td><td>164.80 (-0.53%)</td><td>168.50 (-1.12%)</td><td>132.00 (-4.35%)</td><td>21.30 (+4.07%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>189.50 (n/a)</td><td>165.68 (n/a)</td><td>170.40 (n/a)</td><td>138.00 (n/a)</td><td>20.47 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.33 <b>(+26.23%)</b></td><td>0.24 (+9.05%)</td><td>0.23 (+8.80%)</td><td>0.21 (+4.01%)</td><td>0.05 <b>(+106.15%)</b></td><td>179.70 (-3.85%)</td><td>155.24 (-6.53%)</td><td>157.40 (-8.06%)</td><td>112.30 <b>(-20.80%)</b></td><td>26.62 <b>(+55.83%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>186.90 (n/a)</td><td>166.08 (n/a)</td><td>171.20 (n/a)</td><td>141.80 (n/a)</td><td>17.09 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.24 (-4.85%)</td><td>0.21 (-0.22%)</td><td>0.20 (+1.96%)</td><td>0.18 (+1.73%)</td><td>0.03 <b>(-25.98%)</b></td><td>207.90 (-1.70%)</td><td>179.42 (-0.81%)</td><td>188.50 (-1.93%)</td><td>151.60 (+5.13%)</td><td>22.97 <b>(-24.08%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>211.50 (n/a)</td><td>180.88 (n/a)</td><td>192.20 (n/a)</td><td>144.20 (n/a)</td><td>30.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.25 (-4.61%)</td><td>0.21 (-5.58%)</td><td>0.22 (-0.62%)</td><td>0.16 (-13.36%)</td><td>0.04 <b>(+22.31%)</b></td><td>233.10 (+15.40%)</td><td>183.00 (+7.24%)</td><td>164.40 (+0.61%)</td><td>147.70 (+4.83%)</td><td>35.47 <b>(+48.35%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>202.00 (n/a)</td><td>170.64 (n/a)</td><td>163.40 (n/a)</td><td>140.90 (n/a)</td><td>23.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.26 <b>(+23.20%)</b></td><td>0.21 <b>(+23.36%)</b></td><td>0.23 <b>(+39.10%)</b></td><td>0.14 <b>(+22.73%)</b></td><td>0.04 (+17.97%)</td><td>255.20 (-18.52%)</td><td>180.14 (-19.09%)</td><td>159.10 <b>(-28.11%)</b></td><td>142.40 (-18.81%)</td><td>44.69 (-19.26%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>313.20 (n/a)</td><td>222.64 (n/a)</td><td>221.30 (n/a)</td><td>175.40 (n/a)</td><td>55.35 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.28 (-6.77%)</td><td>0.24 (-2.76%)</td><td>0.24 (+4.22%)</td><td>0.20 (+1.87%)</td><td>0.03 <b>(-33.43%)</b></td><td>199.80 (-1.87%)</td><td>173.08 (+1.67%)</td><td>170.50 (-4.05%)</td><td>147.90 (+7.25%)</td><td>19.72 <b>(-28.69%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>203.60 (n/a)</td><td>170.24 (n/a)</td><td>177.70 (n/a)</td><td>137.90 (n/a)</td><td>27.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.27 (+15.60%)</td><td>0.23 (+8.23%)</td><td>0.22 (+1.26%)</td><td>0.19 (+3.26%)</td><td>0.04 <b>(+55.66%)</b></td><td>217.10 (-3.17%)</td><td>184.74 (-6.44%)</td><td>190.30 (-1.25%)</td><td>149.70 (-13.47%)</td><td>32.15 <b>(+28.82%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>224.20 (n/a)</td><td>197.46 (n/a)</td><td>192.70 (n/a)</td><td>173.00 (n/a)</td><td>24.96 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.29 (+0.15%)</td><td>0.23 (-4.36%)</td><td>0.22 (-0.95%)</td><td>0.20 (-5.48%)</td><td>0.03 (-2.22%)</td><td>205.10 (+5.83%)</td><td>179.46 (+4.54%)</td><td>182.70 (+1.00%)</td><td>142.80 (-0.21%)</td><td>24.00 (+2.18%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>193.80 (n/a)</td><td>171.66 (n/a)</td><td>180.90 (n/a)</td><td>143.10 (n/a)</td><td>23.49 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.31 (-8.60%)</td><td>0.26 (+5.21%)</td><td>0.24 (+1.44%)</td><td>0.23 (+18.24%)</td><td>0.04 <b>(-25.99%)</b></td><td>180.00 (-15.41%)</td><td>159.06 (-6.53%)</td><td>168.90 (-1.46%)</td><td>132.30 (+9.34%)</td><td>23.67 <b>(-30.02%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.06 (n/a)</td><td>212.80 (n/a)</td><td>170.18 (n/a)</td><td>171.40 (n/a)</td><td>121.00 (n/a)</td><td>33.82 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.31 (+3.71%)</td><td>0.26 (+12.14%)</td><td>0.26 (+14.81%)</td><td>0.21 (+7.73%)</td><td>0.04 (-3.09%)</td><td>193.80 (-7.18%)</td><td>159.04 (-11.13%)</td><td>159.90 (-12.91%)</td><td>131.40 (-3.52%)</td><td>24.76 (-13.05%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>208.80 (n/a)</td><td>178.96 (n/a)</td><td>183.60 (n/a)</td><td>136.20 (n/a)</td><td>28.47 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.30 (+0.07%)</td><td>0.25 (+10.81%)</td><td>0.24 (+4.68%)</td><td>0.22 <b>(+26.79%)</b></td><td>0.03 <b>(-35.72%)</b></td><td>182.10 <b>(-21.13%)</b></td><td>166.18 (-11.95%)</td><td>172.50 (-4.49%)</td><td>135.90 (+0.00%)</td><td>19.41 <b>(-50.12%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>230.90 (n/a)</td><td>188.74 (n/a)</td><td>180.60 (n/a)</td><td>135.90 (n/a)</td><td>38.92 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.35 (+6.77%)</td><td>0.25 (+15.92%)</td><td>0.25 <b>(+24.63%)</b></td><td>0.19 (+16.16%)</td><td>0.06 (-10.73%)</td><td>212.00 (-13.93%)</td><td>167.16 (-15.71%)</td><td>163.30 (-19.75%)</td><td>116.80 (-6.34%)</td><td>35.20 <b>(-30.23%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.33 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.07 (n/a)</td><td>246.30 (n/a)</td><td>198.32 (n/a)</td><td>203.50 (n/a)</td><td>124.70 (n/a)</td><td>50.45 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.31 (+7.83%)</td><td>0.26 (+12.37%)</td><td>0.26 <b>(+25.42%)</b></td><td>0.18 (-9.60%)</td><td>0.05 <b>(+36.53%)</b></td><td>223.80 (+10.63%)</td><td>164.16 (-9.59%)</td><td>155.20 <b>(-20.25%)</b></td><td>132.50 (-7.28%)</td><td>35.68 <b>(+43.92%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>202.30 (n/a)</td><td>181.58 (n/a)</td><td>194.60 (n/a)</td><td>142.90 (n/a)</td><td>24.79 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.28 (+16.65%)</td><td>0.21 (-0.60%)</td><td>0.22 (+7.41%)</td><td>0.15 (-17.00%)</td><td>0.05 <b>(+149.92%)</b></td><td>231.60 <b>(+20.50%)</b></td><td>177.34 (+5.10%)</td><td>157.80 (-6.85%)</td><td>125.00 (-14.27%)</td><td>44.90 <b>(+167.50%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>192.20 (n/a)</td><td>168.74 (n/a)</td><td>169.40 (n/a)</td><td>145.80 (n/a)</td><td>16.78 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.25 (+3.61%)</td><td>0.19 (-1.82%)</td><td>0.20 (+14.78%)</td><td>0.09 <b>(-47.08%)</b></td><td>0.06 <b>(+112.54%)</b></td><td>382.50 <b>(+88.98%)</b></td><td>207.88 (+13.68%)</td><td>169.90 (-12.87%)</td><td>141.10 (-3.49%)</td><td>99.27 <b>(+310.55%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>202.40 (n/a)</td><td>182.86 (n/a)</td><td>195.00 (n/a)</td><td>146.20 (n/a)</td><td>24.18 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.25 (-3.28%)</td><td>0.22 (+4.80%)</td><td>0.21 (+0.20%)</td><td>0.20 <b>(+21.84%)</b></td><td>0.02 <b>(-35.55%)</b></td><td>174.30 (-17.90%)</td><td>158.72 (-6.12%)</td><td>163.60 (-0.18%)</td><td>139.90 (+3.40%)</td><td>16.70 <b>(-45.43%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>212.30 (n/a)</td><td>169.06 (n/a)</td><td>163.90 (n/a)</td><td>135.30 (n/a)</td><td>30.60 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.26 (-7.66%)</td><td>0.22 (+0.04%)</td><td>0.22 (+16.49%)</td><td>0.19 (+15.35%)</td><td>0.03 <b>(-48.96%)</b></td><td>183.00 (-13.31%)</td><td>162.62 (-3.72%)</td><td>160.60 (-14.16%)</td><td>132.40 (+8.35%)</td><td>19.70 <b>(-51.29%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>211.10 (n/a)</td><td>168.90 (n/a)</td><td>187.10 (n/a)</td><td>122.20 (n/a)</td><td>40.45 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.27 (-12.40%)</td><td>0.24 (+14.69%)</td><td>0.25 <b>(+29.97%)</b></td><td>0.20 (+16.84%)</td><td>0.03 <b>(-45.80%)</b></td><td>170.80 (-14.39%)</td><td>148.00 (-15.56%)</td><td>141.00 <b>(-23.08%)</b></td><td>128.40 (+14.13%)</td><td>19.78 <b>(-45.08%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>199.50 (n/a)</td><td>175.28 (n/a)</td><td>183.30 (n/a)</td><td>112.50 (n/a)</td><td>36.03 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.27 (-13.69%)</td><td>0.21 (-9.89%)</td><td>0.19 (-19.46%)</td><td>0.16 (-2.59%)</td><td>0.05 (-19.75%)</td><td>212.40 (+2.66%)</td><td>173.14 (+9.80%)</td><td>181.70 <b>(+24.20%)</b></td><td>128.90 (+15.92%)</td><td>35.20 (-6.05%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>206.90 (n/a)</td><td>157.68 (n/a)</td><td>146.30 (n/a)</td><td>111.20 (n/a)</td><td>37.47 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.36 <b>(+65.24%)</b></td><td>0.23 <b>(+22.12%)</b></td><td>0.22 (+16.80%)</td><td>0.18 (+3.74%)</td><td>0.07 <b>(+319.28%)</b></td><td>192.60 (-3.60%)</td><td>160.24 (-13.57%)</td><td>161.40 (-14.38%)</td><td>97.90 <b>(-39.49%)</b></td><td>38.09 <b>(+137.60%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>199.80 (n/a)</td><td>185.40 (n/a)</td><td>188.50 (n/a)</td><td>161.80 (n/a)</td><td>16.03 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.26 (+7.91%)</td><td>0.21 (+5.80%)</td><td>0.22 (+9.87%)</td><td>0.16 (-6.24%)</td><td>0.05 <b>(+78.76%)</b></td><td>214.70 (+6.66%)</td><td>171.64 (-2.58%)</td><td>159.30 (-9.02%)</td><td>131.90 (-7.37%)</td><td>40.57 <b>(+85.43%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>201.30 (n/a)</td><td>176.18 (n/a)</td><td>175.10 (n/a)</td><td>142.40 (n/a)</td><td>21.88 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.83 (-10.79%)</td><td>0.68 (-12.99%)</td><td>0.69 (-10.74%)</td><td>0.50 <b>(-26.68%)</b></td><td>0.12 (+17.95%)</td><td>263.70 <b>(+36.42%)</b></td><td>199.58 (+16.69%)</td><td>189.40 (+12.00%)</td><td>158.10 (+12.13%)</td><td>39.74 <b>(+81.83%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.93 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.68 (n/a)</td><td>0.10 (n/a)</td><td>193.30 (n/a)</td><td>171.04 (n/a)</td><td>169.10 (n/a)</td><td>141.00 (n/a)</td><td>21.86 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.93 (+4.78%)</td><td>0.74 (-4.12%)</td><td>0.72 (-5.81%)</td><td>0.60 (-9.56%)</td><td>0.12 <b>(+50.64%)</b></td><td>217.10 (+10.54%)</td><td>179.88 (+5.48%)</td><td>181.60 (+6.20%)</td><td>141.60 (-4.58%)</td><td>27.60 <b>(+56.71%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.88 (n/a)</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.67 (n/a)</td><td>0.08 (n/a)</td><td>196.40 (n/a)</td><td>170.54 (n/a)</td><td>171.00 (n/a)</td><td>148.40 (n/a)</td><td>17.61 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.95 (+0.93%)</td><td>0.66 (-11.83%)</td><td>0.61 (-12.72%)</td><td>0.38 <b>(-39.97%)</b></td><td>0.26 <b>(+115.60%)</b></td><td>340.50 <b>(+66.59%)</b></td><td>227.40 <b>(+27.18%)</b></td><td>215.40 (+14.57%)</td><td>138.60 (-0.93%)</td><td>91.15 <b>(+243.14%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.94 (n/a)</td><td>0.75 (n/a)</td><td>0.70 (n/a)</td><td>0.64 (n/a)</td><td>0.12 (n/a)</td><td>204.40 (n/a)</td><td>178.80 (n/a)</td><td>188.00 (n/a)</td><td>139.90 (n/a)</td><td>26.56 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (+12.73%)</td><td>0.02 (-2.59%)</td><td>0.02 (-18.30%)</td><td>0.02 (+7.71%)</td><td>0.01 <b>(+42.87%)</b></td><td>205.90 (-7.17%)</td><td>171.80 (+4.39%)</td><td>190.00 <b>(+22.34%)</b></td><td>120.10 (-11.30%)</td><td>37.72 (+13.77%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.80 (n/a)</td><td>164.58 (n/a)</td><td>155.30 (n/a)</td><td>135.40 (n/a)</td><td>33.15 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 <b>(-21.82%)</b></td><td>0.02 (-9.77%)</td><td>0.02 (-2.81%)</td><td>0.02 (-6.67%)</td><td>0.00 <b>(-56.93%)</b></td><td>183.70 (+7.11%)</td><td>171.56 (+9.88%)</td><td>164.90 (+2.87%)</td><td>162.40 <b>(+27.97%)</b></td><td>10.63 <b>(-40.04%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>171.50 (n/a)</td><td>156.14 (n/a)</td><td>160.30 (n/a)</td><td>126.90 (n/a)</td><td>17.72 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (-8.49%)</td><td>0.02 (-19.68%)</td><td>0.02 <b>(-22.12%)</b></td><td>0.02 <b>(-23.81%)</b></td><td>0.00 <b>(+83.39%)</b></td><td>203.10 <b>(+31.29%)</b></td><td>180.00 <b>(+25.63%)</b></td><td>182.50 <b>(+28.43%)</b></td><td>148.00 (+9.31%)</td><td>20.49 <b>(+158.80%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>154.70 (n/a)</td><td>143.28 (n/a)</td><td>142.10 (n/a)</td><td>135.40 (n/a)</td><td>7.92 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_llama_full]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>15.34 (-11.21%)</td><td>12.37 (-2.95%)</td><td>11.99 (+2.42%)</td><td>10.05 (-2.71%)</td><td>1.92 <b>(-29.00%)</b></td><td>208.70 (+2.81%)</td><td>172.70 (+1.76%)</td><td>175.00 (-2.40%)</td><td>136.80 (+12.59%)</td><td>25.80 (-16.08%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>17.27 (n/a)</td><td>12.75 (n/a)</td><td>11.70 (n/a)</td><td>10.33 (n/a)</td><td>2.70 (n/a)</td><td>203.00 (n/a)</td><td>169.72 (n/a)</td><td>179.30 (n/a)</td><td>121.50 (n/a)</td><td>30.74 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>1.00 (+9.53%)</td><td>0.85 (-1.20%)</td><td>0.80 (-10.40%)</td><td>0.72 (+3.47%)</td><td>0.12 <b>(+24.59%)</b></td><td>184.30 (-3.36%)</td><td>158.00 (+1.57%)</td><td>166.00 (+11.63%)</td><td>132.00 (-8.71%)</td><td>21.25 (+7.56%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.91 (n/a)</td><td>0.86 (n/a)</td><td>0.89 (n/a)</td><td>0.69 (n/a)</td><td>0.09 (n/a)</td><td>190.70 (n/a)</td><td>155.56 (n/a)</td><td>148.70 (n/a)</td><td>144.60 (n/a)</td><td>19.76 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.92 (-10.37%)</td><td>0.79 (-5.99%)</td><td>0.81 (-6.32%)</td><td>0.63 (-8.12%)</td><td>0.11 <b>(-24.11%)</b></td><td>210.70 (+8.83%)</td><td>170.54 (+5.53%)</td><td>162.80 (+6.75%)</td><td>143.70 (+11.57%)</td><td>26.02 (-9.57%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>1.03 (n/a)</td><td>0.84 (n/a)</td><td>0.87 (n/a)</td><td>0.68 (n/a)</td><td>0.15 (n/a)</td><td>193.60 (n/a)</td><td>161.60 (n/a)</td><td>152.50 (n/a)</td><td>128.80 (n/a)</td><td>28.78 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>1.00 (+0.30%)</td><td>0.79 (-0.76%)</td><td>0.73 (-11.92%)</td><td>0.67 (+13.03%)</td><td>0.13 (-16.72%)</td><td>197.10 (-11.54%)</td><td>171.42 (-0.56%)</td><td>180.60 (+13.51%)</td><td>132.40 (-0.30%)</td><td>25.46 <b>(-28.40%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.99 (n/a)</td><td>0.79 (n/a)</td><td>0.83 (n/a)</td><td>0.59 (n/a)</td><td>0.16 (n/a)</td><td>222.80 (n/a)</td><td>172.38 (n/a)</td><td>159.10 (n/a)</td><td>132.80 (n/a)</td><td>35.55 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.81 (-18.44%)</td><td>0.75 (-5.32%)</td><td>0.77 (-4.17%)</td><td>0.62 (-2.68%)</td><td>0.08 <b>(-41.49%)</b></td><td>214.70 (+2.73%)</td><td>177.72 (+4.30%)</td><td>171.10 (+4.33%)</td><td>162.30 <b>(+22.58%)</b></td><td>21.27 <b>(-24.65%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>1.00 (n/a)</td><td>0.79 (n/a)</td><td>0.81 (n/a)</td><td>0.63 (n/a)</td><td>0.14 (n/a)</td><td>209.00 (n/a)</td><td>170.40 (n/a)</td><td>164.00 (n/a)</td><td>132.40 (n/a)</td><td>28.23 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.90 (-11.60%)</td><td>0.67 <b>(-27.07%)</b></td><td>0.64 <b>(-34.56%)</b></td><td>0.49 <b>(-34.39%)</b></td><td>0.17 <b>(+44.49%)</b></td><td>270.10 <b>(+52.43%)</b></td><td>207.06 <b>(+41.86%)</b></td><td>208.00 <b>(+52.83%)</b></td><td>146.40 (+13.14%)</td><td>49.33 <b>(+148.08%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>1.02 (n/a)</td><td>0.92 (n/a)</td><td>0.97 (n/a)</td><td>0.75 (n/a)</td><td>0.11 (n/a)</td><td>177.20 (n/a)</td><td>145.96 (n/a)</td><td>136.10 (n/a)</td><td>129.40 (n/a)</td><td>19.88 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (+2.05%)</td><td>0.03 (-10.53%)</td><td>0.02 (-18.30%)</td><td>0.02 (-12.09%)</td><td>0.00 <b>(+56.42%)</b></td><td>203.10 (+13.78%)</td><td>167.66 (+13.59%)</td><td>173.40 <b>(+22.37%)</b></td><td>131.30 (-2.01%)</td><td>29.72 <b>(+68.51%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>178.50 (n/a)</td><td>147.60 (n/a)</td><td>141.70 (n/a)</td><td>134.00 (n/a)</td><td>17.64 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.03 (-7.84%)</td><td>0.02 (-12.77%)</td><td>0.02 (-10.43%)</td><td>0.02 <b>(-24.89%)</b></td><td>0.00 <b>(+45.75%)</b></td><td>242.20 <b>(+33.15%)</b></td><td>185.50 (+16.59%)</td><td>177.20 (+11.66%)</td><td>149.30 (+8.50%)</td><td>34.29 <b>(+117.63%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>181.90 (n/a)</td><td>159.10 (n/a)</td><td>158.70 (n/a)</td><td>137.60 (n/a)</td><td>15.75 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.00 (+0.00%)</td><td>0.00 (-0.47%)</td><td>0.00 (+0.00%)</td><td>0.00 (-2.50%)</td><td>0.00 <b>(+28.54%)</b></td><td>1043.92 (+1.20%)</td><td>966.58 (+0.16%)</td><td>948.07 (+0.03%)</td><td>933.79 (-0.58%)</td><td>44.49 (+16.08%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1031.52 (n/a)</td><td>965.00 (n/a)</td><td>947.79 (n/a)</td><td>939.21 (n/a)</td><td>38.33 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.01 (-1.19%)</td><td>0.01 (-0.49%)</td><td>0.01 (+0.00%)</td><td>0.01 (-2.63%)</td><td>0.00 <b>(+26.05%)</b></td><td>1104.77 (+2.04%)</td><td>1017.79 (+0.44%)</td><td>998.63 (+0.34%)</td><td>982.71 (+0.20%)</td><td>49.66 <b>(+22.40%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1082.65 (n/a)</td><td>1013.31 (n/a)</td><td>995.20 (n/a)</td><td>980.77 (n/a)</td><td>40.58 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>1.01 (n/a)</td><td>0.97 (n/a)</td><td>0.97 (n/a)</td><td>0.95 (n/a)</td><td>0.02 (n/a)</td><td>2218.07 (n/a)</td><td>2161.11 (n/a)</td><td>2161.24 (n/a)</td><td>2080.06 (n/a)</td><td>51.51 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.90 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.84 (n/a)</td><td>0.03 (n/a)</td><td>2510.42 (n/a)</td><td>2394.12 (n/a)</td><td>2377.33 (n/a)</td><td>2320.72 (n/a)</td><td>71.72 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>1.00 (+2.52%)</td><td>0.97 (+2.77%)</td><td>0.98 (+3.79%)</td><td>0.96 (+3.26%)</td><td>0.01 (-10.41%)</td><td>2185.78 (-3.15%)</td><td>2153.41 (-2.70%)</td><td>2147.04 (-3.65%)</td><td>2106.49 (-2.45%)</td><td>32.81 (-15.16%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.97 (n/a)</td><td>0.95 (n/a)</td><td>0.94 (n/a)</td><td>0.93 (n/a)</td><td>0.02 (n/a)</td><td>2256.91 (n/a)</td><td>2213.15 (n/a)</td><td>2228.31 (n/a)</td><td>2159.48 (n/a)</td><td>38.67 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.39 (-1.48%)</td><td>0.39 (-1.25%)</td><td>0.39 (-2.05%)</td><td>0.38 (-0.21%)</td><td>0.01 <b>(-26.32%)</b></td><td>1384.26 (+0.20%)</td><td>1356.09 (+1.25%)</td><td>1355.73 (+2.09%)</td><td>1338.93 (+1.51%)</td><td>18.40 <b>(-25.78%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.01 (n/a)</td><td>1381.55 (n/a)</td><td>1339.37 (n/a)</td><td>1327.98 (n/a)</td><td>1319.01 (n/a)</td><td>24.78 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.26 (+2.79%)</td><td>0.24 (-1.64%)</td><td>0.24 (-2.41%)</td><td>0.23 (-6.42%)</td><td>0.01 <b>(+349.85%)</b></td><td>2291.89 (+6.89%)</td><td>2148.86 (+1.83%)</td><td>2160.82 (+2.47%)</td><td>2035.86 (-2.72%)</td><td>98.40 <b>(+370.49%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.00 (n/a)</td><td>2144.14 (n/a)</td><td>2110.26 (n/a)</td><td>2108.65 (n/a)</td><td>2092.80 (n/a)</td><td>20.91 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.37 (+0.21%)</td><td>0.37 (+0.99%)</td><td>0.37 (+2.19%)</td><td>0.36 (+0.79%)</td><td>0.01 (-6.68%)</td><td>1465.70 (-0.77%)</td><td>1427.91 (-0.98%)</td><td>1421.70 (-2.13%)</td><td>1404.03 (-0.22%)</td><td>26.67 (-7.40%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.35 (n/a)</td><td>0.01 (n/a)</td><td>1477.08 (n/a)</td><td>1442.05 (n/a)</td><td>1452.58 (n/a)</td><td>1407.08 (n/a)</td><td>28.80 (n/a)</td>
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


### test_transpose[M_2048-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>6.69 <b>(+28.28%)</b></td><td>4.80 (+5.02%)</td><td>4.38 (-1.03%)</td><td>3.93 (-2.03%)</td><td>1.09 <b>(+113.46%)</b></td><td>266.60 (+2.07%)</td><td>226.10 (-2.50%)</td><td>239.40 (+1.06%)</td><td>156.60 <b>(-22.09%)</b></td><td>41.46 <b>(+63.21%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>5.22 (n/a)</td><td>4.57 (n/a)</td><td>4.43 (n/a)</td><td>4.02 (n/a)</td><td>0.51 (n/a)</td><td>261.20 (n/a)</td><td>231.90 (n/a)</td><td>236.90 (n/a)</td><td>201.00 (n/a)</td><td>25.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>6.07 (-3.32%)</td><td>5.04 (-2.53%)</td><td>4.57 (-8.79%)</td><td>4.45 (+13.74%)</td><td>0.75 <b>(-29.32%)</b></td><td>235.70 (-12.09%)</td><td>211.54 (+0.78%)</td><td>229.30 (+9.66%)</td><td>172.70 (+3.41%)</td><td>29.42 <b>(-32.69%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>6.28 (n/a)</td><td>5.17 (n/a)</td><td>5.01 (n/a)</td><td>3.91 (n/a)</td><td>1.06 (n/a)</td><td>268.10 (n/a)</td><td>209.90 (n/a)</td><td>209.10 (n/a)</td><td>167.00 (n/a)</td><td>43.70 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>5.88 (+13.91%)</td><td>5.05 (+10.91%)</td><td>5.21 (+14.65%)</td><td>4.03 (+1.59%)</td><td>0.75 <b>(+50.01%)</b></td><td>260.40 (-1.55%)</td><td>211.56 (-9.01%)</td><td>201.40 (-12.78%)</td><td>178.30 (-12.21%)</td><td>33.46 <b>(+29.96%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>5.16 (n/a)</td><td>4.55 (n/a)</td><td>4.54 (n/a)</td><td>3.96 (n/a)</td><td>0.50 (n/a)</td><td>264.50 (n/a)</td><td>232.50 (n/a)</td><td>230.90 (n/a)</td><td>203.10 (n/a)</td><td>25.75 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_1-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>5.90 (-8.30%)</td><td>5.29 (-9.69%)</td><td>5.33 (-9.44%)</td><td>4.32 (-17.92%)</td><td>0.63 <b>(+48.72%)</b></td><td>242.80 <b>(+21.89%)</b></td><td>200.84 (+11.65%)</td><td>196.70 (+10.44%)</td><td>177.70 (+9.09%)</td><td>25.91 <b>(+98.13%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>6.44 (n/a)</td><td>5.85 (n/a)</td><td>5.89 (n/a)</td><td>5.26 (n/a)</td><td>0.42 (n/a)</td><td>199.20 (n/a)</td><td>179.88 (n/a)</td><td>178.10 (n/a)</td><td>162.90 (n/a)</td><td>13.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>6.64 (+14.91%)</td><td>4.55 (-7.06%)</td><td>4.18 (-17.58%)</td><td>3.61 (-8.95%)</td><td>1.19 <b>(+72.24%)</b></td><td>290.50 (+9.83%)</td><td>240.44 (+10.50%)</td><td>251.00 <b>(+21.31%)</b></td><td>158.00 (-13.00%)</td><td>49.31 <b>(+54.19%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>5.77 (n/a)</td><td>4.90 (n/a)</td><td>5.07 (n/a)</td><td>3.96 (n/a)</td><td>0.69 (n/a)</td><td>264.50 (n/a)</td><td>217.60 (n/a)</td><td>206.90 (n/a)</td><td>181.60 (n/a)</td><td>31.98 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>5.74 (-0.12%)</td><td>4.61 (-7.02%)</td><td>4.54 (-11.57%)</td><td>3.96 (+14.09%)</td><td>0.71 <b>(-20.62%)</b></td><td>264.80 (-12.35%)</td><td>231.30 (+5.98%)</td><td>230.90 (+13.13%)</td><td>182.80 (+0.11%)</td><td>32.62 <b>(-32.48%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>5.74 (n/a)</td><td>4.96 (n/a)</td><td>5.14 (n/a)</td><td>3.47 (n/a)</td><td>0.89 (n/a)</td><td>302.10 (n/a)</td><td>218.24 (n/a)</td><td>204.10 (n/a)</td><td>182.60 (n/a)</td><td>48.31 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>5.77 (-8.83%)</td><td>4.85 (-8.04%)</td><td>4.74 (-6.10%)</td><td>3.87 (-14.00%)</td><td>0.74 (+7.95%)</td><td>270.90 (+16.32%)</td><td>220.56 (+9.45%)</td><td>221.40 (+6.49%)</td><td>181.60 (+9.66%)</td><td>34.57 <b>(+39.42%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>6.33 (n/a)</td><td>5.27 (n/a)</td><td>5.04 (n/a)</td><td>4.50 (n/a)</td><td>0.68 (n/a)</td><td>232.90 (n/a)</td><td>201.52 (n/a)</td><td>207.90 (n/a)</td><td>165.60 (n/a)</td><td>24.79 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_2-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>5.46 (-11.94%)</td><td>4.86 (-6.49%)</td><td>5.12 (-1.20%)</td><td>3.86 (-5.40%)</td><td>0.62 (-18.01%)</td><td>271.90 (+5.67%)</td><td>219.16 (+6.57%)</td><td>204.90 (+1.24%)</td><td>192.00 (+13.54%)</td><td>31.52 (-1.78%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>6.20 (n/a)</td><td>5.19 (n/a)</td><td>5.18 (n/a)</td><td>4.08 (n/a)</td><td>0.76 (n/a)</td><td>257.30 (n/a)</td><td>205.64 (n/a)</td><td>202.40 (n/a)</td><td>169.10 (n/a)</td><td>32.09 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>9.77 (+8.61%)</td><td>7.67 (-4.06%)</td><td>7.38 (-7.03%)</td><td>5.97 (-16.31%)</td><td>1.38 <b>(+104.77%)</b></td><td>351.00 (+19.47%)</td><td>280.28 (+6.30%)</td><td>284.10 (+7.57%)</td><td>214.70 (-7.93%)</td><td>49.26 <b>(+124.23%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>8.99 (n/a)</td><td>8.00 (n/a)</td><td>7.94 (n/a)</td><td>7.14 (n/a)</td><td>0.67 (n/a)</td><td>293.80 (n/a)</td><td>263.68 (n/a)</td><td>264.10 (n/a)</td><td>233.20 (n/a)</td><td>21.97 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>9.30 (+1.85%)</td><td>7.79 (-9.28%)</td><td>7.97 (-7.36%)</td><td>6.48 <b>(-21.46%)</b></td><td>1.12 <b>(+212.94%)</b></td><td>323.40 <b>(+27.32%)</b></td><td>273.58 (+11.90%)</td><td>263.30 (+7.95%)</td><td>225.40 (-1.83%)</td><td>39.14 <b>(+294.42%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>9.14 (n/a)</td><td>8.59 (n/a)</td><td>8.60 (n/a)</td><td>8.26 (n/a)</td><td>0.36 (n/a)</td><td>254.00 (n/a)</td><td>244.48 (n/a)</td><td>243.90 (n/a)</td><td>229.60 (n/a)</td><td>9.92 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>9.73 (+9.86%)</td><td>7.62 (-5.88%)</td><td>7.28 (-12.35%)</td><td>6.79 (-3.19%)</td><td>1.22 <b>(+68.46%)</b></td><td>309.00 (+3.28%)</td><td>279.94 (+7.39%)</td><td>288.00 (+14.10%)</td><td>215.40 (-9.00%)</td><td>38.17 <b>(+55.25%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>8.86 (n/a)</td><td>8.10 (n/a)</td><td>8.31 (n/a)</td><td>7.01 (n/a)</td><td>0.72 (n/a)</td><td>299.20 (n/a)</td><td>260.68 (n/a)</td><td>252.40 (n/a)</td><td>236.70 (n/a)</td><td>24.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_1-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>7.96 (-14.23%)</td><td>7.45 (-7.69%)</td><td>7.63 (-3.08%)</td><td>6.68 (-7.17%)</td><td>0.49 <b>(-39.44%)</b></td><td>313.90 (+7.72%)</td><td>282.30 (+7.89%)</td><td>274.80 (+3.15%)</td><td>263.60 (+16.59%)</td><td>19.35 <b>(-22.66%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>9.28 (n/a)</td><td>8.08 (n/a)</td><td>7.87 (n/a)</td><td>7.20 (n/a)</td><td>0.80 (n/a)</td><td>291.40 (n/a)</td><td>261.66 (n/a)</td><td>266.40 (n/a)</td><td>226.10 (n/a)</td><td>25.02 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>9.18 (+2.38%)</td><td>7.31 (-4.76%)</td><td>7.16 (-0.34%)</td><td>6.04 (-13.46%)</td><td>1.20 <b>(+39.78%)</b></td><td>347.30 (+15.57%)</td><td>292.92 (+6.15%)</td><td>292.80 (+0.34%)</td><td>228.50 (-2.31%)</td><td>45.12 <b>(+55.31%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>8.96 (n/a)</td><td>7.67 (n/a)</td><td>7.19 (n/a)</td><td>6.98 (n/a)</td><td>0.86 (n/a)</td><td>300.50 (n/a)</td><td>275.96 (n/a)</td><td>291.80 (n/a)</td><td>233.90 (n/a)</td><td>29.05 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>9.32 (+4.81%)</td><td>7.98 (-5.16%)</td><td>7.86 (-6.29%)</td><td>6.85 (-14.35%)</td><td>0.92 <b>(+134.01%)</b></td><td>306.10 (+16.74%)</td><td>265.38 (+6.35%)</td><td>266.90 (+6.72%)</td><td>225.00 (-4.62%)</td><td>30.03 <b>(+159.23%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>8.89 (n/a)</td><td>8.42 (n/a)</td><td>8.39 (n/a)</td><td>8.00 (n/a)</td><td>0.39 (n/a)</td><td>262.20 (n/a)</td><td>249.54 (n/a)</td><td>250.10 (n/a)</td><td>235.90 (n/a)</td><td>11.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>9.35 (-8.97%)</td><td>7.80 (-13.71%)</td><td>8.26 (-8.89%)</td><td>5.38 <b>(-28.27%)</b></td><td>1.48 <b>(+44.94%)</b></td><td>389.90 <b>(+39.45%)</b></td><td>278.58 (+18.79%)</td><td>253.90 (+9.72%)</td><td>224.20 (+9.85%)</td><td>64.71 <b>(+128.87%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>10.27 (n/a)</td><td>9.04 (n/a)</td><td>9.06 (n/a)</td><td>7.50 (n/a)</td><td>1.02 (n/a)</td><td>279.60 (n/a)</td><td>234.52 (n/a)</td><td>231.40 (n/a)</td><td>204.10 (n/a)</td><td>28.27 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_2-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>8.58 (-10.71%)</td><td>7.74 (-6.57%)</td><td>7.96 (-3.41%)</td><td>7.02 (+0.70%)</td><td>0.68 <b>(-29.18%)</b></td><td>298.80 (-0.70%)</td><td>272.60 (+6.53%)</td><td>263.40 (+3.50%)</td><td>244.40 (+11.96%)</td><td>24.05 <b>(-20.06%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>9.61 (n/a)</td><td>8.28 (n/a)</td><td>8.24 (n/a)</td><td>6.97 (n/a)</td><td>0.96 (n/a)</td><td>300.90 (n/a)</td><td>255.90 (n/a)</td><td>254.50 (n/a)</td><td>218.30 (n/a)</td><td>30.09 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>10.40 (-4.71%)</td><td>8.44 (-10.97%)</td><td>8.10 (-16.53%)</td><td>7.40 (-7.89%)</td><td>1.23 (+6.16%)</td><td>283.30 (+8.54%)</td><td>252.46 (+12.70%)</td><td>258.80 (+19.76%)</td><td>201.70 (+4.94%)</td><td>33.84 <b>(+20.66%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>10.91 (n/a)</td><td>9.48 (n/a)</td><td>9.71 (n/a)</td><td>8.04 (n/a)</td><td>1.16 (n/a)</td><td>261.00 (n/a)</td><td>224.02 (n/a)</td><td>216.10 (n/a)</td><td>192.20 (n/a)</td><td>28.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_4-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>9.12 (-7.72%)</td><td>7.78 (-14.12%)</td><td>8.18 (-8.20%)</td><td>5.47 <b>(-36.73%)</b></td><td>1.37 <b>(+184.57%)</b></td><td>383.20 <b>(+58.02%)</b></td><td>278.10 (+19.85%)</td><td>256.50 (+8.96%)</td><td>230.00 (+8.39%)</td><td>60.38 <b>(+413.87%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>9.88 (n/a)</td><td>9.06 (n/a)</td><td>8.91 (n/a)</td><td>8.65 (n/a)</td><td>0.48 (n/a)</td><td>242.50 (n/a)</td><td>232.04 (n/a)</td><td>235.40 (n/a)</td><td>212.20 (n/a)</td><td>11.75 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>10.02 (-16.67%)</td><td>8.15 (-19.31%)</td><td>8.45 (-15.35%)</td><td>5.98 <b>(-32.58%)</b></td><td>1.50 (+19.17%)</td><td>350.50 <b>(+48.33%)</b></td><td>265.20 <b>(+26.18%)</b></td><td>248.30 (+18.13%)</td><td>209.40 <b>(+20.00%)</b></td><td>53.67 <b>(+115.90%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>12.02 (n/a)</td><td>10.10 (n/a)</td><td>9.98 (n/a)</td><td>8.87 (n/a)</td><td>1.26 (n/a)</td><td>236.30 (n/a)</td><td>210.18 (n/a)</td><td>210.20 (n/a)</td><td>174.50 (n/a)</td><td>24.86 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_4-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>8.39 (-14.41%)</td><td>7.08 <b>(-20.79%)</b></td><td>7.49 (-17.64%)</td><td>5.61 <b>(-31.28%)</b></td><td>1.27 <b>(+93.89%)</b></td><td>373.50 <b>(+45.50%)</b></td><td>304.60 <b>(+29.18%)</b></td><td>280.10 <b>(+21.41%)</b></td><td>250.10 (+16.87%)</td><td>57.28 <b>(+231.55%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>9.80 (n/a)</td><td>8.93 (n/a)</td><td>9.09 (n/a)</td><td>8.17 (n/a)</td><td>0.65 (n/a)</td><td>256.70 (n/a)</td><td>235.80 (n/a)</td><td>230.70 (n/a)</td><td>214.00 (n/a)</td><td>17.27 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>12.48 (-5.11%)</td><td>11.60 (-0.75%)</td><td>11.65 (-0.63%)</td><td>10.38 (-0.96%)</td><td>0.84 <b>(-21.79%)</b></td><td>404.20 (+0.97%)</td><td>363.08 (+0.53%)</td><td>360.10 (+0.64%)</td><td>336.00 (+5.40%)</td><td>27.26 (-17.22%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>13.16 (n/a)</td><td>11.69 (n/a)</td><td>11.72 (n/a)</td><td>10.48 (n/a)</td><td>1.08 (n/a)</td><td>400.30 (n/a)</td><td>361.18 (n/a)</td><td>357.80 (n/a)</td><td>318.80 (n/a)</td><td>32.93 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>12.79 (+4.79%)</td><td>10.71 (-4.69%)</td><td>10.59 (-5.22%)</td><td>8.04 <b>(-21.86%)</b></td><td>1.77 <b>(+114.98%)</b></td><td>521.90 <b>(+27.98%)</b></td><td>401.16 (+7.05%)</td><td>396.00 (+5.52%)</td><td>328.10 (-4.57%)</td><td>73.89 <b>(+168.83%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>12.20 (n/a)</td><td>11.24 (n/a)</td><td>11.18 (n/a)</td><td>10.28 (n/a)</td><td>0.83 (n/a)</td><td>407.80 (n/a)</td><td>374.74 (n/a)</td><td>375.30 (n/a)</td><td>343.80 (n/a)</td><td>27.49 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>12.41 (+1.21%)</td><td>11.97 (+1.06%)</td><td>11.94 (-1.61%)</td><td>11.42 (+1.69%)</td><td>0.39 <b>(-22.48%)</b></td><td>367.30 (-1.66%)</td><td>350.64 (-1.12%)</td><td>351.20 (+1.65%)</td><td>338.10 (-1.20%)</td><td>11.52 <b>(-24.68%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>12.26 (n/a)</td><td>11.85 (n/a)</td><td>12.14 (n/a)</td><td>11.23 (n/a)</td><td>0.50 (n/a)</td><td>373.50 (n/a)</td><td>354.60 (n/a)</td><td>345.50 (n/a)</td><td>342.20 (n/a)</td><td>15.29 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_1-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>12.22 (-7.10%)</td><td>11.22 (-5.79%)</td><td>11.11 (-10.84%)</td><td>10.08 (-0.84%)</td><td>0.82 <b>(-31.08%)</b></td><td>416.30 (+0.85%)</td><td>375.54 (+5.70%)</td><td>377.40 (+12.15%)</td><td>343.30 (+7.65%)</td><td>28.08 <b>(-25.64%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>13.15 (n/a)</td><td>11.91 (n/a)</td><td>12.47 (n/a)</td><td>10.16 (n/a)</td><td>1.20 (n/a)</td><td>412.80 (n/a)</td><td>355.28 (n/a)</td><td>336.50 (n/a)</td><td>318.90 (n/a)</td><td>37.76 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>12.78 (+2.19%)</td><td>12.21 (+3.92%)</td><td>12.35 (+2.64%)</td><td>11.01 (+6.62%)</td><td>0.72 (-13.93%)</td><td>381.10 (-6.20%)</td><td>344.60 (-3.91%)</td><td>339.60 (-2.55%)</td><td>328.30 (-2.15%)</td><td>21.60 <b>(-21.93%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>12.50 (n/a)</td><td>11.75 (n/a)</td><td>12.03 (n/a)</td><td>10.32 (n/a)</td><td>0.84 (n/a)</td><td>406.30 (n/a)</td><td>358.62 (n/a)</td><td>348.50 (n/a)</td><td>335.50 (n/a)</td><td>27.67 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>12.69 (+1.23%)</td><td>10.74 (-9.37%)</td><td>11.05 (-5.08%)</td><td>8.04 <b>(-29.12%)</b></td><td>1.68 <b>(+237.04%)</b></td><td>521.70 <b>(+41.08%)</b></td><td>399.42 (+12.70%)</td><td>379.40 (+5.33%)</td><td>330.50 (-1.23%)</td><td>71.97 <b>(+389.21%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>12.54 (n/a)</td><td>11.85 (n/a)</td><td>11.65 (n/a)</td><td>11.34 (n/a)</td><td>0.50 (n/a)</td><td>369.80 (n/a)</td><td>354.42 (n/a)</td><td>360.20 (n/a)</td><td>334.60 (n/a)</td><td>14.71 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>14.42 (-2.72%)</td><td>13.63 (+9.84%)</td><td>13.99 (+13.23%)</td><td>12.69 <b>(+30.05%)</b></td><td>0.75 <b>(-58.56%)</b></td><td>330.50 <b>(-23.12%)</b></td><td>308.48 (-10.38%)</td><td>299.70 (-11.70%)</td><td>290.80 (+2.79%)</td><td>17.26 <b>(-67.75%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>14.83 (n/a)</td><td>12.41 (n/a)</td><td>12.36 (n/a)</td><td>9.76 (n/a)</td><td>1.81 (n/a)</td><td>429.90 (n/a)</td><td>344.20 (n/a)</td><td>339.40 (n/a)</td><td>282.90 (n/a)</td><td>53.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_2-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>15.14 (-1.28%)</td><td>12.97 (-3.81%)</td><td>12.38 (-4.30%)</td><td>12.00 (+1.39%)</td><td>1.32 (-15.31%)</td><td>349.60 (-1.38%)</td><td>325.76 (+3.66%)</td><td>338.70 (+4.50%)</td><td>277.00 (+1.32%)</td><td>30.47 (-14.32%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>15.34 (n/a)</td><td>13.49 (n/a)</td><td>12.94 (n/a)</td><td>11.83 (n/a)</td><td>1.56 (n/a)</td><td>354.50 (n/a)</td><td>314.26 (n/a)</td><td>324.10 (n/a)</td><td>273.40 (n/a)</td><td>35.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>14.94 (-2.03%)</td><td>12.99 (-2.05%)</td><td>12.49 (-5.77%)</td><td>11.39 (+0.24%)</td><td>1.53 (+10.52%)</td><td>368.30 (-0.22%)</td><td>326.36 (+2.31%)</td><td>335.80 (+6.13%)</td><td>280.80 (+2.07%)</td><td>37.55 (+11.56%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>15.25 (n/a)</td><td>13.27 (n/a)</td><td>13.25 (n/a)</td><td>11.36 (n/a)</td><td>1.39 (n/a)</td><td>369.10 (n/a)</td><td>318.98 (n/a)</td><td>316.40 (n/a)</td><td>275.10 (n/a)</td><td>33.66 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_4-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>14.09 (-5.90%)</td><td>12.36 (-7.75%)</td><td>12.58 (-6.85%)</td><td>10.90 (-11.37%)</td><td>1.20 (+4.75%)</td><td>384.90 (+12.81%)</td><td>341.76 (+8.56%)</td><td>333.40 (+7.34%)</td><td>297.60 (+6.25%)</td><td>32.68 <b>(+23.49%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>14.98 (n/a)</td><td>13.40 (n/a)</td><td>13.50 (n/a)</td><td>12.29 (n/a)</td><td>1.14 (n/a)</td><td>341.20 (n/a)</td><td>314.80 (n/a)</td><td>310.60 (n/a)</td><td>280.10 (n/a)</td><td>26.46 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>13.06 (-8.60%)</td><td>12.61 (-3.57%)</td><td>12.76 (-1.70%)</td><td>11.73 (-0.59%)</td><td>0.54 <b>(-43.74%)</b></td><td>357.70 (+0.62%)</td><td>333.22 (+3.42%)</td><td>328.80 (+1.73%)</td><td>321.30 (+9.43%)</td><td>14.75 <b>(-37.82%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>14.28 (n/a)</td><td>13.07 (n/a)</td><td>12.98 (n/a)</td><td>11.80 (n/a)</td><td>0.95 (n/a)</td><td>355.50 (n/a)</td><td>322.20 (n/a)</td><td>323.20 (n/a)</td><td>293.60 (n/a)</td><td>23.71 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_4-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>15.26 (+5.74%)</td><td>12.48 (-0.64%)</td><td>12.66 (-2.21%)</td><td>9.12 (-14.69%)</td><td>2.19 <b>(+40.34%)</b></td><td>459.80 (+17.24%)</td><td>345.66 (+2.18%)</td><td>331.40 (+2.25%)</td><td>274.90 (-5.44%)</td><td>68.46 <b>(+59.58%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>14.43 (n/a)</td><td>12.56 (n/a)</td><td>12.94 (n/a)</td><td>10.69 (n/a)</td><td>1.56 (n/a)</td><td>392.20 (n/a)</td><td>338.28 (n/a)</td><td>324.10 (n/a)</td><td>290.70 (n/a)</td><td>42.90 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>13.79 (-8.54%)</td><td>13.28 (-2.28%)</td><td>13.45 (-2.83%)</td><td>12.64 (+6.57%)</td><td>0.46 <b>(-69.44%)</b></td><td>331.70 (-6.17%)</td><td>316.16 (+1.41%)</td><td>311.70 (+2.91%)</td><td>304.10 (+9.35%)</td><td>11.04 <b>(-68.51%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>15.08 (n/a)</td><td>13.59 (n/a)</td><td>13.85 (n/a)</td><td>11.86 (n/a)</td><td>1.50 (n/a)</td><td>353.50 (n/a)</td><td>311.76 (n/a)</td><td>302.90 (n/a)</td><td>278.10 (n/a)</td><td>35.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_8-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>14.75 (+5.58%)</td><td>13.18 (-1.29%)</td><td>13.02 (-2.55%)</td><td>10.68 (-16.09%)</td><td>1.64 <b>(+245.21%)</b></td><td>392.80 (+19.17%)</td><td>322.62 (+2.58%)</td><td>322.20 (+2.61%)</td><td>284.40 (-5.26%)</td><td>43.64 <b>(+287.99%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>13.97 (n/a)</td><td>13.35 (n/a)</td><td>13.36 (n/a)</td><td>12.73 (n/a)</td><td>0.48 (n/a)</td><td>329.60 (n/a)</td><td>314.50 (n/a)</td><td>314.00 (n/a)</td><td>300.20 (n/a)</td><td>11.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>13.85 (-8.79%)</td><td>12.71 (-7.22%)</td><td>12.49 (-9.96%)</td><td>12.20 (+5.09%)</td><td>0.66 <b>(-50.37%)</b></td><td>343.80 (-4.84%)</td><td>330.58 (+7.14%)</td><td>335.70 (+11.05%)</td><td>302.80 (+9.63%)</td><td>16.11 <b>(-49.64%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>15.19 (n/a)</td><td>13.70 (n/a)</td><td>13.87 (n/a)</td><td>11.61 (n/a)</td><td>1.32 (n/a)</td><td>361.30 (n/a)</td><td>308.56 (n/a)</td><td>302.30 (n/a)</td><td>276.20 (n/a)</td><td>31.99 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_8-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>17.73 (-7.59%)</td><td>12.82 (-9.96%)</td><td>12.67 (-8.75%)</td><td>9.51 (+2.33%)</td><td>3.37 (-11.44%)</td><td>440.80 (-2.28%)</td><td>345.08 (+10.11%)</td><td>330.90 (+9.57%)</td><td>236.50 (+8.19%)</td><td>86.11 (-4.25%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>19.19 (n/a)</td><td>14.23 (n/a)</td><td>13.89 (n/a)</td><td>9.30 (n/a)</td><td>3.81 (n/a)</td><td>451.10 (n/a)</td><td>313.40 (n/a)</td><td>302.00 (n/a)</td><td>218.60 (n/a)</td><td>89.93 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>3.86 (+16.42%)</td><td>2.95 (-4.52%)</td><td>2.72 (-15.92%)</td><td>2.49 (-8.97%)</td><td>0.56 <b>(+115.56%)</b></td><td>210.50 (+9.86%)</td><td>182.12 (+6.79%)</td><td>192.70 (+18.95%)</td><td>135.80 (-14.10%)</td><td>30.25 <b>(+103.10%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>3.32 (n/a)</td><td>3.09 (n/a)</td><td>3.24 (n/a)</td><td>2.74 (n/a)</td><td>0.26 (n/a)</td><td>191.60 (n/a)</td><td>170.54 (n/a)</td><td>162.00 (n/a)</td><td>158.10 (n/a)</td><td>14.90 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>5.99 (-3.58%)</td><td>4.95 (-5.42%)</td><td>4.85 (-6.90%)</td><td>4.31 (+9.31%)</td><td>0.66 <b>(-26.92%)</b></td><td>243.20 (-8.54%)</td><td>214.70 (+4.40%)</td><td>216.40 (+7.45%)</td><td>175.00 (+3.67%)</td><td>26.53 <b>(-31.08%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>6.21 (n/a)</td><td>5.23 (n/a)</td><td>5.21 (n/a)</td><td>3.94 (n/a)</td><td>0.90 (n/a)</td><td>265.90 (n/a)</td><td>205.66 (n/a)</td><td>201.40 (n/a)</td><td>168.80 (n/a)</td><td>38.49 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_4]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>8.62 (-5.17%)</td><td>7.76 (-5.59%)</td><td>8.05 (+1.49%)</td><td>6.95 (-8.64%)</td><td>0.76 (+7.29%)</td><td>301.80 (+9.47%)</td><td>272.38 (+6.15%)</td><td>260.50 (-1.44%)</td><td>243.30 (+5.46%)</td><td>27.05 <b>(+25.98%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>9.09 (n/a)</td><td>8.22 (n/a)</td><td>7.93 (n/a)</td><td>7.61 (n/a)</td><td>0.70 (n/a)</td><td>275.70 (n/a)</td><td>256.60 (n/a)</td><td>264.30 (n/a)</td><td>230.70 (n/a)</td><td>21.47 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>3.42 (+7.36%)</td><td>2.69 (-1.00%)</td><td>2.67 (-10.43%)</td><td>2.19 <b>(+46.58%)</b></td><td>0.45 <b>(-34.58%)</b></td><td>239.90 <b>(-31.79%)</b></td><td>199.02 (-4.85%)</td><td>196.70 (+11.63%)</td><td>153.50 (-6.86%)</td><td>31.19 <b>(-60.94%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>3.18 (n/a)</td><td>2.72 (n/a)</td><td>2.98 (n/a)</td><td>1.49 (n/a)</td><td>0.69 (n/a)</td><td>351.70 (n/a)</td><td>209.16 (n/a)</td><td>176.20 (n/a)</td><td>164.80 (n/a)</td><td>79.85 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>3.30 (-5.11%)</td><td>2.69 (-7.96%)</td><td>2.65 (-6.58%)</td><td>2.16 (-15.63%)</td><td>0.47 <b>(+23.64%)</b></td><td>243.20 (+18.52%)</td><td>199.48 (+9.92%)</td><td>197.60 (+7.04%)</td><td>158.90 (+5.37%)</td><td>34.92 <b>(+53.68%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>3.48 (n/a)</td><td>2.93 (n/a)</td><td>2.84 (n/a)</td><td>2.55 (n/a)</td><td>0.38 (n/a)</td><td>205.20 (n/a)</td><td>181.48 (n/a)</td><td>184.60 (n/a)</td><td>150.80 (n/a)</td><td>22.72 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>3.35 (+11.05%)</td><td>2.64 (-8.02%)</td><td>2.64 (-12.30%)</td><td>2.18 (-9.18%)</td><td>0.45 <b>(+68.04%)</b></td><td>240.20 (+10.13%)</td><td>202.52 (+10.20%)</td><td>198.70 (+14.06%)</td><td>156.50 (-9.95%)</td><td>31.72 <b>(+64.35%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>3.02 (n/a)</td><td>2.87 (n/a)</td><td>3.01 (n/a)</td><td>2.40 (n/a)</td><td>0.27 (n/a)</td><td>218.10 (n/a)</td><td>183.78 (n/a)</td><td>174.20 (n/a)</td><td>173.80 (n/a)</td><td>19.30 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.23 (-17.96%)</td><td>0.19 (-13.26%)</td><td>0.20 (-13.33%)</td><td>0.17 (+5.11%)</td><td>0.03 <b>(-42.77%)</b></td><td>196.60 (-4.89%)</td><td>172.50 (+12.72%)</td><td>167.50 (+15.36%)</td><td>142.50 <b>(+21.90%)</b></td><td>22.81 <b>(-33.45%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>206.70 (n/a)</td><td>153.04 (n/a)</td><td>145.20 (n/a)</td><td>116.90 (n/a)</td><td>34.27 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_128-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.30 (-2.71%)</td><td>0.22 (-4.17%)</td><td>0.21 (-2.48%)</td><td>0.13 (-19.03%)</td><td>0.07 (+16.95%)</td><td>252.00 <b>(+23.47%)</b></td><td>166.80 (+8.26%)</td><td>153.70 (+2.60%)</td><td>108.40 (+2.75%)</td><td>57.68 <b>(+48.01%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>204.10 (n/a)</td><td>154.08 (n/a)</td><td>149.80 (n/a)</td><td>105.50 (n/a)</td><td>38.97 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.22 (-16.07%)</td><td>0.20 (-10.33%)</td><td>0.20 <b>(-20.51%)</b></td><td>0.18 (+15.68%)</td><td>0.02 <b>(-59.94%)</b></td><td>184.30 (-13.56%)</td><td>163.62 (+7.69%)</td><td>164.40 <b>(+25.78%)</b></td><td>147.90 (+19.18%)</td><td>15.44 <b>(-59.05%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.25 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>213.20 (n/a)</td><td>151.94 (n/a)</td><td>130.70 (n/a)</td><td>124.10 (n/a)</td><td>37.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_128-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.30 (+10.75%)</td><td>0.24 (+16.62%)</td><td>0.25 <b>(+23.01%)</b></td><td>0.17 (+5.41%)</td><td>0.05 <b>(+22.12%)</b></td><td>197.30 (-5.14%)</td><td>142.28 (-13.43%)</td><td>128.60 (-18.71%)</td><td>110.80 (-9.70%)</td><td>34.24 (+6.74%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>208.00 (n/a)</td><td>164.36 (n/a)</td><td>158.20 (n/a)</td><td>122.70 (n/a)</td><td>32.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.53 <b>(+22.73%)</b></td><td>0.39 (+3.47%)</td><td>0.38 (+1.68%)</td><td>0.28 (-13.71%)</td><td>0.10 <b>(+101.16%)</b></td><td>235.40 (+15.90%)</td><td>176.24 (+0.26%)</td><td>170.40 (-1.62%)</td><td>124.80 (-18.54%)</td><td>43.92 <b>(+92.55%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.43 (n/a)</td><td>0.38 (n/a)</td><td>0.38 (n/a)</td><td>0.32 (n/a)</td><td>0.05 (n/a)</td><td>203.10 (n/a)</td><td>175.78 (n/a)</td><td>173.20 (n/a)</td><td>153.20 (n/a)</td><td>22.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.57 (+7.51%)</td><td>0.41 (-6.98%)</td><td>0.38 (-15.71%)</td><td>0.35 (+10.51%)</td><td>0.09 (+10.99%)</td><td>187.30 (-9.52%)</td><td>165.30 (+7.53%)</td><td>172.10 (+18.61%)</td><td>115.70 (-6.99%)</td><td>29.42 (-9.54%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.53 (n/a)</td><td>0.44 (n/a)</td><td>0.45 (n/a)</td><td>0.32 (n/a)</td><td>0.08 (n/a)</td><td>207.00 (n/a)</td><td>153.72 (n/a)</td><td>145.10 (n/a)</td><td>124.40 (n/a)</td><td>32.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.50 (-2.26%)</td><td>0.37 (-9.64%)</td><td>0.35 (-10.11%)</td><td>0.30 (-16.88%)</td><td>0.08 <b>(+26.06%)</b></td><td>215.70 <b>(+20.37%)</b></td><td>183.26 (+12.20%)</td><td>189.90 (+11.25%)</td><td>130.40 (+2.27%)</td><td>31.63 <b>(+50.65%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.51 (n/a)</td><td>0.41 (n/a)</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.06 (n/a)</td><td>179.20 (n/a)</td><td>163.34 (n/a)</td><td>170.70 (n/a)</td><td>127.50 (n/a)</td><td>21.00 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.57 (+14.09%)</td><td>0.41 (+4.91%)</td><td>0.40 (+8.52%)</td><td>0.34 <b>(+22.63%)</b></td><td>0.09 (+0.96%)</td><td>191.20 (-18.43%)</td><td>164.24 (-5.77%)</td><td>165.90 (-7.83%)</td><td>115.60 (-12.36%)</td><td>29.39 <b>(-28.33%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.50 (n/a)</td><td>0.39 (n/a)</td><td>0.36 (n/a)</td><td>0.28 (n/a)</td><td>0.09 (n/a)</td><td>234.40 (n/a)</td><td>174.30 (n/a)</td><td>180.00 (n/a)</td><td>131.90 (n/a)</td><td>41.01 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.41 <b>(-21.18%)</b></td><td>0.36 (-15.95%)</td><td>0.35 (-16.98%)</td><td>0.30 (-3.00%)</td><td>0.04 <b>(-50.93%)</b></td><td>218.30 (+3.07%)</td><td>185.44 (+16.06%)</td><td>187.60 <b>(+20.41%)</b></td><td>160.50 <b>(+26.88%)</b></td><td>22.89 <b>(-34.95%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.52 (n/a)</td><td>0.43 (n/a)</td><td>0.42 (n/a)</td><td>0.31 (n/a)</td><td>0.09 (n/a)</td><td>211.80 (n/a)</td><td>159.78 (n/a)</td><td>155.80 (n/a)</td><td>126.50 (n/a)</td><td>35.18 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_4-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.44 (-8.43%)</td><td>0.35 (-17.74%)</td><td>0.36 (-14.25%)</td><td>0.28 <b>(-25.93%)</b></td><td>0.06 <b>(+56.54%)</b></td><td>233.40 <b>(+34.99%)</b></td><td>189.10 <b>(+23.55%)</b></td><td>180.30 (+16.62%)</td><td>149.30 (+9.22%)</td><td>31.69 <b>(+131.51%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.48 (n/a)</td><td>0.43 (n/a)</td><td>0.42 (n/a)</td><td>0.38 (n/a)</td><td>0.04 (n/a)</td><td>172.90 (n/a)</td><td>153.06 (n/a)</td><td>154.60 (n/a)</td><td>136.70 (n/a)</td><td>13.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.77 <b>(-24.97%)</b></td><td>0.70 (-18.34%)</td><td>0.72 <b>(-20.32%)</b></td><td>0.60 (+17.87%)</td><td>0.07 <b>(-66.58%)</b></td><td>219.00 (-15.18%)</td><td>188.26 (+15.60%)</td><td>182.40 <b>(+25.45%)</b></td><td>170.30 <b>(+33.26%)</b></td><td>19.77 <b>(-63.52%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>1.03 (n/a)</td><td>0.86 (n/a)</td><td>0.90 (n/a)</td><td>0.51 (n/a)</td><td>0.21 (n/a)</td><td>258.20 (n/a)</td><td>162.86 (n/a)</td><td>145.40 (n/a)</td><td>127.80 (n/a)</td><td>54.20 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>1.12 (+10.46%)</td><td>0.82 (-2.73%)</td><td>0.75 (-11.80%)</td><td>0.51 (-17.11%)</td><td>0.25 <b>(+58.42%)</b></td><td>259.40 <b>(+20.65%)</b></td><td>173.04 (+8.00%)</td><td>174.80 (+13.43%)</td><td>116.70 (-9.46%)</td><td>56.79 <b>(+67.47%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>1.02 (n/a)</td><td>0.84 (n/a)</td><td>0.85 (n/a)</td><td>0.61 (n/a)</td><td>0.16 (n/a)</td><td>215.00 (n/a)</td><td>160.22 (n/a)</td><td>154.10 (n/a)</td><td>128.90 (n/a)</td><td>33.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>1.01 (-0.32%)</td><td>0.77 (-12.17%)</td><td>0.70 <b>(-27.12%)</b></td><td>0.63 (-2.98%)</td><td>0.15 (-11.95%)</td><td>207.30 (+3.03%)</td><td>175.70 (+13.06%)</td><td>186.00 <b>(+37.17%)</b></td><td>129.90 (+0.31%)</td><td>29.26 (-10.05%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>1.01 (n/a)</td><td>0.87 (n/a)</td><td>0.97 (n/a)</td><td>0.65 (n/a)</td><td>0.17 (n/a)</td><td>201.20 (n/a)</td><td>155.40 (n/a)</td><td>135.60 (n/a)</td><td>129.50 (n/a)</td><td>32.53 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>1.08 (+11.42%)</td><td>0.84 (+10.19%)</td><td>0.71 (-5.09%)</td><td>0.68 (+8.35%)</td><td>0.20 <b>(+53.95%)</b></td><td>193.90 (-7.71%)</td><td>162.64 (-7.35%)</td><td>185.40 (+5.34%)</td><td>121.80 (-10.24%)</td><td>35.51 <b>(+27.99%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.97 (n/a)</td><td>0.76 (n/a)</td><td>0.74 (n/a)</td><td>0.62 (n/a)</td><td>0.13 (n/a)</td><td>210.10 (n/a)</td><td>175.54 (n/a)</td><td>176.00 (n/a)</td><td>135.70 (n/a)</td><td>27.74 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.88 (-15.33%)</td><td>0.75 (-17.03%)</td><td>0.74 (-15.65%)</td><td>0.66 (-12.89%)</td><td>0.09 <b>(-28.90%)</b></td><td>199.10 (+14.82%)</td><td>176.78 <b>(+20.01%)</b></td><td>176.60 (+18.60%)</td><td>148.70 (+18.11%)</td><td>19.07 (-3.00%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>1.04 (n/a)</td><td>0.90 (n/a)</td><td>0.88 (n/a)</td><td>0.76 (n/a)</td><td>0.12 (n/a)</td><td>173.40 (n/a)</td><td>147.30 (n/a)</td><td>148.90 (n/a)</td><td>125.90 (n/a)</td><td>19.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_4-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.91 (-7.72%)</td><td>0.75 (-7.56%)</td><td>0.74 (-7.43%)</td><td>0.61 (-12.47%)</td><td>0.15 <b>(+21.75%)</b></td><td>216.40 (+14.26%)</td><td>179.28 (+9.66%)</td><td>177.30 (+8.04%)</td><td>144.10 (+8.35%)</td><td>34.73 <b>(+49.32%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.99 (n/a)</td><td>0.82 (n/a)</td><td>0.80 (n/a)</td><td>0.69 (n/a)</td><td>0.12 (n/a)</td><td>189.40 (n/a)</td><td>163.48 (n/a)</td><td>164.10 (n/a)</td><td>133.00 (n/a)</td><td>23.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.82 <b>(-30.45%)</b></td><td>0.72 (-18.73%)</td><td>0.71 (-16.71%)</td><td>0.64 (-8.30%)</td><td>0.07 <b>(-62.39%)</b></td><td>205.20 (+9.09%)</td><td>183.14 <b>(+20.38%)</b></td><td>185.80 <b>(+20.10%)</b></td><td>159.50 <b>(+43.82%)</b></td><td>16.62 <b>(-39.47%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>1.18 (n/a)</td><td>0.89 (n/a)</td><td>0.85 (n/a)</td><td>0.70 (n/a)</td><td>0.18 (n/a)</td><td>188.10 (n/a)</td><td>152.14 (n/a)</td><td>154.70 (n/a)</td><td>110.90 (n/a)</td><td>27.46 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_8-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.87 <b>(-30.80%)</b></td><td>0.68 <b>(-25.14%)</b></td><td>0.68 <b>(-20.51%)</b></td><td>0.48 <b>(-24.02%)</b></td><td>0.14 <b>(-45.20%)</b></td><td>271.50 <b>(+31.60%)</b></td><td>199.46 <b>(+30.35%)</b></td><td>193.20 <b>(+25.78%)</b></td><td>149.90 <b>(+44.55%)</b></td><td>44.25 (+7.66%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>1.26 (n/a)</td><td>0.91 (n/a)</td><td>0.85 (n/a)</td><td>0.64 (n/a)</td><td>0.25 (n/a)</td><td>206.30 (n/a)</td><td>153.02 (n/a)</td><td>153.60 (n/a)</td><td>103.70 (n/a)</td><td>41.10 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:08:01</td><td>0.12 (-10.17%)</td><td>0.09 (-6.92%)</td><td>0.10 (-6.04%)</td><td>0.05 (+6.11%)</td><td>0.03 (-18.90%)</td><td>327.40 (-5.76%)</td><td>191.22 (+3.09%)</td><td>164.90 (+6.39%)</td><td>132.90 (+11.31%)</td><td>78.50 (-15.43%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>347.40 (n/a)</td><td>185.48 (n/a)</td><td>155.00 (n/a)</td><td>119.40 (n/a)</td><td>92.82 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_64-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.13 (+5.28%)</td><td>0.10 (-6.35%)</td><td>0.10 (-9.66%)</td><td>0.07 (-18.86%)</td><td>0.02 <b>(+61.29%)</b></td><td>226.90 <b>(+23.25%)</b></td><td>174.48 (+9.64%)</td><td>170.10 (+10.67%)</td><td>128.50 (-5.03%)</td><td>38.92 <b>(+86.83%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>184.10 (n/a)</td><td>159.14 (n/a)</td><td>153.70 (n/a)</td><td>135.30 (n/a)</td><td>20.83 (n/a)</td>
</tr>
</tbody>
</table>


</details>
