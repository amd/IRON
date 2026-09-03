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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.05 <b>(+55.23%)</b></td><td>0.04 <b>(+36.32%)</b></td><td>0.05 <b>(+51.88%)</b></td><td>0.03 (+4.51%)</td><td>0.01 <b>(+230.60%)</b></td><td>227.80 (-4.33%)</td><td>152.28 <b>(-22.19%)</b></td><td>122.40 <b>(-34.16%)</b></td><td>115.40 <b>(-35.57%)</b></td><td>48.64 <b>(+98.17%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>238.10 (n/a)</td><td>195.72 (n/a)</td><td>185.90 (n/a)</td><td>179.10 (n/a)</td><td>24.54 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.05 (+10.70%)</td><td>0.04 (+14.55%)</td><td>0.04 <b>(+24.34%)</b></td><td>0.02 (-2.72%)</td><td>0.01 <b>(+54.35%)</b></td><td>246.10 (+2.80%)</td><td>167.86 (-9.57%)</td><td>150.70 (-19.58%)</td><td>125.60 (-9.71%)</td><td>51.33 <b>(+39.26%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.40 (n/a)</td><td>185.62 (n/a)</td><td>187.40 (n/a)</td><td>139.10 (n/a)</td><td>36.86 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.05 <b>(+21.95%)</b></td><td>0.04 (+7.85%)</td><td>0.04 (+6.70%)</td><td>0.03 (-2.51%)</td><td>0.01 <b>(+145.17%)</b></td><td>219.00 (+2.53%)</td><td>178.12 (-4.66%)</td><td>174.20 (-6.29%)</td><td>136.00 (-17.97%)</td><td>36.77 <b>(+108.34%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>213.60 (n/a)</td><td>186.82 (n/a)</td><td>185.90 (n/a)</td><td>165.80 (n/a)</td><td>17.65 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (-10.31%)</td><td>0.03 (-0.84%)</td><td>0.03 (+5.79%)</td><td>0.03 (+14.02%)</td><td>0.00 <b>(-46.26%)</b></td><td>212.90 (-12.31%)</td><td>184.34 (-1.98%)</td><td>185.50 (-5.50%)</td><td>152.40 (+11.49%)</td><td>21.49 <b>(-47.64%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>242.80 (n/a)</td><td>188.06 (n/a)</td><td>196.30 (n/a)</td><td>136.70 (n/a)</td><td>41.06 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.05 (+15.40%)</td><td>0.04 (+3.97%)</td><td>0.03 (-2.85%)</td><td>0.02 (-17.89%)</td><td>0.01 <b>(+111.94%)</b></td><td>248.00 <b>(+21.81%)</b></td><td>173.92 (+0.42%)</td><td>178.10 (+2.95%)</td><td>131.20 (-13.34%)</td><td>47.75 <b>(+118.91%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>203.60 (n/a)</td><td>173.20 (n/a)</td><td>173.00 (n/a)</td><td>151.40 (n/a)</td><td>21.81 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (-14.25%)</td><td>0.03 (-4.35%)</td><td>0.03 (-10.24%)</td><td>0.03 (+12.27%)</td><td>0.00 <b>(-54.81%)</b></td><td>204.40 (-10.90%)</td><td>179.08 (+1.88%)</td><td>180.20 (+11.44%)</td><td>158.10 (+16.59%)</td><td>17.04 <b>(-53.44%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>229.40 (n/a)</td><td>175.78 (n/a)</td><td>161.70 (n/a)</td><td>135.60 (n/a)</td><td>36.60 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (+8.20%)</td><td>0.03 (+3.21%)</td><td>0.03 (-8.17%)</td><td>0.03 (+9.63%)</td><td>0.01 <b>(+25.76%)</b></td><td>226.30 (-8.79%)</td><td>193.66 (-2.61%)</td><td>210.20 (+8.91%)</td><td>159.30 (-7.54%)</td><td>31.16 (+2.61%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>248.10 (n/a)</td><td>198.86 (n/a)</td><td>193.00 (n/a)</td><td>172.30 (n/a)</td><td>30.37 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 <b>(+22.23%)</b></td><td>0.04 (+10.66%)</td><td>0.04 (+18.34%)</td><td>0.03 (-12.64%)</td><td>0.01 <b>(+180.29%)</b></td><td>237.10 (+14.49%)</td><td>173.70 (-6.69%)</td><td>156.20 (-15.52%)</td><td>139.90 (-18.19%)</td><td>39.88 <b>(+165.77%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>207.10 (n/a)</td><td>186.16 (n/a)</td><td>184.90 (n/a)</td><td>171.00 (n/a)</td><td>15.01 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.10 <b>(+28.68%)</b></td><td>0.08 (+19.80%)</td><td>0.08 (+7.76%)</td><td>0.06 (+10.63%)</td><td>0.01 <b>(+66.70%)</b></td><td>190.40 (-9.63%)</td><td>155.08 (-15.62%)</td><td>155.50 (-7.22%)</td><td>129.10 <b>(-22.28%)</b></td><td>26.62 (+13.72%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>210.70 (n/a)</td><td>183.78 (n/a)</td><td>167.60 (n/a)</td><td>166.10 (n/a)</td><td>23.41 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.09 (-2.38%)</td><td>0.08 (-0.09%)</td><td>0.07 (+3.24%)</td><td>0.07 (-1.68%)</td><td>0.01 (-2.73%)</td><td>181.00 (+1.69%)</td><td>163.16 (+0.09%)</td><td>167.60 (-3.12%)</td><td>135.80 (+2.41%)</td><td>19.68 (+2.51%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>178.00 (n/a)</td><td>163.02 (n/a)</td><td>173.00 (n/a)</td><td>132.60 (n/a)</td><td>19.20 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (-19.69%)</td><td>0.06 (-18.39%)</td><td>0.07 (-8.97%)</td><td>0.05 <b>(-23.98%)</b></td><td>0.01 (-17.81%)</td><td>243.80 <b>(+31.57%)</b></td><td>195.54 <b>(+22.83%)</b></td><td>176.60 (+9.89%)</td><td>167.10 <b>(+24.52%)</b></td><td>33.09 <b>(+35.93%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>185.30 (n/a)</td><td>159.20 (n/a)</td><td>160.70 (n/a)</td><td>134.20 (n/a)</td><td>24.34 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.09 (+19.56%)</td><td>0.07 (+5.97%)</td><td>0.07 (+5.47%)</td><td>0.05 <b>(-22.83%)</b></td><td>0.01 <b>(+472.27%)</b></td><td>234.90 <b>(+29.56%)</b></td><td>170.62 (-2.58%)</td><td>164.80 (-5.18%)</td><td>139.60 (-16.36%)</td><td>37.66 <b>(+532.97%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>181.30 (n/a)</td><td>175.14 (n/a)</td><td>173.80 (n/a)</td><td>166.90 (n/a)</td><td>5.95 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.09 (+13.41%)</td><td>0.07 (+5.49%)</td><td>0.07 (-2.74%)</td><td>0.05 <b>(+35.10%)</b></td><td>0.01 (-17.89%)</td><td>237.10 <b>(-25.98%)</b></td><td>178.96 (-8.92%)</td><td>168.00 (+2.82%)</td><td>140.10 (-11.83%)</td><td>37.29 <b>(-46.51%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>320.30 (n/a)</td><td>196.48 (n/a)</td><td>163.40 (n/a)</td><td>158.90 (n/a)</td><td>69.73 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.10 (-2.42%)</td><td>0.07 (-1.25%)</td><td>0.08 (+6.68%)</td><td>0.04 (-15.10%)</td><td>0.02 (+12.31%)</td><td>284.10 (+17.79%)</td><td>180.46 (+3.95%)</td><td>158.30 (-6.28%)</td><td>127.10 (+2.42%)</td><td>60.88 <b>(+41.20%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>241.20 (n/a)</td><td>173.60 (n/a)</td><td>168.90 (n/a)</td><td>124.10 (n/a)</td><td>43.11 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.08 (-4.76%)</td><td>0.06 (-3.86%)</td><td>0.07 (+4.55%)</td><td>0.04 <b>(-27.18%)</b></td><td>0.01 <b>(+49.79%)</b></td><td>312.80 <b>(+37.31%)</b></td><td>202.08 (+8.32%)</td><td>175.20 (-4.31%)</td><td>159.00 (+5.02%)</td><td>62.80 <b>(+126.72%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>227.80 (n/a)</td><td>186.56 (n/a)</td><td>183.10 (n/a)</td><td>151.40 (n/a)</td><td>27.70 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.08 (-9.83%)</td><td>0.07 (-8.22%)</td><td>0.07 (-5.21%)</td><td>0.05 (-16.16%)</td><td>0.01 (-14.80%)</td><td>249.40 (+19.27%)</td><td>193.34 (+8.81%)</td><td>187.80 (+5.51%)</td><td>152.40 (+10.92%)</td><td>35.00 (+12.50%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>209.10 (n/a)</td><td>177.68 (n/a)</td><td>178.00 (n/a)</td><td>137.40 (n/a)</td><td>31.11 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.20 (+8.06%)</td><td>0.16 (-0.36%)</td><td>0.14 (-6.03%)</td><td>0.12 (-0.68%)</td><td>0.03 <b>(+40.85%)</b></td><td>197.10 (+0.72%)</td><td>162.64 (+1.83%)</td><td>173.40 (+6.45%)</td><td>124.40 (-7.51%)</td><td>31.49 <b>(+30.78%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>195.70 (n/a)</td><td>159.72 (n/a)</td><td>162.90 (n/a)</td><td>134.50 (n/a)</td><td>24.08 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.19 (+2.06%)</td><td>0.15 (+12.82%)</td><td>0.16 (+9.12%)</td><td>0.10 <b>(+57.39%)</b></td><td>0.04 <b>(-23.88%)</b></td><td>248.30 <b>(-36.46%)</b></td><td>167.36 (-19.05%)</td><td>156.70 (-8.36%)</td><td>126.40 (-2.02%)</td><td>47.63 <b>(-54.68%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>390.80 (n/a)</td><td>206.74 (n/a)</td><td>171.00 (n/a)</td><td>129.00 (n/a)</td><td>105.10 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.19 <b>(+35.68%)</b></td><td>0.14 (+10.90%)</td><td>0.15 (+12.73%)</td><td>0.10 (-11.91%)</td><td>0.04 <b>(+263.17%)</b></td><td>240.40 (+13.50%)</td><td>184.52 (-4.44%)</td><td>166.70 (-11.28%)</td><td>126.50 <b>(-26.28%)</b></td><td>51.77 <b>(+219.31%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>211.80 (n/a)</td><td>193.10 (n/a)</td><td>187.90 (n/a)</td><td>171.60 (n/a)</td><td>16.21 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.19 (-0.20%)</td><td>0.15 (+0.11%)</td><td>0.15 (+4.38%)</td><td>0.12 (-1.59%)</td><td>0.03 (+1.16%)</td><td>202.60 (+1.60%)</td><td>166.92 (+0.00%)</td><td>161.50 (-4.21%)</td><td>128.80 (+0.23%)</td><td>27.94 (+3.77%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>199.40 (n/a)</td><td>166.92 (n/a)</td><td>168.60 (n/a)</td><td>128.50 (n/a)</td><td>26.92 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.21 (+4.51%)</td><td>0.14 (-7.95%)</td><td>0.14 (-5.46%)</td><td>0.11 (-1.71%)</td><td>0.04 (+4.36%)</td><td>217.90 (+1.73%)</td><td>179.12 (+9.01%)</td><td>173.80 (+5.78%)</td><td>117.10 (-4.33%)</td><td>41.12 (+4.09%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>214.20 (n/a)</td><td>164.32 (n/a)</td><td>164.30 (n/a)</td><td>122.40 (n/a)</td><td>39.50 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.18 (-11.41%)</td><td>0.13 (-14.25%)</td><td>0.14 (-8.81%)</td><td>0.06 <b>(-30.90%)</b></td><td>0.04 (-3.74%)</td><td>389.80 <b>(+44.75%)</b></td><td>211.00 <b>(+22.40%)</b></td><td>171.20 (+9.67%)</td><td>133.50 (+12.85%)</td><td>102.18 <b>(+69.83%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>269.30 (n/a)</td><td>172.38 (n/a)</td><td>156.10 (n/a)</td><td>118.30 (n/a)</td><td>60.17 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.19 (+1.68%)</td><td>0.14 (-2.08%)</td><td>0.12 (-10.28%)</td><td>0.11 (+16.86%)</td><td>0.03 (-8.73%)</td><td>217.70 (-14.43%)</td><td>186.60 (+0.59%)</td><td>204.00 (+11.48%)</td><td>129.00 (-1.60%)</td><td>35.56 <b>(-24.69%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>254.40 (n/a)</td><td>185.50 (n/a)</td><td>183.00 (n/a)</td><td>131.10 (n/a)</td><td>47.22 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.16 (+1.16%)</td><td>0.14 (-0.78%)</td><td>0.14 (+9.35%)</td><td>0.10 (-19.53%)</td><td>0.02 <b>(+38.09%)</b></td><td>251.30 <b>(+24.22%)</b></td><td>186.40 (+2.38%)</td><td>173.60 (-8.58%)</td><td>156.50 (-1.14%)</td><td>37.60 <b>(+76.96%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>202.30 (n/a)</td><td>182.06 (n/a)</td><td>189.90 (n/a)</td><td>158.30 (n/a)</td><td>21.25 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.40 (+16.86%)</td><td>0.30 (-0.17%)</td><td>0.33 (+3.06%)</td><td>0.22 (+0.60%)</td><td>0.07 <b>(+40.19%)</b></td><td>227.70 (-0.57%)</td><td>169.38 (+2.01%)</td><td>151.10 (-3.02%)</td><td>122.00 (-14.45%)</td><td>42.01 (+17.74%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.34 (n/a)</td><td>0.30 (n/a)</td><td>0.32 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>229.00 (n/a)</td><td>166.04 (n/a)</td><td>155.80 (n/a)</td><td>142.60 (n/a)</td><td>35.68 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.30 (-19.78%)</td><td>0.27 (+0.82%)</td><td>0.26 (+3.52%)</td><td>0.25 <b>(+35.26%)</b></td><td>0.02 <b>(-75.97%)</b></td><td>197.30 <b>(-26.08%)</b></td><td>183.24 (-7.19%)</td><td>186.20 (-3.37%)</td><td>164.20 <b>(+24.68%)</b></td><td>12.45 <b>(-78.26%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.37 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>266.90 (n/a)</td><td>197.44 (n/a)</td><td>192.70 (n/a)</td><td>131.70 (n/a)</td><td>57.27 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.39 (+8.12%)</td><td>0.30 (-3.79%)</td><td>0.27 <b>(-22.21%)</b></td><td>0.24 (+15.12%)</td><td>0.06 (-2.83%)</td><td>202.70 (-13.15%)</td><td>171.26 (+2.95%)</td><td>184.40 <b>(+28.50%)</b></td><td>125.80 (-7.50%)</td><td>32.49 <b>(-21.23%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.36 (n/a)</td><td>0.31 (n/a)</td><td>0.34 (n/a)</td><td>0.21 (n/a)</td><td>0.06 (n/a)</td><td>233.40 (n/a)</td><td>166.36 (n/a)</td><td>143.50 (n/a)</td><td>136.00 (n/a)</td><td>41.25 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.37 (-4.54%)</td><td>0.32 (+2.08%)</td><td>0.31 (-5.65%)</td><td>0.28 <b>(+32.81%)</b></td><td>0.04 <b>(-40.15%)</b></td><td>174.90 <b>(-24.71%)</b></td><td>155.74 (-5.05%)</td><td>157.10 (+6.01%)</td><td>131.70 (+4.77%)</td><td>19.22 <b>(-53.60%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.39 (n/a)</td><td>0.31 (n/a)</td><td>0.33 (n/a)</td><td>0.21 (n/a)</td><td>0.07 (n/a)</td><td>232.30 (n/a)</td><td>164.02 (n/a)</td><td>148.20 (n/a)</td><td>125.70 (n/a)</td><td>41.43 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.41 (+11.00%)</td><td>0.33 (+18.33%)</td><td>0.32 <b>(+22.94%)</b></td><td>0.25 (+8.62%)</td><td>0.06 (+4.87%)</td><td>197.40 (-7.93%)</td><td>152.80 (-15.81%)</td><td>155.90 (-18.68%)</td><td>119.10 (-9.91%)</td><td>30.34 (-14.89%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.37 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>214.40 (n/a)</td><td>181.50 (n/a)</td><td>191.70 (n/a)</td><td>132.20 (n/a)</td><td>35.65 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.32 <b>(-32.37%)</b></td><td>0.25 (-17.46%)</td><td>0.27 (+4.41%)</td><td>0.16 <b>(-25.53%)</b></td><td>0.06 <b>(-47.45%)</b></td><td>306.20 <b>(+34.30%)</b></td><td>205.62 (+16.41%)</td><td>184.10 (-4.21%)</td><td>156.00 <b>(+47.87%)</b></td><td>58.79 (+6.32%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.47 (n/a)</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>228.00 (n/a)</td><td>176.64 (n/a)</td><td>192.20 (n/a)</td><td>105.50 (n/a)</td><td>55.29 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.39 (-12.00%)</td><td>0.28 (-5.62%)</td><td>0.29 (-2.97%)</td><td>0.16 <b>(-25.17%)</b></td><td>0.08 (-8.83%)</td><td>299.70 <b>(+33.62%)</b></td><td>189.12 (+7.85%)</td><td>171.80 (+3.06%)</td><td>125.60 (+13.67%)</td><td>66.05 <b>(+43.68%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.44 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.09 (n/a)</td><td>224.30 (n/a)</td><td>175.36 (n/a)</td><td>166.70 (n/a)</td><td>110.50 (n/a)</td><td>45.97 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.37 (+0.39%)</td><td>0.28 (+3.53%)</td><td>0.28 (+14.36%)</td><td>0.19 (+8.67%)</td><td>0.07 (-14.97%)</td><td>258.10 (-7.99%)</td><td>185.56 (-5.42%)</td><td>177.60 (-12.56%)</td><td>132.20 (-0.38%)</td><td>45.96 (-19.82%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.37 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>280.50 (n/a)</td><td>196.20 (n/a)</td><td>203.10 (n/a)</td><td>132.70 (n/a)</td><td>57.32 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.02 (-11.38%)</td><td>0.02 (-1.48%)</td><td>0.02 (-6.72%)</td><td>0.01 <b>(+69.53%)</b></td><td>0.00 <b>(-56.94%)</b></td><td>211.20 <b>(-41.01%)</b></td><td>166.14 (-10.53%)</td><td>161.30 (+7.25%)</td><td>141.40 (+12.85%)</td><td>26.93 <b>(-72.34%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>358.00 (n/a)</td><td>185.70 (n/a)</td><td>150.40 (n/a)</td><td>125.30 (n/a)</td><td>97.38 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.02 (-13.18%)</td><td>0.01 (-16.21%)</td><td>0.02 (-17.00%)</td><td>0.01 <b>(-22.24%)</b></td><td>0.00 <b>(+25.17%)</b></td><td>221.10 <b>(+28.62%)</b></td><td>179.28 <b>(+20.39%)</b></td><td>173.50 <b>(+20.49%)</b></td><td>156.70 (+15.22%)</td><td>25.92 <b>(+83.98%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>171.90 (n/a)</td><td>148.92 (n/a)</td><td>144.00 (n/a)</td><td>136.00 (n/a)</td><td>14.09 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.02 (-16.74%)</td><td>0.02 (-8.10%)</td><td>0.02 (-4.25%)</td><td>0.01 (+2.84%)</td><td>0.00 <b>(-58.25%)</b></td><td>185.10 (-2.73%)</td><td>165.98 (+6.78%)</td><td>162.10 (+4.45%)</td><td>153.20 <b>(+20.06%)</b></td><td>13.30 <b>(-50.33%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>190.30 (n/a)</td><td>155.44 (n/a)</td><td>155.20 (n/a)</td><td>127.60 (n/a)</td><td>26.77 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.02 <b>(-24.43%)</b></td><td>0.01 (-17.81%)</td><td>0.01 (-18.39%)</td><td>0.01 (-2.69%)</td><td>0.00 <b>(-46.95%)</b></td><td>219.10 (+2.77%)</td><td>196.84 (+18.89%)</td><td>206.20 <b>(+22.59%)</b></td><td>156.10 <b>(+32.40%)</b></td><td>25.60 <b>(-27.27%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>213.20 (n/a)</td><td>165.56 (n/a)</td><td>168.20 (n/a)</td><td>117.90 (n/a)</td><td>35.21 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.02 (+18.04%)</td><td>0.02 (-3.05%)</td><td>0.01 (-6.73%)</td><td>0.01 (-7.28%)</td><td>0.00 <b>(+80.53%)</b></td><td>216.00 (+7.84%)</td><td>177.62 (+7.27%)</td><td>179.70 (+7.22%)</td><td>109.00 (-15.31%)</td><td>42.62 <b>(+63.58%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>200.30 (n/a)</td><td>165.58 (n/a)</td><td>167.60 (n/a)</td><td>128.70 (n/a)</td><td>26.06 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.02 <b>(-29.07%)</b></td><td>0.01 (-18.08%)</td><td>0.01 (-18.67%)</td><td>0.01 (+3.82%)</td><td>0.00 <b>(-63.19%)</b></td><td>215.60 (-3.66%)</td><td>189.32 (+17.10%)</td><td>185.80 <b>(+22.96%)</b></td><td>165.30 <b>(+41.04%)</b></td><td>21.00 <b>(-50.19%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>223.80 (n/a)</td><td>161.68 (n/a)</td><td>151.10 (n/a)</td><td>117.20 (n/a)</td><td>42.17 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.02 (-17.78%)</td><td>0.01 (-19.44%)</td><td>0.01 <b>(-23.72%)</b></td><td>0.01 (-18.07%)</td><td>0.00 (-12.22%)</td><td>202.10 <b>(+22.04%)</b></td><td>188.72 <b>(+24.21%)</b></td><td>197.00 <b>(+31.07%)</b></td><td>164.10 <b>(+21.65%)</b></td><td>15.81 <b>(+29.65%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>165.60 (n/a)</td><td>151.94 (n/a)</td><td>150.30 (n/a)</td><td>134.90 (n/a)</td><td>12.19 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.01 (-5.04%)</td><td>0.01 (-5.11%)</td><td>0.01 (+4.32%)</td><td>0.01 <b>(-40.94%)</b></td><td>0.00 <b>(+119.20%)</b></td><td>378.30 <b>(+69.34%)</b></td><td>232.64 (+12.41%)</td><td>202.50 (-4.16%)</td><td>181.80 (+5.33%)</td><td>82.53 <b>(+311.25%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>223.40 (n/a)</td><td>206.96 (n/a)</td><td>211.30 (n/a)</td><td>172.60 (n/a)</td><td>20.07 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (-6.91%)</td><td>0.03 (+1.01%)</td><td>0.03 (+0.68%)</td><td>0.03 (+18.50%)</td><td>0.00 <b>(-38.92%)</b></td><td>174.50 (-15.62%)</td><td>155.78 (-3.12%)</td><td>156.20 (-0.64%)</td><td>128.40 (+7.45%)</td><td>17.88 <b>(-44.98%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>206.80 (n/a)</td><td>160.80 (n/a)</td><td>157.20 (n/a)</td><td>119.50 (n/a)</td><td>32.50 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (-16.73%)</td><td>0.03 (+8.41%)</td><td>0.03 (+16.74%)</td><td>0.02 <b>(+43.72%)</b></td><td>0.00 <b>(-47.56%)</b></td><td>235.40 <b>(-30.42%)</b></td><td>179.58 (-14.30%)</td><td>172.30 (-14.36%)</td><td>154.50 <b>(+20.14%)</b></td><td>33.18 <b>(-57.51%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>338.30 (n/a)</td><td>209.54 (n/a)</td><td>201.20 (n/a)</td><td>128.60 (n/a)</td><td>78.08 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.05 <b>(+32.48%)</b></td><td>0.03 (-4.03%)</td><td>0.03 (-8.30%)</td><td>0.02 <b>(-28.43%)</b></td><td>0.01 <b>(+222.65%)</b></td><td>255.20 <b>(+39.76%)</b></td><td>181.62 (+12.75%)</td><td>171.90 (+9.07%)</td><td>105.70 <b>(-24.55%)</b></td><td>56.21 <b>(+232.04%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>182.60 (n/a)</td><td>161.08 (n/a)</td><td>157.60 (n/a)</td><td>140.10 (n/a)</td><td>16.93 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (-4.73%)</td><td>0.03 (-2.63%)</td><td>0.03 (-2.69%)</td><td>0.02 (+0.91%)</td><td>0.00 (-17.83%)</td><td>215.80 (-0.92%)</td><td>174.98 (+2.08%)</td><td>164.20 (+2.75%)</td><td>156.50 (+4.96%)</td><td>24.99 (-14.03%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.80 (n/a)</td><td>171.42 (n/a)</td><td>159.80 (n/a)</td><td>149.10 (n/a)</td><td>29.07 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (+2.72%)</td><td>0.03 (+5.66%)</td><td>0.03 (+12.89%)</td><td>0.02 (-9.38%)</td><td>0.01 (+19.09%)</td><td>241.70 (+10.31%)</td><td>171.76 (-3.32%)</td><td>163.20 (-11.40%)</td><td>119.80 (-2.60%)</td><td>48.87 <b>(+29.22%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>219.10 (n/a)</td><td>177.66 (n/a)</td><td>184.20 (n/a)</td><td>123.00 (n/a)</td><td>37.82 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 <b>(+38.26%)</b></td><td>0.03 (+5.85%)</td><td>0.03 (-2.96%)</td><td>0.02 (-10.84%)</td><td>0.01 <b>(+232.62%)</b></td><td>236.30 (+12.15%)</td><td>190.40 (-1.24%)</td><td>196.90 (+3.04%)</td><td>122.50 <b>(-27.64%)</b></td><td>42.58 <b>(+156.28%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.70 (n/a)</td><td>192.80 (n/a)</td><td>191.10 (n/a)</td><td>169.30 (n/a)</td><td>16.61 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 <b>(+20.37%)</b></td><td>0.03 (+6.34%)</td><td>0.03 (+1.72%)</td><td>0.02 <b>(-20.92%)</b></td><td>0.01 <b>(+181.15%)</b></td><td>297.10 <b>(+26.48%)</b></td><td>209.10 (-1.43%)</td><td>203.60 (-1.69%)</td><td>155.60 (-16.92%)</td><td>56.80 <b>(+189.02%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>234.90 (n/a)</td><td>212.14 (n/a)</td><td>207.10 (n/a)</td><td>187.30 (n/a)</td><td>19.65 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 <b>(+22.95%)</b></td><td>0.03 (+11.30%)</td><td>0.02 (+8.89%)</td><td>0.02 (+4.43%)</td><td>0.00 <b>(+112.19%)</b></td><td>232.30 (-4.25%)</td><td>204.92 (-9.16%)</td><td>214.50 (-8.18%)</td><td>168.60 (-18.67%)</td><td>27.66 <b>(+67.82%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>242.60 (n/a)</td><td>225.58 (n/a)</td><td>233.60 (n/a)</td><td>207.30 (n/a)</td><td>16.48 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.08 (+1.29%)</td><td>0.06 (+4.60%)</td><td>0.06 (-6.56%)</td><td>0.06 <b>(+25.46%)</b></td><td>0.01 <b>(-20.92%)</b></td><td>184.90 <b>(-20.30%)</b></td><td>168.44 (-6.23%)</td><td>180.60 (+7.05%)</td><td>127.80 (-1.31%)</td><td>24.03 <b>(-38.16%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>232.00 (n/a)</td><td>179.64 (n/a)</td><td>168.70 (n/a)</td><td>129.50 (n/a)</td><td>38.86 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 <b>(-26.60%)</b></td><td>0.06 (-11.34%)</td><td>0.06 (+1.38%)</td><td>0.05 <b>(+25.21%)</b></td><td>0.00 <b>(-71.56%)</b></td><td>206.10 <b>(-20.15%)</b></td><td>186.84 (+6.39%)</td><td>176.20 (-1.34%)</td><td>172.90 <b>(+36.25%)</b></td><td>16.60 <b>(-68.34%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>258.10 (n/a)</td><td>175.62 (n/a)</td><td>178.60 (n/a)</td><td>126.90 (n/a)</td><td>52.41 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (-9.17%)</td><td>0.07 (-9.27%)</td><td>0.07 (-4.49%)</td><td>0.06 (-11.09%)</td><td>0.01 (-9.20%)</td><td>188.80 (+12.45%)</td><td>161.22 (+10.27%)</td><td>157.70 (+4.71%)</td><td>140.50 (+10.11%)</td><td>20.02 (+14.33%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>167.90 (n/a)</td><td>146.20 (n/a)</td><td>150.60 (n/a)</td><td>127.60 (n/a)</td><td>17.51 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.10 (+11.65%)</td><td>0.07 (-6.91%)</td><td>0.06 <b>(-25.85%)</b></td><td>0.06 (+3.09%)</td><td>0.02 (+6.77%)</td><td>189.40 (-3.02%)</td><td>165.24 (+7.20%)</td><td>181.60 <b>(+34.92%)</b></td><td>110.20 (-10.48%)</td><td>32.86 (-10.02%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>195.30 (n/a)</td><td>154.14 (n/a)</td><td>134.60 (n/a)</td><td>123.10 (n/a)</td><td>36.52 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 <b>(-23.99%)</b></td><td>0.06 <b>(-22.14%)</b></td><td>0.06 <b>(-20.27%)</b></td><td>0.05 (-13.85%)</td><td>0.01 <b>(-52.39%)</b></td><td>214.80 (+16.05%)</td><td>192.16 <b>(+26.30%)</b></td><td>187.40 <b>(+25.44%)</b></td><td>165.00 <b>(+31.58%)</b></td><td>20.77 <b>(-24.86%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>185.10 (n/a)</td><td>152.14 (n/a)</td><td>149.40 (n/a)</td><td>125.40 (n/a)</td><td>27.64 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.09 (+0.53%)</td><td>0.06 (-14.49%)</td><td>0.06 (-6.34%)</td><td>0.04 <b>(-34.46%)</b></td><td>0.02 <b>(+93.05%)</b></td><td>250.90 <b>(+52.52%)</b></td><td>183.16 <b>(+22.89%)</b></td><td>166.40 (+6.80%)</td><td>121.60 (-0.57%)</td><td>49.63 <b>(+198.58%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>164.50 (n/a)</td><td>149.04 (n/a)</td><td>155.80 (n/a)</td><td>122.30 (n/a)</td><td>16.62 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (-3.88%)</td><td>0.06 (-16.58%)</td><td>0.06 (-9.53%)</td><td>0.03 <b>(-45.37%)</b></td><td>0.01 <b>(+173.51%)</b></td><td>304.70 <b>(+83.11%)</b></td><td>194.84 <b>(+27.58%)</b></td><td>174.00 (+10.55%)</td><td>143.50 (+4.06%)</td><td>63.72 <b>(+452.76%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>166.40 (n/a)</td><td>152.72 (n/a)</td><td>157.40 (n/a)</td><td>137.90 (n/a)</td><td>11.53 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (-8.13%)</td><td>0.05 (-10.20%)</td><td>0.05 (-8.46%)</td><td>0.03 (-6.65%)</td><td>0.01 <b>(-20.53%)</b></td><td>339.30 (+7.10%)</td><td>241.80 (+10.20%)</td><td>226.50 (+9.21%)</td><td>190.60 (+8.85%)</td><td>56.81 (-2.32%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>316.80 (n/a)</td><td>219.42 (n/a)</td><td>207.40 (n/a)</td><td>175.10 (n/a)</td><td>58.16 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.14 (-2.36%)</td><td>0.12 (-3.99%)</td><td>0.11 (-12.45%)</td><td>0.09 (+0.23%)</td><td>0.02 (-3.36%)</td><td>222.60 (-0.27%)</td><td>180.96 (+3.96%)</td><td>188.10 (+14.28%)</td><td>148.10 (+2.42%)</td><td>32.18 (-3.51%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>223.20 (n/a)</td><td>174.06 (n/a)</td><td>164.60 (n/a)</td><td>144.60 (n/a)</td><td>33.36 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.16 (+18.03%)</td><td>0.13 (+3.16%)</td><td>0.12 (-1.40%)</td><td>0.11 (-2.77%)</td><td>0.02 <b>(+124.70%)</b></td><td>187.30 (+2.86%)</td><td>167.34 (-1.66%)</td><td>176.70 (+1.44%)</td><td>127.90 (-15.30%)</td><td>23.63 <b>(+93.41%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>182.10 (n/a)</td><td>170.16 (n/a)</td><td>174.20 (n/a)</td><td>151.00 (n/a)</td><td>12.22 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.16 (+11.16%)</td><td>0.14 <b>(+29.88%)</b></td><td>0.14 <b>(+21.74%)</b></td><td>0.12 <b>(+79.16%)</b></td><td>0.02 <b>(-37.25%)</b></td><td>173.20 <b>(-44.20%)</b></td><td>150.70 <b>(-26.74%)</b></td><td>154.70 (-17.84%)</td><td>129.30 (-10.02%)</td><td>18.41 <b>(-70.42%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>310.40 (n/a)</td><td>205.70 (n/a)</td><td>188.30 (n/a)</td><td>143.70 (n/a)</td><td>62.21 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.15 (+12.95%)</td><td>0.13 (+9.52%)</td><td>0.13 (+6.90%)</td><td>0.10 (+1.41%)</td><td>0.02 <b>(+67.92%)</b></td><td>210.30 (-1.41%)</td><td>170.22 (-7.27%)</td><td>165.00 (-6.46%)</td><td>138.70 (-11.49%)</td><td>31.34 <b>(+44.45%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>213.30 (n/a)</td><td>183.56 (n/a)</td><td>176.40 (n/a)</td><td>156.70 (n/a)</td><td>21.69 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.17 <b>(+21.84%)</b></td><td>0.13 (+6.03%)</td><td>0.12 (-3.73%)</td><td>0.11 (+9.53%)</td><td>0.03 <b>(+63.33%)</b></td><td>196.40 (-8.69%)</td><td>168.14 (-4.43%)</td><td>177.00 (+3.87%)</td><td>122.10 (-17.94%)</td><td>28.91 (+17.63%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>215.10 (n/a)</td><td>175.94 (n/a)</td><td>170.40 (n/a)</td><td>148.80 (n/a)</td><td>24.58 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.18 (+15.68%)</td><td>0.12 (+3.53%)</td><td>0.11 (-6.77%)</td><td>0.10 (+4.91%)</td><td>0.04 <b>(+27.35%)</b></td><td>216.60 (-4.67%)</td><td>181.26 (-2.20%)</td><td>198.30 (+7.25%)</td><td>115.80 (-13.58%)</td><td>42.55 (+2.33%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>227.20 (n/a)</td><td>185.34 (n/a)</td><td>184.90 (n/a)</td><td>134.00 (n/a)</td><td>41.58 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 (-17.48%)</td><td>0.10 (-13.11%)</td><td>0.10 (-7.69%)</td><td>0.07 <b>(-20.98%)</b></td><td>0.02 (-14.79%)</td><td>312.80 <b>(+26.54%)</b></td><td>227.72 (+15.73%)</td><td>214.30 (+8.34%)</td><td>166.00 <b>(+21.17%)</b></td><td>56.16 <b>(+34.63%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>247.20 (n/a)</td><td>196.76 (n/a)</td><td>197.80 (n/a)</td><td>137.00 (n/a)</td><td>41.71 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.12 (+2.01%)</td><td>0.09 (-13.55%)</td><td>0.08 (-19.99%)</td><td>0.08 (-12.03%)</td><td>0.02 <b>(+47.26%)</b></td><td>271.40 (+13.65%)</td><td>238.82 (+17.59%)</td><td>257.90 <b>(+24.95%)</b></td><td>174.70 (-1.96%)</td><td>41.32 <b>(+67.71%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>238.80 (n/a)</td><td>203.10 (n/a)</td><td>206.40 (n/a)</td><td>178.20 (n/a)</td><td>24.64 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>188.50 (n/a)</td><td>147.74 (n/a)</td><td>135.80 (n/a)</td><td>108.10 (n/a)</td><td>32.99 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>213.80 (n/a)</td><td>155.72 (n/a)</td><td>147.40 (n/a)</td><td>105.60 (n/a)</td><td>43.33 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>250.60 (n/a)</td><td>177.98 (n/a)</td><td>178.90 (n/a)</td><td>116.60 (n/a)</td><td>48.28 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>220.40 (n/a)</td><td>180.36 (n/a)</td><td>172.50 (n/a)</td><td>149.50 (n/a)</td><td>26.40 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>248.60 (n/a)</td><td>177.08 (n/a)</td><td>171.00 (n/a)</td><td>133.20 (n/a)</td><td>43.39 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>240.10 (n/a)</td><td>198.30 (n/a)</td><td>199.20 (n/a)</td><td>126.10 (n/a)</td><td>44.64 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>209.80 (n/a)</td><td>176.46 (n/a)</td><td>195.70 (n/a)</td><td>107.10 (n/a)</td><td>40.94 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>234.50 (n/a)</td><td>202.22 (n/a)</td><td>195.20 (n/a)</td><td>180.00 (n/a)</td><td>21.42 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>228.30 (n/a)</td><td>193.02 (n/a)</td><td>207.40 (n/a)</td><td>156.60 (n/a)</td><td>33.72 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>241.10 (n/a)</td><td>193.16 (n/a)</td><td>187.90 (n/a)</td><td>152.30 (n/a)</td><td>32.07 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>216.20 (n/a)</td><td>186.22 (n/a)</td><td>182.50 (n/a)</td><td>137.80 (n/a)</td><td>32.41 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>249.90 (n/a)</td><td>213.68 (n/a)</td><td>213.50 (n/a)</td><td>194.30 (n/a)</td><td>22.70 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.36 (-10.06%)</td><td>0.27 (-11.64%)</td><td>0.26 (-15.23%)</td><td>0.22 (+2.60%)</td><td>0.05 <b>(-36.03%)</b></td><td>223.60 (-2.53%)</td><td>185.90 (+9.37%)</td><td>187.80 (+17.96%)</td><td>136.70 (+11.14%)</td><td>31.79 <b>(-32.62%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.40 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.08 (n/a)</td><td>229.40 (n/a)</td><td>169.98 (n/a)</td><td>159.20 (n/a)</td><td>123.00 (n/a)</td><td>47.18 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>203.80 (n/a)</td><td>171.66 (n/a)</td><td>180.80 (n/a)</td><td>133.20 (n/a)</td><td>28.14 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.46 (n/a)</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.09 (n/a)</td><td>202.00 (n/a)</td><td>172.22 (n/a)</td><td>194.10 (n/a)</td><td>106.10 (n/a)</td><td>39.67 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.51 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>253.00 (n/a)</td><td>201.46 (n/a)</td><td>213.70 (n/a)</td><td>95.50 (n/a)</td><td>61.45 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>208.30 (n/a)</td><td>165.72 (n/a)</td><td>162.30 (n/a)</td><td>124.50 (n/a)</td><td>34.83 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>156.00 (n/a)</td><td>128.80 (n/a)</td><td>122.00 (n/a)</td><td>112.60 (n/a)</td><td>17.24 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>150.50 (n/a)</td><td>126.96 (n/a)</td><td>113.50 (n/a)</td><td>111.80 (n/a)</td><td>19.43 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>221.30 (n/a)</td><td>172.18 (n/a)</td><td>176.60 (n/a)</td><td>132.20 (n/a)</td><td>33.79 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>185.50 (n/a)</td><td>134.72 (n/a)</td><td>129.40 (n/a)</td><td>106.40 (n/a)</td><td>30.33 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>187.90 (n/a)</td><td>162.24 (n/a)</td><td>159.10 (n/a)</td><td>147.30 (n/a)</td><td>15.52 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>176.40 (n/a)</td><td>154.94 (n/a)</td><td>159.20 (n/a)</td><td>130.60 (n/a)</td><td>17.74 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>197.10 (n/a)</td><td>167.12 (n/a)</td><td>167.20 (n/a)</td><td>132.30 (n/a)</td><td>23.77 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>213.40 (n/a)</td><td>180.92 (n/a)</td><td>188.60 (n/a)</td><td>125.80 (n/a)</td><td>32.65 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>216.50 (n/a)</td><td>169.22 (n/a)</td><td>175.80 (n/a)</td><td>120.10 (n/a)</td><td>35.78 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>229.80 (n/a)</td><td>183.12 (n/a)</td><td>164.60 (n/a)</td><td>155.90 (n/a)</td><td>33.28 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.25 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>251.70 (n/a)</td><td>178.88 (n/a)</td><td>184.50 (n/a)</td><td>96.70 (n/a)</td><td>61.63 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.46 (n/a)</td><td>0.35 (n/a)</td><td>0.36 (n/a)</td><td>0.28 (n/a)</td><td>0.07 (n/a)</td><td>175.70 (n/a)</td><td>144.00 (n/a)</td><td>138.10 (n/a)</td><td>107.70 (n/a)</td><td>27.45 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.45 (n/a)</td><td>0.35 (n/a)</td><td>0.41 (n/a)</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>234.50 (n/a)</td><td>155.94 (n/a)</td><td>120.00 (n/a)</td><td>110.20 (n/a)</td><td>55.92 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.33 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>206.60 (n/a)</td><td>158.92 (n/a)</td><td>149.40 (n/a)</td><td>140.30 (n/a)</td><td>27.59 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>216.50 (n/a)</td><td>159.88 (n/a)</td><td>155.20 (n/a)</td><td>115.80 (n/a)</td><td>40.69 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>167.30 (n/a)</td><td>128.24 (n/a)</td><td>125.50 (n/a)</td><td>105.90 (n/a)</td><td>24.23 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>166.00 (n/a)</td><td>143.06 (n/a)</td><td>141.70 (n/a)</td><td>120.10 (n/a)</td><td>17.62 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>199.40 (n/a)</td><td>153.54 (n/a)</td><td>143.60 (n/a)</td><td>121.30 (n/a)</td><td>35.07 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.80 (n/a)</td><td>164.56 (n/a)</td><td>174.80 (n/a)</td><td>127.80 (n/a)</td><td>31.28 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.70 (n/a)</td><td>176.56 (n/a)</td><td>180.70 (n/a)</td><td>139.00 (n/a)</td><td>30.16 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>291.90 (n/a)</td><td>203.54 (n/a)</td><td>189.80 (n/a)</td><td>151.90 (n/a)</td><td>52.30 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>337.10 (n/a)</td><td>230.52 (n/a)</td><td>208.70 (n/a)</td><td>176.30 (n/a)</td><td>63.86 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>375.20 (n/a)</td><td>205.80 (n/a)</td><td>149.20 (n/a)</td><td>138.60 (n/a)</td><td>100.47 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.20 (n/a)</td><td>162.80 (n/a)</td><td>164.50 (n/a)</td><td>123.30 (n/a)</td><td>31.81 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.00 (n/a)</td><td>157.64 (n/a)</td><td>152.90 (n/a)</td><td>118.60 (n/a)</td><td>34.60 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.00 (n/a)</td><td>160.14 (n/a)</td><td>152.60 (n/a)</td><td>144.80 (n/a)</td><td>17.24 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.40 (n/a)</td><td>153.34 (n/a)</td><td>159.30 (n/a)</td><td>116.10 (n/a)</td><td>37.24 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.60 (n/a)</td><td>174.38 (n/a)</td><td>164.50 (n/a)</td><td>138.20 (n/a)</td><td>37.65 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>325.70 (n/a)</td><td>218.96 (n/a)</td><td>188.40 (n/a)</td><td>169.60 (n/a)</td><td>64.09 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>354.70 (n/a)</td><td>234.84 (n/a)</td><td>209.90 (n/a)</td><td>186.90 (n/a)</td><td>67.82 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>249.90 (n/a)</td><td>179.76 (n/a)</td><td>167.80 (n/a)</td><td>147.00 (n/a)</td><td>41.34 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>258.40 (n/a)</td><td>177.12 (n/a)</td><td>165.90 (n/a)</td><td>130.00 (n/a)</td><td>50.67 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>247.10 (n/a)</td><td>178.86 (n/a)</td><td>173.70 (n/a)</td><td>146.10 (n/a)</td><td>40.81 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>190.90 (n/a)</td><td>173.40 (n/a)</td><td>173.40 (n/a)</td><td>156.00 (n/a)</td><td>17.10 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>176.50 (n/a)</td><td>152.94 (n/a)</td><td>152.50 (n/a)</td><td>130.30 (n/a)</td><td>18.10 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>214.60 (n/a)</td><td>176.44 (n/a)</td><td>159.30 (n/a)</td><td>145.90 (n/a)</td><td>30.58 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>203.50 (n/a)</td><td>171.52 (n/a)</td><td>172.00 (n/a)</td><td>132.10 (n/a)</td><td>31.73 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>333.70 (n/a)</td><td>223.36 (n/a)</td><td>216.60 (n/a)</td><td>154.10 (n/a)</td><td>69.16 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>185.90 (n/a)</td><td>170.42 (n/a)</td><td>173.80 (n/a)</td><td>138.70 (n/a)</td><td>18.55 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>188.50 (n/a)</td><td>156.68 (n/a)</td><td>150.00 (n/a)</td><td>124.50 (n/a)</td><td>27.54 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>200.80 (n/a)</td><td>177.26 (n/a)</td><td>180.70 (n/a)</td><td>149.60 (n/a)</td><td>18.62 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>188.60 (n/a)</td><td>168.80 (n/a)</td><td>166.20 (n/a)</td><td>150.30 (n/a)</td><td>14.17 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>200.90 (n/a)</td><td>169.84 (n/a)</td><td>184.10 (n/a)</td><td>134.80 (n/a)</td><td>31.38 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>240.20 (n/a)</td><td>196.94 (n/a)</td><td>210.30 (n/a)</td><td>139.90 (n/a)</td><td>39.98 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>235.30 (n/a)</td><td>183.58 (n/a)</td><td>169.70 (n/a)</td><td>159.00 (n/a)</td><td>31.67 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>219.60 (n/a)</td><td>187.12 (n/a)</td><td>191.90 (n/a)</td><td>133.00 (n/a)</td><td>32.78 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>4.90 (+12.82%)</td><td>4.27 (+4.54%)</td><td>4.23 (+1.25%)</td><td>3.74 (+6.12%)</td><td>0.41 <b>(+28.88%)</b></td><td>2514.40 (-5.76%)</td><td>2219.02 (-4.16%)</td><td>2223.50 (-1.23%)</td><td>1919.80 (-11.37%)</td><td>210.92 (+5.09%)</td><td>1926.93 (+12.82%)</td><td>1679.42 (+4.54%)</td><td>1663.73 (+1.25%)</td><td>1471.30 (+6.12%)</td><td>162.60 <b>(+28.88%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>4.34 (n/a)</td><td>4.08 (n/a)</td><td>4.18 (n/a)</td><td>3.52 (n/a)</td><td>0.32 (n/a)</td><td>2668.20 (n/a)</td><td>2315.36 (n/a)</td><td>2251.30 (n/a)</td><td>2166.00 (n/a)</td><td>200.71 (n/a)</td><td>1707.97 (n/a)</td><td>1606.49 (n/a)</td><td>1643.18 (n/a)</td><td>1386.49 (n/a)</td><td>126.16 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>1.21 (-9.78%)</td><td>1.01 (+5.48%)</td><td>1.06 (+15.31%)</td><td>0.65 (-8.39%)</td><td>0.22 (-17.96%)</td><td>342.00 (+9.16%)</td><td>229.86 (-6.25%)</td><td>207.80 (-13.27%)</td><td>182.40 (+10.88%)</td><td>64.83 (-1.29%)</td><td>51.75 (-9.78%)</td><td>43.17 (+5.48%)</td><td>45.42 (+15.31%)</td><td>27.59 (-8.39%)</td><td>9.50 (-17.96%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>1.34 (n/a)</td><td>0.96 (n/a)</td><td>0.92 (n/a)</td><td>0.71 (n/a)</td><td>0.27 (n/a)</td><td>313.30 (n/a)</td><td>245.18 (n/a)</td><td>239.60 (n/a)</td><td>164.50 (n/a)</td><td>65.68 (n/a)</td><td>57.36 (n/a)</td><td>40.93 (n/a)</td><td>39.39 (n/a)</td><td>30.12 (n/a)</td><td>11.57 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>1.22 (-0.76%)</td><td>1.02 (+4.68%)</td><td>1.02 (+7.08%)</td><td>0.91 <b>(+35.53%)</b></td><td>0.12 <b>(-52.00%)</b></td><td>243.50 <b>(-26.21%)</b></td><td>217.96 (-8.67%)</td><td>217.30 (-6.62%)</td><td>181.00 (+0.72%)</td><td>23.38 <b>(-63.33%)</b></td><td>52.13 (-0.76%)</td><td>43.73 (+4.68%)</td><td>43.42 (+7.08%)</td><td>38.76 <b>(+35.53%)</b></td><td>5.09 <b>(-52.00%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>1.23 (n/a)</td><td>0.98 (n/a)</td><td>0.95 (n/a)</td><td>0.67 (n/a)</td><td>0.25 (n/a)</td><td>330.00 (n/a)</td><td>238.66 (n/a)</td><td>232.70 (n/a)</td><td>179.70 (n/a)</td><td>63.76 (n/a)</td><td>52.52 (n/a)</td><td>41.78 (n/a)</td><td>40.55 (n/a)</td><td>28.60 (n/a)</td><td>10.60 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.52 (+0.71%)</td><td>0.52 (+0.18%)</td><td>0.52 (+0.06%)</td><td>0.52 (+0.08%)</td><td>0.00 <b>(+466.45%)</b></td><td>48463.80 (-0.08%)</td><td>48384.22 (-0.18%)</td><td>48455.10 (-0.06%)</td><td>48086.60 (-0.71%)</td><td>166.44 <b>(+461.67%)</b></td><td>357.27 (+0.71%)</td><td>355.08 (+0.18%)</td><td>354.55 (+0.06%)</td><td>354.49 (+0.08%)</td><td>1.23 <b>(+466.43%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48502.80 (n/a)</td><td>48469.48 (n/a)</td><td>48482.90 (n/a)</td><td>48430.00 (n/a)</td><td>29.63 (n/a)</td><td>354.74 (n/a)</td><td>354.45 (n/a)</td><td>354.35 (n/a)</td><td>354.20 (n/a)</td><td>0.22 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.22 (+0.92%)</td><td>0.21 (+0.41%)</td><td>0.21 (-0.04%)</td><td>0.21 (+1.34%)</td><td>0.00 <b>(-22.38%)</b></td><td>118947.90 (-1.32%)</td><td>118316.16 (-0.41%)</td><td>118527.70 (+0.04%)</td><td>117044.50 (-0.91%)</td><td>757.54 <b>(-24.24%)</b></td><td>146.78 (+0.92%)</td><td>145.21 (+0.41%)</td><td>144.94 (-0.04%)</td><td>144.43 (+1.34%)</td><td>0.94 <b>(-22.38%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>120542.50 (n/a)</td><td>118808.90 (n/a)</td><td>118484.50 (n/a)</td><td>118117.30 (n/a)</td><td>999.90 (n/a)</td><td>145.45 (n/a)</td><td>144.61 (n/a)</td><td>145.00 (n/a)</td><td>142.52 (n/a)</td><td>1.21 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.90 (+0.56%)</td><td>0.89 (+0.58%)</td><td>0.89 (+0.33%)</td><td>0.89 (+1.26%)</td><td>0.00 <b>(-37.61%)</b></td><td>28306.10 (-1.24%)</td><td>28195.72 (-0.58%)</td><td>28234.30 (-0.33%)</td><td>28027.30 (-0.56%)</td><td>119.48 <b>(-38.69%)</b></td><td>612.97 (+0.56%)</td><td>609.32 (+0.58%)</td><td>608.48 (+0.33%)</td><td>606.93 (+1.26%)</td><td>2.59 <b>(-37.61%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28661.60 (n/a)</td><td>28360.88 (n/a)</td><td>28327.10 (n/a)</td><td>28184.60 (n/a)</td><td>194.88 (n/a)</td><td>609.55 (n/a)</td><td>605.78 (n/a)</td><td>606.48 (n/a)</td><td>599.40 (n/a)</td><td>4.15 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>3.54 (-2.42%)</td><td>3.46 (-0.57%)</td><td>3.53 (+0.29%)</td><td>3.34 (+0.06%)</td><td>0.11 (-19.52%)</td><td>7540.20 (-0.05%)</td><td>7281.10 (+0.53%)</td><td>7126.40 (-0.28%)</td><td>7104.80 (+2.48%)</td><td>226.52 (-18.15%)</td><td>2418.07 (-2.42%)</td><td>2361.33 (-0.57%)</td><td>2410.73 (+0.29%)</td><td>2278.45 (+0.06%)</td><td>72.64 (-19.52%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>3.63 (n/a)</td><td>3.48 (n/a)</td><td>3.52 (n/a)</td><td>3.34 (n/a)</td><td>0.13 (n/a)</td><td>7544.30 (n/a)</td><td>7242.62 (n/a)</td><td>7146.70 (n/a)</td><td>6932.70 (n/a)</td><td>276.76 (n/a)</td><td>2478.09 (n/a)</td><td>2374.81 (n/a)</td><td>2403.87 (n/a)</td><td>2277.19 (n/a)</td><td>90.25 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>3.27 (+12.90%)</td><td>2.89 (+2.38%)</td><td>2.82 (+0.07%)</td><td>2.73 (+0.04%)</td><td>0.22 <b>(+233.05%)</b></td><td>9229.00 (-0.04%)</td><td>8745.44 (-1.96%)</td><td>8926.30 (-0.07%)</td><td>7703.50 (-11.43%)</td><td>599.24 <b>(+190.27%)</b></td><td>2230.15 (+12.90%)</td><td>1972.49 (+2.38%)</td><td>1924.63 (+0.07%)</td><td>1861.50 (+0.04%)</td><td>147.03 <b>(+233.05%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>2.89 (n/a)</td><td>2.82 (n/a)</td><td>2.82 (n/a)</td><td>2.73 (n/a)</td><td>0.06 (n/a)</td><td>9232.30 (n/a)</td><td>8920.56 (n/a)</td><td>8932.40 (n/a)</td><td>8697.30 (n/a)</td><td>206.44 (n/a)</td><td>1975.32 (n/a)</td><td>1926.69 (n/a)</td><td>1923.33 (n/a)</td><td>1860.84 (n/a)</td><td>44.15 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>3.30 (-0.98%)</td><td>3.20 (-1.57%)</td><td>3.15 (-3.66%)</td><td>3.14 (-0.77%)</td><td>0.08 (+1.17%)</td><td>8024.20 (+0.77%)</td><td>7870.74 (+1.60%)</td><td>8001.80 (+3.80%)</td><td>7617.30 (+0.99%)</td><td>200.47 (+3.02%)</td><td>2255.37 (-0.98%)</td><td>2183.90 (-1.57%)</td><td>2147.01 (-3.66%)</td><td>2141.02 (-0.77%)</td><td>56.20 (+1.17%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>3.34 (n/a)</td><td>3.25 (n/a)</td><td>3.26 (n/a)</td><td>3.16 (n/a)</td><td>0.08 (n/a)</td><td>7962.70 (n/a)</td><td>7747.12 (n/a)</td><td>7709.00 (n/a)</td><td>7542.80 (n/a)</td><td>194.59 (n/a)</td><td>2277.64 (n/a)</td><td>2218.69 (n/a)</td><td>2228.55 (n/a)</td><td>2157.53 (n/a)</td><td>55.55 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.79 (-0.26%)</td><td>0.79 (-0.05%)</td><td>0.79 (-0.02%)</td><td>0.79 (+0.03%)</td><td>0.00 <b>(-89.06%)</b></td><td>96134.00 (-0.03%)</td><td>96118.50 (+0.05%)</td><td>96116.50 (+0.02%)</td><td>96100.90 (+0.26%)</td><td>13.41 <b>(-89.00%)</b></td><td>715.08 (-0.26%)</td><td>714.95 (-0.05%)</td><td>714.96 (-0.02%)</td><td>714.83 (+0.03%)</td><td>0.10 <b>(-89.06%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>96163.80 (n/a)</td><td>96067.28 (n/a)</td><td>96102.00 (n/a)</td><td>95854.20 (n/a)</td><td>121.94 (n/a)</td><td>716.92 (n/a)</td><td>715.33 (n/a)</td><td>715.07 (n/a)</td><td>714.61 (n/a)</td><td>0.91 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.73 (+0.00%)</td><td>0.73 (-0.00%)</td><td>0.73 (-0.04%)</td><td>0.73 (+0.10%)</td><td>0.00 <b>(-36.46%)</b></td><td>103436.50 (-0.10%)</td><td>103367.56 (+0.00%)</td><td>103376.60 (+0.04%)</td><td>103301.70 (-0.00%)</td><td>63.56 <b>(-36.54%)</b></td><td>665.23 (+0.00%)</td><td>664.81 (-0.00%)</td><td>664.75 (-0.04%)</td><td>664.36 (+0.10%)</td><td>0.41 <b>(-36.45%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103542.70 (n/a)</td><td>103366.20 (n/a)</td><td>103331.60 (n/a)</td><td>103303.50 (n/a)</td><td>100.16 (n/a)</td><td>665.22 (n/a)</td><td>664.82 (n/a)</td><td>665.04 (n/a)</td><td>663.68 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.69 (-0.43%)</td><td>0.69 (-0.43%)</td><td>0.69 (-0.47%)</td><td>0.69 (-0.43%)</td><td>0.00 (+9.53%)</td><td>109388.40 (+0.43%)</td><td>109224.84 (+0.43%)</td><td>109278.50 (+0.48%)</td><td>109008.60 (+0.43%)</td><td>170.18 (+10.47%)</td><td>630.40 (-0.43%)</td><td>629.16 (-0.43%)</td><td>628.85 (-0.47%)</td><td>628.22 (-0.43%)</td><td>0.98 (+9.53%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.70 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>108917.00 (n/a)</td><td>108757.52 (n/a)</td><td>108760.20 (n/a)</td><td>108541.80 (n/a)</td><td>154.04 (n/a)</td><td>633.12 (n/a)</td><td>631.86 (n/a)</td><td>631.84 (n/a)</td><td>630.93 (n/a)</td><td>0.90 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>7.09 (-6.46%)</td><td>6.38 (-9.91%)</td><td>6.51 (-7.36%)</td><td>4.82 <b>(-26.55%)</b></td><td>0.92 <b>(+144.49%)</b></td><td>1850.00 <b>(+36.15%)</b></td><td>1424.20 (+12.97%)</td><td>1368.20 (+7.94%)</td><td>1256.70 (+6.91%)</td><td>244.28 <b>(+261.64%)</b></td><td>427.22 (-6.46%)</td><td>384.54 (-9.91%)</td><td>392.38 (-7.36%)</td><td>290.20 <b>(-26.55%)</b></td><td>55.42 <b>(+144.49%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>7.58 (n/a)</td><td>7.09 (n/a)</td><td>7.03 (n/a)</td><td>6.56 (n/a)</td><td>0.38 (n/a)</td><td>1358.80 (n/a)</td><td>1260.70 (n/a)</td><td>1267.50 (n/a)</td><td>1175.50 (n/a)</td><td>67.55 (n/a)</td><td>456.72 (n/a)</td><td>426.82 (n/a)</td><td>423.55 (n/a)</td><td>395.11 (n/a)</td><td>22.67 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>7.00 (+2.50%)</td><td>6.70 (+0.60%)</td><td>6.74 (+0.81%)</td><td>6.42 (+0.51%)</td><td>0.26 <b>(+51.40%)</b></td><td>1389.10 (-0.52%)</td><td>1331.32 (-0.53%)</td><td>1321.50 (-0.80%)</td><td>1273.10 (-2.44%)</td><td>51.52 <b>(+46.81%)</b></td><td>421.71 (+2.50%)</td><td>403.74 (+0.60%)</td><td>406.26 (+0.81%)</td><td>386.48 (+0.51%)</td><td>15.59 <b>(+51.39%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>6.83 (n/a)</td><td>6.66 (n/a)</td><td>6.69 (n/a)</td><td>6.38 (n/a)</td><td>0.17 (n/a)</td><td>1396.30 (n/a)</td><td>1338.46 (n/a)</td><td>1332.20 (n/a)</td><td>1304.90 (n/a)</td><td>35.09 (n/a)</td><td>411.41 (n/a)</td><td>401.32 (n/a)</td><td>402.98 (n/a)</td><td>384.50 (n/a)</td><td>10.29 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>7.06 (+0.22%)</td><td>6.63 (+6.80%)</td><td>6.56 (+8.51%)</td><td>6.21 (+18.46%)</td><td>0.39 <b>(-47.44%)</b></td><td>1435.80 (-15.59%)</td><td>1347.30 (-7.20%)</td><td>1359.20 (-7.84%)</td><td>1263.20 (-0.22%)</td><td>78.43 <b>(-55.50%)</b></td><td>425.02 (+0.22%)</td><td>399.57 (+6.80%)</td><td>394.98 (+8.51%)</td><td>373.91 (+18.46%)</td><td>23.39 <b>(-47.44%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>7.04 (n/a)</td><td>6.21 (n/a)</td><td>6.04 (n/a)</td><td>5.24 (n/a)</td><td>0.74 (n/a)</td><td>1700.90 (n/a)</td><td>1451.76 (n/a)</td><td>1474.80 (n/a)</td><td>1266.00 (n/a)</td><td>176.24 (n/a)</td><td>424.07 (n/a)</td><td>374.11 (n/a)</td><td>364.02 (n/a)</td><td>315.64 (n/a)</td><td>44.50 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>8.46 (+4.36%)</td><td>7.83 (+0.13%)</td><td>7.90 (-0.18%)</td><td>7.30 (-0.81%)</td><td>0.48 <b>(+61.97%)</b></td><td>4775.10 (+0.82%)</td><td>4466.82 (+0.05%)</td><td>4410.90 (+0.18%)</td><td>4121.20 (-4.18%)</td><td>271.24 <b>(+57.13%)</b></td><td>521.08 (+4.36%)</td><td>482.19 (+0.13%)</td><td>486.86 (-0.18%)</td><td>449.73 (-0.81%)</td><td>29.39 <b>(+61.97%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>8.11 (n/a)</td><td>7.82 (n/a)</td><td>7.92 (n/a)</td><td>7.36 (n/a)</td><td>0.29 (n/a)</td><td>4736.30 (n/a)</td><td>4464.74 (n/a)</td><td>4403.00 (n/a)</td><td>4301.10 (n/a)</td><td>172.62 (n/a)</td><td>499.29 (n/a)</td><td>481.55 (n/a)</td><td>487.73 (n/a)</td><td>453.41 (n/a)</td><td>18.15 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>7.60 (+0.66%)</td><td>7.42 (+0.47%)</td><td>7.58 (+0.66%)</td><td>6.77 (-4.81%)</td><td>0.36 <b>(+65.93%)</b></td><td>5147.60 (+5.06%)</td><td>4706.98 (-0.33%)</td><td>4598.70 (-0.66%)</td><td>4585.00 (-0.66%)</td><td>246.44 <b>(+74.06%)</b></td><td>468.38 (+0.66%)</td><td>457.17 (+0.47%)</td><td>466.98 (+0.66%)</td><td>417.18 (-4.81%)</td><td>22.37 <b>(+65.93%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>7.55 (n/a)</td><td>7.39 (n/a)</td><td>7.53 (n/a)</td><td>7.12 (n/a)</td><td>0.22 (n/a)</td><td>4899.90 (n/a)</td><td>4722.68 (n/a)</td><td>4629.20 (n/a)</td><td>4615.30 (n/a)</td><td>141.58 (n/a)</td><td>465.30 (n/a)</td><td>455.04 (n/a)</td><td>463.90 (n/a)</td><td>438.27 (n/a)</td><td>13.48 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>7.76 (+2.19%)</td><td>7.18 (+2.68%)</td><td>7.30 (+5.72%)</td><td>6.69 (+6.11%)</td><td>0.44 (-19.41%)</td><td>5211.90 (-5.76%)</td><td>4873.68 (-2.80%)</td><td>4776.80 (-5.41%)</td><td>4493.90 (-2.14%)</td><td>299.36 <b>(-24.28%)</b></td><td>477.87 (+2.19%)</td><td>441.96 (+2.68%)</td><td>449.56 (+5.72%)</td><td>412.04 (+6.11%)</td><td>27.21 (-19.41%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>7.59 (n/a)</td><td>6.99 (n/a)</td><td>6.90 (n/a)</td><td>6.30 (n/a)</td><td>0.55 (n/a)</td><td>5530.40 (n/a)</td><td>5014.06 (n/a)</td><td>5049.80 (n/a)</td><td>4592.20 (n/a)</td><td>395.33 (n/a)</td><td>467.64 (n/a)</td><td>430.42 (n/a)</td><td>425.26 (n/a)</td><td>388.30 (n/a)</td><td>33.76 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.79 (+0.32%)</td><td>0.79 (+0.04%)</td><td>0.79 (-0.02%)</td><td>0.79 (-0.08%)</td><td>0.00 <b>(+176.75%)</b></td><td>95600.40 (+0.08%)</td><td>95385.12 (-0.04%)</td><td>95410.50 (+0.02%)</td><td>95048.70 (-0.32%)</td><td>203.77 <b>(+176.02%)</b></td><td>722.99 (+0.32%)</td><td>720.44 (+0.04%)</td><td>720.25 (-0.02%)</td><td>718.82 (-0.08%)</td><td>1.54 <b>(+176.75%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95525.90 (n/a)</td><td>95420.38 (n/a)</td><td>95389.00 (n/a)</td><td>95350.60 (n/a)</td><td>73.82 (n/a)</td><td>720.70 (n/a)</td><td>720.18 (n/a)</td><td>720.41 (n/a)</td><td>719.38 (n/a)</td><td>0.56 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.74 (+0.01%)</td><td>0.74 (+0.04%)</td><td>0.74 (+0.05%)</td><td>0.73 (+0.09%)</td><td>0.00 <b>(-23.89%)</b></td><td>102729.60 (-0.09%)</td><td>102627.74 (-0.04%)</td><td>102583.20 (-0.05%)</td><td>102569.00 (-0.00%)</td><td>73.36 <b>(-23.97%)</b></td><td>669.98 (+0.01%)</td><td>669.60 (+0.04%)</td><td>669.89 (+0.05%)</td><td>668.94 (+0.09%)</td><td>0.48 <b>(-23.89%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>102817.60 (n/a)</td><td>102672.56 (n/a)</td><td>102638.60 (n/a)</td><td>102574.10 (n/a)</td><td>96.49 (n/a)</td><td>669.95 (n/a)</td><td>669.31 (n/a)</td><td>669.53 (n/a)</td><td>668.36 (n/a)</td><td>0.63 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.70 (-0.24%)</td><td>0.70 (-0.06%)</td><td>0.70 (-0.14%)</td><td>0.70 (+0.11%)</td><td>0.00 <b>(-49.05%)</b></td><td>107659.20 (-0.11%)</td><td>107410.94 (+0.05%)</td><td>107362.30 (+0.14%)</td><td>107258.60 (+0.24%)</td><td>159.98 <b>(-49.00%)</b></td><td>640.69 (-0.24%)</td><td>639.78 (-0.06%)</td><td>640.07 (-0.14%)</td><td>638.31 (+0.11%)</td><td>0.95 <b>(-49.05%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.71 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>107776.80 (n/a)</td><td>107352.14 (n/a)</td><td>107213.40 (n/a)</td><td>107004.80 (n/a)</td><td>313.66 (n/a)</td><td>642.21 (n/a)</td><td>640.14 (n/a)</td><td>640.96 (n/a)</td><td>637.61 (n/a)</td><td>1.87 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>4.24 (+16.67%)</td><td>3.79 (+12.86%)</td><td>3.92 (+9.05%)</td><td>2.90 (-2.27%)</td><td>0.52 <b>(+49.48%)</b></td><td>2782.80 (+2.32%)</td><td>2163.82 (-10.59%)</td><td>2055.60 (-8.30%)</td><td>1899.20 (-14.29%)</td><td>352.18 <b>(+35.60%)</b></td><td>1113.06 (+16.67%)</td><td>994.61 (+12.86%)</td><td>1028.39 (+9.05%)</td><td>759.65 (-2.27%)</td><td>136.05 <b>(+49.48%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>3.64 (n/a)</td><td>3.36 (n/a)</td><td>3.60 (n/a)</td><td>2.96 (n/a)</td><td>0.35 (n/a)</td><td>2719.70 (n/a)</td><td>2420.08 (n/a)</td><td>2241.70 (n/a)</td><td>2215.90 (n/a)</td><td>259.72 (n/a)</td><td>954.00 (n/a)</td><td>881.31 (n/a)</td><td>943.00 (n/a)</td><td>777.27 (n/a)</td><td>91.02 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.50 (+15.91%)</td><td>0.35 (+3.63%)</td><td>0.32 (-1.16%)</td><td>0.29 (-1.61%)</td><td>0.08 <b>(+57.02%)</b></td><td>4348.20 (+1.63%)</td><td>3672.48 (-1.62%)</td><td>3837.00 (+1.17%)</td><td>2488.20 (-13.72%)</td><td>699.18 <b>(+35.06%)</b></td><td>26.97 (+15.91%)</td><td>18.96 (+3.63%)</td><td>17.49 (-1.16%)</td><td>15.43 (-1.61%)</td><td>4.57 <b>(+57.02%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.43 (n/a)</td><td>0.34 (n/a)</td><td>0.33 (n/a)</td><td>0.29 (n/a)</td><td>0.05 (n/a)</td><td>4278.30 (n/a)</td><td>3732.78 (n/a)</td><td>3792.50 (n/a)</td><td>2884.00 (n/a)</td><td>517.67 (n/a)</td><td>23.27 (n/a)</td><td>18.30 (n/a)</td><td>17.70 (n/a)</td><td>15.69 (n/a)</td><td>2.91 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>6.44 <b>(+30.97%)</b></td><td>4.60 (+14.26%)</td><td>4.75 <b>(+29.78%)</b></td><td>3.26 (+3.25%)</td><td>1.24 <b>(+59.01%)</b></td><td>2037.80 (-3.15%)</td><td>1529.48 (-10.09%)</td><td>1400.20 <b>(-22.95%)</b></td><td>1032.80 <b>(-23.65%)</b></td><td>398.60 <b>(+23.56%)</b></td><td>1989.93 <b>(+30.97%)</b></td><td>1422.04 (+14.26%)</td><td>1467.78 <b>(+29.78%)</b></td><td>1008.52 (+3.25%)</td><td>383.93 <b>(+59.01%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>4.92 (n/a)</td><td>4.03 (n/a)</td><td>3.66 (n/a)</td><td>3.16 (n/a)</td><td>0.78 (n/a)</td><td>2104.10 (n/a)</td><td>1701.08 (n/a)</td><td>1817.20 (n/a)</td><td>1352.70 (n/a)</td><td>322.60 (n/a)</td><td>1519.33 (n/a)</td><td>1244.60 (n/a)</td><td>1130.96 (n/a)</td><td>976.77 (n/a)</td><td>241.45 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>13.40 (n/a)</td><td>12.76 (n/a)</td><td>13.18 (n/a)</td><td>10.77 (n/a)</td><td>1.12 (n/a)</td><td>13.39 (n/a)</td><td>12.76 (n/a)</td><td>13.17 (n/a)</td><td>10.76 (n/a)</td><td>1.12 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>25.13 (+0.36%)</td><td>24.53 (+0.70%)</td><td>24.55 (+0.38%)</td><td>24.04 (+2.88%)</td><td>0.40 <b>(-43.64%)</b></td><td>25.11 (+0.36%)</td><td>24.52 (+0.70%)</td><td>24.53 (+0.38%)</td><td>24.02 (+2.88%)</td><td>0.40 <b>(-43.64%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>25.04 (n/a)</td><td>24.36 (n/a)</td><td>24.46 (n/a)</td><td>23.36 (n/a)</td><td>0.70 (n/a)</td><td>25.02 (n/a)</td><td>24.35 (n/a)</td><td>24.44 (n/a)</td><td>23.35 (n/a)</td><td>0.70 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>40.73 (-5.64%)</td><td>39.81 (-2.83%)</td><td>39.94 (-1.99%)</td><td>38.66 (-0.11%)</td><td>0.74 <b>(-55.46%)</b></td><td>40.71 (-5.64%)</td><td>39.79 (-2.83%)</td><td>39.92 (-1.99%)</td><td>38.64 (-0.11%)</td><td>0.74 <b>(-55.46%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>43.17 (n/a)</td><td>40.98 (n/a)</td><td>40.76 (n/a)</td><td>38.70 (n/a)</td><td>1.67 (n/a)</td><td>43.14 (n/a)</td><td>40.95 (n/a)</td><td>40.73 (n/a)</td><td>38.68 (n/a)</td><td>1.67 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>44.58 (-0.78%)</td><td>43.13 (+0.09%)</td><td>43.00 (-0.29%)</td><td>42.20 (+0.25%)</td><td>0.89 <b>(-23.73%)</b></td><td>44.55 (-0.78%)</td><td>43.11 (+0.09%)</td><td>42.97 (-0.29%)</td><td>42.17 (+0.25%)</td><td>0.88 <b>(-23.73%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>44.93 (n/a)</td><td>43.10 (n/a)</td><td>43.12 (n/a)</td><td>42.09 (n/a)</td><td>1.16 (n/a)</td><td>44.90 (n/a)</td><td>43.07 (n/a)</td><td>43.09 (n/a)</td><td>42.06 (n/a)</td><td>1.16 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>13.37 (n/a)</td><td>12.61 (n/a)</td><td>12.43 (n/a)</td><td>12.30 (n/a)</td><td>0.44 (n/a)</td><td>13.36 (n/a)</td><td>12.60 (n/a)</td><td>12.42 (n/a)</td><td>12.29 (n/a)</td><td>0.44 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>25.16 (+2.71%)</td><td>24.31 (+1.73%)</td><td>24.29 (+1.20%)</td><td>23.59 (+3.51%)</td><td>0.56 (-14.09%)</td><td>25.14 (+2.71%)</td><td>24.29 (+1.73%)</td><td>24.28 (+1.20%)</td><td>23.57 (+3.51%)</td><td>0.56 (-14.09%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>24.49 (n/a)</td><td>23.89 (n/a)</td><td>24.01 (n/a)</td><td>22.79 (n/a)</td><td>0.65 (n/a)</td><td>24.48 (n/a)</td><td>23.88 (n/a)</td><td>23.99 (n/a)</td><td>22.77 (n/a)</td><td>0.65 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>40.15 (-1.90%)</td><td>39.48 (+1.12%)</td><td>39.79 (-0.86%)</td><td>38.00 (+11.62%)</td><td>0.88 <b>(-69.02%)</b></td><td>40.13 (-1.90%)</td><td>39.46 (+1.12%)</td><td>39.77 (-0.86%)</td><td>37.97 (+11.62%)</td><td>0.88 <b>(-69.02%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>40.93 (n/a)</td><td>39.05 (n/a)</td><td>40.14 (n/a)</td><td>34.04 (n/a)</td><td>2.85 (n/a)</td><td>40.90 (n/a)</td><td>39.02 (n/a)</td><td>40.11 (n/a)</td><td>34.02 (n/a)</td><td>2.85 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>45.19 (-0.78%)</td><td>42.94 (-1.96%)</td><td>42.43 (-3.40%)</td><td>41.50 (-0.62%)</td><td>1.55 (+13.48%)</td><td>45.17 (-0.78%)</td><td>42.91 (-1.96%)</td><td>42.40 (-3.40%)</td><td>41.48 (-0.62%)</td><td>1.55 (+13.48%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>45.55 (n/a)</td><td>43.80 (n/a)</td><td>43.92 (n/a)</td><td>41.76 (n/a)</td><td>1.36 (n/a)</td><td>45.52 (n/a)</td><td>43.77 (n/a)</td><td>43.90 (n/a)</td><td>41.74 (n/a)</td><td>1.36 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>9.52 (-3.19%)</td><td>8.60 (-1.40%)</td><td>8.54 (+1.51%)</td><td>7.88 (-1.16%)</td><td>0.60 <b>(-29.58%)</b></td><td>9.51 (-3.19%)</td><td>8.58 (-1.40%)</td><td>8.52 (+1.51%)</td><td>7.87 (-1.16%)</td><td>0.59 <b>(-29.58%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>9.84 (n/a)</td><td>8.72 (n/a)</td><td>8.41 (n/a)</td><td>7.97 (n/a)</td><td>0.85 (n/a)</td><td>9.82 (n/a)</td><td>8.71 (n/a)</td><td>8.39 (n/a)</td><td>7.96 (n/a)</td><td>0.84 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.98 (-0.53%)</td><td>0.89 (+2.13%)</td><td>0.89 (-3.43%)</td><td>0.80 (+7.68%)</td><td>0.06 <b>(-44.70%)</b></td><td>0.96 (-0.53%)</td><td>0.88 (+2.13%)</td><td>0.87 (-3.43%)</td><td>0.79 (+7.68%)</td><td>0.06 <b>(-44.70%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.98 (n/a)</td><td>0.87 (n/a)</td><td>0.92 (n/a)</td><td>0.74 (n/a)</td><td>0.12 (n/a)</td><td>0.97 (n/a)</td><td>0.86 (n/a)</td><td>0.90 (n/a)</td><td>0.73 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>1.39 (-7.77%)</td><td>1.14 (+0.34%)</td><td>1.05 (-0.34%)</td><td>0.96 (+16.32%)</td><td>0.19 <b>(-26.74%)</b></td><td>1.37 (-7.77%)</td><td>1.13 (+0.34%)</td><td>1.04 (-0.34%)</td><td>0.95 (+16.32%)</td><td>0.19 <b>(-26.74%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>1.51 (n/a)</td><td>1.14 (n/a)</td><td>1.05 (n/a)</td><td>0.83 (n/a)</td><td>0.26 (n/a)</td><td>1.49 (n/a)</td><td>1.13 (n/a)</td><td>1.04 (n/a)</td><td>0.82 (n/a)</td><td>0.26 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>18.37 (-0.17%)</td><td>16.02 (-4.04%)</td><td>15.66 (-7.38%)</td><td>13.94 (-1.95%)</td><td>1.91 (+14.41%)</td><td>18.16 (-0.17%)</td><td>15.84 (-4.04%)</td><td>15.48 (-7.38%)</td><td>13.78 (-1.95%)</td><td>1.89 (+14.41%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>18.40 (n/a)</td><td>16.70 (n/a)</td><td>16.91 (n/a)</td><td>14.22 (n/a)</td><td>1.67 (n/a)</td><td>18.19 (n/a)</td><td>16.50 (n/a)</td><td>16.71 (n/a)</td><td>14.05 (n/a)</td><td>1.65 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>13.70 (-0.00%)</td><td>12.20 (-7.06%)</td><td>13.20 (-0.60%)</td><td>7.53 <b>(-39.87%)</b></td><td>2.62 <b>(+366.67%)</b></td><td>13.46 (-0.00%)</td><td>11.98 (-7.06%)</td><td>12.97 (-0.60%)</td><td>7.40 <b>(-39.87%)</b></td><td>2.57 <b>(+366.67%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>13.70 (n/a)</td><td>13.12 (n/a)</td><td>13.28 (n/a)</td><td>12.52 (n/a)</td><td>0.56 (n/a)</td><td>13.46 (n/a)</td><td>12.89 (n/a)</td><td>13.05 (n/a)</td><td>12.30 (n/a)</td><td>0.55 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>9.28 (+13.24%)</td><td>8.14 (+11.96%)</td><td>7.93 (+10.01%)</td><td>7.39 (+17.95%)</td><td>0.79 (+11.82%)</td><td>9.12 (+13.24%)</td><td>8.00 (+11.96%)</td><td>7.79 (+10.01%)</td><td>7.26 (+17.95%)</td><td>0.78 (+11.82%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>8.19 (n/a)</td><td>7.27 (n/a)</td><td>7.21 (n/a)</td><td>6.26 (n/a)</td><td>0.71 (n/a)</td><td>8.05 (n/a)</td><td>7.14 (n/a)</td><td>7.08 (n/a)</td><td>6.15 (n/a)</td><td>0.70 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>6.42 (-7.96%)</td><td>5.64 (+4.48%)</td><td>5.38 (+2.18%)</td><td>4.94 (+13.41%)</td><td>0.62 <b>(-43.91%)</b></td><td>6.32 (-7.96%)</td><td>5.55 (+4.48%)</td><td>5.30 (+2.18%)</td><td>4.86 (+13.41%)</td><td>0.61 <b>(-43.91%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>6.98 (n/a)</td><td>5.40 (n/a)</td><td>5.27 (n/a)</td><td>4.36 (n/a)</td><td>1.10 (n/a)</td><td>6.86 (n/a)</td><td>5.31 (n/a)</td><td>5.18 (n/a)</td><td>4.29 (n/a)</td><td>1.09 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>13.25 (n/a)</td><td>12.47 (n/a)</td><td>12.64 (n/a)</td><td>11.13 (n/a)</td><td>0.88 (n/a)</td><td>13.24 (n/a)</td><td>12.46 (n/a)</td><td>12.63 (n/a)</td><td>11.12 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>13.32 (n/a)</td><td>12.01 (n/a)</td><td>12.26 (n/a)</td><td>10.54 (n/a)</td><td>1.26 (n/a)</td><td>13.32 (n/a)</td><td>12.00 (n/a)</td><td>12.25 (n/a)</td><td>10.53 (n/a)</td><td>1.26 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>195.40 (n/a)</td><td>165.80 (n/a)</td><td>162.50 (n/a)</td><td>129.30 (n/a)</td><td>28.00 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>221.50 (n/a)</td><td>175.70 (n/a)</td><td>186.00 (n/a)</td><td>130.00 (n/a)</td><td>42.17 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>209.20 (n/a)</td><td>150.38 (n/a)</td><td>135.60 (n/a)</td><td>125.10 (n/a)</td><td>34.54 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>208.90 (n/a)</td><td>157.68 (n/a)</td><td>148.80 (n/a)</td><td>128.40 (n/a)</td><td>32.20 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>162.90 (n/a)</td><td>150.36 (n/a)</td><td>154.60 (n/a)</td><td>134.10 (n/a)</td><td>11.04 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>177.70 (n/a)</td><td>163.66 (n/a)</td><td>167.10 (n/a)</td><td>131.50 (n/a)</td><td>18.77 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>170.50 (n/a)</td><td>160.34 (n/a)</td><td>156.40 (n/a)</td><td>152.30 (n/a)</td><td>8.00 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>319.30 (n/a)</td><td>256.62 (n/a)</td><td>230.30 (n/a)</td><td>203.70 (n/a)</td><td>53.91 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.70 (n/a)</td><td>176.62 (n/a)</td><td>174.90 (n/a)</td><td>143.90 (n/a)</td><td>29.03 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.00 (n/a)</td><td>169.14 (n/a)</td><td>170.10 (n/a)</td><td>131.60 (n/a)</td><td>23.75 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.90 (n/a)</td><td>167.94 (n/a)</td><td>170.40 (n/a)</td><td>122.70 (n/a)</td><td>30.58 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>176.30 (n/a)</td><td>147.98 (n/a)</td><td>153.30 (n/a)</td><td>121.00 (n/a)</td><td>24.46 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.80 (n/a)</td><td>178.00 (n/a)</td><td>176.20 (n/a)</td><td>130.30 (n/a)</td><td>32.10 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>353.00 (n/a)</td><td>232.48 (n/a)</td><td>223.00 (n/a)</td><td>179.70 (n/a)</td><td>70.61 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>256.10 (n/a)</td><td>212.44 (n/a)</td><td>215.40 (n/a)</td><td>149.90 (n/a)</td><td>39.27 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>263.10 (n/a)</td><td>222.36 (n/a)</td><td>213.30 (n/a)</td><td>199.10 (n/a)</td><td>25.96 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>184.60 (n/a)</td><td>152.82 (n/a)</td><td>157.60 (n/a)</td><td>109.20 (n/a)</td><td>33.17 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>185.10 (n/a)</td><td>147.50 (n/a)</td><td>153.10 (n/a)</td><td>105.80 (n/a)</td><td>33.58 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.00 (n/a)</td><td>192.90 (n/a)</td><td>183.10 (n/a)</td><td>180.80 (n/a)</td><td>174.80 (n/a)</td><td>8.87 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>193.40 (n/a)</td><td>166.90 (n/a)</td><td>179.90 (n/a)</td><td>115.40 (n/a)</td><td>30.54 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>253.30 (n/a)</td><td>185.48 (n/a)</td><td>177.10 (n/a)</td><td>153.90 (n/a)</td><td>39.24 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>295.10 (n/a)</td><td>194.40 (n/a)</td><td>169.70 (n/a)</td><td>150.30 (n/a)</td><td>60.78 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>250.50 (n/a)</td><td>186.44 (n/a)</td><td>181.10 (n/a)</td><td>155.60 (n/a)</td><td>38.56 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>285.50 (n/a)</td><td>219.82 (n/a)</td><td>218.90 (n/a)</td><td>177.60 (n/a)</td><td>40.76 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>236.80 (n/a)</td><td>174.14 (n/a)</td><td>163.90 (n/a)</td><td>136.30 (n/a)</td><td>39.53 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>217.80 (n/a)</td><td>167.08 (n/a)</td><td>167.20 (n/a)</td><td>129.00 (n/a)</td><td>36.52 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>180.80 (n/a)</td><td>162.88 (n/a)</td><td>166.20 (n/a)</td><td>139.70 (n/a)</td><td>17.04 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>216.80 (n/a)</td><td>168.56 (n/a)</td><td>154.40 (n/a)</td><td>140.00 (n/a)</td><td>33.19 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>180.50 (n/a)</td><td>157.20 (n/a)</td><td>169.70 (n/a)</td><td>125.20 (n/a)</td><td>24.88 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>203.80 (n/a)</td><td>187.16 (n/a)</td><td>186.50 (n/a)</td><td>168.40 (n/a)</td><td>12.78 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>266.30 (n/a)</td><td>199.76 (n/a)</td><td>192.70 (n/a)</td><td>160.60 (n/a)</td><td>39.91 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>301.40 (n/a)</td><td>238.44 (n/a)</td><td>232.70 (n/a)</td><td>204.90 (n/a)</td><td>37.42 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (-6.11%)</td><td>0.02 (-11.44%)</td><td>0.02 (-8.66%)</td><td>0.02 (-13.71%)</td><td>0.00 <b>(+20.91%)</b></td><td>228.70 (+15.86%)</td><td>186.62 (+14.49%)</td><td>177.70 (+9.49%)</td><td>140.10 (+6.54%)</td><td>35.86 <b>(+51.71%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>197.40 (n/a)</td><td>163.00 (n/a)</td><td>162.30 (n/a)</td><td>131.50 (n/a)</td><td>23.64 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (+14.94%)</td><td>0.02 (-0.23%)</td><td>0.02 (-0.04%)</td><td>0.02 (-10.81%)</td><td>0.01 <b>(+74.20%)</b></td><td>221.30 (+12.11%)</td><td>185.14 (+2.67%)</td><td>190.40 (+0.05%)</td><td>126.50 (-13.00%)</td><td>36.20 <b>(+63.05%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>197.40 (n/a)</td><td>180.32 (n/a)</td><td>190.30 (n/a)</td><td>145.40 (n/a)</td><td>22.20 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (+2.19%)</td><td>0.03 (+4.11%)</td><td>0.02 (+1.29%)</td><td>0.02 (+8.29%)</td><td>0.01 (-7.56%)</td><td>180.70 (-7.66%)</td><td>151.02 (-4.76%)</td><td>164.30 (-1.26%)</td><td>114.20 (-2.14%)</td><td>27.83 (-16.73%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>195.70 (n/a)</td><td>158.56 (n/a)</td><td>166.40 (n/a)</td><td>116.70 (n/a)</td><td>33.42 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 <b>(-25.61%)</b></td><td>0.02 (-3.90%)</td><td>0.02 (-1.14%)</td><td>0.02 (+9.91%)</td><td>0.00 <b>(-47.34%)</b></td><td>219.20 (-9.01%)</td><td>182.38 (-1.42%)</td><td>193.40 (+1.15%)</td><td>137.80 <b>(+34.44%)</b></td><td>35.43 <b>(-31.94%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>240.90 (n/a)</td><td>185.00 (n/a)</td><td>191.20 (n/a)</td><td>102.50 (n/a)</td><td>52.06 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (-0.42%)</td><td>0.03 (+16.31%)</td><td>0.02 (+5.40%)</td><td>0.02 <b>(+73.84%)</b></td><td>0.00 <b>(-51.19%)</b></td><td>185.80 <b>(-42.46%)</b></td><td>165.22 (-19.39%)</td><td>172.10 (-5.13%)</td><td>142.60 (+0.42%)</td><td>18.47 <b>(-73.48%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>322.90 (n/a)</td><td>204.96 (n/a)</td><td>181.40 (n/a)</td><td>142.00 (n/a)</td><td>69.63 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (+2.22%)</td><td>0.02 (+5.14%)</td><td>0.02 (+14.98%)</td><td>0.02 (-0.55%)</td><td>0.00 (+8.24%)</td><td>219.60 (+0.55%)</td><td>183.76 (-4.58%)</td><td>177.20 (-13.01%)</td><td>146.50 (-2.20%)</td><td>29.21 (+9.84%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.40 (n/a)</td><td>192.58 (n/a)</td><td>203.70 (n/a)</td><td>149.80 (n/a)</td><td>26.60 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (+2.93%)</td><td>0.02 (+5.93%)</td><td>0.02 (+5.45%)</td><td>0.02 <b>(+22.43%)</b></td><td>0.01 (-12.75%)</td><td>253.80 (-18.34%)</td><td>191.54 (-8.26%)</td><td>188.10 (-5.14%)</td><td>133.50 (-2.84%)</td><td>43.52 <b>(-32.81%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>310.80 (n/a)</td><td>208.78 (n/a)</td><td>198.30 (n/a)</td><td>137.40 (n/a)</td><td>64.78 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.02 (-9.46%)</td><td>0.02 (-15.14%)</td><td>0.02 (-3.53%)</td><td>0.01 <b>(-22.98%)</b></td><td>0.00 (+13.59%)</td><td>299.10 <b>(+29.82%)</b></td><td>246.82 (+19.36%)</td><td>232.20 (+3.66%)</td><td>190.20 (+10.45%)</td><td>45.60 <b>(+66.06%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>230.40 (n/a)</td><td>206.78 (n/a)</td><td>224.00 (n/a)</td><td>172.20 (n/a)</td><td>27.46 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (+3.21%)</td><td>0.05 (+12.24%)</td><td>0.05 (+15.12%)</td><td>0.04 (+11.83%)</td><td>0.01 (-12.11%)</td><td>189.30 (-10.58%)</td><td>167.48 (-11.33%)</td><td>162.70 (-13.13%)</td><td>145.80 (-3.12%)</td><td>18.99 <b>(-22.58%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.70 (n/a)</td><td>188.88 (n/a)</td><td>187.30 (n/a)</td><td>150.50 (n/a)</td><td>24.52 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (-15.67%)</td><td>0.05 (-12.70%)</td><td>0.05 (-17.38%)</td><td>0.03 (-7.19%)</td><td>0.01 <b>(-29.40%)</b></td><td>244.70 (+7.75%)</td><td>184.38 (+12.52%)</td><td>180.60 <b>(+21.05%)</b></td><td>143.70 (+18.56%)</td><td>38.36 (-9.60%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.10 (n/a)</td><td>163.86 (n/a)</td><td>149.20 (n/a)</td><td>121.20 (n/a)</td><td>42.44 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (+0.08%)</td><td>0.05 (-1.21%)</td><td>0.05 (-1.22%)</td><td>0.03 (-12.65%)</td><td>0.01 (+16.38%)</td><td>238.70 (+14.48%)</td><td>172.24 (+2.72%)</td><td>161.20 (+1.26%)</td><td>130.40 (-0.08%)</td><td>41.45 <b>(+34.95%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.50 (n/a)</td><td>167.68 (n/a)</td><td>159.20 (n/a)</td><td>130.50 (n/a)</td><td>30.71 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (+2.25%)</td><td>0.05 (+7.06%)</td><td>0.05 (+0.84%)</td><td>0.04 <b>(+26.31%)</b></td><td>0.01 (-15.23%)</td><td>188.30 <b>(-20.85%)</b></td><td>162.00 (-8.42%)</td><td>174.20 (-0.80%)</td><td>121.90 (-2.17%)</td><td>28.16 <b>(-33.91%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.90 (n/a)</td><td>176.90 (n/a)</td><td>175.60 (n/a)</td><td>124.60 (n/a)</td><td>42.61 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 <b>(+22.89%)</b></td><td>0.05 (+1.32%)</td><td>0.04 (-3.36%)</td><td>0.04 (-3.95%)</td><td>0.01 <b>(+183.23%)</b></td><td>207.30 (+4.12%)</td><td>181.32 (+0.60%)</td><td>184.30 (+3.48%)</td><td>134.80 (-18.60%)</td><td>27.90 <b>(+130.79%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>199.10 (n/a)</td><td>180.24 (n/a)</td><td>178.10 (n/a)</td><td>165.60 (n/a)</td><td>12.09 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (+10.79%)</td><td>0.05 (+1.24%)</td><td>0.05 (+5.56%)</td><td>0.04 (-6.44%)</td><td>0.01 <b>(+79.02%)</b></td><td>194.90 (+6.91%)</td><td>169.30 (-0.08%)</td><td>167.00 (-5.28%)</td><td>133.50 (-9.74%)</td><td>23.59 <b>(+72.15%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>182.30 (n/a)</td><td>169.44 (n/a)</td><td>176.30 (n/a)</td><td>147.90 (n/a)</td><td>13.70 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (-14.92%)</td><td>0.05 (-7.88%)</td><td>0.04 (-16.10%)</td><td>0.04 <b>(+20.62%)</b></td><td>0.01 <b>(-46.51%)</b></td><td>200.80 (-17.09%)</td><td>177.48 (+4.06%)</td><td>188.20 (+19.19%)</td><td>140.50 (+17.57%)</td><td>24.48 <b>(-48.78%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>242.20 (n/a)</td><td>170.56 (n/a)</td><td>157.90 (n/a)</td><td>119.50 (n/a)</td><td>47.81 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (+15.76%)</td><td>0.05 (+12.60%)</td><td>0.04 (-8.72%)</td><td>0.04 <b>(+23.12%)</b></td><td>0.01 (-4.65%)</td><td>210.30 (-18.77%)</td><td>180.90 (-12.35%)</td><td>194.00 (+9.54%)</td><td>145.50 (-13.65%)</td><td>29.18 <b>(-34.46%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>258.90 (n/a)</td><td>206.38 (n/a)</td><td>177.10 (n/a)</td><td>168.50 (n/a)</td><td>44.51 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 <b>(+35.86%)</b></td><td>0.05 (+15.35%)</td><td>0.05 (+17.94%)</td><td>0.04 (-4.97%)</td><td>0.01 <b>(+401.47%)</b></td><td>219.80 (+5.27%)</td><td>176.68 (-11.18%)</td><td>168.10 (-15.19%)</td><td>140.50 <b>(-26.40%)</b></td><td>31.76 <b>(+294.18%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>208.80 (n/a)</td><td>198.92 (n/a)</td><td>198.20 (n/a)</td><td>190.90 (n/a)</td><td>8.06 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (-6.10%)</td><td>0.03 (-7.76%)</td><td>0.04 (-0.76%)</td><td>0.03 (-16.52%)</td><td>0.01 <b>(+24.50%)</b></td><td>289.30 (+19.79%)</td><td>243.90 (+9.83%)</td><td>232.80 (+0.74%)</td><td>190.00 (+6.50%)</td><td>42.92 <b>(+65.48%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>241.50 (n/a)</td><td>222.08 (n/a)</td><td>231.10 (n/a)</td><td>178.40 (n/a)</td><td>25.94 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 <b>(+20.18%)</b></td><td>0.11 (+16.16%)</td><td>0.10 (+6.81%)</td><td>0.09 <b>(+32.91%)</b></td><td>0.02 (+5.07%)</td><td>192.70 <b>(-24.79%)</b></td><td>157.86 (-14.85%)</td><td>158.70 (-6.37%)</td><td>127.10 (-16.82%)</td><td>25.49 <b>(-37.37%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>256.20 (n/a)</td><td>185.38 (n/a)</td><td>169.50 (n/a)</td><td>152.80 (n/a)</td><td>40.70 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 <b>(+26.01%)</b></td><td>0.11 (+19.95%)</td><td>0.10 (+7.69%)</td><td>0.09 <b>(+67.08%)</b></td><td>0.02 (-10.83%)</td><td>184.60 <b>(-40.16%)</b></td><td>157.26 (-19.72%)</td><td>160.10 (-7.13%)</td><td>126.70 <b>(-20.61%)</b></td><td>25.84 <b>(-59.10%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>308.50 (n/a)</td><td>195.90 (n/a)</td><td>172.40 (n/a)</td><td>159.60 (n/a)</td><td>63.18 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (+11.41%)</td><td>0.09 (+10.60%)</td><td>0.10 <b>(+31.15%)</b></td><td>0.06 (-3.29%)</td><td>0.02 <b>(+43.34%)</b></td><td>281.90 (+3.37%)</td><td>194.96 (-7.19%)</td><td>160.40 <b>(-23.76%)</b></td><td>153.50 (-10.29%)</td><td>55.52 <b>(+33.62%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>272.70 (n/a)</td><td>210.06 (n/a)</td><td>210.40 (n/a)</td><td>171.10 (n/a)</td><td>41.55 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.10 (-10.53%)</td><td>0.08 (-9.70%)</td><td>0.09 (-4.81%)</td><td>0.06 (-9.03%)</td><td>0.02 (-4.28%)</td><td>283.80 (+9.96%)</td><td>205.84 (+11.08%)</td><td>182.50 (+5.01%)</td><td>164.10 (+11.78%)</td><td>48.30 (+13.77%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>258.10 (n/a)</td><td>185.30 (n/a)</td><td>173.80 (n/a)</td><td>146.80 (n/a)</td><td>42.45 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 (+7.32%)</td><td>0.10 (+9.34%)</td><td>0.10 (+14.67%)</td><td>0.08 (+12.66%)</td><td>0.02 (-4.08%)</td><td>209.10 (-11.25%)</td><td>162.02 (-9.33%)</td><td>157.30 (-12.80%)</td><td>122.90 (-6.82%)</td><td>30.87 <b>(-20.30%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>235.60 (n/a)</td><td>178.70 (n/a)</td><td>180.40 (n/a)</td><td>131.90 (n/a)</td><td>38.73 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.12 (-19.39%)</td><td>0.10 (+0.77%)</td><td>0.09 (+1.70%)</td><td>0.08 <b>(+21.23%)</b></td><td>0.01 <b>(-53.13%)</b></td><td>198.40 (-17.51%)</td><td>172.62 (-5.40%)</td><td>178.70 (-1.65%)</td><td>139.30 <b>(+24.04%)</b></td><td>23.32 <b>(-50.04%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>240.50 (n/a)</td><td>182.48 (n/a)</td><td>181.70 (n/a)</td><td>112.30 (n/a)</td><td>46.67 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.09 <b>(-25.20%)</b></td><td>0.09 (-8.92%)</td><td>0.09 (-6.84%)</td><td>0.08 (+10.71%)</td><td>0.01 <b>(-70.37%)</b></td><td>205.70 (-9.66%)</td><td>186.28 (+6.71%)</td><td>180.20 (+7.33%)</td><td>175.30 <b>(+33.71%)</b></td><td>12.55 <b>(-64.33%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>227.70 (n/a)</td><td>174.56 (n/a)</td><td>167.90 (n/a)</td><td>131.10 (n/a)</td><td>35.18 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.09 (+4.71%)</td><td>0.07 (-0.09%)</td><td>0.07 (+4.52%)</td><td>0.06 (+14.83%)</td><td>0.01 (-14.54%)</td><td>281.10 (-12.92%)</td><td>230.58 (-1.47%)</td><td>222.80 (-4.34%)</td><td>175.30 (-4.52%)</td><td>39.89 <b>(-28.57%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>322.80 (n/a)</td><td>234.02 (n/a)</td><td>232.90 (n/a)</td><td>183.60 (n/a)</td><td>55.84 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.22 (+18.66%)</td><td>0.20 (+13.00%)</td><td>0.20 (+14.70%)</td><td>0.18 (+8.76%)</td><td>0.02 <b>(+68.56%)</b></td><td>183.80 (-8.05%)</td><td>166.82 (-11.26%)</td><td>163.60 (-12.79%)</td><td>149.00 (-15.72%)</td><td>13.40 <b>(+30.99%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>199.90 (n/a)</td><td>187.98 (n/a)</td><td>187.60 (n/a)</td><td>176.80 (n/a)</td><td>10.23 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.24 (-2.68%)</td><td>0.21 (+8.02%)</td><td>0.22 <b>(+20.74%)</b></td><td>0.19 (+6.35%)</td><td>0.02 <b>(-34.78%)</b></td><td>176.50 (-5.97%)</td><td>155.14 (-8.47%)</td><td>152.20 (-17.19%)</td><td>134.30 (+2.75%)</td><td>15.33 <b>(-37.64%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>187.70 (n/a)</td><td>169.50 (n/a)</td><td>183.80 (n/a)</td><td>130.70 (n/a)</td><td>24.58 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.32 <b>(+52.35%)</b></td><td>0.21 (+12.64%)</td><td>0.18 (-11.60%)</td><td>0.18 <b>(+29.73%)</b></td><td>0.06 <b>(+94.46%)</b></td><td>182.40 <b>(-22.91%)</b></td><td>163.94 (-8.96%)</td><td>178.20 (+13.14%)</td><td>101.10 <b>(-34.35%)</b></td><td>35.18 (-1.57%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>236.60 (n/a)</td><td>180.08 (n/a)</td><td>157.50 (n/a)</td><td>154.00 (n/a)</td><td>35.75 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.24 (-11.99%)</td><td>0.18 (-13.14%)</td><td>0.19 (+1.59%)</td><td>0.11 <b>(-36.38%)</b></td><td>0.05 (+6.63%)</td><td>303.00 <b>(+57.16%)</b></td><td>192.90 (+19.55%)</td><td>169.10 (-1.57%)</td><td>135.70 (+13.65%)</td><td>65.49 <b>(+96.38%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>192.80 (n/a)</td><td>161.36 (n/a)</td><td>171.80 (n/a)</td><td>119.40 (n/a)</td><td>33.35 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.22 (-15.07%)</td><td>0.18 (-6.50%)</td><td>0.17 (-5.32%)</td><td>0.16 (+6.99%)</td><td>0.02 <b>(-45.89%)</b></td><td>203.30 (-6.53%)</td><td>184.58 (+4.42%)</td><td>193.40 (+5.63%)</td><td>151.60 (+17.79%)</td><td>21.35 <b>(-40.32%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>217.50 (n/a)</td><td>176.76 (n/a)</td><td>183.10 (n/a)</td><td>128.70 (n/a)</td><td>35.77 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.27 <b>(+41.15%)</b></td><td>0.18 (+4.32%)</td><td>0.17 (-0.32%)</td><td>0.12 <b>(-22.36%)</b></td><td>0.05 <b>(+295.63%)</b></td><td>271.90 <b>(+28.80%)</b></td><td>196.10 (+2.11%)</td><td>187.90 (+0.32%)</td><td>122.90 <b>(-29.16%)</b></td><td>54.89 <b>(+251.79%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>211.10 (n/a)</td><td>192.04 (n/a)</td><td>187.30 (n/a)</td><td>173.50 (n/a)</td><td>15.60 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.24 (+14.64%)</td><td>0.17 (-0.48%)</td><td>0.15 (-9.84%)</td><td>0.14 (-4.89%)</td><td>0.04 <b>(+74.43%)</b></td><td>238.10 (+5.12%)</td><td>200.48 (+3.05%)</td><td>214.20 (+10.93%)</td><td>136.80 (-12.76%)</td><td>40.43 <b>(+59.83%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>226.50 (n/a)</td><td>194.54 (n/a)</td><td>193.10 (n/a)</td><td>156.80 (n/a)</td><td>25.30 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 <b>(+27.25%)</b></td><td>0.03 (-0.27%)</td><td>0.02 (-14.06%)</td><td>0.02 (+2.16%)</td><td>0.01 <b>(+96.07%)</b></td><td>179.90 (-2.12%)</td><td>162.76 (+3.30%)</td><td>176.70 (+16.33%)</td><td>103.70 <b>(-21.44%)</b></td><td>33.06 <b>(+46.75%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>183.80 (n/a)</td><td>157.56 (n/a)</td><td>151.90 (n/a)</td><td>132.00 (n/a)</td><td>22.53 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (+4.20%)</td><td>0.03 (+16.18%)</td><td>0.03 (+18.65%)</td><td>0.02 (+17.78%)</td><td>0.01 (-17.41%)</td><td>167.00 (-15.10%)</td><td>141.12 (-15.33%)</td><td>146.70 (-15.69%)</td><td>107.80 (-4.01%)</td><td>22.29 <b>(-31.30%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>196.70 (n/a)</td><td>166.68 (n/a)</td><td>174.00 (n/a)</td><td>112.30 (n/a)</td><td>32.45 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (+18.78%)</td><td>0.02 (-0.36%)</td><td>0.02 (-6.50%)</td><td>0.02 (-5.46%)</td><td>0.00 <b>(+128.70%)</b></td><td>253.80 (+5.79%)</td><td>220.80 (+2.32%)</td><td>231.00 (+6.94%)</td><td>160.80 (-15.86%)</td><td>35.38 <b>(+96.64%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>239.90 (n/a)</td><td>215.80 (n/a)</td><td>216.00 (n/a)</td><td>191.10 (n/a)</td><td>17.99 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.02 (-6.20%)</td><td>0.02 (+0.26%)</td><td>0.02 (-13.68%)</td><td>0.02 <b>(+29.59%)</b></td><td>0.00 <b>(-49.57%)</b></td><td>213.70 <b>(-22.82%)</b></td><td>195.46 (-3.87%)</td><td>207.00 (+15.84%)</td><td>167.70 (+6.61%)</td><td>21.49 <b>(-58.19%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>276.90 (n/a)</td><td>203.32 (n/a)</td><td>178.70 (n/a)</td><td>157.30 (n/a)</td><td>51.41 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (-18.90%)</td><td>0.02 (-0.18%)</td><td>0.02 (-0.08%)</td><td>0.02 <b>(+34.85%)</b></td><td>0.00 <b>(-65.88%)</b></td><td>188.40 <b>(-25.86%)</b></td><td>176.18 (-4.36%)</td><td>181.90 (+0.06%)</td><td>153.90 <b>(+23.32%)</b></td><td>14.75 <b>(-68.48%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>254.10 (n/a)</td><td>184.22 (n/a)</td><td>181.80 (n/a)</td><td>124.80 (n/a)</td><td>46.80 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (-13.47%)</td><td>0.02 (-15.35%)</td><td>0.02 <b>(-20.14%)</b></td><td>0.02 (-14.12%)</td><td>0.00 (+10.99%)</td><td>186.90 (+16.45%)</td><td>174.26 (+18.33%)</td><td>179.90 <b>(+25.19%)</b></td><td>159.80 (+15.63%)</td><td>12.73 <b>(+47.34%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>160.50 (n/a)</td><td>147.26 (n/a)</td><td>143.70 (n/a)</td><td>138.20 (n/a)</td><td>8.64 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (+7.36%)</td><td>0.03 <b>(+32.39%)</b></td><td>0.03 <b>(+31.16%)</b></td><td>0.02 <b>(+63.71%)</b></td><td>0.00 <b>(-56.46%)</b></td><td>175.20 <b>(-38.93%)</b></td><td>150.04 <b>(-29.71%)</b></td><td>145.10 <b>(-23.75%)</b></td><td>133.00 (-6.86%)</td><td>16.05 <b>(-76.34%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>286.90 (n/a)</td><td>213.46 (n/a)</td><td>190.30 (n/a)</td><td>142.80 (n/a)</td><td>67.85 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 <b>(+21.01%)</b></td><td>0.03 (+18.54%)</td><td>0.03 <b>(+25.07%)</b></td><td>0.02 (+14.05%)</td><td>0.00 <b>(+33.90%)</b></td><td>170.70 (-12.33%)</td><td>138.46 (-15.29%)</td><td>129.10 <b>(-20.06%)</b></td><td>118.90 (-17.37%)</td><td>21.26 (-0.76%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>194.70 (n/a)</td><td>163.46 (n/a)</td><td>161.50 (n/a)</td><td>143.90 (n/a)</td><td>21.42 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 <b>(+25.66%)</b></td><td>0.03 <b>(+23.38%)</b></td><td>0.03 <b>(+24.77%)</b></td><td>0.02 <b>(+27.27%)</b></td><td>0.01 <b>(+42.85%)</b></td><td>173.70 <b>(-21.44%)</b></td><td>142.38 (-18.38%)</td><td>142.00 (-19.86%)</td><td>109.90 <b>(-20.42%)</b></td><td>27.88 (-10.25%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.10 (n/a)</td><td>174.44 (n/a)</td><td>177.20 (n/a)</td><td>138.10 (n/a)</td><td>31.06 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 <b>(+42.96%)</b></td><td>0.03 <b>(+25.74%)</b></td><td>0.03 <b>(+27.31%)</b></td><td>0.02 (+2.89%)</td><td>0.01 <b>(+120.66%)</b></td><td>189.80 (-2.82%)</td><td>145.00 (-18.22%)</td><td>147.10 <b>(-21.42%)</b></td><td>102.00 <b>(-30.04%)</b></td><td>32.00 <b>(+45.80%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>195.30 (n/a)</td><td>177.30 (n/a)</td><td>187.20 (n/a)</td><td>145.80 (n/a)</td><td>21.95 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (-11.08%)</td><td>0.02 (-12.00%)</td><td>0.02 (-13.71%)</td><td>0.02 (-18.95%)</td><td>0.00 (+18.29%)</td><td>224.50 <b>(+23.35%)</b></td><td>184.04 (+14.97%)</td><td>194.60 (+15.90%)</td><td>147.50 (+12.42%)</td><td>32.03 <b>(+62.29%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>182.00 (n/a)</td><td>160.08 (n/a)</td><td>167.90 (n/a)</td><td>131.20 (n/a)</td><td>19.74 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (+16.07%)</td><td>0.02 (+16.42%)</td><td>0.02 (+11.01%)</td><td>0.02 <b>(+36.33%)</b></td><td>0.00 <b>(-23.05%)</b></td><td>184.40 <b>(-26.65%)</b></td><td>165.68 (-15.18%)</td><td>166.00 (-9.93%)</td><td>143.80 (-13.89%)</td><td>15.43 <b>(-53.02%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>251.40 (n/a)</td><td>195.32 (n/a)</td><td>184.30 (n/a)</td><td>167.00 (n/a)</td><td>32.84 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (+14.54%)</td><td>0.02 (+3.78%)</td><td>0.02 (+0.29%)</td><td>0.02 (+2.58%)</td><td>0.00 <b>(+77.09%)</b></td><td>213.10 (-2.52%)</td><td>189.52 (-3.10%)</td><td>189.90 (-0.31%)</td><td>161.70 (-12.74%)</td><td>19.97 <b>(+49.27%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.60 (n/a)</td><td>195.58 (n/a)</td><td>190.50 (n/a)</td><td>185.30 (n/a)</td><td>13.38 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (-10.28%)</td><td>0.02 (+1.30%)</td><td>0.02 (+0.01%)</td><td>0.02 (-6.07%)</td><td>0.00 (-15.62%)</td><td>225.60 (+6.47%)</td><td>182.82 (-1.70%)</td><td>189.90 (+0.00%)</td><td>150.90 (+11.53%)</td><td>30.55 (-0.89%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.90 (n/a)</td><td>185.98 (n/a)</td><td>189.90 (n/a)</td><td>135.30 (n/a)</td><td>30.82 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (-12.06%)</td><td>0.02 (-9.64%)</td><td>0.03 (+7.28%)</td><td>0.02 <b>(-24.20%)</b></td><td>0.00 (-5.06%)</td><td>240.90 <b>(+31.93%)</b></td><td>177.72 (+11.63%)</td><td>163.30 (-6.79%)</td><td>145.80 (+13.64%)</td><td>39.42 <b>(+43.02%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>182.60 (n/a)</td><td>159.20 (n/a)</td><td>175.20 (n/a)</td><td>128.30 (n/a)</td><td>27.57 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 <b>(+20.79%)</b></td><td>0.02 (+5.12%)</td><td>0.02 (+3.06%)</td><td>0.02 (-14.72%)</td><td>0.00 <b>(+219.68%)</b></td><td>234.40 (+17.26%)</td><td>175.60 (-2.02%)</td><td>169.80 (-2.97%)</td><td>139.50 (-17.21%)</td><td>37.33 <b>(+207.92%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>199.90 (n/a)</td><td>179.22 (n/a)</td><td>175.00 (n/a)</td><td>168.50 (n/a)</td><td>12.12 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (+6.90%)</td><td>0.05 (+1.19%)</td><td>0.05 (+10.74%)</td><td>0.04 (-3.33%)</td><td>0.01 <b>(+27.84%)</b></td><td>205.90 (+3.47%)</td><td>167.86 (-0.11%)</td><td>159.80 (-9.72%)</td><td>129.50 (-6.50%)</td><td>31.38 <b>(+27.78%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.00 (n/a)</td><td>168.04 (n/a)</td><td>177.00 (n/a)</td><td>138.50 (n/a)</td><td>24.56 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (-5.87%)</td><td>0.05 (-12.63%)</td><td>0.05 <b>(-20.50%)</b></td><td>0.04 <b>(-24.33%)</b></td><td>0.01 <b>(+77.58%)</b></td><td>209.20 <b>(+32.15%)</b></td><td>169.28 (+16.89%)</td><td>180.80 <b>(+25.82%)</b></td><td>135.40 (+6.20%)</td><td>31.07 <b>(+139.02%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>158.30 (n/a)</td><td>144.82 (n/a)</td><td>143.70 (n/a)</td><td>127.50 (n/a)</td><td>13.00 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (+10.71%)</td><td>0.04 <b>(+22.57%)</b></td><td>0.04 (+19.26%)</td><td>0.03 <b>(+39.78%)</b></td><td>0.00 <b>(-38.84%)</b></td><td>240.50 <b>(-28.44%)</b></td><td>213.78 <b>(-20.78%)</b></td><td>222.00 (-16.13%)</td><td>188.80 (-9.67%)</td><td>23.01 <b>(-61.17%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>336.10 (n/a)</td><td>269.86 (n/a)</td><td>264.70 (n/a)</td><td>209.00 (n/a)</td><td>59.26 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.05 (-6.25%)</td><td>0.04 (+2.03%)</td><td>0.04 (+8.08%)</td><td>0.04 <b>(+34.33%)</b></td><td>0.01 <b>(-54.66%)</b></td><td>205.00 <b>(-25.56%)</b></td><td>184.44 (-6.74%)</td><td>189.80 (-7.46%)</td><td>152.70 (+6.63%)</td><td>20.29 <b>(-62.81%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>275.40 (n/a)</td><td>197.76 (n/a)</td><td>205.10 (n/a)</td><td>143.20 (n/a)</td><td>54.56 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (+5.77%)</td><td>0.06 <b>(+21.87%)</b></td><td>0.06 <b>(+26.83%)</b></td><td>0.05 <b>(+78.10%)</b></td><td>0.01 <b>(-48.22%)</b></td><td>158.00 <b>(-43.87%)</b></td><td>140.24 <b>(-22.94%)</b></td><td>139.40 <b>(-21.15%)</b></td><td>120.20 (-5.43%)</td><td>16.32 <b>(-72.85%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>281.50 (n/a)</td><td>181.98 (n/a)</td><td>176.80 (n/a)</td><td>127.10 (n/a)</td><td>60.13 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (+0.86%)</td><td>0.05 (-5.09%)</td><td>0.04 <b>(-24.87%)</b></td><td>0.04 (+3.06%)</td><td>0.01 <b>(+24.68%)</b></td><td>196.10 (-2.97%)</td><td>164.78 (+6.75%)</td><td>185.80 <b>(+33.09%)</b></td><td>124.00 (-0.80%)</td><td>35.71 (+16.88%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.10 (n/a)</td><td>154.36 (n/a)</td><td>139.60 (n/a)</td><td>125.00 (n/a)</td><td>30.55 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (-1.93%)</td><td>0.06 (+11.46%)</td><td>0.05 (+7.79%)</td><td>0.04 (+15.43%)</td><td>0.01 <b>(-21.44%)</b></td><td>187.10 (-13.38%)</td><td>151.38 (-12.27%)</td><td>157.50 (-7.19%)</td><td>120.50 (+1.95%)</td><td>27.11 <b>(-33.14%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.00 (n/a)</td><td>172.56 (n/a)</td><td>169.70 (n/a)</td><td>118.20 (n/a)</td><td>40.54 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (+11.36%)</td><td>0.06 (+13.28%)</td><td>0.06 (+18.76%)</td><td>0.04 (+8.85%)</td><td>0.01 <b>(+21.40%)</b></td><td>184.40 (-8.12%)</td><td>149.00 (-11.10%)</td><td>140.20 (-15.80%)</td><td>112.60 (-10.14%)</td><td>30.82 (+2.85%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.70 (n/a)</td><td>167.60 (n/a)</td><td>166.50 (n/a)</td><td>125.30 (n/a)</td><td>29.96 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (+0.82%)</td><td>0.06 <b>(+20.35%)</b></td><td>0.06 <b>(+21.89%)</b></td><td>0.05 <b>(+26.40%)</b></td><td>0.01 <b>(-39.24%)</b></td><td>166.40 <b>(-20.87%)</b></td><td>137.64 (-18.81%)</td><td>131.20 (-17.95%)</td><td>128.50 (-0.77%)</td><td>16.15 <b>(-52.94%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.30 (n/a)</td><td>169.52 (n/a)</td><td>159.90 (n/a)</td><td>129.50 (n/a)</td><td>34.32 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (+19.06%)</td><td>0.06 (+19.47%)</td><td>0.06 (+11.60%)</td><td>0.04 <b>(+36.37%)</b></td><td>0.01 (-2.87%)</td><td>185.40 <b>(-26.66%)</b></td><td>145.18 (-17.86%)</td><td>146.00 (-10.43%)</td><td>117.80 (-16.04%)</td><td>26.52 <b>(-41.44%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>252.80 (n/a)</td><td>176.74 (n/a)</td><td>163.00 (n/a)</td><td>140.30 (n/a)</td><td>45.28 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (+17.40%)</td><td>0.06 <b>(+21.38%)</b></td><td>0.06 <b>(+29.42%)</b></td><td>0.05 (+11.06%)</td><td>0.01 <b>(+35.91%)</b></td><td>164.60 (-10.01%)</td><td>135.32 (-17.13%)</td><td>127.20 <b>(-22.72%)</b></td><td>111.60 (-14.81%)</td><td>21.14 (+7.97%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.90 (n/a)</td><td>163.30 (n/a)</td><td>164.60 (n/a)</td><td>131.00 (n/a)</td><td>19.58 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (+7.67%)</td><td>0.06 <b>(+30.18%)</b></td><td>0.05 <b>(+27.37%)</b></td><td>0.05 <b>(+102.62%)</b></td><td>0.01 <b>(-51.47%)</b></td><td>166.90 <b>(-50.65%)</b></td><td>148.16 <b>(-29.10%)</b></td><td>150.60 <b>(-21.48%)</b></td><td>124.30 (-7.10%)</td><td>16.05 <b>(-79.10%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>338.20 (n/a)</td><td>208.98 (n/a)</td><td>191.80 (n/a)</td><td>133.80 (n/a)</td><td>76.82 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (+10.57%)</td><td>0.05 (-0.54%)</td><td>0.05 (+5.54%)</td><td>0.03 <b>(-32.84%)</b></td><td>0.01 <b>(+131.85%)</b></td><td>297.70 <b>(+48.85%)</b></td><td>187.90 (+6.48%)</td><td>168.80 (-5.27%)</td><td>142.30 (-9.54%)</td><td>62.52 <b>(+237.21%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>200.00 (n/a)</td><td>176.46 (n/a)</td><td>178.20 (n/a)</td><td>157.30 (n/a)</td><td>18.54 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (+10.04%)</td><td>0.05 (+7.90%)</td><td>0.05 (+0.78%)</td><td>0.05 (+5.02%)</td><td>0.01 <b>(+76.41%)</b></td><td>177.40 (-4.78%)</td><td>160.60 (-6.60%)</td><td>172.70 (-0.75%)</td><td>139.20 (-9.14%)</td><td>19.47 <b>(+51.65%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>186.30 (n/a)</td><td>171.94 (n/a)</td><td>174.00 (n/a)</td><td>153.20 (n/a)</td><td>12.84 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (+14.65%)</td><td>0.05 (+3.37%)</td><td>0.05 (+11.08%)</td><td>0.03 <b>(-24.56%)</b></td><td>0.01 <b>(+262.15%)</b></td><td>254.80 <b>(+32.50%)</b></td><td>181.12 (+0.95%)</td><td>157.20 (-9.97%)</td><td>145.70 (-12.81%)</td><td>46.60 <b>(+308.23%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>192.30 (n/a)</td><td>179.42 (n/a)</td><td>174.60 (n/a)</td><td>167.10 (n/a)</td><td>11.41 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 <b>(+35.40%)</b></td><td>0.06 <b>(+29.41%)</b></td><td>0.06 <b>(+33.60%)</b></td><td>0.04 (+13.49%)</td><td>0.01 <b>(+135.23%)</b></td><td>198.50 (-11.90%)</td><td>153.64 <b>(-20.95%)</b></td><td>144.20 <b>(-25.17%)</b></td><td>123.20 <b>(-26.18%)</b></td><td>31.57 <b>(+52.27%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>225.30 (n/a)</td><td>194.36 (n/a)</td><td>192.70 (n/a)</td><td>166.90 (n/a)</td><td>20.73 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.14 <b>(+28.28%)</b></td><td>0.11 (+11.99%)</td><td>0.10 (+8.71%)</td><td>0.08 (-1.32%)</td><td>0.02 <b>(+118.64%)</b></td><td>195.40 (+1.35%)</td><td>159.24 (-9.02%)</td><td>162.50 (-7.98%)</td><td>118.60 <b>(-22.08%)</b></td><td>27.42 <b>(+68.17%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>192.80 (n/a)</td><td>175.02 (n/a)</td><td>176.60 (n/a)</td><td>152.20 (n/a)</td><td>16.31 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.14 (+11.53%)</td><td>0.12 (+19.60%)</td><td>0.12 <b>(+24.26%)</b></td><td>0.10 <b>(+26.56%)</b></td><td>0.02 (+6.05%)</td><td>169.70 <b>(-21.00%)</b></td><td>142.84 (-16.77%)</td><td>139.90 (-19.55%)</td><td>116.20 (-10.34%)</td><td>23.35 <b>(-23.00%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>214.80 (n/a)</td><td>171.62 (n/a)</td><td>173.90 (n/a)</td><td>129.60 (n/a)</td><td>30.32 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.09 <b>(-22.94%)</b></td><td>0.08 (-15.31%)</td><td>0.08 (-3.35%)</td><td>0.05 <b>(-38.70%)</b></td><td>0.02 (+14.65%)</td><td>340.60 <b>(+63.12%)</b></td><td>227.32 <b>(+21.84%)</b></td><td>201.80 (+3.49%)</td><td>189.40 <b>(+29.81%)</b></td><td>64.11 <b>(+148.79%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>208.80 (n/a)</td><td>186.58 (n/a)</td><td>195.00 (n/a)</td><td>145.90 (n/a)</td><td>25.77 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (+8.59%)</td><td>0.09 (+11.02%)</td><td>0.09 (+17.15%)</td><td>0.07 (+2.77%)</td><td>0.02 (+17.89%)</td><td>234.30 (-2.70%)</td><td>184.94 (-9.40%)</td><td>173.30 (-14.67%)</td><td>143.20 (-7.91%)</td><td>34.68 (+8.63%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>240.80 (n/a)</td><td>204.12 (n/a)</td><td>203.10 (n/a)</td><td>155.50 (n/a)</td><td>31.93 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.14 (+11.51%)</td><td>0.11 (+12.45%)</td><td>0.12 (+10.07%)</td><td>0.09 <b>(+24.68%)</b></td><td>0.02 (-18.19%)</td><td>185.20 (-19.79%)</td><td>148.66 (-14.07%)</td><td>131.90 (-9.16%)</td><td>116.40 (-10.32%)</td><td>30.90 <b>(-40.39%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>230.90 (n/a)</td><td>173.00 (n/a)</td><td>145.20 (n/a)</td><td>129.80 (n/a)</td><td>51.85 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.14 <b>(+35.43%)</b></td><td>0.12 (+19.42%)</td><td>0.10 (+2.10%)</td><td>0.10 (+12.05%)</td><td>0.02 <b>(+180.38%)</b></td><td>166.00 (-10.75%)</td><td>145.04 (-14.22%)</td><td>163.00 (-2.04%)</td><td>114.40 <b>(-26.19%)</b></td><td>26.95 <b>(+85.98%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>186.00 (n/a)</td><td>169.08 (n/a)</td><td>166.40 (n/a)</td><td>155.00 (n/a)</td><td>14.49 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.17 <b>(+34.59%)</b></td><td>0.12 (+13.64%)</td><td>0.10 (+1.76%)</td><td>0.09 (+13.01%)</td><td>0.04 <b>(+78.55%)</b></td><td>181.70 (-11.54%)</td><td>144.24 (-9.03%)</td><td>156.80 (-1.75%)</td><td>96.30 <b>(-25.69%)</b></td><td>37.90 <b>(+21.54%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>205.40 (n/a)</td><td>158.56 (n/a)</td><td>159.60 (n/a)</td><td>129.60 (n/a)</td><td>31.18 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 <b>(-21.22%)</b></td><td>0.09 (-17.41%)</td><td>0.09 <b>(-20.94%)</b></td><td>0.08 (-12.18%)</td><td>0.01 <b>(-45.60%)</b></td><td>193.40 (+13.90%)</td><td>176.36 <b>(+20.17%)</b></td><td>180.70 <b>(+26.45%)</b></td><td>154.70 <b>(+27.01%)</b></td><td>14.56 <b>(-22.51%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>169.80 (n/a)</td><td>146.76 (n/a)</td><td>142.90 (n/a)</td><td>121.80 (n/a)</td><td>18.79 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 (+9.12%)</td><td>0.10 (-5.31%)</td><td>0.10 <b>(-21.79%)</b></td><td>0.09 <b>(+23.42%)</b></td><td>0.02 (-17.00%)</td><td>182.30 (-18.98%)</td><td>163.70 (+3.53%)</td><td>172.30 <b>(+27.91%)</b></td><td>122.10 (-8.33%)</td><td>24.02 <b>(-39.31%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>225.00 (n/a)</td><td>158.12 (n/a)</td><td>134.70 (n/a)</td><td>133.20 (n/a)</td><td>39.58 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 <b>(+22.73%)</b></td><td>0.10 (+2.59%)</td><td>0.09 (-1.39%)</td><td>0.08 (-5.25%)</td><td>0.02 <b>(+130.06%)</b></td><td>204.10 (+5.59%)</td><td>170.22 (+0.14%)</td><td>173.70 (+1.40%)</td><td>124.30 (-18.49%)</td><td>33.71 <b>(+102.75%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>193.30 (n/a)</td><td>169.98 (n/a)</td><td>171.30 (n/a)</td><td>152.50 (n/a)</td><td>16.63 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 (+9.35%)</td><td>0.10 (+5.25%)</td><td>0.10 (-0.67%)</td><td>0.09 (+11.90%)</td><td>0.02 (+14.12%)</td><td>184.70 (-10.64%)</td><td>163.28 (-4.88%)</td><td>171.30 (+0.71%)</td><td>122.00 (-8.55%)</td><td>24.04 (-8.45%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>206.70 (n/a)</td><td>171.66 (n/a)</td><td>170.10 (n/a)</td><td>133.40 (n/a)</td><td>26.26 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 (+4.60%)</td><td>0.09 (-9.33%)</td><td>0.09 <b>(-21.43%)</b></td><td>0.07 (-5.56%)</td><td>0.02 (+8.42%)</td><td>245.10 (+5.92%)</td><td>183.18 (+10.90%)</td><td>183.40 <b>(+27.27%)</b></td><td>128.80 (-4.38%)</td><td>42.40 (+7.27%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>231.40 (n/a)</td><td>165.18 (n/a)</td><td>144.10 (n/a)</td><td>134.70 (n/a)</td><td>39.53 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (-5.94%)</td><td>0.10 (+9.65%)</td><td>0.10 (+11.49%)</td><td>0.07 (+18.55%)</td><td>0.02 <b>(-21.13%)</b></td><td>236.20 (-15.64%)</td><td>172.44 (-10.72%)</td><td>158.80 (-10.28%)</td><td>151.60 (+6.31%)</td><td>35.82 <b>(-30.75%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>280.00 (n/a)</td><td>193.14 (n/a)</td><td>177.00 (n/a)</td><td>142.60 (n/a)</td><td>51.73 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (-14.73%)</td><td>0.09 (-8.99%)</td><td>0.09 (-10.71%)</td><td>0.08 (+2.03%)</td><td>0.01 <b>(-34.17%)</b></td><td>218.10 (-1.98%)</td><td>180.82 (+7.97%)</td><td>179.60 (+12.04%)</td><td>153.50 (+17.35%)</td><td>27.18 <b>(-25.68%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>222.50 (n/a)</td><td>167.48 (n/a)</td><td>160.30 (n/a)</td><td>130.80 (n/a)</td><td>36.58 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (-13.21%)</td><td>0.09 (-4.06%)</td><td>0.09 (-0.16%)</td><td>0.07 (+6.89%)</td><td>0.01 <b>(-27.65%)</b></td><td>218.60 (-6.42%)</td><td>182.12 (+2.67%)</td><td>180.50 (+0.17%)</td><td>150.10 (+15.28%)</td><td>29.32 <b>(-22.30%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>233.60 (n/a)</td><td>177.38 (n/a)</td><td>180.20 (n/a)</td><td>130.20 (n/a)</td><td>37.74 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 (-3.93%)</td><td>0.10 (-7.68%)</td><td>0.10 (-13.35%)</td><td>0.08 (+9.85%)</td><td>0.02 (-5.52%)</td><td>202.60 (-8.98%)</td><td>165.76 (+7.51%)</td><td>162.50 (+15.41%)</td><td>125.80 (+4.05%)</td><td>34.18 (-13.34%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>222.60 (n/a)</td><td>154.18 (n/a)</td><td>140.80 (n/a)</td><td>120.90 (n/a)</td><td>39.44 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.39 <b>(+34.56%)</b></td><td>0.24 (+11.93%)</td><td>0.20 (-2.24%)</td><td>0.16 (+19.68%)</td><td>0.09 <b>(+33.31%)</b></td><td>199.60 (-16.45%)</td><td>152.60 (-10.00%)</td><td>162.70 (+2.33%)</td><td>84.80 <b>(-25.68%)</b></td><td>46.20 (-17.39%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>238.90 (n/a)</td><td>169.56 (n/a)</td><td>159.00 (n/a)</td><td>114.10 (n/a)</td><td>55.93 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.26 (+0.80%)</td><td>0.22 (-1.57%)</td><td>0.20 (-16.98%)</td><td>0.17 (+13.47%)</td><td>0.04 <b>(-21.48%)</b></td><td>190.50 (-11.85%)</td><td>154.76 (-0.41%)</td><td>160.00 <b>(+20.48%)</b></td><td>123.70 (-0.80%)</td><td>26.40 <b>(-31.74%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.25 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>216.10 (n/a)</td><td>155.40 (n/a)</td><td>132.80 (n/a)</td><td>124.70 (n/a)</td><td>38.67 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.16 (-13.09%)</td><td>0.14 (+2.31%)</td><td>0.15 (+2.10%)</td><td>0.10 (+18.27%)</td><td>0.02 <b>(-37.08%)</b></td><td>313.40 (-15.43%)</td><td>233.76 (-5.76%)</td><td>213.00 (-2.07%)</td><td>208.20 (+15.09%)</td><td>44.78 <b>(-39.68%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>370.60 (n/a)</td><td>248.04 (n/a)</td><td>217.50 (n/a)</td><td>180.90 (n/a)</td><td>74.23 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.18 (-14.23%)</td><td>0.16 (-3.94%)</td><td>0.15 (+0.52%)</td><td>0.14 (+9.27%)</td><td>0.02 <b>(-49.37%)</b></td><td>232.60 (-8.50%)</td><td>210.86 (+1.92%)</td><td>215.50 (-0.51%)</td><td>178.00 (+16.57%)</td><td>20.52 <b>(-45.82%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>254.20 (n/a)</td><td>206.88 (n/a)</td><td>216.60 (n/a)</td><td>152.70 (n/a)</td><td>37.88 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.22 (-14.11%)</td><td>0.20 (-0.24%)</td><td>0.20 (+3.74%)</td><td>0.16 (+5.31%)</td><td>0.03 <b>(-33.04%)</b></td><td>206.60 (-5.06%)</td><td>169.32 (-1.27%)</td><td>160.40 (-3.61%)</td><td>149.20 (+16.47%)</td><td>24.34 <b>(-26.44%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>217.60 (n/a)</td><td>171.50 (n/a)</td><td>166.40 (n/a)</td><td>128.10 (n/a)</td><td>33.09 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.33 (+16.86%)</td><td>0.23 (+8.50%)</td><td>0.21 (+7.31%)</td><td>0.19 (+1.07%)</td><td>0.06 <b>(+43.38%)</b></td><td>176.10 (-1.07%)</td><td>149.54 (-6.26%)</td><td>159.50 (-6.83%)</td><td>100.40 (-14.41%)</td><td>30.55 (+19.84%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>178.00 (n/a)</td><td>159.52 (n/a)</td><td>171.20 (n/a)</td><td>117.30 (n/a)</td><td>25.50 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.27 (+0.11%)</td><td>0.22 (-3.11%)</td><td>0.21 (-5.21%)</td><td>0.18 (-5.09%)</td><td>0.04 <b>(+21.04%)</b></td><td>187.20 (+5.41%)</td><td>155.76 (+4.31%)</td><td>157.70 (+5.48%)</td><td>123.20 (-0.08%)</td><td>29.60 <b>(+28.13%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>177.60 (n/a)</td><td>149.32 (n/a)</td><td>149.50 (n/a)</td><td>123.30 (n/a)</td><td>23.10 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.27 (+2.91%)</td><td>0.20 (-16.22%)</td><td>0.20 <b>(-20.23%)</b></td><td>0.14 <b>(-28.20%)</b></td><td>0.05 <b>(+89.92%)</b></td><td>236.90 <b>(+39.27%)</b></td><td>171.00 <b>(+24.91%)</b></td><td>162.00 <b>(+25.39%)</b></td><td>122.80 (-2.85%)</td><td>46.87 <b>(+151.90%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>170.10 (n/a)</td><td>136.90 (n/a)</td><td>129.20 (n/a)</td><td>126.40 (n/a)</td><td>18.61 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.25 (-5.37%)</td><td>0.18 (-12.31%)</td><td>0.17 (-19.38%)</td><td>0.10 <b>(-28.55%)</b></td><td>0.06 (-3.38%)</td><td>342.40 <b>(+39.98%)</b></td><td>208.66 (+16.94%)</td><td>188.50 <b>(+24.09%)</b></td><td>132.70 (+5.65%)</td><td>83.92 <b>(+39.42%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>244.60 (n/a)</td><td>178.44 (n/a)</td><td>151.90 (n/a)</td><td>125.60 (n/a)</td><td>60.19 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.26 (-1.07%)</td><td>0.21 (-3.09%)</td><td>0.20 (-13.21%)</td><td>0.17 (+12.15%)</td><td>0.04 (-12.88%)</td><td>195.20 (-10.83%)</td><td>161.72 (+1.97%)</td><td>164.30 (+15.22%)</td><td>126.70 (+1.12%)</td><td>27.77 <b>(-23.97%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>218.90 (n/a)</td><td>158.60 (n/a)</td><td>142.60 (n/a)</td><td>125.30 (n/a)</td><td>36.52 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.29 (+16.88%)</td><td>0.24 (+13.84%)</td><td>0.26 <b>(+22.87%)</b></td><td>0.18 <b>(+35.84%)</b></td><td>0.05 (+0.66%)</td><td>181.80 <b>(-26.40%)</b></td><td>141.90 (-13.79%)</td><td>126.00 (-18.60%)</td><td>112.30 (-14.47%)</td><td>29.57 <b>(-37.56%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>247.00 (n/a)</td><td>164.60 (n/a)</td><td>154.80 (n/a)</td><td>131.30 (n/a)</td><td>47.35 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.26 (+6.96%)</td><td>0.22 (+12.75%)</td><td>0.20 (+10.24%)</td><td>0.18 <b>(+26.25%)</b></td><td>0.03 <b>(-21.65%)</b></td><td>182.50 <b>(-20.79%)</b></td><td>154.44 (-12.93%)</td><td>160.10 (-9.29%)</td><td>126.50 (-6.50%)</td><td>21.40 <b>(-42.23%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>230.40 (n/a)</td><td>177.38 (n/a)</td><td>176.50 (n/a)</td><td>135.30 (n/a)</td><td>37.03 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.23 (-10.27%)</td><td>0.18 (-10.08%)</td><td>0.18 (-5.71%)</td><td>0.12 <b>(-25.65%)</b></td><td>0.04 (+1.49%)</td><td>267.70 <b>(+34.46%)</b></td><td>190.12 (+12.86%)</td><td>179.60 (+6.08%)</td><td>143.20 (+11.44%)</td><td>46.32 <b>(+56.26%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>199.10 (n/a)</td><td>168.46 (n/a)</td><td>169.30 (n/a)</td><td>128.50 (n/a)</td><td>29.64 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.24 (+7.92%)</td><td>0.19 (-2.86%)</td><td>0.19 (+5.55%)</td><td>0.12 <b>(-24.99%)</b></td><td>0.05 <b>(+88.81%)</b></td><td>271.70 <b>(+33.32%)</b></td><td>186.78 (+7.52%)</td><td>169.90 (-5.24%)</td><td>136.10 (-7.35%)</td><td>52.94 <b>(+140.34%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>203.80 (n/a)</td><td>173.72 (n/a)</td><td>179.30 (n/a)</td><td>146.90 (n/a)</td><td>22.03 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.24 (+0.94%)</td><td>0.19 (-3.91%)</td><td>0.19 (-5.98%)</td><td>0.15 (-13.17%)</td><td>0.04 (+19.67%)</td><td>223.40 (+15.15%)</td><td>175.88 (+5.14%)</td><td>172.40 (+6.35%)</td><td>136.80 (-0.87%)</td><td>33.36 <b>(+33.27%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>194.00 (n/a)</td><td>167.28 (n/a)</td><td>162.10 (n/a)</td><td>138.00 (n/a)</td><td>25.03 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.26 (+9.19%)</td><td>0.19 (+3.38%)</td><td>0.17 (+0.97%)</td><td>0.16 <b>(+35.68%)</b></td><td>0.04 (-7.63%)</td><td>207.60 <b>(-26.28%)</b></td><td>182.58 (-5.76%)</td><td>195.00 (-0.96%)</td><td>124.10 (-8.41%)</td><td>33.54 <b>(-40.06%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>281.60 (n/a)</td><td>193.74 (n/a)</td><td>196.90 (n/a)</td><td>135.50 (n/a)</td><td>55.95 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/mha</summary>


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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.18 (+0.05%)</td><td>0.18 (+0.13%)</td><td>0.18 (+0.10%)</td><td>0.18 (+0.18%)</td><td>0.00 <b>(-24.59%)</b></td><td>47492.80 (-0.18%)</td><td>47397.46 (-0.13%)</td><td>47392.00 (-0.10%)</td><td>47341.00 (-0.05%)</td><td>58.99 <b>(-24.74%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47576.60 (n/a)</td><td>47461.04 (n/a)</td><td>47439.20 (n/a)</td><td>47365.90 (n/a)</td><td>78.38 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.18 (+0.05%)</td><td>0.18 (-0.02%)</td><td>0.18 (-0.09%)</td><td>0.18 (+0.02%)</td><td>0.00 <b>(+31.85%)</b></td><td>47518.00 (-0.02%)</td><td>47439.04 (+0.02%)</td><td>47450.30 (+0.09%)</td><td>47340.20 (-0.05%)</td><td>81.69 <b>(+31.87%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47527.20 (n/a)</td><td>47427.68 (n/a)</td><td>47408.60 (n/a)</td><td>47362.70 (n/a)</td><td>61.95 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (+0.09%)</td><td>0.11 (+0.02%)</td><td>0.11 (+0.00%)</td><td>0.11 (+0.01%)</td><td>0.00 <b>(+138.81%)</b></td><td>374411.40 (-0.01%)</td><td>374254.40 (-0.02%)</td><td>374284.60 (-0.00%)</td><td>373916.80 (-0.09%)</td><td>202.13 <b>(+138.76%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.00 (n/a)</td><td>374445.90 (n/a)</td><td>374332.68 (n/a)</td><td>374287.60 (n/a)</td><td>374264.20 (n/a)</td><td>84.66 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.18 <b>(+25.73%)</b></td><td>0.15 <b>(+23.09%)</b></td><td>0.16 <b>(+20.37%)</b></td><td>0.13 <b>(+38.89%)</b></td><td>0.02 (+2.36%)</td><td>188.10 <b>(-28.01%)</b></td><td>162.32 (-19.44%)</td><td>158.30 (-16.90%)</td><td>140.30 <b>(-20.46%)</b></td><td>20.54 <b>(-41.61%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>261.30 (n/a)</td><td>201.50 (n/a)</td><td>190.50 (n/a)</td><td>176.40 (n/a)</td><td>35.17 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.36 (+1.72%)</td><td>0.28 (-4.21%)</td><td>0.28 (-2.05%)</td><td>0.22 (-15.56%)</td><td>0.05 <b>(+48.57%)</b></td><td>221.10 (+18.43%)</td><td>180.42 (+6.09%)</td><td>177.30 (+2.07%)</td><td>137.40 (-1.72%)</td><td>32.06 <b>(+75.74%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.35 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.04 (n/a)</td><td>186.70 (n/a)</td><td>170.06 (n/a)</td><td>173.70 (n/a)</td><td>139.80 (n/a)</td><td>18.24 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>13.41 (+5.15%)</td><td>12.66 (+1.28%)</td><td>12.48 (-1.38%)</td><td>12.28 (+1.98%)</td><td>0.47 <b>(+51.27%)</b></td><td>853.90 (-1.94%)</td><td>829.38 (-1.20%)</td><td>840.10 (+1.40%)</td><td>781.70 (-4.90%)</td><td>30.05 <b>(+41.41%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>12.76 (n/a)</td><td>12.50 (n/a)</td><td>12.66 (n/a)</td><td>12.04 (n/a)</td><td>0.31 (n/a)</td><td>870.80 (n/a)</td><td>839.48 (n/a)</td><td>828.50 (n/a)</td><td>822.00 (n/a)</td><td>21.25 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.30 <b>(+28.64%)</b></td><td>0.25 <b>(+21.89%)</b></td><td>0.24 (+11.92%)</td><td>0.23 <b>(+39.85%)</b></td><td>0.03 (-0.32%)</td><td>177.90 <b>(-28.47%)</b></td><td>164.54 (-18.52%)</td><td>173.30 (-10.62%)</td><td>137.50 <b>(-22.23%)</b></td><td>16.47 <b>(-44.59%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>248.70 (n/a)</td><td>201.94 (n/a)</td><td>193.90 (n/a)</td><td>176.80 (n/a)</td><td>29.73 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 <b>(+37.56%)</b></td><td>0.03 (+19.79%)</td><td>0.03 (+17.12%)</td><td>0.03 (+5.95%)</td><td>0.00 <b>(+276.65%)</b></td><td>181.90 (-5.65%)</td><td>153.38 (-15.56%)</td><td>150.90 (-14.65%)</td><td>128.00 <b>(-27.27%)</b></td><td>19.53 <b>(+159.76%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>192.80 (n/a)</td><td>181.64 (n/a)</td><td>176.80 (n/a)</td><td>176.00 (n/a)</td><td>7.52 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (+12.89%)</td><td>0.03 (+1.89%)</td><td>0.02 (+3.21%)</td><td>0.02 (-3.26%)</td><td>0.01 <b>(+31.23%)</b></td><td>194.40 (+3.40%)</td><td>160.40 (-0.77%)</td><td>165.70 (-3.10%)</td><td>117.10 (-11.42%)</td><td>29.86 (+19.99%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>188.00 (n/a)</td><td>161.64 (n/a)</td><td>171.00 (n/a)</td><td>132.20 (n/a)</td><td>24.88 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.05 (+4.12%)</td><td>0.03 (-19.14%)</td><td>0.04 (-15.33%)</td><td>0.02 <b>(-46.44%)</b></td><td>0.02 <b>(+136.34%)</b></td><td>338.10 <b>(+86.69%)</b></td><td>211.12 <b>(+44.92%)</b></td><td>167.20 (+18.08%)</td><td>120.40 (-3.99%)</td><td>101.10 <b>(+336.08%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>181.10 (n/a)</td><td>145.68 (n/a)</td><td>141.60 (n/a)</td><td>125.40 (n/a)</td><td>23.18 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 <b>(-26.02%)</b></td><td>0.03 (-14.13%)</td><td>0.03 (-7.89%)</td><td>0.02 (+10.79%)</td><td>0.00 <b>(-57.08%)</b></td><td>181.10 (-9.72%)</td><td>162.16 (+13.02%)</td><td>150.30 (+8.60%)</td><td>149.00 <b>(+35.21%)</b></td><td>17.20 <b>(-49.52%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>200.60 (n/a)</td><td>143.48 (n/a)</td><td>138.40 (n/a)</td><td>110.20 (n/a)</td><td>34.08 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (+15.95%)</td><td>0.03 (+15.11%)</td><td>0.04 <b>(+39.77%)</b></td><td>0.02 <b>(-24.22%)</b></td><td>0.01 <b>(+122.03%)</b></td><td>255.10 <b>(+31.97%)</b></td><td>161.06 (-6.98%)</td><td>128.10 <b>(-28.44%)</b></td><td>117.30 (-13.75%)</td><td>57.63 <b>(+158.85%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>193.30 (n/a)</td><td>173.14 (n/a)</td><td>179.00 (n/a)</td><td>136.00 (n/a)</td><td>22.26 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (-10.14%)</td><td>0.02 (-14.97%)</td><td>0.02 (-14.33%)</td><td>0.02 <b>(-24.25%)</b></td><td>0.01 (+12.71%)</td><td>234.50 <b>(+31.96%)</b></td><td>186.78 <b>(+20.29%)</b></td><td>188.90 (+16.75%)</td><td>125.10 (+11.30%)</td><td>43.00 <b>(+69.66%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>177.70 (n/a)</td><td>155.28 (n/a)</td><td>161.80 (n/a)</td><td>112.40 (n/a)</td><td>25.34 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (+8.15%)</td><td>0.03 (+10.74%)</td><td>0.04 <b>(+35.60%)</b></td><td>0.02 (-14.95%)</td><td>0.01 <b>(+78.67%)</b></td><td>245.30 (+17.59%)</td><td>166.96 (-5.09%)</td><td>135.50 <b>(-26.24%)</b></td><td>125.70 (-7.51%)</td><td>52.70 <b>(+94.04%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>208.60 (n/a)</td><td>175.92 (n/a)</td><td>183.70 (n/a)</td><td>135.90 (n/a)</td><td>27.16 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.02 <b>(-23.81%)</b></td><td>0.02 (-19.11%)</td><td>0.02 (-12.85%)</td><td>0.02 <b>(-25.20%)</b></td><td>0.00 <b>(-27.43%)</b></td><td>232.90 <b>(+33.70%)</b></td><td>202.62 <b>(+23.56%)</b></td><td>195.30 (+14.75%)</td><td>176.40 <b>(+31.25%)</b></td><td>21.69 <b>(+29.44%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>174.20 (n/a)</td><td>163.98 (n/a)</td><td>170.20 (n/a)</td><td>134.40 (n/a)</td><td>16.76 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 <b>(-23.26%)</b></td><td>0.03 (-3.21%)</td><td>0.03 (+3.84%)</td><td>0.02 (-0.27%)</td><td>0.00 <b>(-48.49%)</b></td><td>236.30 (+0.30%)</td><td>184.86 (+0.06%)</td><td>179.00 (-3.71%)</td><td>155.90 <b>(+30.35%)</b></td><td>30.81 <b>(-28.18%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>235.60 (n/a)</td><td>184.74 (n/a)</td><td>185.90 (n/a)</td><td>119.60 (n/a)</td><td>42.90 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 <b>(-23.60%)</b></td><td>0.02 <b>(-22.46%)</b></td><td>0.02 (-19.05%)</td><td>0.02 <b>(-29.68%)</b></td><td>0.00 <b>(-23.57%)</b></td><td>254.60 <b>(+42.23%)</b></td><td>204.78 <b>(+29.13%)</b></td><td>203.40 <b>(+23.50%)</b></td><td>162.90 <b>(+30.84%)</b></td><td>32.97 <b>(+41.07%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>179.00 (n/a)</td><td>158.58 (n/a)</td><td>164.70 (n/a)</td><td>124.50 (n/a)</td><td>23.37 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (+7.19%)</td><td>0.03 (-4.93%)</td><td>0.02 (-17.05%)</td><td>0.02 (-18.16%)</td><td>0.01 <b>(+96.49%)</b></td><td>258.10 <b>(+22.15%)</b></td><td>197.34 (+11.39%)</td><td>216.00 <b>(+20.60%)</b></td><td>134.70 (-6.72%)</td><td>57.48 <b>(+116.51%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.30 (n/a)</td><td>177.16 (n/a)</td><td>179.10 (n/a)</td><td>144.40 (n/a)</td><td>26.55 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (+16.90%)</td><td>0.02 (-6.26%)</td><td>0.02 (-10.01%)</td><td>0.02 <b>(-23.32%)</b></td><td>0.00 <b>(+610.32%)</b></td><td>246.40 <b>(+30.44%)</b></td><td>200.54 (+9.24%)</td><td>204.10 (+11.11%)</td><td>152.50 (-14.47%)</td><td>33.92 <b>(+681.20%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>188.90 (n/a)</td><td>183.58 (n/a)</td><td>183.70 (n/a)</td><td>178.30 (n/a)</td><td>4.34 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (+7.97%)</td><td>0.02 (-1.46%)</td><td>0.03 (+13.49%)</td><td>0.01 <b>(-37.84%)</b></td><td>0.01 <b>(+196.72%)</b></td><td>340.40 <b>(+60.87%)</b></td><td>211.68 (+10.09%)</td><td>167.30 (-11.90%)</td><td>158.10 (-7.38%)</td><td>78.64 <b>(+322.37%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.60 (n/a)</td><td>192.28 (n/a)</td><td>189.90 (n/a)</td><td>170.70 (n/a)</td><td>18.62 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (+2.18%)</td><td>0.02 (+1.61%)</td><td>0.02 (+4.79%)</td><td>0.02 (-4.55%)</td><td>0.00 (+13.30%)</td><td>202.20 (+4.77%)</td><td>177.66 (-1.29%)</td><td>182.20 (-4.56%)</td><td>145.00 (-2.16%)</td><td>21.90 (+14.98%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>193.00 (n/a)</td><td>179.98 (n/a)</td><td>190.90 (n/a)</td><td>148.20 (n/a)</td><td>19.05 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 <b>(+28.06%)</b></td><td>0.02 (+5.79%)</td><td>0.02 (+2.23%)</td><td>0.02 (-0.12%)</td><td>0.01 <b>(+132.15%)</b></td><td>223.40 (+0.13%)</td><td>196.56 (-3.26%)</td><td>207.20 (-2.17%)</td><td>137.20 <b>(-21.91%)</b></td><td>33.92 <b>(+75.01%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>223.10 (n/a)</td><td>203.18 (n/a)</td><td>211.80 (n/a)</td><td>175.70 (n/a)</td><td>19.38 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.02 (+3.93%)</td><td>0.02 (+6.99%)</td><td>0.02 (+7.26%)</td><td>0.02 (+17.52%)</td><td>0.00 <b>(-20.27%)</b></td><td>255.50 (-14.92%)</td><td>218.48 (-7.65%)</td><td>221.10 (-6.79%)</td><td>180.30 (-3.79%)</td><td>27.32 <b>(-35.57%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>300.30 (n/a)</td><td>236.58 (n/a)</td><td>237.20 (n/a)</td><td>187.40 (n/a)</td><td>42.41 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (-1.03%)</td><td>0.05 (-0.89%)</td><td>0.05 (-0.04%)</td><td>0.04 (+0.50%)</td><td>0.01 (-1.24%)</td><td>182.70 (-0.49%)</td><td>162.16 (+0.87%)</td><td>164.30 (+0.00%)</td><td>124.60 (+1.05%)</td><td>22.49 (+0.39%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.60 (n/a)</td><td>160.76 (n/a)</td><td>164.30 (n/a)</td><td>123.30 (n/a)</td><td>22.40 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.09 (+16.23%)</td><td>0.08 (+10.42%)</td><td>0.08 (+8.61%)</td><td>0.06 (+6.31%)</td><td>0.01 (+17.53%)</td><td>191.50 (-5.94%)</td><td>160.76 (-9.33%)</td><td>153.20 (-7.93%)</td><td>135.30 (-13.99%)</td><td>21.41 (-4.76%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>203.60 (n/a)</td><td>177.30 (n/a)</td><td>166.40 (n/a)</td><td>157.30 (n/a)</td><td>22.48 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (+3.09%)</td><td>0.05 (+12.66%)</td><td>0.06 <b>(+31.19%)</b></td><td>0.03 (-13.05%)</td><td>0.01 <b>(+41.31%)</b></td><td>240.50 (+15.02%)</td><td>169.50 (-8.49%)</td><td>148.20 <b>(-23.80%)</b></td><td>130.40 (-2.98%)</td><td>47.08 <b>(+61.55%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.10 (n/a)</td><td>185.22 (n/a)</td><td>194.50 (n/a)</td><td>134.40 (n/a)</td><td>29.14 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.08 <b>(+35.77%)</b></td><td>0.07 <b>(+36.10%)</b></td><td>0.07 <b>(+23.48%)</b></td><td>0.06 <b>(+90.70%)</b></td><td>0.01 <b>(-34.02%)</b></td><td>161.10 <b>(-47.54%)</b></td><td>142.90 <b>(-29.56%)</b></td><td>143.50 (-19.02%)</td><td>123.70 <b>(-26.37%)</b></td><td>14.59 <b>(-75.21%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>307.10 (n/a)</td><td>202.86 (n/a)</td><td>177.20 (n/a)</td><td>168.00 (n/a)</td><td>58.87 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 <b>(+29.98%)</b></td><td>0.05 (+7.98%)</td><td>0.05 (+8.63%)</td><td>0.03 <b>(-36.12%)</b></td><td>0.02 <b>(+372.52%)</b></td><td>293.50 <b>(+56.53%)</b></td><td>178.50 (+1.48%)</td><td>163.50 (-7.94%)</td><td>124.40 <b>(-23.07%)</b></td><td>68.67 <b>(+466.30%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>187.50 (n/a)</td><td>175.90 (n/a)</td><td>177.60 (n/a)</td><td>161.70 (n/a)</td><td>12.13 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.09 <b>(+40.42%)</b></td><td>0.08 <b>(+36.74%)</b></td><td>0.08 <b>(+36.99%)</b></td><td>0.07 <b>(+32.54%)</b></td><td>0.01 <b>(+59.20%)</b></td><td>156.60 <b>(-24.57%)</b></td><td>131.70 <b>(-26.58%)</b></td><td>134.90 <b>(-27.00%)</b></td><td>108.90 <b>(-28.82%)</b></td><td>18.40 (-14.28%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>207.60 (n/a)</td><td>179.38 (n/a)</td><td>184.80 (n/a)</td><td>153.00 (n/a)</td><td>21.47 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.08 <b>(+38.81%)</b></td><td>0.06 <b>(+29.40%)</b></td><td>0.06 <b>(+34.31%)</b></td><td>0.05 <b>(+25.55%)</b></td><td>0.01 <b>(+55.55%)</b></td><td>163.30 <b>(-20.38%)</b></td><td>137.44 <b>(-22.11%)</b></td><td>140.10 <b>(-25.56%)</b></td><td>96.90 <b>(-27.96%)</b></td><td>24.98 (-13.76%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.10 (n/a)</td><td>176.46 (n/a)</td><td>188.20 (n/a)</td><td>134.50 (n/a)</td><td>28.97 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (+5.61%)</td><td>0.06 <b>(+22.84%)</b></td><td>0.06 <b>(+30.49%)</b></td><td>0.06 <b>(+42.76%)</b></td><td>0.01 <b>(-41.39%)</b></td><td>166.10 <b>(-29.95%)</b></td><td>152.06 <b>(-20.86%)</b></td><td>153.40 <b>(-23.34%)</b></td><td>126.80 (-5.30%)</td><td>15.17 <b>(-60.59%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>237.10 (n/a)</td><td>192.14 (n/a)</td><td>200.10 (n/a)</td><td>133.90 (n/a)</td><td>38.50 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.08 <b>(+45.39%)</b></td><td>0.05 (+5.82%)</td><td>0.05 (-1.40%)</td><td>0.03 <b>(-20.16%)</b></td><td>0.02 <b>(+399.26%)</b></td><td>236.30 <b>(+25.23%)</b></td><td>170.80 (+2.25%)</td><td>165.70 (+1.41%)</td><td>109.20 <b>(-31.19%)</b></td><td>53.56 <b>(+330.43%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>188.70 (n/a)</td><td>167.04 (n/a)</td><td>163.40 (n/a)</td><td>158.70 (n/a)</td><td>12.44 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.08 <b>(+34.84%)</b></td><td>0.06 <b>(+23.59%)</b></td><td>0.06 (+16.61%)</td><td>0.05 (+4.61%)</td><td>0.01 <b>(+236.42%)</b></td><td>184.50 (-4.40%)</td><td>149.74 (-16.57%)</td><td>154.50 (-14.26%)</td><td>117.20 <b>(-25.87%)</b></td><td>30.82 <b>(+135.80%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>193.00 (n/a)</td><td>179.48 (n/a)</td><td>180.20 (n/a)</td><td>158.10 (n/a)</td><td>13.07 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (+9.61%)</td><td>0.06 <b>(+25.76%)</b></td><td>0.06 <b>(+27.71%)</b></td><td>0.05 <b>(+31.04%)</b></td><td>0.01 <b>(-32.12%)</b></td><td>162.80 <b>(-23.68%)</b></td><td>145.48 <b>(-21.84%)</b></td><td>147.50 <b>(-21.67%)</b></td><td>125.30 (-8.74%)</td><td>14.60 <b>(-52.78%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.30 (n/a)</td><td>186.14 (n/a)</td><td>188.30 (n/a)</td><td>137.30 (n/a)</td><td>30.92 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (+9.71%)</td><td>0.05 <b>(+28.65%)</b></td><td>0.05 <b>(+30.17%)</b></td><td>0.05 <b>(+64.51%)</b></td><td>0.00 <b>(-54.18%)</b></td><td>189.70 <b>(-39.20%)</b></td><td>169.58 <b>(-24.96%)</b></td><td>166.80 <b>(-23.17%)</b></td><td>154.10 (-8.87%)</td><td>13.29 <b>(-75.03%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>312.00 (n/a)</td><td>226.00 (n/a)</td><td>217.10 (n/a)</td><td>169.10 (n/a)</td><td>53.24 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 <b>(+31.06%)</b></td><td>0.05 (+6.20%)</td><td>0.05 (+1.36%)</td><td>0.04 (-6.50%)</td><td>0.01 <b>(+193.07%)</b></td><td>204.90 (+6.94%)</td><td>170.00 (-3.56%)</td><td>166.70 (-1.36%)</td><td>125.40 <b>(-23.68%)</b></td><td>30.08 <b>(+133.92%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>191.60 (n/a)</td><td>176.28 (n/a)</td><td>169.00 (n/a)</td><td>164.30 (n/a)</td><td>12.86 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (+2.86%)</td><td>0.05 (+19.51%)</td><td>0.05 <b>(+28.14%)</b></td><td>0.02 (-13.43%)</td><td>0.01 (+11.33%)</td><td>371.00 (+15.50%)</td><td>207.90 (-13.40%)</td><td>174.40 <b>(-21.97%)</b></td><td>142.50 (-2.80%)</td><td>93.03 <b>(+30.90%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>321.20 (n/a)</td><td>240.06 (n/a)</td><td>223.50 (n/a)</td><td>146.60 (n/a)</td><td>71.07 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.05 (+9.39%)</td><td>0.04 (+8.60%)</td><td>0.05 <b>(+21.90%)</b></td><td>0.03 (-18.19%)</td><td>0.01 <b>(+122.36%)</b></td><td>296.50 <b>(+22.22%)</b></td><td>206.70 (-4.86%)</td><td>179.50 (-17.96%)</td><td>174.40 (-8.60%)</td><td>51.79 <b>(+150.75%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>242.60 (n/a)</td><td>217.26 (n/a)</td><td>218.80 (n/a)</td><td>190.80 (n/a)</td><td>20.65 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.12 (+1.18%)</td><td>0.11 (+9.67%)</td><td>0.11 (+3.88%)</td><td>0.10 <b>(+35.88%)</b></td><td>0.01 <b>(-38.49%)</b></td><td>169.70 <b>(-26.41%)</b></td><td>150.78 (-11.00%)</td><td>154.90 (-3.73%)</td><td>131.90 (-1.20%)</td><td>15.85 <b>(-57.04%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>230.60 (n/a)</td><td>169.42 (n/a)</td><td>160.90 (n/a)</td><td>133.50 (n/a)</td><td>36.89 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.19 (+16.25%)</td><td>0.16 (+10.47%)</td><td>0.16 (+7.93%)</td><td>0.13 (-4.57%)</td><td>0.03 <b>(+111.95%)</b></td><td>195.80 (+4.76%)</td><td>152.74 (-8.00%)</td><td>152.40 (-7.36%)</td><td>129.80 (-13.93%)</td><td>26.47 <b>(+89.82%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>186.90 (n/a)</td><td>166.02 (n/a)</td><td>164.50 (n/a)</td><td>150.80 (n/a)</td><td>13.95 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 (+19.46%)</td><td>0.12 <b>(+38.38%)</b></td><td>0.13 <b>(+44.07%)</b></td><td>0.10 <b>(+80.21%)</b></td><td>0.02 <b>(-21.47%)</b></td><td>163.90 <b>(-44.52%)</b></td><td>139.24 <b>(-30.39%)</b></td><td>130.00 <b>(-30.59%)</b></td><td>122.80 (-16.29%)</td><td>19.27 <b>(-65.63%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>295.40 (n/a)</td><td>200.04 (n/a)</td><td>187.30 (n/a)</td><td>146.70 (n/a)</td><td>56.08 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.16 <b>(+20.74%)</b></td><td>0.13 (+16.67%)</td><td>0.13 (+8.17%)</td><td>0.10 <b>(+58.60%)</b></td><td>0.03 (-9.92%)</td><td>205.10 <b>(-36.93%)</b></td><td>160.92 (-18.07%)</td><td>156.50 (-7.56%)</td><td>128.00 (-17.21%)</td><td>32.37 <b>(-55.29%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>325.20 (n/a)</td><td>196.42 (n/a)</td><td>169.30 (n/a)</td><td>154.60 (n/a)</td><td>72.41 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (-12.87%)</td><td>0.09 (-10.00%)</td><td>0.10 (-12.18%)</td><td>0.08 (-6.85%)</td><td>0.01 (-16.87%)</td><td>218.20 (+7.38%)</td><td>178.10 (+10.69%)</td><td>168.10 (+13.89%)</td><td>151.60 (+14.76%)</td><td>29.13 (+0.70%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>203.20 (n/a)</td><td>160.90 (n/a)</td><td>147.60 (n/a)</td><td>132.10 (n/a)</td><td>28.93 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.17 <b>(+32.44%)</b></td><td>0.13 <b>(+21.98%)</b></td><td>0.13 (+13.17%)</td><td>0.11 <b>(+52.90%)</b></td><td>0.02 (+3.52%)</td><td>186.40 <b>(-34.62%)</b></td><td>160.24 (-19.57%)</td><td>160.40 (-11.63%)</td><td>124.00 <b>(-24.48%)</b></td><td>23.11 <b>(-52.56%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>285.10 (n/a)</td><td>199.22 (n/a)</td><td>181.50 (n/a)</td><td>164.20 (n/a)</td><td>48.72 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (-2.99%)</td><td>0.08 (-9.56%)</td><td>0.08 (-15.55%)</td><td>0.06 (-16.49%)</td><td>0.02 <b>(+39.38%)</b></td><td>274.50 (+19.76%)</td><td>205.20 (+13.28%)</td><td>204.10 (+18.39%)</td><td>155.50 (+3.05%)</td><td>48.50 <b>(+64.68%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>229.20 (n/a)</td><td>181.14 (n/a)</td><td>172.40 (n/a)</td><td>150.90 (n/a)</td><td>29.45 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.15 <b>(+30.14%)</b></td><td>0.11 (+17.11%)</td><td>0.10 (+4.17%)</td><td>0.09 <b>(+27.18%)</b></td><td>0.03 <b>(+53.45%)</b></td><td>202.10 <b>(-21.39%)</b></td><td>173.62 (-13.76%)</td><td>185.10 (-4.04%)</td><td>119.80 <b>(-23.21%)</b></td><td>33.24 (-9.39%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>257.10 (n/a)</td><td>201.32 (n/a)</td><td>192.90 (n/a)</td><td>156.00 (n/a)</td><td>36.68 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 <b>(+30.71%)</b></td><td>0.10 <b>(+28.57%)</b></td><td>0.09 (+14.13%)</td><td>0.09 <b>(+60.30%)</b></td><td>0.01 (-16.45%)</td><td>174.90 <b>(-37.62%)</b></td><td>163.02 <b>(-24.17%)</b></td><td>172.50 (-12.35%)</td><td>129.50 <b>(-23.51%)</b></td><td>19.09 <b>(-60.52%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>280.40 (n/a)</td><td>214.98 (n/a)</td><td>196.80 (n/a)</td><td>169.30 (n/a)</td><td>48.34 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.14 (-18.30%)</td><td>0.11 (+10.43%)</td><td>0.11 (+15.98%)</td><td>0.09 <b>(+61.71%)</b></td><td>0.02 <b>(-61.48%)</b></td><td>198.00 <b>(-38.18%)</b></td><td>165.52 (-18.04%)</td><td>166.30 (-13.74%)</td><td>136.20 <b>(+22.37%)</b></td><td>22.27 <b>(-70.64%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>320.30 (n/a)</td><td>201.96 (n/a)</td><td>192.80 (n/a)</td><td>111.30 (n/a)</td><td>75.87 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (-7.86%)</td><td>0.09 (+1.39%)</td><td>0.09 (-6.99%)</td><td>0.05 (+10.30%)</td><td>0.02 (-12.44%)</td><td>303.80 (-9.34%)</td><td>199.22 (-3.96%)</td><td>184.80 (+7.50%)</td><td>143.90 (+8.52%)</td><td>65.40 (-17.96%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>335.10 (n/a)</td><td>207.44 (n/a)</td><td>171.90 (n/a)</td><td>132.60 (n/a)</td><td>79.72 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 <b>(+21.80%)</b></td><td>0.10 <b>(+34.01%)</b></td><td>0.10 <b>(+26.47%)</b></td><td>0.08 <b>(+51.23%)</b></td><td>0.02 (-13.11%)</td><td>228.20 <b>(-33.87%)</b></td><td>185.68 <b>(-27.79%)</b></td><td>168.40 <b>(-20.94%)</b></td><td>160.10 (-17.90%)</td><td>31.92 <b>(-54.23%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>345.10 (n/a)</td><td>257.14 (n/a)</td><td>213.00 (n/a)</td><td>195.00 (n/a)</td><td>69.75 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.10 (-14.69%)</td><td>0.08 (-5.75%)</td><td>0.08 (-5.14%)</td><td>0.06 (-1.46%)</td><td>0.01 <b>(-23.78%)</b></td><td>259.80 (+1.48%)</td><td>204.54 (+5.06%)</td><td>199.10 (+5.46%)</td><td>170.30 (+17.29%)</td><td>35.93 (-10.27%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>256.00 (n/a)</td><td>194.68 (n/a)</td><td>188.80 (n/a)</td><td>145.20 (n/a)</td><td>40.05 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.12 <b>(+30.48%)</b></td><td>0.09 <b>(+22.38%)</b></td><td>0.08 (+0.10%)</td><td>0.07 <b>(+36.77%)</b></td><td>0.02 <b>(+40.57%)</b></td><td>239.30 <b>(-26.89%)</b></td><td>196.00 (-18.08%)</td><td>211.60 (-0.09%)</td><td>148.20 <b>(-23.37%)</b></td><td>40.81 <b>(-24.02%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>327.30 (n/a)</td><td>239.26 (n/a)</td><td>211.80 (n/a)</td><td>193.40 (n/a)</td><td>53.71 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (+3.78%)</td><td>0.08 (-6.88%)</td><td>0.08 (-3.41%)</td><td>0.05 <b>(-37.19%)</b></td><td>0.02 <b>(+101.57%)</b></td><td>347.70 <b>(+59.20%)</b></td><td>223.56 (+13.92%)</td><td>203.60 (+3.51%)</td><td>154.90 (-3.61%)</td><td>73.20 <b>(+232.00%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>218.40 (n/a)</td><td>196.24 (n/a)</td><td>196.70 (n/a)</td><td>160.70 (n/a)</td><td>22.05 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.25 <b>(+21.80%)</b></td><td>0.19 (+2.58%)</td><td>0.18 (-4.94%)</td><td>0.17 (+6.44%)</td><td>0.04 <b>(+83.44%)</b></td><td>197.60 (-6.04%)</td><td>178.22 (-1.03%)</td><td>186.30 (+5.19%)</td><td>129.00 (-17.94%)</td><td>28.37 <b>(+38.60%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>210.30 (n/a)</td><td>180.08 (n/a)</td><td>177.10 (n/a)</td><td>157.20 (n/a)</td><td>20.47 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.27 (+9.24%)</td><td>0.23 <b>(+20.03%)</b></td><td>0.22 <b>(+32.98%)</b></td><td>0.19 (+16.78%)</td><td>0.03 (-16.36%)</td><td>169.50 (-14.35%)</td><td>143.66 (-17.79%)</td><td>147.00 <b>(-24.81%)</b></td><td>121.80 (-8.49%)</td><td>19.54 <b>(-37.08%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>197.90 (n/a)</td><td>174.74 (n/a)</td><td>195.50 (n/a)</td><td>133.10 (n/a)</td><td>31.05 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.32 (-0.17%)</td><td>0.29 (+19.27%)</td><td>0.30 (+13.81%)</td><td>0.25 <b>(+54.80%)</b></td><td>0.03 <b>(-58.55%)</b></td><td>163.70 <b>(-35.40%)</b></td><td>141.30 <b>(-20.74%)</b></td><td>137.20 (-12.16%)</td><td>129.50 (+0.15%)</td><td>13.95 <b>(-73.29%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.26 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>253.40 (n/a)</td><td>178.28 (n/a)</td><td>156.20 (n/a)</td><td>129.30 (n/a)</td><td>52.23 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.26 <b>(+40.80%)</b></td><td>0.22 <b>(+30.32%)</b></td><td>0.23 <b>(+34.10%)</b></td><td>0.16 (+1.15%)</td><td>0.04 <b>(+233.51%)</b></td><td>207.60 (-1.14%)</td><td>153.44 <b>(-21.26%)</b></td><td>142.70 <b>(-25.44%)</b></td><td>126.00 <b>(-28.97%)</b></td><td>31.99 <b>(+139.89%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>210.00 (n/a)</td><td>194.88 (n/a)</td><td>191.40 (n/a)</td><td>177.40 (n/a)</td><td>13.33 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.31 (-0.10%)</td><td>0.22 (-2.23%)</td><td>0.22 (-5.94%)</td><td>0.16 (-12.79%)</td><td>0.06 <b>(+21.19%)</b></td><td>259.20 (+14.69%)</td><td>191.50 (+4.42%)</td><td>190.20 (+6.32%)</td><td>134.30 (+0.15%)</td><td>47.93 <b>(+41.24%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>226.00 (n/a)</td><td>183.40 (n/a)</td><td>178.90 (n/a)</td><td>134.10 (n/a)</td><td>33.94 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.21 (-17.11%)</td><td>0.18 (-15.08%)</td><td>0.18 (-9.05%)</td><td>0.16 (-17.15%)</td><td>0.02 <b>(-21.73%)</b></td><td>205.70 <b>(+20.72%)</b></td><td>182.18 (+17.57%)</td><td>185.10 (+9.98%)</td><td>159.10 <b>(+20.71%)</b></td><td>22.35 (+12.07%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>170.40 (n/a)</td><td>154.96 (n/a)</td><td>168.30 (n/a)</td><td>131.80 (n/a)</td><td>19.95 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.30 (-2.32%)</td><td>0.22 (+7.40%)</td><td>0.22 (+19.18%)</td><td>0.15 (+14.24%)</td><td>0.06 (-9.91%)</td><td>238.10 (-12.46%)</td><td>181.00 (-8.35%)</td><td>167.30 (-16.10%)</td><td>123.30 (+2.41%)</td><td>48.46 (-14.71%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.31 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>272.00 (n/a)</td><td>197.48 (n/a)</td><td>199.40 (n/a)</td><td>120.40 (n/a)</td><td>56.82 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.25 (-2.31%)</td><td>0.20 (-9.91%)</td><td>0.20 (-11.27%)</td><td>0.13 <b>(-30.57%)</b></td><td>0.05 <b>(+67.16%)</b></td><td>262.00 <b>(+44.04%)</b></td><td>176.52 (+16.02%)</td><td>168.00 (+12.68%)</td><td>129.40 (+2.37%)</td><td>51.85 <b>(+150.67%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>181.90 (n/a)</td><td>152.14 (n/a)</td><td>149.10 (n/a)</td><td>126.40 (n/a)</td><td>20.68 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.24 (+8.49%)</td><td>0.20 (-0.71%)</td><td>0.18 (-9.37%)</td><td>0.17 (+2.64%)</td><td>0.03 <b>(+48.44%)</b></td><td>211.70 (-2.58%)</td><td>190.26 (+1.47%)</td><td>205.00 (+10.33%)</td><td>153.60 (-7.80%)</td><td>25.04 <b>(+32.63%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>217.30 (n/a)</td><td>187.50 (n/a)</td><td>185.80 (n/a)</td><td>166.60 (n/a)</td><td>18.88 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.25 <b>(+20.84%)</b></td><td>0.19 (+9.88%)</td><td>0.18 (+4.05%)</td><td>0.17 (+7.90%)</td><td>0.04 <b>(+55.58%)</b></td><td>197.50 (-7.32%)</td><td>174.20 (-8.07%)</td><td>177.30 (-3.90%)</td><td>129.50 (-17.20%)</td><td>26.95 (+15.19%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>213.10 (n/a)</td><td>189.50 (n/a)</td><td>184.50 (n/a)</td><td>156.40 (n/a)</td><td>23.39 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.28 <b>(+47.61%)</b></td><td>0.18 (+9.43%)</td><td>0.16 (-5.33%)</td><td>0.10 (-19.25%)</td><td>0.07 <b>(+167.87%)</b></td><td>334.10 <b>(+23.83%)</b></td><td>211.62 (-0.22%)</td><td>216.50 (+5.61%)</td><td>124.50 <b>(-32.23%)</b></td><td>78.96 <b>(+124.74%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>269.80 (n/a)</td><td>212.08 (n/a)</td><td>205.00 (n/a)</td><td>183.70 (n/a)</td><td>35.13 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.21 <b>(-28.87%)</b></td><td>0.17 (-11.56%)</td><td>0.15 (-17.29%)</td><td>0.14 <b>(+57.61%)</b></td><td>0.04 <b>(-53.29%)</b></td><td>240.00 <b>(-36.54%)</b></td><td>201.04 (-0.56%)</td><td>219.90 <b>(+20.96%)</b></td><td>156.40 <b>(+40.52%)</b></td><td>39.64 <b>(-61.59%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>378.20 (n/a)</td><td>202.18 (n/a)</td><td>181.80 (n/a)</td><td>111.30 (n/a)</td><td>103.21 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.21 (+8.39%)</td><td>0.18 (+1.39%)</td><td>0.19 (+8.08%)</td><td>0.11 <b>(-28.93%)</b></td><td>0.04 <b>(+167.53%)</b></td><td>304.20 <b>(+40.70%)</b></td><td>208.34 (+3.09%)</td><td>188.10 (-7.48%)</td><td>162.80 (-7.76%)</td><td>57.12 <b>(+253.97%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>216.20 (n/a)</td><td>202.10 (n/a)</td><td>203.30 (n/a)</td><td>176.50 (n/a)</td><td>16.14 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.19 (+11.57%)</td><td>0.18 (+13.61%)</td><td>0.18 (+16.07%)</td><td>0.15 (+6.85%)</td><td>0.02 <b>(+37.48%)</b></td><td>215.30 (-6.43%)</td><td>188.06 (-11.75%)</td><td>180.70 (-13.83%)</td><td>172.30 (-10.35%)</td><td>17.93 (+13.69%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>230.10 (n/a)</td><td>213.10 (n/a)</td><td>209.70 (n/a)</td><td>192.20 (n/a)</td><td>15.77 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.17 (+4.05%)</td><td>0.12 (-6.33%)</td><td>0.12 (-7.90%)</td><td>0.06 <b>(-35.91%)</b></td><td>0.04 <b>(+51.70%)</b></td><td>338.70 <b>(+56.01%)</b></td><td>190.74 (+16.30%)</td><td>173.50 (+8.57%)</td><td>120.30 (-3.91%)</td><td>85.76 <b>(+141.99%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>217.10 (n/a)</td><td>164.00 (n/a)</td><td>159.80 (n/a)</td><td>125.20 (n/a)</td><td>35.44 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.16 (+9.61%)</td><td>0.12 (-7.13%)</td><td>0.11 (-10.69%)</td><td>0.10 (-10.81%)</td><td>0.02 <b>(+73.80%)</b></td><td>213.90 (+12.11%)</td><td>178.66 (+9.54%)</td><td>181.40 (+11.98%)</td><td>130.80 (-8.72%)</td><td>30.04 <b>(+68.90%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>190.80 (n/a)</td><td>163.10 (n/a)</td><td>162.00 (n/a)</td><td>143.30 (n/a)</td><td>17.79 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.16 <b>(+25.85%)</b></td><td>0.13 <b>(+30.18%)</b></td><td>0.13 (+19.93%)</td><td>0.10 <b>(+75.04%)</b></td><td>0.02 (-18.56%)</td><td>195.10 <b>(-42.87%)</b></td><td>158.56 <b>(-26.71%)</b></td><td>161.40 (-16.63%)</td><td>131.10 <b>(-20.50%)</b></td><td>25.19 <b>(-64.91%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>341.50 (n/a)</td><td>216.36 (n/a)</td><td>193.60 (n/a)</td><td>164.90 (n/a)</td><td>71.78 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.16 (+18.90%)</td><td>0.14 (+16.61%)</td><td>0.15 <b>(+21.76%)</b></td><td>0.11 (+13.41%)</td><td>0.02 <b>(+55.03%)</b></td><td>181.30 (-11.82%)</td><td>148.14 (-13.64%)</td><td>136.20 (-17.90%)</td><td>129.60 (-15.84%)</td><td>22.19 (+11.56%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>205.60 (n/a)</td><td>171.54 (n/a)</td><td>165.90 (n/a)</td><td>154.00 (n/a)</td><td>19.89 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 (-16.46%)</td><td>0.10 (-16.90%)</td><td>0.10 (-16.65%)</td><td>0.09 (-6.38%)</td><td>0.02 <b>(-25.01%)</b></td><td>230.10 (+6.77%)</td><td>201.14 (+19.56%)</td><td>203.20 (+19.95%)</td><td>162.70 (+19.72%)</td><td>29.48 (-3.11%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>215.50 (n/a)</td><td>168.24 (n/a)</td><td>169.40 (n/a)</td><td>135.90 (n/a)</td><td>30.43 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.14 (-5.57%)</td><td>0.12 (+0.15%)</td><td>0.12 (+8.11%)</td><td>0.10 (-1.19%)</td><td>0.02 (+4.74%)</td><td>210.30 (+1.20%)</td><td>177.34 (+0.18%)</td><td>165.90 (-7.53%)</td><td>150.70 (+5.90%)</td><td>27.00 (+15.93%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>207.80 (n/a)</td><td>177.02 (n/a)</td><td>179.40 (n/a)</td><td>142.30 (n/a)</td><td>23.29 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.16 <b>(+23.96%)</b></td><td>0.11 (+0.55%)</td><td>0.10 (-16.57%)</td><td>0.09 (-4.64%)</td><td>0.03 <b>(+77.55%)</b></td><td>232.40 (+4.87%)</td><td>194.12 (+2.61%)</td><td>211.10 (+19.88%)</td><td>130.70 (-19.32%)</td><td>45.06 <b>(+51.04%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>221.60 (n/a)</td><td>189.18 (n/a)</td><td>176.10 (n/a)</td><td>162.00 (n/a)</td><td>29.83 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.12 (-8.35%)</td><td>0.10 (-5.13%)</td><td>0.10 (+6.01%)</td><td>0.06 <b>(-34.44%)</b></td><td>0.02 <b>(+46.05%)</b></td><td>361.40 <b>(+52.55%)</b></td><td>223.90 (+11.01%)</td><td>196.80 (-5.66%)</td><td>173.80 (+9.10%)</td><td>78.28 <b>(+152.35%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>236.90 (n/a)</td><td>201.70 (n/a)</td><td>208.60 (n/a)</td><td>159.30 (n/a)</td><td>31.02 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.20 (+13.95%)</td><td>0.16 <b>(+24.13%)</b></td><td>0.18 <b>(+31.08%)</b></td><td>0.12 <b>(+87.46%)</b></td><td>0.03 (-19.85%)</td><td>203.00 <b>(-46.65%)</b></td><td>154.74 <b>(-25.98%)</b></td><td>135.40 <b>(-23.72%)</b></td><td>123.90 (-12.25%)</td><td>34.23 <b>(-64.91%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>380.50 (n/a)</td><td>209.06 (n/a)</td><td>177.50 (n/a)</td><td>141.20 (n/a)</td><td>97.54 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.19 <b>(+23.05%)</b></td><td>0.15 (+15.88%)</td><td>0.16 <b>(+24.61%)</b></td><td>0.11 (+1.18%)</td><td>0.03 <b>(+69.34%)</b></td><td>217.30 (-1.14%)</td><td>164.70 (-12.18%)</td><td>154.90 (-19.74%)</td><td>130.40 (-18.75%)</td><td>33.65 <b>(+40.05%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>219.80 (n/a)</td><td>187.54 (n/a)</td><td>193.00 (n/a)</td><td>160.50 (n/a)</td><td>24.02 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.20 <b>(+40.71%)</b></td><td>0.16 (+17.43%)</td><td>0.16 (+16.49%)</td><td>0.12 (-3.52%)</td><td>0.04 <b>(+488.91%)</b></td><td>197.00 (+3.63%)</td><td>155.90 (-11.51%)</td><td>149.60 (-14.17%)</td><td>120.40 <b>(-28.93%)</b></td><td>34.93 <b>(+330.59%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>190.10 (n/a)</td><td>176.18 (n/a)</td><td>174.30 (n/a)</td><td>169.40 (n/a)</td><td>8.11 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.23 <b>(+22.56%)</b></td><td>0.15 (-5.60%)</td><td>0.13 (-18.95%)</td><td>0.10 <b>(-23.01%)</b></td><td>0.05 <b>(+95.51%)</b></td><td>255.80 <b>(+29.91%)</b></td><td>182.74 (+11.93%)</td><td>185.10 <b>(+23.40%)</b></td><td>109.20 (-18.39%)</td><td>52.68 <b>(+95.12%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>196.90 (n/a)</td><td>163.26 (n/a)</td><td>150.00 (n/a)</td><td>133.80 (n/a)</td><td>27.00 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 <b>(-28.10%)</b></td><td>0.13 (-10.67%)</td><td>0.13 (+6.89%)</td><td>0.12 (+12.19%)</td><td>0.01 <b>(-84.87%)</b></td><td>199.10 (-10.88%)</td><td>190.00 (+6.96%)</td><td>185.00 (-6.47%)</td><td>182.70 <b>(+39.15%)</b></td><td>8.08 <b>(-80.47%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>223.40 (n/a)</td><td>177.64 (n/a)</td><td>197.80 (n/a)</td><td>131.30 (n/a)</td><td>41.40 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.21 (+5.01%)</td><td>0.14 (-14.68%)</td><td>0.13 (-18.36%)</td><td>0.10 (-18.43%)</td><td>0.04 <b>(+35.12%)</b></td><td>247.50 <b>(+22.59%)</b></td><td>188.44 <b>(+21.17%)</b></td><td>183.80 <b>(+22.53%)</b></td><td>116.70 (-4.81%)</td><td>49.73 <b>(+54.86%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>201.90 (n/a)</td><td>155.52 (n/a)</td><td>150.00 (n/a)</td><td>122.60 (n/a)</td><td>32.11 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.15 (-4.86%)</td><td>0.13 (-6.01%)</td><td>0.13 (-10.63%)</td><td>0.11 (-10.54%)</td><td>0.02 <b>(+33.54%)</b></td><td>220.30 (+11.77%)</td><td>188.42 (+7.09%)</td><td>195.40 (+11.91%)</td><td>164.40 (+5.12%)</td><td>23.83 <b>(+52.27%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>197.10 (n/a)</td><td>175.94 (n/a)</td><td>174.60 (n/a)</td><td>156.40 (n/a)</td><td>15.65 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.16 (-7.41%)</td><td>0.14 (-4.67%)</td><td>0.14 (-13.00%)</td><td>0.13 (+12.50%)</td><td>0.01 <b>(-41.04%)</b></td><td>192.90 (-11.11%)</td><td>175.34 (+3.30%)</td><td>180.90 (+14.93%)</td><td>149.80 (+8.00%)</td><td>16.41 <b>(-45.18%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>217.00 (n/a)</td><td>169.74 (n/a)</td><td>157.40 (n/a)</td><td>138.70 (n/a)</td><td>29.94 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.15 (+3.38%)</td><td>0.12 (+0.15%)</td><td>0.14 <b>(+21.42%)</b></td><td>0.05 <b>(-49.24%)</b></td><td>0.04 <b>(+179.23%)</b></td><td>340.30 <b>(+97.05%)</b></td><td>177.92 (+13.89%)</td><td>129.80 (-17.64%)</td><td>126.70 (-3.21%)</td><td>91.99 <b>(+437.08%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>172.70 (n/a)</td><td>156.22 (n/a)</td><td>157.60 (n/a)</td><td>130.90 (n/a)</td><td>17.13 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.15 (-2.55%)</td><td>0.11 (-13.90%)</td><td>0.11 (-15.67%)</td><td>0.07 <b>(-34.38%)</b></td><td>0.03 <b>(+39.74%)</b></td><td>256.60 <b>(+52.38%)</b></td><td>173.30 <b>(+20.62%)</b></td><td>163.80 (+18.61%)</td><td>123.50 (+2.57%)</td><td>49.92 <b>(+124.31%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>168.40 (n/a)</td><td>143.68 (n/a)</td><td>138.10 (n/a)</td><td>120.40 (n/a)</td><td>22.25 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.14 (-4.94%)</td><td>0.11 (-3.78%)</td><td>0.11 (-9.39%)</td><td>0.10 <b>(+21.16%)</b></td><td>0.01 <b>(-44.74%)</b></td><td>183.70 (-17.48%)</td><td>162.16 (+0.77%)</td><td>164.00 (+10.36%)</td><td>133.20 (+5.21%)</td><td>18.26 <b>(-53.26%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>222.60 (n/a)</td><td>160.92 (n/a)</td><td>148.60 (n/a)</td><td>126.60 (n/a)</td><td>39.06 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.14 (-0.27%)</td><td>0.11 (-2.64%)</td><td>0.11 (-0.71%)</td><td>0.09 (+2.24%)</td><td>0.02 (+7.52%)</td><td>208.80 (-2.20%)</td><td>175.16 (+3.14%)</td><td>169.70 (+0.71%)</td><td>129.70 (+0.31%)</td><td>32.10 (+7.55%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>213.50 (n/a)</td><td>169.82 (n/a)</td><td>168.50 (n/a)</td><td>129.30 (n/a)</td><td>29.85 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.12 (+4.62%)</td><td>0.12 (+10.84%)</td><td>0.12 (+14.61%)</td><td>0.11 (+17.19%)</td><td>0.00 <b>(-47.78%)</b></td><td>165.60 (-14.68%)</td><td>155.88 (-10.21%)</td><td>152.70 (-12.74%)</td><td>150.70 (-4.44%)</td><td>6.41 <b>(-57.10%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>194.10 (n/a)</td><td>173.60 (n/a)</td><td>175.00 (n/a)</td><td>157.70 (n/a)</td><td>14.94 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.15 <b>(+23.50%)</b></td><td>0.11 (+10.60%)</td><td>0.10 (-2.70%)</td><td>0.09 <b>(+36.99%)</b></td><td>0.02 (+15.07%)</td><td>198.20 <b>(-27.00%)</b></td><td>169.88 (-10.54%)</td><td>179.80 (+2.74%)</td><td>122.80 (-19.00%)</td><td>29.40 <b>(-37.17%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>271.50 (n/a)</td><td>189.90 (n/a)</td><td>175.00 (n/a)</td><td>151.60 (n/a)</td><td>46.80 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 (+18.31%)</td><td>0.10 (-4.02%)</td><td>0.09 (-4.69%)</td><td>0.06 <b>(-34.25%)</b></td><td>0.03 <b>(+238.46%)</b></td><td>307.20 <b>(+52.08%)</b></td><td>203.90 (+11.12%)</td><td>196.40 (+4.91%)</td><td>139.60 (-15.50%)</td><td>63.84 <b>(+347.14%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>202.00 (n/a)</td><td>183.50 (n/a)</td><td>187.20 (n/a)</td><td>165.20 (n/a)</td><td>14.28 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.14 <b>(+23.50%)</b></td><td>0.10 (+6.31%)</td><td>0.09 (-9.97%)</td><td>0.08 <b>(+37.88%)</b></td><td>0.02 (+6.65%)</td><td>232.10 <b>(-27.47%)</b></td><td>187.90 (-7.91%)</td><td>195.30 (+11.09%)</td><td>135.20 (-19.04%)</td><td>39.12 <b>(-39.87%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>320.00 (n/a)</td><td>204.04 (n/a)</td><td>175.80 (n/a)</td><td>167.00 (n/a)</td><td>65.07 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.74 (-9.81%)</td><td>0.55 (-11.47%)</td><td>0.55 (-13.50%)</td><td>0.43 (-11.37%)</td><td>0.11 (-9.13%)</td><td>226.80 (+12.84%)</td><td>183.44 (+13.01%)</td><td>179.50 (+15.66%)</td><td>133.30 (+10.90%)</td><td>34.34 (+11.55%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.82 (n/a)</td><td>0.62 (n/a)</td><td>0.63 (n/a)</td><td>0.49 (n/a)</td><td>0.13 (n/a)</td><td>201.00 (n/a)</td><td>162.32 (n/a)</td><td>155.20 (n/a)</td><td>120.20 (n/a)</td><td>30.79 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.68 (+14.21%)</td><td>0.57 (+7.87%)</td><td>0.56 (+4.10%)</td><td>0.47 (+19.20%)</td><td>0.08 (+1.92%)</td><td>211.20 (-16.09%)</td><td>176.60 (-7.82%)</td><td>174.80 (-3.96%)</td><td>144.00 (-12.41%)</td><td>25.58 <b>(-26.94%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.60 (n/a)</td><td>0.52 (n/a)</td><td>0.54 (n/a)</td><td>0.39 (n/a)</td><td>0.08 (n/a)</td><td>251.70 (n/a)</td><td>191.58 (n/a)</td><td>182.00 (n/a)</td><td>164.40 (n/a)</td><td>35.01 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.69 (+13.68%)</td><td>0.59 (+12.88%)</td><td>0.62 <b>(+20.27%)</b></td><td>0.45 (+5.17%)</td><td>0.09 <b>(+22.02%)</b></td><td>217.30 (-4.90%)</td><td>168.86 (-11.00%)</td><td>157.50 (-16.84%)</td><td>142.60 (-12.03%)</td><td>28.89 (+6.41%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.61 (n/a)</td><td>0.53 (n/a)</td><td>0.52 (n/a)</td><td>0.43 (n/a)</td><td>0.07 (n/a)</td><td>228.50 (n/a)</td><td>189.74 (n/a)</td><td>189.40 (n/a)</td><td>162.10 (n/a)</td><td>27.15 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.69 (+16.08%)</td><td>0.53 (+1.63%)</td><td>0.50 (-8.09%)</td><td>0.43 (-1.00%)</td><td>0.11 <b>(+53.14%)</b></td><td>231.20 (+1.05%)</td><td>193.58 (+0.17%)</td><td>196.90 (+8.78%)</td><td>141.60 (-13.87%)</td><td>38.81 <b>(+34.81%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.60 (n/a)</td><td>0.52 (n/a)</td><td>0.54 (n/a)</td><td>0.43 (n/a)</td><td>0.07 (n/a)</td><td>228.80 (n/a)</td><td>193.26 (n/a)</td><td>181.00 (n/a)</td><td>164.40 (n/a)</td><td>28.79 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.52 <b>(-21.38%)</b></td><td>0.47 (-14.18%)</td><td>0.47 (-8.05%)</td><td>0.43 (-8.39%)</td><td>0.03 <b>(-59.34%)</b></td><td>172.50 (+9.18%)</td><td>156.94 (+15.11%)</td><td>155.80 (+8.72%)</td><td>142.40 <b>(+27.14%)</b></td><td>10.70 <b>(-42.94%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.66 (n/a)</td><td>0.55 (n/a)</td><td>0.51 (n/a)</td><td>0.47 (n/a)</td><td>0.08 (n/a)</td><td>158.00 (n/a)</td><td>136.34 (n/a)</td><td>143.30 (n/a)</td><td>112.00 (n/a)</td><td>18.76 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.69 <b>(+22.12%)</b></td><td>0.54 (+17.54%)</td><td>0.52 <b>(+20.09%)</b></td><td>0.43 <b>(+24.21%)</b></td><td>0.11 (+13.36%)</td><td>172.10 (-19.50%)</td><td>140.70 (-15.28%)</td><td>142.10 (-16.75%)</td><td>106.10 (-18.13%)</td><td>28.60 <b>(-21.22%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.57 (n/a)</td><td>0.46 (n/a)</td><td>0.43 (n/a)</td><td>0.34 (n/a)</td><td>0.10 (n/a)</td><td>213.80 (n/a)</td><td>166.08 (n/a)</td><td>170.70 (n/a)</td><td>129.60 (n/a)</td><td>36.31 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.49 (-11.73%)</td><td>0.42 (+8.96%)</td><td>0.40 (+12.83%)</td><td>0.39 <b>(+41.44%)</b></td><td>0.04 <b>(-63.61%)</b></td><td>190.80 <b>(-29.31%)</b></td><td>177.20 (-12.97%)</td><td>182.60 (-11.36%)</td><td>151.50 (+13.23%)</td><td>15.36 <b>(-70.99%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.55 (n/a)</td><td>0.38 (n/a)</td><td>0.36 (n/a)</td><td>0.27 (n/a)</td><td>0.11 (n/a)</td><td>269.90 (n/a)</td><td>203.60 (n/a)</td><td>206.00 (n/a)</td><td>133.80 (n/a)</td><td>52.95 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.51 (-16.99%)</td><td>0.39 (-1.30%)</td><td>0.40 (+10.32%)</td><td>0.22 (-9.84%)</td><td>0.11 <b>(-25.05%)</b></td><td>339.60 (+10.94%)</td><td>207.60 (-0.15%)</td><td>184.70 (-9.33%)</td><td>143.70 <b>(+20.45%)</b></td><td>76.09 (+10.02%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.62 (n/a)</td><td>0.39 (n/a)</td><td>0.36 (n/a)</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>306.10 (n/a)</td><td>207.92 (n/a)</td><td>203.70 (n/a)</td><td>119.30 (n/a)</td><td>69.16 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.34 (+16.89%)</td><td>0.28 <b>(+20.53%)</b></td><td>0.28 <b>(+33.76%)</b></td><td>0.25 <b>(+24.81%)</b></td><td>0.04 <b>(-22.07%)</b></td><td>148.30 (-19.88%)</td><td>130.86 (-18.36%)</td><td>132.80 <b>(-25.27%)</b></td><td>107.40 (-14.42%)</td><td>14.74 <b>(-48.11%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>185.10 (n/a)</td><td>160.28 (n/a)</td><td>177.70 (n/a)</td><td>125.50 (n/a)</td><td>28.41 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.34 (+18.59%)</td><td>0.22 (-3.91%)</td><td>0.24 (-3.16%)</td><td>0.10 <b>(-35.75%)</b></td><td>0.09 <b>(+62.91%)</b></td><td>361.80 <b>(+55.68%)</b></td><td>199.24 (+16.56%)</td><td>156.80 (+3.23%)</td><td>108.70 (-15.74%)</td><td>99.11 <b>(+122.18%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>232.40 (n/a)</td><td>170.94 (n/a)</td><td>151.90 (n/a)</td><td>129.00 (n/a)</td><td>44.61 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.29 (+17.93%)</td><td>0.22 (+9.67%)</td><td>0.22 (+4.77%)</td><td>0.18 <b>(+21.36%)</b></td><td>0.04 (+15.69%)</td><td>208.50 (-17.62%)</td><td>168.84 (-9.15%)</td><td>166.60 (-4.58%)</td><td>126.80 (-15.18%)</td><td>30.04 <b>(-23.78%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>253.10 (n/a)</td><td>185.84 (n/a)</td><td>174.60 (n/a)</td><td>149.50 (n/a)</td><td>39.41 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.29 (-2.04%)</td><td>0.20 (-12.08%)</td><td>0.18 <b>(-22.89%)</b></td><td>0.15 (-10.45%)</td><td>0.06 (+6.19%)</td><td>239.70 (+11.70%)</td><td>193.44 (+15.20%)</td><td>203.90 <b>(+29.71%)</b></td><td>128.00 (+2.07%)</td><td>49.18 <b>(+21.32%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>214.60 (n/a)</td><td>167.92 (n/a)</td><td>157.20 (n/a)</td><td>125.40 (n/a)</td><td>40.54 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.24 <b>(-22.25%)</b></td><td>0.21 (-5.45%)</td><td>0.21 (+7.06%)</td><td>0.20 (+13.17%)</td><td>0.02 <b>(-70.42%)</b></td><td>188.70 (-11.62%)</td><td>174.80 (+1.12%)</td><td>174.60 (-6.58%)</td><td>153.50 <b>(+28.67%)</b></td><td>13.51 <b>(-66.85%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>213.50 (n/a)</td><td>172.86 (n/a)</td><td>186.90 (n/a)</td><td>119.30 (n/a)</td><td>40.74 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.21 <b>(-22.37%)</b></td><td>0.20 <b>(-20.41%)</b></td><td>0.20 <b>(-22.27%)</b></td><td>0.19 (-11.83%)</td><td>0.01 <b>(-66.11%)</b></td><td>190.20 (+13.42%)</td><td>184.50 <b>(+25.15%)</b></td><td>186.10 <b>(+28.61%)</b></td><td>178.00 <b>(+28.80%)</b></td><td>5.69 <b>(-51.18%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.02 (n/a)</td><td>167.70 (n/a)</td><td>147.42 (n/a)</td><td>144.70 (n/a)</td><td>138.20 (n/a)</td><td>11.66 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.24 (-9.83%)</td><td>0.19 (-12.04%)</td><td>0.19 (-9.68%)</td><td>0.15 <b>(-21.26%)</b></td><td>0.04 <b>(+34.24%)</b></td><td>246.40 <b>(+26.94%)</b></td><td>197.46 (+16.23%)</td><td>194.80 (+10.74%)</td><td>151.70 (+10.89%)</td><td>41.84 <b>(+92.09%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>194.10 (n/a)</td><td>169.88 (n/a)</td><td>175.90 (n/a)</td><td>136.80 (n/a)</td><td>21.78 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.28 (+14.80%)</td><td>0.21 (-1.67%)</td><td>0.21 (-5.32%)</td><td>0.16 (-0.49%)</td><td>0.04 <b>(+28.84%)</b></td><td>237.60 (+0.51%)</td><td>180.30 (+2.70%)</td><td>172.20 (+5.58%)</td><td>132.10 (-12.86%)</td><td>38.19 (+9.93%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>236.40 (n/a)</td><td>175.56 (n/a)</td><td>163.10 (n/a)</td><td>151.60 (n/a)</td><td>34.74 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.34 (-0.41%)</td><td>0.27 (-0.51%)</td><td>0.28 (+3.59%)</td><td>0.17 (-19.56%)</td><td>0.07 (+16.47%)</td><td>236.30 <b>(+24.30%)</b></td><td>160.22 (+2.84%)</td><td>148.10 (-3.46%)</td><td>119.80 (+0.42%)</td><td>47.02 <b>(+42.41%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.34 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.06 (n/a)</td><td>190.10 (n/a)</td><td>155.80 (n/a)</td><td>153.40 (n/a)</td><td>119.30 (n/a)</td><td>33.02 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.31 (-7.81%)</td><td>0.24 (-1.51%)</td><td>0.24 (+4.34%)</td><td>0.20 (-1.00%)</td><td>0.04 <b>(-20.57%)</b></td><td>205.00 (+1.03%)</td><td>171.62 (+0.60%)</td><td>169.80 (-4.18%)</td><td>130.90 (+8.45%)</td><td>27.36 (-11.22%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>202.90 (n/a)</td><td>170.60 (n/a)</td><td>177.20 (n/a)</td><td>120.70 (n/a)</td><td>30.82 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.32 (+3.96%)</td><td>0.25 (-4.90%)</td><td>0.23 (-13.60%)</td><td>0.17 (-19.50%)</td><td>0.06 <b>(+30.51%)</b></td><td>245.00 <b>(+24.24%)</b></td><td>174.16 (+7.93%)</td><td>175.30 (+15.71%)</td><td>127.10 (-3.79%)</td><td>46.63 <b>(+52.84%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>197.20 (n/a)</td><td>161.36 (n/a)</td><td>151.50 (n/a)</td><td>132.10 (n/a)</td><td>30.51 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.34 (+4.25%)</td><td>0.26 (+7.73%)</td><td>0.23 (-0.42%)</td><td>0.20 (+2.29%)</td><td>0.06 <b>(+23.66%)</b></td><td>206.60 (-2.22%)</td><td>166.76 (-5.83%)</td><td>176.40 (+0.40%)</td><td>121.50 (-4.03%)</td><td>38.22 (+18.25%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>211.30 (n/a)</td><td>177.08 (n/a)</td><td>175.70 (n/a)</td><td>126.60 (n/a)</td><td>32.32 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.30 (-6.17%)</td><td>0.24 (-13.62%)</td><td>0.22 (-16.58%)</td><td>0.20 (-6.54%)</td><td>0.04 (-12.46%)</td><td>203.50 (+6.99%)</td><td>177.72 (+15.46%)</td><td>185.30 (+19.94%)</td><td>135.40 (+6.53%)</td><td>27.03 (+1.19%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.05 (n/a)</td><td>190.20 (n/a)</td><td>153.92 (n/a)</td><td>154.50 (n/a)</td><td>127.10 (n/a)</td><td>26.71 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.33 (+2.27%)</td><td>0.26 (-2.31%)</td><td>0.24 (-9.42%)</td><td>0.18 (-15.28%)</td><td>0.06 (+19.34%)</td><td>229.80 (+18.03%)</td><td>166.00 (+4.22%)</td><td>171.50 (+10.36%)</td><td>124.80 (-2.19%)</td><td>42.43 <b>(+34.04%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>194.70 (n/a)</td><td>159.28 (n/a)</td><td>155.40 (n/a)</td><td>127.60 (n/a)</td><td>31.65 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.29 (+6.61%)</td><td>0.23 (-7.99%)</td><td>0.25 (-6.68%)</td><td>0.18 (-2.31%)</td><td>0.05 <b>(+29.80%)</b></td><td>230.50 (+2.35%)</td><td>184.90 (+10.43%)</td><td>163.10 (+7.16%)</td><td>141.20 (-6.24%)</td><td>42.06 <b>(+29.76%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>225.20 (n/a)</td><td>167.44 (n/a)</td><td>152.20 (n/a)</td><td>150.60 (n/a)</td><td>32.42 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.31 (+14.52%)</td><td>0.24 (-6.57%)</td><td>0.21 (-17.97%)</td><td>0.19 (-7.47%)</td><td>0.05 <b>(+73.13%)</b></td><td>214.70 (+8.11%)</td><td>178.86 (+8.93%)</td><td>190.50 <b>(+21.88%)</b></td><td>131.60 (-12.67%)</td><td>31.36 <b>(+57.93%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>198.60 (n/a)</td><td>164.20 (n/a)</td><td>156.30 (n/a)</td><td>150.70 (n/a)</td><td>19.86 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.27 (+4.70%)</td><td>0.21 (-10.86%)</td><td>0.18 <b>(-24.59%)</b></td><td>0.17 (-17.27%)</td><td>0.05 <b>(+130.47%)</b></td><td>206.70 <b>(+20.88%)</b></td><td>174.78 (+16.07%)</td><td>193.10 <b>(+32.62%)</b></td><td>129.00 (-4.52%)</td><td>37.52 <b>(+167.83%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>171.00 (n/a)</td><td>150.58 (n/a)</td><td>145.60 (n/a)</td><td>135.10 (n/a)</td><td>14.01 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.29 (-2.99%)</td><td>0.25 <b>(+20.13%)</b></td><td>0.26 (+18.42%)</td><td>0.18 <b>(+105.28%)</b></td><td>0.04 <b>(-48.18%)</b></td><td>189.20 <b>(-51.27%)</b></td><td>145.28 <b>(-27.56%)</b></td><td>135.00 (-15.57%)</td><td>121.10 (+3.06%)</td><td>26.38 <b>(-75.50%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>388.30 (n/a)</td><td>200.56 (n/a)</td><td>159.90 (n/a)</td><td>117.50 (n/a)</td><td>107.70 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.28 (+1.83%)</td><td>0.21 (+3.29%)</td><td>0.20 (+2.78%)</td><td>0.17 (+6.21%)</td><td>0.04 (-1.04%)</td><td>206.90 (-5.83%)</td><td>174.14 (-3.42%)</td><td>177.40 (-2.69%)</td><td>125.20 (-1.80%)</td><td>31.16 (-6.94%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>219.70 (n/a)</td><td>180.30 (n/a)</td><td>182.30 (n/a)</td><td>127.50 (n/a)</td><td>33.49 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.28 (-0.51%)</td><td>0.23 (+15.58%)</td><td>0.23 <b>(+29.78%)</b></td><td>0.16 <b>(+64.51%)</b></td><td>0.04 <b>(-37.26%)</b></td><td>212.80 <b>(-39.22%)</b></td><td>159.64 <b>(-21.16%)</b></td><td>149.40 <b>(-22.91%)</b></td><td>123.60 (+0.49%)</td><td>33.68 <b>(-61.96%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>350.10 (n/a)</td><td>202.48 (n/a)</td><td>193.80 (n/a)</td><td>123.00 (n/a)</td><td>88.53 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.25 (-6.85%)</td><td>0.20 (-8.98%)</td><td>0.20 (-13.55%)</td><td>0.18 (-1.91%)</td><td>0.03 <b>(-22.21%)</b></td><td>196.40 (+1.97%)</td><td>173.88 (+8.95%)</td><td>173.20 (+15.70%)</td><td>137.90 (+7.40%)</td><td>22.56 (-18.04%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>192.60 (n/a)</td><td>159.60 (n/a)</td><td>149.70 (n/a)</td><td>128.40 (n/a)</td><td>27.52 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.23 (+19.56%)</td><td>0.19 (+13.21%)</td><td>0.20 (+17.25%)</td><td>0.15 (-6.21%)</td><td>0.03 <b>(+120.27%)</b></td><td>234.30 (+6.60%)</td><td>184.06 (-10.04%)</td><td>178.40 (-14.72%)</td><td>151.20 (-16.33%)</td><td>32.88 <b>(+95.03%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>219.80 (n/a)</td><td>204.60 (n/a)</td><td>209.20 (n/a)</td><td>180.70 (n/a)</td><td>16.86 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.22 (-17.57%)</td><td>0.20 (-5.07%)</td><td>0.20 (+0.64%)</td><td>0.18 (+11.19%)</td><td>0.02 <b>(-56.22%)</b></td><td>198.40 (-10.10%)</td><td>176.86 (+2.58%)</td><td>174.60 (-0.63%)</td><td>157.60 <b>(+21.32%)</b></td><td>16.96 <b>(-51.80%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>220.70 (n/a)</td><td>172.42 (n/a)</td><td>175.70 (n/a)</td><td>129.90 (n/a)</td><td>35.18 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.21 <b>(-21.35%)</b></td><td>0.17 <b>(-22.25%)</b></td><td>0.18 <b>(-20.06%)</b></td><td>0.11 <b>(-40.46%)</b></td><td>0.04 (+11.90%)</td><td>315.30 <b>(+67.98%)</b></td><td>213.64 <b>(+32.40%)</b></td><td>195.20 <b>(+25.05%)</b></td><td>169.80 <b>(+27.19%)</b></td><td>57.87 <b>(+148.32%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>187.70 (n/a)</td><td>161.36 (n/a)</td><td>156.10 (n/a)</td><td>133.50 (n/a)</td><td>23.30 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>1.01 (-9.20%)</td><td>0.82 (+4.85%)</td><td>0.84 <b>(+28.52%)</b></td><td>0.66 (+2.93%)</td><td>0.15 <b>(-27.51%)</b></td><td>200.10 (-2.82%)</td><td>163.58 (-6.63%)</td><td>156.20 <b>(-22.17%)</b></td><td>130.00 (+10.17%)</td><td>30.52 <b>(-23.50%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>1.11 (n/a)</td><td>0.79 (n/a)</td><td>0.65 (n/a)</td><td>0.64 (n/a)</td><td>0.21 (n/a)</td><td>205.90 (n/a)</td><td>175.20 (n/a)</td><td>200.70 (n/a)</td><td>118.00 (n/a)</td><td>39.90 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.95 (-3.50%)</td><td>0.85 (+9.42%)</td><td>0.90 (+14.93%)</td><td>0.63 (+6.37%)</td><td>0.13 (-18.71%)</td><td>208.20 (-6.00%)</td><td>157.16 (-9.64%)</td><td>146.00 (-12.99%)</td><td>137.60 (+3.61%)</td><td>29.01 (-19.06%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.99 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.59 (n/a)</td><td>0.16 (n/a)</td><td>221.50 (n/a)</td><td>173.92 (n/a)</td><td>167.80 (n/a)</td><td>132.80 (n/a)</td><td>35.84 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.92 (+8.90%)</td><td>0.79 (+7.04%)</td><td>0.76 (+6.52%)</td><td>0.73 (+6.52%)</td><td>0.07 (+19.43%)</td><td>178.40 (-6.11%)</td><td>167.34 (-6.46%)</td><td>171.70 (-6.12%)</td><td>143.10 (-8.15%)</td><td>13.94 (+2.23%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.84 (n/a)</td><td>0.74 (n/a)</td><td>0.72 (n/a)</td><td>0.69 (n/a)</td><td>0.06 (n/a)</td><td>190.00 (n/a)</td><td>178.90 (n/a)</td><td>182.90 (n/a)</td><td>155.80 (n/a)</td><td>13.63 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (+17.81%)</td><td>0.02 (+4.70%)</td><td>0.03 (+8.48%)</td><td>0.02 <b>(-21.26%)</b></td><td>0.00 <b>(+704.65%)</b></td><td>232.10 <b>(+27.04%)</b></td><td>173.82 (-2.02%)</td><td>163.10 (-7.80%)</td><td>146.60 (-15.11%)</td><td>33.98 <b>(+798.04%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>182.70 (n/a)</td><td>177.40 (n/a)</td><td>176.90 (n/a)</td><td>172.70 (n/a)</td><td>3.78 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (+15.58%)</td><td>0.03 (+10.72%)</td><td>0.02 (+10.75%)</td><td>0.02 (-6.04%)</td><td>0.01 <b>(+51.63%)</b></td><td>225.10 (+6.43%)</td><td>168.24 (-7.93%)</td><td>164.90 (-9.74%)</td><td>125.00 (-13.43%)</td><td>36.73 <b>(+42.20%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.50 (n/a)</td><td>182.74 (n/a)</td><td>182.70 (n/a)</td><td>144.40 (n/a)</td><td>25.83 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 <b>(+20.03%)</b></td><td>0.03 (+15.75%)</td><td>0.02 (+15.41%)</td><td>0.02 (-5.01%)</td><td>0.01 <b>(+94.95%)</b></td><td>243.60 (+5.27%)</td><td>170.82 (-10.93%)</td><td>165.20 (-13.37%)</td><td>135.40 (-16.68%)</td><td>43.58 <b>(+70.35%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>231.40 (n/a)</td><td>191.78 (n/a)</td><td>190.70 (n/a)</td><td>162.50 (n/a)</td><td>25.58 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>16.33 (+4.35%)</td><td>13.89 (+3.96%)</td><td>12.93 (-13.49%)</td><td>11.40 (+17.75%)</td><td>2.16 <b>(-20.04%)</b></td><td>184.10 (-15.08%)</td><td>153.94 (-5.50%)</td><td>162.30 (+15.60%)</td><td>128.50 (-4.18%)</td><td>23.61 <b>(-35.71%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>15.64 (n/a)</td><td>13.36 (n/a)</td><td>14.94 (n/a)</td><td>9.68 (n/a)</td><td>2.70 (n/a)</td><td>216.80 (n/a)</td><td>162.90 (n/a)</td><td>140.40 (n/a)</td><td>134.10 (n/a)</td><td>36.73 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>1.05 <b>(+33.76%)</b></td><td>0.89 <b>(+33.50%)</b></td><td>0.87 <b>(+22.90%)</b></td><td>0.72 <b>(+36.00%)</b></td><td>0.15 <b>(+46.29%)</b></td><td>182.30 <b>(-26.46%)</b></td><td>151.98 <b>(-24.87%)</b></td><td>152.00 (-18.63%)</td><td>125.90 <b>(-25.24%)</b></td><td>25.89 <b>(-21.88%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.78 (n/a)</td><td>0.67 (n/a)</td><td>0.71 (n/a)</td><td>0.53 (n/a)</td><td>0.10 (n/a)</td><td>247.90 (n/a)</td><td>202.30 (n/a)</td><td>186.80 (n/a)</td><td>168.40 (n/a)</td><td>33.14 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>1.05 <b>(+32.49%)</b></td><td>0.81 (+13.75%)</td><td>0.82 (+13.59%)</td><td>0.62 (+2.93%)</td><td>0.16 <b>(+119.21%)</b></td><td>213.80 (-2.86%)</td><td>167.28 (-10.16%)</td><td>160.10 (-11.98%)</td><td>125.70 <b>(-24.50%)</b></td><td>32.71 <b>(+58.47%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.79 (n/a)</td><td>0.72 (n/a)</td><td>0.73 (n/a)</td><td>0.60 (n/a)</td><td>0.07 (n/a)</td><td>220.10 (n/a)</td><td>186.20 (n/a)</td><td>181.90 (n/a)</td><td>166.50 (n/a)</td><td>20.64 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.99 (+19.01%)</td><td>0.80 <b>(+22.93%)</b></td><td>0.83 <b>(+38.95%)</b></td><td>0.61 (+18.00%)</td><td>0.15 (+5.44%)</td><td>216.80 (-15.25%)</td><td>169.54 (-19.19%)</td><td>158.50 <b>(-28.02%)</b></td><td>133.10 (-15.97%)</td><td>32.16 <b>(-23.58%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.83 (n/a)</td><td>0.65 (n/a)</td><td>0.60 (n/a)</td><td>0.52 (n/a)</td><td>0.14 (n/a)</td><td>255.80 (n/a)</td><td>209.80 (n/a)</td><td>220.20 (n/a)</td><td>158.40 (n/a)</td><td>42.08 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>1.13 <b>(+36.87%)</b></td><td>0.94 <b>(+25.75%)</b></td><td>0.92 (+18.88%)</td><td>0.72 (+17.88%)</td><td>0.17 <b>(+109.01%)</b></td><td>182.80 (-15.13%)</td><td>143.78 (-19.17%)</td><td>143.10 (-15.87%)</td><td>117.30 <b>(-26.92%)</b></td><td>26.72 <b>(+24.03%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.82 (n/a)</td><td>0.75 (n/a)</td><td>0.78 (n/a)</td><td>0.61 (n/a)</td><td>0.08 (n/a)</td><td>215.40 (n/a)</td><td>177.88 (n/a)</td><td>170.10 (n/a)</td><td>160.50 (n/a)</td><td>21.54 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>1.03 <b>(+25.85%)</b></td><td>0.84 <b>(+24.99%)</b></td><td>0.84 <b>(+33.69%)</b></td><td>0.63 (+12.23%)</td><td>0.18 <b>(+52.19%)</b></td><td>208.40 (-10.90%)</td><td>163.94 (-18.87%)</td><td>156.90 <b>(-25.18%)</b></td><td>127.70 <b>(-20.54%)</b></td><td>35.62 (+6.11%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.82 (n/a)</td><td>0.67 (n/a)</td><td>0.63 (n/a)</td><td>0.56 (n/a)</td><td>0.12 (n/a)</td><td>233.90 (n/a)</td><td>202.08 (n/a)</td><td>209.70 (n/a)</td><td>160.70 (n/a)</td><td>33.57 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (+1.11%)</td><td>0.03 <b>(+23.23%)</b></td><td>0.03 <b>(+40.72%)</b></td><td>0.02 (-5.00%)</td><td>0.01 (+1.25%)</td><td>239.00 (+5.29%)</td><td>156.46 (-18.29%)</td><td>142.70 <b>(-28.97%)</b></td><td>119.40 (-1.16%)</td><td>47.88 (+13.56%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>227.00 (n/a)</td><td>191.48 (n/a)</td><td>200.90 (n/a)</td><td>120.80 (n/a)</td><td>42.17 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (+19.65%)</td><td>0.03 <b>(+29.98%)</b></td><td>0.03 <b>(+29.29%)</b></td><td>0.03 <b>(+34.35%)</b></td><td>0.00 (-15.19%)</td><td>155.60 <b>(-25.55%)</b></td><td>134.66 <b>(-24.14%)</b></td><td>133.70 <b>(-22.63%)</b></td><td>114.20 (-16.46%)</td><td>15.83 <b>(-48.60%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.00 (n/a)</td><td>177.52 (n/a)</td><td>172.80 (n/a)</td><td>136.70 (n/a)</td><td>30.80 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.00 (-2.27%)</td><td>0.00 (-1.42%)</td><td>0.00 (-2.33%)</td><td>0.00 (-2.56%)</td><td>0.00 (-4.35%)</td><td>1065.68 (+0.62%)</td><td>982.89 (+1.08%)</td><td>969.53 (+2.50%)</td><td>950.49 (+2.74%)</td><td>46.99 (-13.28%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1059.09 (n/a)</td><td>972.42 (n/a)</td><td>945.86 (n/a)</td><td>925.17 (n/a)</td><td>54.18 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.01 (+1.19%)</td><td>0.01 (+1.75%)</td><td>0.01 (+1.27%)</td><td>0.01 (+4.05%)</td><td>0.00 (-17.45%)</td><td>1063.55 (-3.72%)</td><td>1009.58 (-1.70%)</td><td>1023.40 (-0.80%)</td><td>964.41 (-1.64%)</td><td>41.38 (-18.61%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1104.59 (n/a)</td><td>1027.06 (n/a)</td><td>1031.70 (n/a)</td><td>980.46 (n/a)</td><td>50.84 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.98 (+0.66%)</td><td>0.97 (+2.10%)</td><td>0.97 (+2.21%)</td><td>0.95 (+2.62%)</td><td>0.01 <b>(-34.13%)</b></td><td>2205.73 (-2.56%)</td><td>2166.42 (-2.07%)</td><td>2166.78 (-2.16%)</td><td>2141.55 (-0.65%)</td><td>24.51 <b>(-36.16%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.97 (n/a)</td><td>0.95 (n/a)</td><td>0.95 (n/a)</td><td>0.93 (n/a)</td><td>0.02 (n/a)</td><td>2263.62 (n/a)</td><td>2212.11 (n/a)</td><td>2214.51 (n/a)</td><td>2155.49 (n/a)</td><td>38.40 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.42 (+8.81%)</td><td>0.40 (+5.19%)</td><td>0.40 (+3.87%)</td><td>0.39 (+3.26%)</td><td>0.01 <b>(+225.82%)</b></td><td>1345.32 (-3.17%)</td><td>1301.22 (-4.89%)</td><td>1311.24 (-3.74%)</td><td>1248.84 (-8.11%)</td><td>35.68 <b>(+189.22%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.38 (n/a)</td><td>0.38 (n/a)</td><td>0.00 (n/a)</td><td>1389.32 (n/a)</td><td>1368.19 (n/a)</td><td>1362.24 (n/a)</td><td>1359.12 (n/a)</td><td>12.34 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.27 (+1.17%)</td><td>0.25 (-0.33%)</td><td>0.25 (-1.87%)</td><td>0.24 (-1.63%)</td><td>0.01 <b>(+25.77%)</b></td><td>2172.68 (+1.67%)</td><td>2067.21 (+0.38%)</td><td>2076.18 (+1.89%)</td><td>1960.40 (-1.16%)</td><td>78.88 <b>(+25.94%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.01 (n/a)</td><td>2137.08 (n/a)</td><td>2059.43 (n/a)</td><td>2037.66 (n/a)</td><td>1983.32 (n/a)</td><td>62.63 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.38 (+0.90%)</td><td>0.37 (+0.03%)</td><td>0.37 (-1.16%)</td><td>0.37 (+1.95%)</td><td>0.01 (-11.49%)</td><td>1435.30 (-1.92%)</td><td>1418.68 (-0.03%)</td><td>1427.39 (+1.17%)</td><td>1373.30 (-0.88%)</td><td>25.67 (-14.53%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.01 (n/a)</td><td>1463.44 (n/a)</td><td>1419.09 (n/a)</td><td>1410.92 (n/a)</td><td>1385.54 (n/a)</td><td>30.04 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/transpose</summary>


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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>5.69 (-3.19%)</td><td>4.68 (-2.70%)</td><td>4.46 (-5.67%)</td><td>3.89 (+3.54%)</td><td>0.78 (-19.37%)</td><td>269.60 (-3.40%)</td><td>229.24 (+1.63%)</td><td>235.30 (+5.99%)</td><td>184.30 (+3.31%)</td><td>36.99 (-18.94%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>5.88 (n/a)</td><td>4.81 (n/a)</td><td>4.72 (n/a)</td><td>3.76 (n/a)</td><td>0.97 (n/a)</td><td>279.10 (n/a)</td><td>225.56 (n/a)</td><td>222.00 (n/a)</td><td>178.40 (n/a)</td><td>45.64 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>4.97 (-9.96%)</td><td>4.16 (-14.78%)</td><td>4.24 (-10.80%)</td><td>3.02 <b>(-33.90%)</b></td><td>0.72 <b>(+94.07%)</b></td><td>347.10 <b>(+51.31%)</b></td><td>259.10 <b>(+20.15%)</b></td><td>247.00 (+12.12%)</td><td>211.10 (+11.05%)</td><td>52.15 <b>(+242.17%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>5.52 (n/a)</td><td>4.88 (n/a)</td><td>4.76 (n/a)</td><td>4.57 (n/a)</td><td>0.37 (n/a)</td><td>229.40 (n/a)</td><td>215.64 (n/a)</td><td>220.30 (n/a)</td><td>190.10 (n/a)</td><td>15.24 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>5.93 (+4.54%)</td><td>5.03 (+11.96%)</td><td>5.16 <b>(+22.08%)</b></td><td>3.92 (+19.34%)</td><td>0.87 (-13.86%)</td><td>267.20 (-16.21%)</td><td>213.82 (-12.11%)</td><td>203.10 (-18.07%)</td><td>176.90 (-4.38%)</td><td>39.02 <b>(-29.67%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>5.67 (n/a)</td><td>4.49 (n/a)</td><td>4.23 (n/a)</td><td>3.29 (n/a)</td><td>1.01 (n/a)</td><td>318.90 (n/a)</td><td>243.28 (n/a)</td><td>247.90 (n/a)</td><td>185.00 (n/a)</td><td>55.48 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>6.24 (-10.26%)</td><td>4.85 (-1.59%)</td><td>4.58 (-1.91%)</td><td>3.84 (-1.69%)</td><td>0.92 <b>(-22.28%)</b></td><td>273.20 (+1.71%)</td><td>222.16 (+0.51%)</td><td>229.00 (+1.96%)</td><td>168.00 (+11.41%)</td><td>39.68 (-8.96%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>6.95 (n/a)</td><td>4.93 (n/a)</td><td>4.67 (n/a)</td><td>3.90 (n/a)</td><td>1.18 (n/a)</td><td>268.60 (n/a)</td><td>221.04 (n/a)</td><td>224.60 (n/a)</td><td>150.80 (n/a)</td><td>43.59 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>9.65 (+14.68%)</td><td>7.84 (-1.52%)</td><td>7.51 (-4.25%)</td><td>7.23 (-5.61%)</td><td>1.02 <b>(+202.70%)</b></td><td>290.10 (+5.95%)</td><td>270.52 (+2.60%)</td><td>279.20 (+4.45%)</td><td>217.30 (-12.80%)</td><td>30.33 <b>(+175.77%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>8.42 (n/a)</td><td>7.97 (n/a)</td><td>7.85 (n/a)</td><td>7.66 (n/a)</td><td>0.34 (n/a)</td><td>273.80 (n/a)</td><td>263.66 (n/a)</td><td>267.30 (n/a)</td><td>249.20 (n/a)</td><td>11.00 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>8.65 (+10.42%)</td><td>8.12 (+10.94%)</td><td>8.20 (+10.11%)</td><td>7.48 (+15.52%)</td><td>0.43 (-16.34%)</td><td>280.50 (-13.43%)</td><td>258.88 (-10.03%)</td><td>255.70 (-9.17%)</td><td>242.40 (-9.42%)</td><td>14.12 <b>(-34.93%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>7.84 (n/a)</td><td>7.32 (n/a)</td><td>7.45 (n/a)</td><td>6.47 (n/a)</td><td>0.52 (n/a)</td><td>324.00 (n/a)</td><td>287.74 (n/a)</td><td>281.50 (n/a)</td><td>267.60 (n/a)</td><td>21.69 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>8.07 (-1.21%)</td><td>7.70 (+5.38%)</td><td>7.62 (+7.74%)</td><td>7.51 (+17.73%)</td><td>0.22 <b>(-71.91%)</b></td><td>279.20 (-15.06%)</td><td>272.62 (-5.88%)</td><td>275.20 (-7.18%)</td><td>259.90 (+1.21%)</td><td>7.43 <b>(-75.53%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>8.17 (n/a)</td><td>7.30 (n/a)</td><td>7.07 (n/a)</td><td>6.38 (n/a)</td><td>0.77 (n/a)</td><td>328.70 (n/a)</td><td>289.66 (n/a)</td><td>296.50 (n/a)</td><td>256.80 (n/a)</td><td>30.37 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>8.82 (-11.19%)</td><td>7.54 (-5.84%)</td><td>7.87 (-0.27%)</td><td>6.19 (-12.00%)</td><td>1.06 (-8.60%)</td><td>338.60 (+13.62%)</td><td>282.60 (+6.34%)</td><td>266.30 (+0.26%)</td><td>237.80 (+12.59%)</td><td>40.98 (+18.91%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>9.93 (n/a)</td><td>8.01 (n/a)</td><td>7.90 (n/a)</td><td>7.04 (n/a)</td><td>1.16 (n/a)</td><td>298.00 (n/a)</td><td>265.74 (n/a)</td><td>265.60 (n/a)</td><td>211.20 (n/a)</td><td>34.46 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>10.66 <b>(+22.75%)</b></td><td>8.86 (+9.36%)</td><td>8.90 (+10.35%)</td><td>6.52 (-13.93%)</td><td>1.59 <b>(+292.11%)</b></td><td>321.40 (+16.15%)</td><td>243.74 (-6.07%)</td><td>235.60 (-9.38%)</td><td>196.70 (-18.52%)</td><td>48.57 <b>(+275.86%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>8.69 (n/a)</td><td>8.10 (n/a)</td><td>8.07 (n/a)</td><td>7.58 (n/a)</td><td>0.41 (n/a)</td><td>276.70 (n/a)</td><td>259.50 (n/a)</td><td>260.00 (n/a)</td><td>241.40 (n/a)</td><td>12.92 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>9.33 (+0.99%)</td><td>8.27 (-0.00%)</td><td>8.37 (+7.33%)</td><td>6.54 (-13.83%)</td><td>1.16 <b>(+48.94%)</b></td><td>320.40 (+16.04%)</td><td>258.04 (+1.04%)</td><td>250.40 (-6.85%)</td><td>224.80 (-0.97%)</td><td>39.53 <b>(+69.47%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>9.24 (n/a)</td><td>8.27 (n/a)</td><td>7.80 (n/a)</td><td>7.59 (n/a)</td><td>0.78 (n/a)</td><td>276.10 (n/a)</td><td>255.38 (n/a)</td><td>268.80 (n/a)</td><td>227.00 (n/a)</td><td>23.33 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>13.59 (+19.07%)</td><td>11.81 (+14.62%)</td><td>11.44 (+9.04%)</td><td>10.41 <b>(+20.50%)</b></td><td>1.25 (+12.61%)</td><td>403.00 (-17.01%)</td><td>358.34 (-12.86%)</td><td>366.70 (-8.30%)</td><td>308.60 (-16.03%)</td><td>36.75 <b>(-22.17%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>11.41 (n/a)</td><td>10.30 (n/a)</td><td>10.49 (n/a)</td><td>8.64 (n/a)</td><td>1.11 (n/a)</td><td>485.60 (n/a)</td><td>411.22 (n/a)</td><td>399.90 (n/a)</td><td>367.50 (n/a)</td><td>47.21 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>14.67 (+13.43%)</td><td>12.10 (-0.84%)</td><td>11.93 (-5.04%)</td><td>9.76 (-11.96%)</td><td>1.81 <b>(+145.19%)</b></td><td>429.80 (+13.58%)</td><td>352.84 (+2.36%)</td><td>351.50 (+5.30%)</td><td>285.80 (-11.84%)</td><td>53.00 <b>(+144.65%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>12.94 (n/a)</td><td>12.21 (n/a)</td><td>12.57 (n/a)</td><td>11.09 (n/a)</td><td>0.74 (n/a)</td><td>378.40 (n/a)</td><td>344.72 (n/a)</td><td>333.80 (n/a)</td><td>324.20 (n/a)</td><td>21.66 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>14.77 (+13.13%)</td><td>12.03 (+8.56%)</td><td>12.08 (+10.75%)</td><td>10.18 (+8.96%)</td><td>1.73 <b>(+29.48%)</b></td><td>411.90 (-8.22%)</td><td>354.00 (-7.53%)</td><td>347.20 (-9.72%)</td><td>284.00 (-11.61%)</td><td>47.66 (+4.07%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>13.05 (n/a)</td><td>11.08 (n/a)</td><td>10.91 (n/a)</td><td>9.35 (n/a)</td><td>1.34 (n/a)</td><td>448.80 (n/a)</td><td>382.82 (n/a)</td><td>384.60 (n/a)</td><td>321.30 (n/a)</td><td>45.80 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>15.39 (+8.04%)</td><td>13.24 (+6.87%)</td><td>13.71 (+12.15%)</td><td>11.31 (-2.38%)</td><td>1.70 <b>(+57.78%)</b></td><td>370.90 (+2.43%)</td><td>320.96 (-5.69%)</td><td>305.90 (-10.84%)</td><td>272.50 (-7.44%)</td><td>41.74 <b>(+53.41%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>14.25 (n/a)</td><td>12.39 (n/a)</td><td>12.22 (n/a)</td><td>11.58 (n/a)</td><td>1.08 (n/a)</td><td>362.10 (n/a)</td><td>340.34 (n/a)</td><td>343.10 (n/a)</td><td>294.40 (n/a)</td><td>27.21 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>13.71 (-6.45%)</td><td>11.78 (-6.73%)</td><td>12.08 (-4.80%)</td><td>9.02 <b>(-20.72%)</b></td><td>1.84 <b>(+42.91%)</b></td><td>465.10 <b>(+26.11%)</b></td><td>363.86 (+8.70%)</td><td>347.20 (+5.02%)</td><td>305.90 (+6.88%)</td><td>63.08 <b>(+94.75%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>14.66 (n/a)</td><td>12.63 (n/a)</td><td>12.69 (n/a)</td><td>11.37 (n/a)</td><td>1.29 (n/a)</td><td>368.80 (n/a)</td><td>334.74 (n/a)</td><td>330.60 (n/a)</td><td>286.20 (n/a)</td><td>32.39 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>15.14 (-1.19%)</td><td>12.85 (-1.69%)</td><td>12.82 (-0.47%)</td><td>11.13 (-6.81%)</td><td>1.46 (+6.99%)</td><td>377.00 (+7.32%)</td><td>329.72 (+1.91%)</td><td>327.20 (+0.46%)</td><td>277.00 (+1.21%)</td><td>35.89 (+15.19%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>15.32 (n/a)</td><td>13.07 (n/a)</td><td>12.88 (n/a)</td><td>11.94 (n/a)</td><td>1.36 (n/a)</td><td>351.30 (n/a)</td><td>323.54 (n/a)</td><td>325.70 (n/a)</td><td>273.70 (n/a)</td><td>31.16 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>15.49 (+5.36%)</td><td>12.79 (-8.56%)</td><td>12.65 (-9.43%)</td><td>10.72 (-15.98%)</td><td>1.87 <b>(+143.50%)</b></td><td>391.20 (+19.01%)</td><td>333.40 (+10.90%)</td><td>331.40 (+10.39%)</td><td>270.70 (-5.08%)</td><td>47.16 <b>(+174.19%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>14.71 (n/a)</td><td>13.99 (n/a)</td><td>13.97 (n/a)</td><td>12.76 (n/a)</td><td>0.77 (n/a)</td><td>328.70 (n/a)</td><td>300.62 (n/a)</td><td>300.20 (n/a)</td><td>285.20 (n/a)</td><td>17.20 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>13.57 (-3.50%)</td><td>12.43 (+2.56%)</td><td>12.49 (+1.29%)</td><td>11.46 <b>(+28.20%)</b></td><td>0.76 <b>(-62.33%)</b></td><td>365.90 <b>(-22.00%)</b></td><td>338.50 (-4.71%)</td><td>335.90 (-1.29%)</td><td>309.20 (+3.62%)</td><td>20.45 <b>(-70.04%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>14.06 (n/a)</td><td>12.12 (n/a)</td><td>12.33 (n/a)</td><td>8.94 (n/a)</td><td>2.02 (n/a)</td><td>469.10 (n/a)</td><td>355.22 (n/a)</td><td>340.30 (n/a)</td><td>298.40 (n/a)</td><td>68.27 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>3.34 (-1.31%)</td><td>2.83 (-0.76%)</td><td>2.69 (+3.60%)</td><td>2.39 (-0.52%)</td><td>0.44 (-1.51%)</td><td>219.00 (+0.55%)</td><td>189.02 (+0.78%)</td><td>194.70 (-3.47%)</td><td>157.00 (+1.36%)</td><td>28.61 (+1.42%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>3.38 (n/a)</td><td>2.85 (n/a)</td><td>2.60 (n/a)</td><td>2.41 (n/a)</td><td>0.45 (n/a)</td><td>217.80 (n/a)</td><td>187.56 (n/a)</td><td>201.70 (n/a)</td><td>154.90 (n/a)</td><td>28.21 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>5.61 (-0.39%)</td><td>4.94 (+4.11%)</td><td>5.02 (+5.91%)</td><td>4.29 (+6.29%)</td><td>0.50 (-18.26%)</td><td>244.40 (-5.89%)</td><td>214.16 (-4.39%)</td><td>208.80 (-5.56%)</td><td>186.80 (+0.38%)</td><td>22.00 <b>(-22.39%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>5.63 (n/a)</td><td>4.74 (n/a)</td><td>4.74 (n/a)</td><td>4.04 (n/a)</td><td>0.62 (n/a)</td><td>259.70 (n/a)</td><td>224.00 (n/a)</td><td>221.10 (n/a)</td><td>186.10 (n/a)</td><td>28.35 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>8.82 (+8.27%)</td><td>7.56 (+5.66%)</td><td>8.02 (+11.34%)</td><td>6.23 (+1.25%)</td><td>1.09 <b>(+44.82%)</b></td><td>336.40 (-1.23%)</td><td>282.46 (-4.55%)</td><td>261.60 (-10.16%)</td><td>237.70 (-7.62%)</td><td>42.23 <b>(+33.58%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>8.15 (n/a)</td><td>7.15 (n/a)</td><td>7.20 (n/a)</td><td>6.16 (n/a)</td><td>0.75 (n/a)</td><td>340.60 (n/a)</td><td>295.94 (n/a)</td><td>291.20 (n/a)</td><td>257.30 (n/a)</td><td>31.61 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>3.51 (-9.95%)</td><td>2.61 (+1.32%)</td><td>2.54 (-0.32%)</td><td>2.02 <b>(+34.86%)</b></td><td>0.61 <b>(-30.16%)</b></td><td>259.20 <b>(-25.84%)</b></td><td>208.88 (-6.44%)</td><td>206.80 (+0.34%)</td><td>149.50 (+11.07%)</td><td>45.54 <b>(-42.50%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>3.90 (n/a)</td><td>2.58 (n/a)</td><td>2.54 (n/a)</td><td>1.50 (n/a)</td><td>0.87 (n/a)</td><td>349.50 (n/a)</td><td>223.26 (n/a)</td><td>206.10 (n/a)</td><td>134.60 (n/a)</td><td>79.20 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.22 (-8.05%)</td><td>0.18 (-2.05%)</td><td>0.18 (+14.23%)</td><td>0.11 <b>(-30.07%)</b></td><td>0.05 (+14.29%)</td><td>311.90 <b>(+43.01%)</b></td><td>194.66 (+5.91%)</td><td>177.30 (-12.44%)</td><td>148.00 (+8.82%)</td><td>67.60 <b>(+80.46%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>218.10 (n/a)</td><td>183.80 (n/a)</td><td>202.50 (n/a)</td><td>136.00 (n/a)</td><td>37.46 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.20 (-15.10%)</td><td>0.19 (+3.52%)</td><td>0.18 (+0.57%)</td><td>0.18 (+18.81%)</td><td>0.01 <b>(-75.38%)</b></td><td>183.00 (-15.86%)</td><td>176.84 (-5.65%)</td><td>181.50 (-0.55%)</td><td>166.20 (+17.79%)</td><td>7.59 <b>(-75.92%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>217.50 (n/a)</td><td>187.42 (n/a)</td><td>182.50 (n/a)</td><td>141.10 (n/a)</td><td>31.50 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.44 (+1.69%)</td><td>0.39 (+3.37%)</td><td>0.39 (+1.49%)</td><td>0.33 (+6.07%)</td><td>0.05 (-7.54%)</td><td>200.30 (-5.74%)</td><td>169.98 (-3.56%)</td><td>167.70 (-1.47%)</td><td>147.40 (-1.67%)</td><td>20.77 (-14.90%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.44 (n/a)</td><td>0.38 (n/a)</td><td>0.39 (n/a)</td><td>0.31 (n/a)</td><td>0.05 (n/a)</td><td>212.50 (n/a)</td><td>176.26 (n/a)</td><td>170.20 (n/a)</td><td>149.90 (n/a)</td><td>24.41 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.52 (-5.53%)</td><td>0.36 (-12.15%)</td><td>0.37 (-0.35%)</td><td>0.22 <b>(-29.68%)</b></td><td>0.11 <b>(+23.54%)</b></td><td>294.70 <b>(+42.23%)</b></td><td>197.04 (+19.00%)</td><td>175.50 (+0.34%)</td><td>125.70 (+5.90%)</td><td>63.53 <b>(+92.99%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.55 (n/a)</td><td>0.41 (n/a)</td><td>0.37 (n/a)</td><td>0.32 (n/a)</td><td>0.09 (n/a)</td><td>207.20 (n/a)</td><td>165.58 (n/a)</td><td>174.90 (n/a)</td><td>118.70 (n/a)</td><td>32.92 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.46 (-12.34%)</td><td>0.39 (-3.87%)</td><td>0.37 (-7.95%)</td><td>0.31 (+5.80%)</td><td>0.07 <b>(-24.97%)</b></td><td>208.20 (-5.49%)</td><td>171.62 (+2.50%)</td><td>177.80 (+8.61%)</td><td>141.60 (+14.10%)</td><td>28.44 <b>(-21.69%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.53 (n/a)</td><td>0.41 (n/a)</td><td>0.40 (n/a)</td><td>0.30 (n/a)</td><td>0.09 (n/a)</td><td>220.30 (n/a)</td><td>167.44 (n/a)</td><td>163.70 (n/a)</td><td>124.10 (n/a)</td><td>36.32 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.86 (+1.02%)</td><td>0.78 (+15.13%)</td><td>0.76 <b>(+25.27%)</b></td><td>0.71 <b>(+20.50%)</b></td><td>0.07 <b>(-39.13%)</b></td><td>185.20 (-17.03%)</td><td>169.82 (-14.36%)</td><td>171.70 <b>(-20.18%)</b></td><td>152.20 (-1.04%)</td><td>14.86 <b>(-50.21%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.85 (n/a)</td><td>0.67 (n/a)</td><td>0.61 (n/a)</td><td>0.59 (n/a)</td><td>0.11 (n/a)</td><td>223.20 (n/a)</td><td>198.30 (n/a)</td><td>215.10 (n/a)</td><td>153.80 (n/a)</td><td>29.85 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.84 (-18.86%)</td><td>0.74 (-4.40%)</td><td>0.71 (-0.08%)</td><td>0.64 <b>(+20.17%)</b></td><td>0.08 <b>(-64.43%)</b></td><td>206.00 (-16.80%)</td><td>179.20 (-1.41%)</td><td>183.90 (+0.05%)</td><td>156.70 <b>(+23.19%)</b></td><td>19.55 <b>(-62.60%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>1.03 (n/a)</td><td>0.77 (n/a)</td><td>0.71 (n/a)</td><td>0.53 (n/a)</td><td>0.23 (n/a)</td><td>247.60 (n/a)</td><td>181.76 (n/a)</td><td>183.80 (n/a)</td><td>127.20 (n/a)</td><td>52.28 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.96 (-3.28%)</td><td>0.79 (+11.46%)</td><td>0.80 <b>(+26.60%)</b></td><td>0.60 <b>(+26.65%)</b></td><td>0.13 <b>(-48.37%)</b></td><td>219.30 <b>(-21.06%)</b></td><td>169.44 (-16.85%)</td><td>164.50 <b>(-20.99%)</b></td><td>135.90 (+3.35%)</td><td>30.43 <b>(-55.80%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>1.00 (n/a)</td><td>0.71 (n/a)</td><td>0.63 (n/a)</td><td>0.47 (n/a)</td><td>0.25 (n/a)</td><td>277.80 (n/a)</td><td>203.78 (n/a)</td><td>208.20 (n/a)</td><td>131.50 (n/a)</td><td>68.85 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>1.03 <b>(+28.72%)</b></td><td>0.68 (-5.31%)</td><td>0.63 (-13.61%)</td><td>0.52 (-11.22%)</td><td>0.20 <b>(+137.98%)</b></td><td>254.50 (+12.66%)</td><td>202.62 (+10.26%)</td><td>206.80 (+15.72%)</td><td>126.80 <b>(-22.30%)</b></td><td>47.16 <b>(+92.17%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.80 (n/a)</td><td>0.72 (n/a)</td><td>0.73 (n/a)</td><td>0.58 (n/a)</td><td>0.09 (n/a)</td><td>225.90 (n/a)</td><td>183.76 (n/a)</td><td>178.70 (n/a)</td><td>163.20 (n/a)</td><td>24.54 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 (+0.79%)</td><td>0.10 (-1.33%)</td><td>0.10 (-6.10%)</td><td>0.08 (-4.09%)</td><td>0.02 (-0.01%)</td><td>199.90 (+4.28%)</td><td>167.84 (+1.33%)</td><td>171.40 (+6.53%)</td><td>130.60 (-0.76%)</td><td>24.74 (-1.02%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>191.70 (n/a)</td><td>165.64 (n/a)</td><td>160.90 (n/a)</td><td>131.60 (n/a)</td><td>24.99 (n/a)</td>
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
