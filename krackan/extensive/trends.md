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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (+18.06%)</td><td>0.04 (-0.69%)</td><td>0.04 (-13.77%)</td><td>0.03 (+12.71%)</td><td>0.01 (+14.73%)</td><td>202.10 (-11.28%)</td><td>153.72 (+0.95%)</td><td>141.90 (+15.93%)</td><td>97.70 (-15.34%)</td><td>44.63 (-8.25%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>227.80 (n/a)</td><td>152.28 (n/a)</td><td>122.40 (n/a)</td><td>115.40 (n/a)</td><td>48.64 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (-3.20%)</td><td>0.04 (+1.30%)</td><td>0.04 (-8.47%)</td><td>0.03 <b>(+27.87%)</b></td><td>0.01 <b>(-38.44%)</b></td><td>192.50 <b>(-21.78%)</b></td><td>158.36 (-5.66%)</td><td>164.70 (+9.29%)</td><td>129.80 (+3.34%)</td><td>25.81 <b>(-49.72%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>246.10 (n/a)</td><td>167.86 (n/a)</td><td>150.70 (n/a)</td><td>125.60 (n/a)</td><td>51.33 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (+9.41%)</td><td>0.04 (+8.25%)</td><td>0.03 (-4.63%)</td><td>0.03 (+8.70%)</td><td>0.01 <b>(+26.90%)</b></td><td>201.50 (-7.99%)</td><td>166.30 (-6.64%)</td><td>182.70 (+4.88%)</td><td>124.30 (-8.60%)</td><td>37.84 (+2.90%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>219.00 (n/a)</td><td>178.12 (n/a)</td><td>174.20 (n/a)</td><td>136.00 (n/a)</td><td>36.77 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (+16.84%)</td><td>0.03 (+0.87%)</td><td>0.03 (-4.56%)</td><td>0.03 (+2.27%)</td><td>0.01 <b>(+79.26%)</b></td><td>208.20 (-2.21%)</td><td>186.26 (+1.04%)</td><td>194.40 (+4.80%)</td><td>130.40 (-14.44%)</td><td>32.16 <b>(+49.61%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>212.90 (n/a)</td><td>184.34 (n/a)</td><td>185.50 (n/a)</td><td>152.40 (n/a)</td><td>21.49 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.04 (-8.35%)</td><td>0.04 (-5.98%)</td><td>0.03 (-2.52%)</td><td>0.03 (+18.95%)</td><td>0.00 <b>(-46.72%)</b></td><td>208.50 (-15.93%)</td><td>177.68 (+2.16%)</td><td>182.70 (+2.58%)</td><td>143.10 (+9.07%)</td><td>23.87 <b>(-50.00%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>248.00 (n/a)</td><td>173.92 (n/a)</td><td>178.10 (n/a)</td><td>131.20 (n/a)</td><td>47.75 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.04 (-5.71%)</td><td>0.03 (-5.31%)</td><td>0.03 (-0.71%)</td><td>0.03 (-13.16%)</td><td>0.00 <b>(+37.32%)</b></td><td>235.30 (+15.12%)</td><td>190.82 (+6.56%)</td><td>181.50 (+0.72%)</td><td>167.70 (+6.07%)</td><td>28.22 <b>(+65.59%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>204.40 (n/a)</td><td>179.08 (n/a)</td><td>180.20 (n/a)</td><td>158.10 (n/a)</td><td>17.04 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.04 (+3.59%)</td><td>0.03 (-15.01%)</td><td>0.03 (-10.53%)</td><td>0.02 <b>(-26.04%)</b></td><td>0.01 <b>(+36.07%)</b></td><td>306.00 <b>(+35.22%)</b></td><td>234.38 <b>(+21.03%)</b></td><td>234.90 (+11.75%)</td><td>153.70 (-3.52%)</td><td>54.72 <b>(+75.58%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>226.30 (n/a)</td><td>193.66 (n/a)</td><td>210.20 (n/a)</td><td>159.30 (n/a)</td><td>31.16 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.04 (-18.96%)</td><td>0.03 <b>(-21.80%)</b></td><td>0.03 <b>(-26.16%)</b></td><td>0.02 (-19.61%)</td><td>0.01 <b>(-27.22%)</b></td><td>294.90 <b>(+24.38%)</b></td><td>220.68 <b>(+27.05%)</b></td><td>211.60 <b>(+35.47%)</b></td><td>172.60 <b>(+23.37%)</b></td><td>45.57 (+14.26%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.10 (n/a)</td><td>173.70 (n/a)</td><td>156.20 (n/a)</td><td>139.90 (n/a)</td><td>39.88 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.07 <b>(-24.68%)</b></td><td>0.07 (-16.38%)</td><td>0.07 (-12.42%)</td><td>0.06 (-2.44%)</td><td>0.00 <b>(-74.87%)</b></td><td>195.20 (+2.52%)</td><td>181.54 (+17.06%)</td><td>177.50 (+14.15%)</td><td>171.40 <b>(+32.77%)</b></td><td>9.43 <b>(-64.57%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>190.40 (n/a)</td><td>155.08 (n/a)</td><td>155.50 (n/a)</td><td>129.10 (n/a)</td><td>26.62 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.09 (-2.26%)</td><td>0.07 (-9.00%)</td><td>0.07 (-10.07%)</td><td>0.06 (-18.93%)</td><td>0.01 <b>(+34.19%)</b></td><td>223.30 <b>(+23.37%)</b></td><td>181.94 (+11.51%)</td><td>186.40 (+11.22%)</td><td>138.90 (+2.28%)</td><td>32.64 <b>(+65.82%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>181.00 (n/a)</td><td>163.16 (n/a)</td><td>167.60 (n/a)</td><td>135.80 (n/a)</td><td>19.68 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.10 <b>(+36.73%)</b></td><td>0.08 <b>(+22.25%)</b></td><td>0.08 (+16.93%)</td><td>0.06 (+17.33%)</td><td>0.02 <b>(+56.19%)</b></td><td>207.80 (-14.77%)</td><td>161.68 (-17.32%)</td><td>151.00 (-14.50%)</td><td>122.20 <b>(-26.87%)</b></td><td>32.56 (-1.60%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>243.80 (n/a)</td><td>195.54 (n/a)</td><td>176.60 (n/a)</td><td>167.10 (n/a)</td><td>33.09 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.09 (+7.86%)</td><td>0.08 (+5.92%)</td><td>0.08 (+1.77%)</td><td>0.06 (+6.71%)</td><td>0.02 (+16.32%)</td><td>220.10 (-6.30%)</td><td>161.72 (-5.22%)</td><td>161.90 (-1.76%)</td><td>129.40 (-7.31%)</td><td>36.52 (-3.03%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>234.90 (n/a)</td><td>170.62 (n/a)</td><td>164.80 (n/a)</td><td>139.60 (n/a)</td><td>37.66 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.09 (+7.73%)</td><td>0.08 (+8.18%)</td><td>0.08 (+3.68%)</td><td>0.05 (+4.92%)</td><td>0.02 (+19.69%)</td><td>226.00 (-4.68%)</td><td>166.66 (-6.87%)</td><td>162.10 (-3.51%)</td><td>130.10 (-7.14%)</td><td>38.51 (+3.25%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>237.10 (n/a)</td><td>178.96 (n/a)</td><td>168.00 (n/a)</td><td>140.10 (n/a)</td><td>37.29 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.10 (-1.25%)</td><td>0.07 (-1.18%)</td><td>0.07 (-8.53%)</td><td>0.05 <b>(+24.99%)</b></td><td>0.02 (-19.90%)</td><td>227.30 (-19.99%)</td><td>176.14 (-2.39%)</td><td>173.00 (+9.29%)</td><td>128.70 (+1.26%)</td><td>37.33 <b>(-38.68%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>284.10 (n/a)</td><td>180.46 (n/a)</td><td>158.30 (n/a)</td><td>127.10 (n/a)</td><td>60.88 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.09 (+14.78%)</td><td>0.07 (+14.04%)</td><td>0.08 (+17.08%)</td><td>0.05 <b>(+35.70%)</b></td><td>0.02 (+16.04%)</td><td>230.50 <b>(-26.31%)</b></td><td>175.46 (-13.17%)</td><td>149.60 (-14.61%)</td><td>138.50 (-12.89%)</td><td>44.44 <b>(-29.24%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>312.80 (n/a)</td><td>202.08 (n/a)</td><td>175.20 (n/a)</td><td>159.00 (n/a)</td><td>62.80 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.09 (+15.23%)</td><td>0.07 (+11.15%)</td><td>0.08 (+18.85%)</td><td>0.05 (+6.25%)</td><td>0.02 <b>(+63.06%)</b></td><td>234.70 (-5.89%)</td><td>179.12 (-7.35%)</td><td>158.10 (-15.81%)</td><td>132.20 (-13.25%)</td><td>47.29 <b>(+35.12%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>249.40 (n/a)</td><td>193.34 (n/a)</td><td>187.80 (n/a)</td><td>152.40 (n/a)</td><td>35.00 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.19 (-2.89%)</td><td>0.16 (+3.79%)</td><td>0.17 (+17.25%)</td><td>0.11 (-9.47%)</td><td>0.03 (+3.21%)</td><td>217.70 (+10.45%)</td><td>157.74 (-3.01%)</td><td>147.90 (-14.71%)</td><td>128.20 (+3.05%)</td><td>36.96 (+17.38%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>197.10 (n/a)</td><td>162.64 (n/a)</td><td>173.40 (n/a)</td><td>124.40 (n/a)</td><td>31.49 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.19 (-4.22%)</td><td>0.16 (+5.97%)</td><td>0.17 (+7.71%)</td><td>0.14 <b>(+37.75%)</b></td><td>0.02 <b>(-36.04%)</b></td><td>180.30 <b>(-27.39%)</b></td><td>152.24 (-9.03%)</td><td>145.50 (-7.15%)</td><td>131.90 (+4.35%)</td><td>22.04 <b>(-53.73%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>248.30 (n/a)</td><td>167.36 (n/a)</td><td>156.70 (n/a)</td><td>126.40 (n/a)</td><td>47.63 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.19 (-1.27%)</td><td>0.18 <b>(+23.40%)</b></td><td>0.18 (+19.98%)</td><td>0.14 <b>(+41.71%)</b></td><td>0.02 <b>(-52.91%)</b></td><td>169.70 <b>(-29.41%)</b></td><td>141.74 <b>(-23.18%)</b></td><td>138.90 (-16.68%)</td><td>128.10 (+1.26%)</td><td>16.63 <b>(-67.87%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>240.40 (n/a)</td><td>184.52 (n/a)</td><td>166.70 (n/a)</td><td>126.50 (n/a)</td><td>51.77 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.19 (-1.43%)</td><td>0.15 (+1.81%)</td><td>0.15 (+0.54%)</td><td>0.11 (-9.18%)</td><td>0.03 <b>(+30.67%)</b></td><td>223.10 (+10.12%)</td><td>167.20 (+0.17%)</td><td>160.70 (-0.50%)</td><td>130.60 (+1.40%)</td><td>39.67 <b>(+41.99%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>202.60 (n/a)</td><td>166.92 (n/a)</td><td>161.50 (n/a)</td><td>128.80 (n/a)</td><td>27.94 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.17 (-19.48%)</td><td>0.13 (-9.09%)</td><td>0.13 (-4.93%)</td><td>0.09 <b>(-23.62%)</b></td><td>0.03 <b>(-24.87%)</b></td><td>285.30 <b>(+30.93%)</b></td><td>196.60 (+9.76%)</td><td>182.90 (+5.24%)</td><td>145.40 <b>(+24.17%)</b></td><td>52.50 <b>(+27.68%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>217.90 (n/a)</td><td>179.12 (n/a)</td><td>173.80 (n/a)</td><td>117.10 (n/a)</td><td>41.12 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.19 (+4.68%)</td><td>0.13 (-5.24%)</td><td>0.12 (-17.46%)</td><td>0.09 <b>(+45.29%)</b></td><td>0.04 (-7.73%)</td><td>268.30 <b>(-31.17%)</b></td><td>209.52 (-0.70%)</td><td>207.40 <b>(+21.14%)</b></td><td>127.50 (-4.49%)</td><td>57.13 <b>(-44.09%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>389.80 (n/a)</td><td>211.00 (n/a)</td><td>171.20 (n/a)</td><td>133.50 (n/a)</td><td>102.18 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.13 <b>(-32.83%)</b></td><td>0.11 (-16.50%)</td><td>0.12 (-1.79%)</td><td>0.09 <b>(-22.94%)</b></td><td>0.02 <b>(-50.71%)</b></td><td>282.50 <b>(+29.77%)</b></td><td>219.52 (+17.64%)</td><td>207.70 (+1.81%)</td><td>192.00 <b>(+48.84%)</b></td><td>35.86 (+0.83%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>217.70 (n/a)</td><td>186.60 (n/a)</td><td>204.00 (n/a)</td><td>129.00 (n/a)</td><td>35.56 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.16 (+0.24%)</td><td>0.13 (-4.45%)</td><td>0.13 (-7.46%)</td><td>0.10 (+4.82%)</td><td>0.02 (+3.80%)</td><td>239.80 (-4.58%)</td><td>195.08 (+4.66%)</td><td>187.60 (+8.06%)</td><td>156.10 (-0.26%)</td><td>36.16 (-3.82%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>251.30 (n/a)</td><td>186.40 (n/a)</td><td>173.60 (n/a)</td><td>156.50 (n/a)</td><td>37.60 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.34 (-16.73%)</td><td>0.28 (-8.57%)</td><td>0.27 (-16.63%)</td><td>0.23 (+6.69%)</td><td>0.04 <b>(-44.32%)</b></td><td>213.40 (-6.28%)</td><td>179.56 (+6.01%)</td><td>181.30 (+19.99%)</td><td>146.50 <b>(+20.08%)</b></td><td>25.78 <b>(-38.63%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.40 (n/a)</td><td>0.30 (n/a)</td><td>0.33 (n/a)</td><td>0.22 (n/a)</td><td>0.07 (n/a)</td><td>227.70 (n/a)</td><td>169.38 (n/a)</td><td>151.10 (n/a)</td><td>122.00 (n/a)</td><td>42.01 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.29 (-2.87%)</td><td>0.24 (-9.26%)</td><td>0.25 (-3.53%)</td><td>0.15 <b>(-38.39%)</b></td><td>0.05 <b>(+184.22%)</b></td><td>320.30 <b>(+62.34%)</b></td><td>212.06 (+15.73%)</td><td>193.00 (+3.65%)</td><td>169.00 (+2.92%)</td><td>61.95 <b>(+397.58%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.02 (n/a)</td><td>197.30 (n/a)</td><td>183.24 (n/a)</td><td>186.20 (n/a)</td><td>164.20 (n/a)</td><td>12.45 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.41 (+4.93%)</td><td>0.32 (+6.40%)</td><td>0.29 (+8.10%)</td><td>0.26 (+5.97%)</td><td>0.06 (-2.14%)</td><td>191.30 (-5.62%)</td><td>160.20 (-6.46%)</td><td>170.60 (-7.48%)</td><td>119.90 (-4.69%)</td><td>28.17 (-13.30%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.39 (n/a)</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.06 (n/a)</td><td>202.70 (n/a)</td><td>171.26 (n/a)</td><td>184.40 (n/a)</td><td>125.80 (n/a)</td><td>32.49 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.40 (+6.81%)</td><td>0.29 (-10.15%)</td><td>0.28 (-11.93%)</td><td>0.21 <b>(-26.55%)</b></td><td>0.07 <b>(+72.17%)</b></td><td>238.10 <b>(+36.13%)</b></td><td>178.82 (+14.82%)</td><td>178.30 (+13.49%)</td><td>123.30 (-6.38%)</td><td>40.80 <b>(+112.25%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.37 (n/a)</td><td>0.32 (n/a)</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.04 (n/a)</td><td>174.90 (n/a)</td><td>155.74 (n/a)</td><td>157.10 (n/a)</td><td>131.70 (n/a)</td><td>19.22 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.47 (+12.98%)</td><td>0.33 (+0.49%)</td><td>0.32 (+2.84%)</td><td>0.23 (-9.51%)</td><td>0.09 <b>(+34.92%)</b></td><td>218.20 (+10.54%)</td><td>155.48 (+1.75%)</td><td>151.60 (-2.76%)</td><td>105.40 (-11.50%)</td><td>40.39 <b>(+33.10%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.41 (n/a)</td><td>0.33 (n/a)</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.06 (n/a)</td><td>197.40 (n/a)</td><td>152.80 (n/a)</td><td>155.90 (n/a)</td><td>119.10 (n/a)</td><td>30.34 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.39 <b>(+24.60%)</b></td><td>0.27 (+8.49%)</td><td>0.27 (-0.50%)</td><td>0.18 (+12.33%)</td><td>0.08 <b>(+32.24%)</b></td><td>272.60 (-10.97%)</td><td>191.06 (-7.08%)</td><td>185.00 (+0.49%)</td><td>125.20 (-19.74%)</td><td>52.79 (-10.20%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.27 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>306.20 (n/a)</td><td>205.62 (n/a)</td><td>184.10 (n/a)</td><td>156.00 (n/a)</td><td>58.79 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.31 <b>(-21.92%)</b></td><td>0.26 (-8.30%)</td><td>0.27 (-6.30%)</td><td>0.20 <b>(+24.99%)</b></td><td>0.04 <b>(-54.93%)</b></td><td>239.80 (-19.99%)</td><td>193.46 (+2.29%)</td><td>183.30 (+6.69%)</td><td>160.90 <b>(+28.11%)</b></td><td>29.58 <b>(-55.22%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.39 (n/a)</td><td>0.28 (n/a)</td><td>0.29 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>299.70 (n/a)</td><td>189.12 (n/a)</td><td>171.80 (n/a)</td><td>125.60 (n/a)</td><td>66.05 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.30 (-19.90%)</td><td>0.24 (-15.20%)</td><td>0.24 (-14.95%)</td><td>0.18 (-5.88%)</td><td>0.04 <b>(-31.82%)</b></td><td>274.20 (+6.24%)</td><td>215.04 (+15.89%)</td><td>208.80 (+17.57%)</td><td>165.00 <b>(+24.81%)</b></td><td>41.07 (-10.65%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.37 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.07 (n/a)</td><td>258.10 (n/a)</td><td>185.56 (n/a)</td><td>177.60 (n/a)</td><td>132.20 (n/a)</td><td>45.96 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (+9.21%)</td><td>0.02 (-0.23%)</td><td>0.02 (-0.22%)</td><td>0.01 (-8.75%)</td><td>0.00 <b>(+37.90%)</b></td><td>231.40 (+9.56%)</td><td>169.28 (+1.89%)</td><td>161.60 (+0.19%)</td><td>129.40 (-8.49%)</td><td>37.63 <b>(+39.73%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>211.20 (n/a)</td><td>166.14 (n/a)</td><td>161.30 (n/a)</td><td>141.40 (n/a)</td><td>26.93 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 <b>(+46.60%)</b></td><td>0.02 (+11.34%)</td><td>0.02 (-0.55%)</td><td>0.01 (+11.07%)</td><td>0.00 <b>(+134.59%)</b></td><td>199.00 (-10.00%)</td><td>166.44 (-7.16%)</td><td>174.50 (+0.58%)</td><td>106.90 <b>(-31.78%)</b></td><td>35.71 <b>(+37.75%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>221.10 (n/a)</td><td>179.28 (n/a)</td><td>173.50 (n/a)</td><td>156.70 (n/a)</td><td>25.92 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (-0.27%)</td><td>0.01 (-5.69%)</td><td>0.02 (-3.85%)</td><td>0.01 <b>(-20.19%)</b></td><td>0.00 <b>(+85.97%)</b></td><td>231.90 <b>(+25.28%)</b></td><td>178.98 (+7.83%)</td><td>168.60 (+4.01%)</td><td>153.60 (+0.26%)</td><td>31.54 <b>(+137.18%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>185.10 (n/a)</td><td>165.98 (n/a)</td><td>162.10 (n/a)</td><td>153.20 (n/a)</td><td>13.30 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (+10.91%)</td><td>0.02 (+14.09%)</td><td>0.02 <b>(+26.63%)</b></td><td>0.01 (+1.31%)</td><td>0.00 <b>(+45.69%)</b></td><td>216.30 (-1.28%)</td><td>174.96 (-11.12%)</td><td>162.80 <b>(-21.05%)</b></td><td>140.70 (-9.87%)</td><td>33.95 <b>(+32.61%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>219.10 (n/a)</td><td>196.84 (n/a)</td><td>206.20 (n/a)</td><td>156.10 (n/a)</td><td>25.60 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 <b>(-24.09%)</b></td><td>0.01 (-7.11%)</td><td>0.01 (-2.58%)</td><td>0.01 (-4.11%)</td><td>0.00 <b>(-50.81%)</b></td><td>225.30 (+4.31%)</td><td>183.84 (+3.50%)</td><td>184.50 (+2.67%)</td><td>143.60 <b>(+31.74%)</b></td><td>29.21 <b>(-31.47%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>216.00 (n/a)</td><td>177.62 (n/a)</td><td>179.70 (n/a)</td><td>109.00 (n/a)</td><td>42.62 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (+5.31%)</td><td>0.01 (-5.15%)</td><td>0.01 (-3.12%)</td><td>0.01 <b>(-25.30%)</b></td><td>0.00 <b>(+102.14%)</b></td><td>288.60 <b>(+33.86%)</b></td><td>207.58 (+9.65%)</td><td>191.80 (+3.23%)</td><td>156.90 (-5.08%)</td><td>53.67 <b>(+155.55%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>215.60 (n/a)</td><td>189.32 (n/a)</td><td>185.80 (n/a)</td><td>165.30 (n/a)</td><td>21.00 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 <b>(+23.32%)</b></td><td>0.01 (-3.85%)</td><td>0.01 (-12.83%)</td><td>0.01 (-14.64%)</td><td>0.00 <b>(+188.29%)</b></td><td>236.80 (+17.17%)</td><td>204.20 (+8.20%)</td><td>226.00 (+14.72%)</td><td>133.10 (-18.89%)</td><td>42.51 <b>(+168.97%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>202.10 (n/a)</td><td>188.72 (n/a)</td><td>197.00 (n/a)</td><td>164.10 (n/a)</td><td>15.81 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.01 (-13.98%)</td><td>0.01 (-9.73%)</td><td>0.01 (-12.42%)</td><td>0.01 (+11.37%)</td><td>0.00 <b>(-38.71%)</b></td><td>339.70 (-10.20%)</td><td>246.72 (+6.05%)</td><td>231.30 (+14.22%)</td><td>211.30 (+16.23%)</td><td>52.74 <b>(-36.10%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>378.30 (n/a)</td><td>232.64 (n/a)</td><td>202.50 (n/a)</td><td>181.80 (n/a)</td><td>82.53 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 <b>(-22.72%)</b></td><td>0.03 <b>(-22.57%)</b></td><td>0.03 <b>(-24.09%)</b></td><td>0.02 <b>(-23.78%)</b></td><td>0.00 (-12.25%)</td><td>228.90 <b>(+31.17%)</b></td><td>201.92 <b>(+29.62%)</b></td><td>205.70 <b>(+31.69%)</b></td><td>166.10 <b>(+29.36%)</b></td><td>27.16 <b>(+51.88%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>174.50 (n/a)</td><td>155.78 (n/a)</td><td>156.20 (n/a)</td><td>128.40 (n/a)</td><td>17.88 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (-6.90%)</td><td>0.03 (-5.78%)</td><td>0.03 (-6.16%)</td><td>0.02 (+1.90%)</td><td>0.00 <b>(-29.58%)</b></td><td>231.00 (-1.87%)</td><td>188.52 (+4.98%)</td><td>183.70 (+6.62%)</td><td>165.90 (+7.38%)</td><td>25.12 <b>(-24.28%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>235.40 (n/a)</td><td>179.58 (n/a)</td><td>172.30 (n/a)</td><td>154.50 (n/a)</td><td>33.18 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 <b>(-35.85%)</b></td><td>0.03 (-15.28%)</td><td>0.03 (-15.00%)</td><td>0.02 (+11.30%)</td><td>0.00 <b>(-64.98%)</b></td><td>229.30 (-10.15%)</td><td>199.68 (+9.94%)</td><td>202.20 (+17.63%)</td><td>164.80 <b>(+55.91%)</b></td><td>28.38 <b>(-49.51%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>255.20 (n/a)</td><td>181.62 (n/a)</td><td>171.90 (n/a)</td><td>105.70 (n/a)</td><td>56.21 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (-9.86%)</td><td>0.03 (-13.01%)</td><td>0.03 (-18.11%)</td><td>0.02 (-12.68%)</td><td>0.00 (-11.90%)</td><td>247.20 (+14.55%)</td><td>201.16 (+14.96%)</td><td>200.60 <b>(+22.17%)</b></td><td>173.60 (+10.93%)</td><td>28.44 (+13.81%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.80 (n/a)</td><td>174.98 (n/a)</td><td>164.20 (n/a)</td><td>156.50 (n/a)</td><td>24.99 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 <b>(-30.95%)</b></td><td>0.03 (-19.74%)</td><td>0.03 (-19.45%)</td><td>0.02 (-3.76%)</td><td>0.00 <b>(-60.40%)</b></td><td>251.20 (+3.93%)</td><td>204.14 (+18.85%)</td><td>202.60 <b>(+24.14%)</b></td><td>173.50 <b>(+44.82%)</b></td><td>29.51 <b>(-39.61%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>241.70 (n/a)</td><td>171.76 (n/a)</td><td>163.20 (n/a)</td><td>119.80 (n/a)</td><td>48.87 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 <b>(-22.65%)</b></td><td>0.03 (-2.37%)</td><td>0.03 (+0.50%)</td><td>0.03 (+15.04%)</td><td>0.00 <b>(-61.74%)</b></td><td>205.40 (-13.08%)</td><td>187.08 (-1.74%)</td><td>195.90 (-0.51%)</td><td>158.30 <b>(+29.22%)</b></td><td>19.10 <b>(-55.14%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>236.30 (n/a)</td><td>190.40 (n/a)</td><td>196.90 (n/a)</td><td>122.50 (n/a)</td><td>42.58 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 <b>(+38.49%)</b></td><td>0.03 (+8.93%)</td><td>0.03 (+9.08%)</td><td>0.02 (-14.61%)</td><td>0.01 <b>(+76.20%)</b></td><td>347.90 (+17.10%)</td><td>207.40 (-0.81%)</td><td>186.60 (-8.35%)</td><td>112.30 <b>(-27.83%)</b></td><td>87.05 <b>(+53.26%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>297.10 (n/a)</td><td>209.10 (n/a)</td><td>203.60 (n/a)</td><td>155.60 (n/a)</td><td>56.80 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 <b>(-21.24%)</b></td><td>0.02 (-18.07%)</td><td>0.02 (-13.83%)</td><td>0.02 <b>(-28.14%)</b></td><td>0.00 (-10.55%)</td><td>323.30 <b>(+39.17%)</b></td><td>251.64 <b>(+22.80%)</b></td><td>248.90 (+16.04%)</td><td>214.00 <b>(+26.93%)</b></td><td>43.74 <b>(+58.17%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.30 (n/a)</td><td>204.92 (n/a)</td><td>214.50 (n/a)</td><td>168.60 (n/a)</td><td>27.66 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.07 (-11.01%)</td><td>0.05 (-18.56%)</td><td>0.05 (-14.47%)</td><td>0.03 <b>(-45.53%)</b></td><td>0.02 <b>(+51.44%)</b></td><td>339.50 <b>(+83.61%)</b></td><td>221.26 <b>(+31.36%)</b></td><td>211.10 (+16.89%)</td><td>143.60 (+12.36%)</td><td>75.98 <b>(+216.16%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>184.90 (n/a)</td><td>168.44 (n/a)</td><td>180.60 (n/a)</td><td>127.80 (n/a)</td><td>24.03 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (+3.71%)</td><td>0.05 (-9.45%)</td><td>0.05 <b>(-20.10%)</b></td><td>0.04 <b>(-22.56%)</b></td><td>0.01 <b>(+104.83%)</b></td><td>266.20 <b>(+29.16%)</b></td><td>211.44 (+13.17%)</td><td>220.50 <b>(+25.14%)</b></td><td>166.70 (-3.59%)</td><td>41.06 <b>(+147.43%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>206.10 (n/a)</td><td>186.84 (n/a)</td><td>176.20 (n/a)</td><td>172.90 (n/a)</td><td>16.60 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (-17.97%)</td><td>0.05 (-19.75%)</td><td>0.06 (-14.33%)</td><td>0.04 <b>(-32.19%)</b></td><td>0.01 <b>(+21.68%)</b></td><td>278.40 <b>(+47.46%)</b></td><td>204.90 <b>(+27.09%)</b></td><td>184.00 (+16.68%)</td><td>171.30 <b>(+21.92%)</b></td><td>44.25 <b>(+121.07%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>188.80 (n/a)</td><td>161.22 (n/a)</td><td>157.70 (n/a)</td><td>140.50 (n/a)</td><td>20.02 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 <b>(-39.37%)</b></td><td>0.05 <b>(-29.19%)</b></td><td>0.05 (-16.25%)</td><td>0.03 <b>(-45.09%)</b></td><td>0.01 <b>(-36.05%)</b></td><td>345.00 <b>(+82.15%)</b></td><td>235.80 <b>(+42.70%)</b></td><td>216.80 (+19.38%)</td><td>181.80 <b>(+64.97%)</b></td><td>65.30 <b>(+98.73%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>189.40 (n/a)</td><td>165.24 (n/a)</td><td>181.60 (n/a)</td><td>110.20 (n/a)</td><td>32.86 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.08 <b>(+32.69%)</b></td><td>0.07 <b>(+21.53%)</b></td><td>0.06 (+12.66%)</td><td>0.05 (+8.19%)</td><td>0.01 <b>(+113.08%)</b></td><td>198.50 (-7.59%)</td><td>161.20 (-16.11%)</td><td>166.30 (-11.26%)</td><td>124.40 <b>(-24.61%)</b></td><td>30.05 <b>(+44.69%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>214.80 (n/a)</td><td>192.16 (n/a)</td><td>187.40 (n/a)</td><td>165.00 (n/a)</td><td>20.77 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.07 <b>(-20.04%)</b></td><td>0.05 (-13.10%)</td><td>0.05 <b>(-21.40%)</b></td><td>0.04 (-7.08%)</td><td>0.01 <b>(-33.50%)</b></td><td>270.10 (+7.65%)</td><td>205.76 (+12.34%)</td><td>211.70 <b>(+27.22%)</b></td><td>152.10 <b>(+25.08%)</b></td><td>44.05 (-11.25%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>250.90 (n/a)</td><td>183.16 (n/a)</td><td>166.40 (n/a)</td><td>121.60 (n/a)</td><td>49.63 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.07 (-6.64%)</td><td>0.06 (-1.62%)</td><td>0.06 (+1.79%)</td><td>0.04 (+13.00%)</td><td>0.01 <b>(-21.36%)</b></td><td>269.60 (-11.52%)</td><td>192.62 (-1.14%)</td><td>171.00 (-1.72%)</td><td>153.70 (+7.11%)</td><td>46.20 <b>(-27.50%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>304.70 (n/a)</td><td>194.84 (n/a)</td><td>174.00 (n/a)</td><td>143.50 (n/a)</td><td>63.72 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (+8.21%)</td><td>0.05 (+6.85%)</td><td>0.05 (+1.76%)</td><td>0.03 (+8.39%)</td><td>0.01 <b>(+30.94%)</b></td><td>313.10 (-7.72%)</td><td>229.06 (-5.27%)</td><td>222.60 (-1.72%)</td><td>176.10 (-7.61%)</td><td>58.03 (+2.14%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>339.30 (n/a)</td><td>241.80 (n/a)</td><td>226.50 (n/a)</td><td>190.60 (n/a)</td><td>56.81 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.15 (+6.60%)</td><td>0.13 (+8.27%)</td><td>0.12 (+8.28%)</td><td>0.11 (+14.05%)</td><td>0.02 (-5.23%)</td><td>195.20 (-12.31%)</td><td>166.06 (-8.23%)</td><td>173.70 (-7.66%)</td><td>138.90 (-6.21%)</td><td>25.34 <b>(-21.25%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>222.60 (n/a)</td><td>180.96 (n/a)</td><td>188.10 (n/a)</td><td>148.10 (n/a)</td><td>32.18 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.13 <b>(-23.75%)</b></td><td>0.11 (-10.95%)</td><td>0.12 (+1.41%)</td><td>0.09 <b>(-21.73%)</b></td><td>0.02 <b>(-25.69%)</b></td><td>239.30 <b>(+27.76%)</b></td><td>187.74 (+12.19%)</td><td>174.20 (-1.41%)</td><td>167.80 <b>(+31.20%)</b></td><td>30.11 <b>(+27.43%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>187.30 (n/a)</td><td>167.34 (n/a)</td><td>176.70 (n/a)</td><td>127.90 (n/a)</td><td>23.63 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.17 (+5.25%)</td><td>0.14 (-0.47%)</td><td>0.14 (+0.87%)</td><td>0.11 (-7.35%)</td><td>0.03 <b>(+54.02%)</b></td><td>187.00 (+7.97%)</td><td>154.06 (+2.23%)</td><td>153.40 (-0.84%)</td><td>122.80 (-5.03%)</td><td>29.38 <b>(+59.61%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>173.20 (n/a)</td><td>150.70 (n/a)</td><td>154.70 (n/a)</td><td>129.30 (n/a)</td><td>18.41 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.15 (-0.10%)</td><td>0.12 (-3.82%)</td><td>0.12 (-6.28%)</td><td>0.09 (-5.37%)</td><td>0.02 (-3.49%)</td><td>222.30 (+5.71%)</td><td>176.94 (+3.95%)</td><td>176.10 (+6.73%)</td><td>138.90 (+0.14%)</td><td>32.25 (+2.91%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>210.30 (n/a)</td><td>170.22 (n/a)</td><td>165.00 (n/a)</td><td>138.70 (n/a)</td><td>31.34 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.15 (-11.37%)</td><td>0.12 (-4.41%)</td><td>0.12 (+0.64%)</td><td>0.10 (-7.27%)</td><td>0.02 <b>(-25.99%)</b></td><td>211.80 (+7.84%)</td><td>174.30 (+3.66%)</td><td>175.80 (-0.68%)</td><td>137.80 (+12.86%)</td><td>26.36 (-8.82%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>196.40 (n/a)</td><td>168.14 (n/a)</td><td>177.00 (n/a)</td><td>122.10 (n/a)</td><td>28.91 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.18 (-1.02%)</td><td>0.13 (+4.96%)</td><td>0.12 (+9.75%)</td><td>0.10 (-0.47%)</td><td>0.03 (-9.48%)</td><td>217.60 (+0.46%)</td><td>170.88 (-5.73%)</td><td>180.70 (-8.88%)</td><td>117.00 (+1.04%)</td><td>37.99 (-10.70%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>216.60 (n/a)</td><td>181.26 (n/a)</td><td>198.30 (n/a)</td><td>115.80 (n/a)</td><td>42.55 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.15 (+17.05%)</td><td>0.11 (+16.91%)</td><td>0.12 <b>(+20.22%)</b></td><td>0.08 (+14.76%)</td><td>0.03 (+16.09%)</td><td>272.60 (-12.85%)</td><td>194.86 (-14.43%)</td><td>178.20 (-16.85%)</td><td>141.80 (-14.58%)</td><td>49.08 (-12.61%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>312.80 (n/a)</td><td>227.72 (n/a)</td><td>214.30 (n/a)</td><td>166.00 (n/a)</td><td>56.16 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.10 <b>(-20.17%)</b></td><td>0.09 (+0.26%)</td><td>0.09 (+15.90%)</td><td>0.08 (+7.87%)</td><td>0.01 <b>(-66.28%)</b></td><td>251.60 (-7.30%)</td><td>232.52 (-2.64%)</td><td>222.60 (-13.69%)</td><td>218.90 <b>(+25.30%)</b></td><td>16.05 <b>(-61.16%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>271.40 (n/a)</td><td>238.82 (n/a)</td><td>257.90 (n/a)</td><td>174.70 (n/a)</td><td>41.32 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>183.60 (n/a)</td><td>157.08 (n/a)</td><td>151.60 (n/a)</td><td>130.50 (n/a)</td><td>20.21 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>192.90 (n/a)</td><td>160.60 (n/a)</td><td>168.50 (n/a)</td><td>123.20 (n/a)</td><td>28.66 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.10 (n/a)</td><td>195.94 (n/a)</td><td>192.40 (n/a)</td><td>140.40 (n/a)</td><td>37.36 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>214.50 (n/a)</td><td>185.50 (n/a)</td><td>191.10 (n/a)</td><td>136.60 (n/a)</td><td>31.02 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>223.60 (n/a)</td><td>180.74 (n/a)</td><td>185.50 (n/a)</td><td>145.60 (n/a)</td><td>33.59 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>236.30 (n/a)</td><td>196.10 (n/a)</td><td>191.20 (n/a)</td><td>169.90 (n/a)</td><td>24.41 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>217.90 (n/a)</td><td>190.60 (n/a)</td><td>195.00 (n/a)</td><td>155.80 (n/a)</td><td>24.70 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>216.60 (n/a)</td><td>190.96 (n/a)</td><td>199.90 (n/a)</td><td>135.70 (n/a)</td><td>31.70 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>218.40 (n/a)</td><td>187.54 (n/a)</td><td>180.40 (n/a)</td><td>153.80 (n/a)</td><td>25.16 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>210.00 (n/a)</td><td>186.72 (n/a)</td><td>175.60 (n/a)</td><td>168.00 (n/a)</td><td>21.25 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>215.80 (n/a)</td><td>186.74 (n/a)</td><td>194.40 (n/a)</td><td>143.60 (n/a)</td><td>30.58 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>240.60 (n/a)</td><td>198.46 (n/a)</td><td>186.50 (n/a)</td><td>165.50 (n/a)</td><td>29.03 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.37 (+1.63%)</td><td>0.29 (+5.72%)</td><td>0.29 (+11.15%)</td><td>0.22 (+1.36%)</td><td>0.05 (-1.41%)</td><td>220.60 (-1.34%)</td><td>175.70 (-5.49%)</td><td>169.00 (-10.01%)</td><td>134.50 (-1.61%)</td><td>31.31 (-1.52%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.36 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.05 (n/a)</td><td>223.60 (n/a)</td><td>185.90 (n/a)</td><td>187.80 (n/a)</td><td>136.70 (n/a)</td><td>31.79 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.37 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.05 (n/a)</td><td>214.50 (n/a)</td><td>170.24 (n/a)</td><td>173.70 (n/a)</td><td>132.30 (n/a)</td><td>30.14 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.36 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>251.50 (n/a)</td><td>190.56 (n/a)</td><td>189.00 (n/a)</td><td>137.20 (n/a)</td><td>45.22 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.34 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.04 (n/a)</td><td>203.80 (n/a)</td><td>178.90 (n/a)</td><td>182.00 (n/a)</td><td>145.70 (n/a)</td><td>25.39 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>214.80 (n/a)</td><td>177.50 (n/a)</td><td>164.20 (n/a)</td><td>147.90 (n/a)</td><td>28.98 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>185.30 (n/a)</td><td>167.66 (n/a)</td><td>180.50 (n/a)</td><td>144.10 (n/a)</td><td>20.99 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>200.30 (n/a)</td><td>173.56 (n/a)</td><td>178.10 (n/a)</td><td>144.00 (n/a)</td><td>20.93 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>235.00 (n/a)</td><td>187.58 (n/a)</td><td>180.20 (n/a)</td><td>158.10 (n/a)</td><td>28.91 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>213.30 (n/a)</td><td>170.72 (n/a)</td><td>172.20 (n/a)</td><td>131.30 (n/a)</td><td>33.66 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>212.20 (n/a)</td><td>164.90 (n/a)</td><td>178.80 (n/a)</td><td>116.00 (n/a)</td><td>39.58 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>212.90 (n/a)</td><td>187.44 (n/a)</td><td>204.90 (n/a)</td><td>119.10 (n/a)</td><td>39.47 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>296.10 (n/a)</td><td>218.80 (n/a)</td><td>232.10 (n/a)</td><td>155.80 (n/a)</td><td>57.79 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>231.50 (n/a)</td><td>184.60 (n/a)</td><td>187.20 (n/a)</td><td>143.00 (n/a)</td><td>32.03 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>238.60 (n/a)</td><td>194.62 (n/a)</td><td>205.70 (n/a)</td><td>147.50 (n/a)</td><td>35.11 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>237.10 (n/a)</td><td>190.16 (n/a)</td><td>189.20 (n/a)</td><td>145.00 (n/a)</td><td>33.35 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>203.10 (n/a)</td><td>180.98 (n/a)</td><td>190.00 (n/a)</td><td>145.30 (n/a)</td><td>22.63 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.36 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>206.80 (n/a)</td><td>177.90 (n/a)</td><td>182.90 (n/a)</td><td>138.20 (n/a)</td><td>26.59 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.35 (n/a)</td><td>0.29 (n/a)</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.06 (n/a)</td><td>233.70 (n/a)</td><td>175.72 (n/a)</td><td>166.30 (n/a)</td><td>140.50 (n/a)</td><td>38.81 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>246.50 (n/a)</td><td>219.24 (n/a)</td><td>226.30 (n/a)</td><td>194.10 (n/a)</td><td>21.84 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>196.00 (n/a)</td><td>164.14 (n/a)</td><td>169.60 (n/a)</td><td>116.90 (n/a)</td><td>32.24 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>182.80 (n/a)</td><td>164.62 (n/a)</td><td>167.20 (n/a)</td><td>135.30 (n/a)</td><td>17.86 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.00 (n/a)</td><td>170.82 (n/a)</td><td>166.20 (n/a)</td><td>139.10 (n/a)</td><td>26.81 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>234.90 (n/a)</td><td>186.66 (n/a)</td><td>218.00 (n/a)</td><td>121.60 (n/a)</td><td>58.66 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>233.90 (n/a)</td><td>168.62 (n/a)</td><td>154.10 (n/a)</td><td>108.50 (n/a)</td><td>56.48 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>217.60 (n/a)</td><td>196.78 (n/a)</td><td>212.50 (n/a)</td><td>128.20 (n/a)</td><td>38.44 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.70 (n/a)</td><td>183.98 (n/a)</td><td>183.50 (n/a)</td><td>163.10 (n/a)</td><td>20.02 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.50 (n/a)</td><td>205.64 (n/a)</td><td>210.60 (n/a)</td><td>174.20 (n/a)</td><td>18.33 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.50 (n/a)</td><td>177.24 (n/a)</td><td>186.20 (n/a)</td><td>132.70 (n/a)</td><td>27.28 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.20 (n/a)</td><td>160.64 (n/a)</td><td>160.70 (n/a)</td><td>121.70 (n/a)</td><td>30.75 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>265.10 (n/a)</td><td>174.44 (n/a)</td><td>180.20 (n/a)</td><td>111.70 (n/a)</td><td>59.11 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>185.90 (n/a)</td><td>152.58 (n/a)</td><td>157.60 (n/a)</td><td>127.80 (n/a)</td><td>24.88 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.30 (n/a)</td><td>171.70 (n/a)</td><td>167.10 (n/a)</td><td>129.50 (n/a)</td><td>35.65 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>253.60 (n/a)</td><td>206.32 (n/a)</td><td>219.90 (n/a)</td><td>146.50 (n/a)</td><td>41.40 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.40 (n/a)</td><td>181.40 (n/a)</td><td>189.80 (n/a)</td><td>130.70 (n/a)</td><td>28.97 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>323.20 (n/a)</td><td>232.90 (n/a)</td><td>223.50 (n/a)</td><td>190.60 (n/a)</td><td>53.56 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>182.60 (n/a)</td><td>163.38 (n/a)</td><td>161.60 (n/a)</td><td>148.30 (n/a)</td><td>12.88 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>198.70 (n/a)</td><td>176.04 (n/a)</td><td>185.40 (n/a)</td><td>118.90 (n/a)</td><td>32.41 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>186.70 (n/a)</td><td>163.72 (n/a)</td><td>173.70 (n/a)</td><td>120.20 (n/a)</td><td>26.63 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>190.50 (n/a)</td><td>164.88 (n/a)</td><td>175.30 (n/a)</td><td>109.90 (n/a)</td><td>31.73 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>206.10 (n/a)</td><td>171.48 (n/a)</td><td>161.30 (n/a)</td><td>143.80 (n/a)</td><td>24.37 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>200.50 (n/a)</td><td>170.18 (n/a)</td><td>174.80 (n/a)</td><td>128.20 (n/a)</td><td>26.14 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>305.70 (n/a)</td><td>207.20 (n/a)</td><td>202.50 (n/a)</td><td>129.10 (n/a)</td><td>63.25 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>261.20 (n/a)</td><td>214.78 (n/a)</td><td>218.10 (n/a)</td><td>163.90 (n/a)</td><td>34.78 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>196.10 (n/a)</td><td>174.22 (n/a)</td><td>177.50 (n/a)</td><td>142.60 (n/a)</td><td>23.44 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>203.50 (n/a)</td><td>158.94 (n/a)</td><td>143.40 (n/a)</td><td>135.50 (n/a)</td><td>29.85 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>207.70 (n/a)</td><td>171.56 (n/a)</td><td>175.90 (n/a)</td><td>127.50 (n/a)</td><td>29.99 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>213.30 (n/a)</td><td>164.94 (n/a)</td><td>169.80 (n/a)</td><td>125.40 (n/a)</td><td>34.21 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>201.00 (n/a)</td><td>175.16 (n/a)</td><td>175.30 (n/a)</td><td>154.20 (n/a)</td><td>17.18 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>205.80 (n/a)</td><td>178.12 (n/a)</td><td>191.90 (n/a)</td><td>135.80 (n/a)</td><td>27.90 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>205.00 (n/a)</td><td>181.38 (n/a)</td><td>180.50 (n/a)</td><td>155.60 (n/a)</td><td>21.57 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>257.40 (n/a)</td><td>218.14 (n/a)</td><td>211.10 (n/a)</td><td>197.00 (n/a)</td><td>23.74 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>4.33 (-11.60%)</td><td>4.10 (-3.99%)</td><td>4.18 (-1.12%)</td><td>3.54 (-5.35%)</td><td>0.32 <b>(-21.91%)</b></td><td>2656.50 (+5.65%)</td><td>2306.88 (+3.96%)</td><td>2248.80 (+1.14%)</td><td>2171.90 (+13.13%)</td><td>200.02 (-5.17%)</td><td>1703.33 (-11.60%)</td><td>1612.43 (-3.99%)</td><td>1645.03 (-1.12%)</td><td>1392.58 (-5.35%)</td><td>126.97 <b>(-21.91%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>4.90 (n/a)</td><td>4.27 (n/a)</td><td>4.23 (n/a)</td><td>3.74 (n/a)</td><td>0.41 (n/a)</td><td>2514.40 (n/a)</td><td>2219.02 (n/a)</td><td>2223.50 (n/a)</td><td>1919.80 (n/a)</td><td>210.92 (n/a)</td><td>1926.93 (n/a)</td><td>1679.42 (n/a)</td><td>1663.73 (n/a)</td><td>1471.30 (n/a)</td><td>162.60 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>1.45 (+19.89%)</td><td>1.00 (-1.08%)</td><td>1.08 (+1.27%)</td><td>0.66 (+2.65%)</td><td>0.33 <b>(+46.70%)</b></td><td>333.20 (-2.57%)</td><td>241.14 (+4.91%)</td><td>205.20 (-1.25%)</td><td>152.10 (-16.61%)</td><td>78.96 <b>(+21.81%)</b></td><td>62.04 (+19.89%)</td><td>42.71 (-1.08%)</td><td>46.00 (+1.27%)</td><td>28.32 (+2.65%)</td><td>13.93 <b>(+46.70%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>1.21 (n/a)</td><td>1.01 (n/a)</td><td>1.06 (n/a)</td><td>0.65 (n/a)</td><td>0.22 (n/a)</td><td>342.00 (n/a)</td><td>229.86 (n/a)</td><td>207.80 (n/a)</td><td>182.40 (n/a)</td><td>64.83 (n/a)</td><td>51.75 (n/a)</td><td>43.17 (n/a)</td><td>45.42 (n/a)</td><td>27.59 (n/a)</td><td>9.50 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>1.17 (-4.12%)</td><td>0.96 (-5.94%)</td><td>0.99 (-2.87%)</td><td>0.70 <b>(-22.54%)</b></td><td>0.19 <b>(+61.32%)</b></td><td>314.30 <b>(+29.08%)</b></td><td>237.56 (+8.99%)</td><td>223.80 (+2.99%)</td><td>188.80 (+4.31%)</td><td>51.38 <b>(+119.75%)</b></td><td>49.98 (-4.12%)</td><td>41.13 (-5.94%)</td><td>42.18 (-2.88%)</td><td>30.02 <b>(-22.54%)</b></td><td>8.21 <b>(+61.32%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>1.22 (n/a)</td><td>1.02 (n/a)</td><td>1.02 (n/a)</td><td>0.91 (n/a)</td><td>0.12 (n/a)</td><td>243.50 (n/a)</td><td>217.96 (n/a)</td><td>217.30 (n/a)</td><td>181.00 (n/a)</td><td>23.38 (n/a)</td><td>52.13 (n/a)</td><td>43.73 (n/a)</td><td>43.42 (n/a)</td><td>38.76 (n/a)</td><td>5.09 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.52 (-0.66%)</td><td>0.52 (-0.18%)</td><td>0.52 (-0.04%)</td><td>0.52 (-0.15%)</td><td>0.00 <b>(-69.11%)</b></td><td>48536.60 (+0.15%)</td><td>48469.22 (+0.18%)</td><td>48476.60 (+0.04%)</td><td>48403.90 (+0.66%)</td><td>51.85 <b>(-68.85%)</b></td><td>354.93 (-0.66%)</td><td>354.45 (-0.18%)</td><td>354.40 (-0.04%)</td><td>353.96 (-0.15%)</td><td>0.38 <b>(-69.10%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48463.80 (n/a)</td><td>48384.22 (n/a)</td><td>48455.10 (n/a)</td><td>48086.60 (n/a)</td><td>166.44 (n/a)</td><td>357.27 (n/a)</td><td>355.08 (n/a)</td><td>354.55 (n/a)</td><td>354.49 (n/a)</td><td>1.23 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.21 (-0.92%)</td><td>0.21 (-0.27%)</td><td>0.21 (+0.04%)</td><td>0.21 (-0.46%)</td><td>0.00 <b>(-33.04%)</b></td><td>119502.50 (+0.47%)</td><td>118635.40 (+0.27%)</td><td>118479.90 (-0.04%)</td><td>118136.70 (+0.93%)</td><td>515.30 <b>(-31.98%)</b></td><td>145.42 (-0.92%)</td><td>144.81 (-0.27%)</td><td>145.00 (+0.04%)</td><td>143.76 (-0.46%)</td><td>0.63 <b>(-33.04%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>118947.90 (n/a)</td><td>118316.16 (n/a)</td><td>118527.70 (n/a)</td><td>117044.50 (n/a)</td><td>757.54 (n/a)</td><td>146.78 (n/a)</td><td>145.21 (n/a)</td><td>144.94 (n/a)</td><td>144.43 (n/a)</td><td>0.94 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.90 (+0.19%)</td><td>0.89 (-0.21%)</td><td>0.89 (-0.07%)</td><td>0.88 (-0.87%)</td><td>0.01 <b>(+71.33%)</b></td><td>28554.10 (+0.88%)</td><td>28255.80 (+0.21%)</td><td>28255.40 (+0.07%)</td><td>27975.50 (-0.18%)</td><td>206.10 <b>(+72.49%)</b></td><td>614.10 (+0.19%)</td><td>608.04 (-0.21%)</td><td>608.02 (-0.07%)</td><td>601.66 (-0.87%)</td><td>4.43 <b>(+71.33%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.00 (n/a)</td><td>28306.10 (n/a)</td><td>28195.72 (n/a)</td><td>28234.30 (n/a)</td><td>28027.30 (n/a)</td><td>119.48 (n/a)</td><td>612.97 (n/a)</td><td>609.32 (n/a)</td><td>608.48 (n/a)</td><td>606.93 (n/a)</td><td>2.59 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>3.55 (+0.11%)</td><td>3.46 (+0.02%)</td><td>3.49 (-1.16%)</td><td>3.33 (-0.09%)</td><td>0.10 (-8.85%)</td><td>7547.10 (+0.09%)</td><td>7278.98 (-0.03%)</td><td>7210.10 (+1.17%)</td><td>7097.00 (-0.11%)</td><td>205.90 (-9.10%)</td><td>2420.72 (+0.11%)</td><td>2361.70 (+0.02%)</td><td>2382.74 (-1.16%)</td><td>2276.36 (-0.09%)</td><td>66.21 (-8.85%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>3.54 (n/a)</td><td>3.46 (n/a)</td><td>3.53 (n/a)</td><td>3.34 (n/a)</td><td>0.11 (n/a)</td><td>7540.20 (n/a)</td><td>7281.10 (n/a)</td><td>7126.40 (n/a)</td><td>7104.80 (n/a)</td><td>226.52 (n/a)</td><td>2418.07 (n/a)</td><td>2361.33 (n/a)</td><td>2410.73 (n/a)</td><td>2278.45 (n/a)</td><td>72.64 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>3.18 (-2.59%)</td><td>2.97 (+2.84%)</td><td>3.01 (+6.86%)</td><td>2.79 (+2.23%)</td><td>0.16 <b>(-27.98%)</b></td><td>9027.90 (-2.18%)</td><td>8487.46 (-2.95%)</td><td>8353.20 (-6.42%)</td><td>7908.60 (+2.66%)</td><td>441.54 <b>(-26.32%)</b></td><td>2172.29 (-2.59%)</td><td>2028.55 (+2.84%)</td><td>2056.69 (+6.86%)</td><td>1902.97 (+2.23%)</td><td>105.89 <b>(-27.98%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>3.27 (n/a)</td><td>2.89 (n/a)</td><td>2.82 (n/a)</td><td>2.73 (n/a)</td><td>0.22 (n/a)</td><td>9229.00 (n/a)</td><td>8745.44 (n/a)</td><td>8926.30 (n/a)</td><td>7703.50 (n/a)</td><td>599.24 (n/a)</td><td>2230.15 (n/a)</td><td>1972.49 (n/a)</td><td>1924.63 (n/a)</td><td>1861.50 (n/a)</td><td>147.03 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>3.30 (-0.01%)</td><td>3.21 (+0.44%)</td><td>3.17 (+0.90%)</td><td>3.13 (-0.27%)</td><td>0.08 (+1.28%)</td><td>8046.30 (+0.28%)</td><td>7836.36 (-0.44%)</td><td>7930.30 (-0.89%)</td><td>7617.70 (+0.01%)</td><td>202.08 (+0.80%)</td><td>2255.25 (-0.01%)</td><td>2193.50 (+0.44%)</td><td>2166.36 (+0.90%)</td><td>2135.14 (-0.27%)</td><td>56.92 (+1.28%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>3.30 (n/a)</td><td>3.20 (n/a)</td><td>3.15 (n/a)</td><td>3.14 (n/a)</td><td>0.08 (n/a)</td><td>8024.20 (n/a)</td><td>7870.74 (n/a)</td><td>8001.80 (n/a)</td><td>7617.30 (n/a)</td><td>200.47 (n/a)</td><td>2255.37 (n/a)</td><td>2183.90 (n/a)</td><td>2147.01 (n/a)</td><td>2141.02 (n/a)</td><td>56.20 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.79 (+0.02%)</td><td>0.78 (-0.07%)</td><td>0.78 (-0.08%)</td><td>0.78 (-0.16%)</td><td>0.00 <b>(+489.15%)</b></td><td>96292.40 (+0.16%)</td><td>96182.56 (+0.07%)</td><td>96195.70 (+0.08%)</td><td>96079.90 (-0.02%)</td><td>78.91 <b>(+488.52%)</b></td><td>715.23 (+0.02%)</td><td>714.47 (-0.07%)</td><td>714.37 (-0.08%)</td><td>713.65 (-0.16%)</td><td>0.59 <b>(+489.27%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>96134.00 (n/a)</td><td>96118.50 (n/a)</td><td>96116.50 (n/a)</td><td>96100.90 (n/a)</td><td>13.41 (n/a)</td><td>715.08 (n/a)</td><td>714.95 (n/a)</td><td>714.96 (n/a)</td><td>714.83 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.73 (+0.03%)</td><td>0.73 (+0.05%)</td><td>0.73 (+0.08%)</td><td>0.73 (+0.04%)</td><td>0.00 <b>(-25.91%)</b></td><td>103393.50 (-0.04%)</td><td>103311.40 (-0.05%)</td><td>103296.70 (-0.08%)</td><td>103273.00 (-0.03%)</td><td>47.07 <b>(-25.95%)</b></td><td>665.42 (+0.03%)</td><td>665.17 (+0.05%)</td><td>665.26 (+0.08%)</td><td>664.64 (+0.04%)</td><td>0.30 <b>(-25.92%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103436.50 (n/a)</td><td>103367.56 (n/a)</td><td>103376.60 (n/a)</td><td>103301.70 (n/a)</td><td>63.56 (n/a)</td><td>665.23 (n/a)</td><td>664.81 (n/a)</td><td>664.75 (n/a)</td><td>664.36 (n/a)</td><td>0.41 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.70 (+0.38%)</td><td>0.69 (+0.47%)</td><td>0.69 (+0.55%)</td><td>0.69 (+0.41%)</td><td>0.00 (-17.64%)</td><td>108945.40 (-0.40%)</td><td>108713.24 (-0.47%)</td><td>108681.80 (-0.55%)</td><td>108601.40 (-0.37%)</td><td>139.06 (-18.29%)</td><td>632.77 (+0.38%)</td><td>632.12 (+0.47%)</td><td>632.30 (+0.55%)</td><td>630.77 (+0.41%)</td><td>0.81 (-17.64%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>109388.40 (n/a)</td><td>109224.84 (n/a)</td><td>109278.50 (n/a)</td><td>109008.60 (n/a)</td><td>170.18 (n/a)</td><td>630.40 (n/a)</td><td>629.16 (n/a)</td><td>628.85 (n/a)</td><td>628.22 (n/a)</td><td>0.98 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>7.12 (+0.44%)</td><td>6.87 (+7.55%)</td><td>6.89 (+5.72%)</td><td>6.51 <b>(+35.05%)</b></td><td>0.27 <b>(-71.18%)</b></td><td>1369.90 <b>(-25.95%)</b></td><td>1299.66 (-8.74%)</td><td>1294.20 (-5.41%)</td><td>1251.20 (-0.44%)</td><td>50.75 <b>(-79.22%)</b></td><td>429.10 (+0.44%)</td><td>413.59 (+7.55%)</td><td>414.82 (+5.72%)</td><td>391.91 <b>(+35.05%)</b></td><td>15.97 <b>(-71.18%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>7.09 (n/a)</td><td>6.38 (n/a)</td><td>6.51 (n/a)</td><td>4.82 (n/a)</td><td>0.92 (n/a)</td><td>1850.00 (n/a)</td><td>1424.20 (n/a)</td><td>1368.20 (n/a)</td><td>1256.70 (n/a)</td><td>244.28 (n/a)</td><td>427.22 (n/a)</td><td>384.54 (n/a)</td><td>392.38 (n/a)</td><td>290.20 (n/a)</td><td>55.42 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>6.97 (-0.39%)</td><td>6.30 (-5.95%)</td><td>6.56 (-2.78%)</td><td>4.75 <b>(-25.98%)</b></td><td>0.89 <b>(+244.95%)</b></td><td>1876.80 <b>(+35.11%)</b></td><td>1441.70 (+8.29%)</td><td>1359.20 (+2.85%)</td><td>1278.10 (+0.39%)</td><td>246.50 <b>(+378.44%)</b></td><td>420.06 (-0.39%)</td><td>379.73 (-5.95%)</td><td>394.98 (-2.78%)</td><td>286.05 <b>(-25.98%)</b></td><td>53.76 <b>(+244.96%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>7.00 (n/a)</td><td>6.70 (n/a)</td><td>6.74 (n/a)</td><td>6.42 (n/a)</td><td>0.26 (n/a)</td><td>1389.10 (n/a)</td><td>1331.32 (n/a)</td><td>1321.50 (n/a)</td><td>1273.10 (n/a)</td><td>51.52 (n/a)</td><td>421.71 (n/a)</td><td>403.74 (n/a)</td><td>406.26 (n/a)</td><td>386.48 (n/a)</td><td>15.59 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>6.57 (-6.92%)</td><td>6.36 (-4.18%)</td><td>6.36 (-2.97%)</td><td>6.15 (-0.89%)</td><td>0.16 <b>(-57.84%)</b></td><td>1448.70 (+0.90%)</td><td>1403.06 (+4.14%)</td><td>1400.80 (+3.06%)</td><td>1357.20 (+7.44%)</td><td>36.11 <b>(-53.96%)</b></td><td>395.59 (-6.92%)</td><td>382.84 (-4.18%)</td><td>383.25 (-2.97%)</td><td>370.59 (-0.89%)</td><td>9.86 <b>(-57.84%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>7.06 (n/a)</td><td>6.63 (n/a)</td><td>6.56 (n/a)</td><td>6.21 (n/a)</td><td>0.39 (n/a)</td><td>1435.80 (n/a)</td><td>1347.30 (n/a)</td><td>1359.20 (n/a)</td><td>1263.20 (n/a)</td><td>78.43 (n/a)</td><td>425.02 (n/a)</td><td>399.57 (n/a)</td><td>394.98 (n/a)</td><td>373.91 (n/a)</td><td>23.39 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>8.02 (-5.21%)</td><td>7.68 (-1.88%)</td><td>7.90 (-0.06%)</td><td>7.26 (-0.62%)</td><td>0.37 <b>(-23.44%)</b></td><td>4805.10 (+0.63%)</td><td>4547.50 (+1.81%)</td><td>4413.50 (+0.06%)</td><td>4347.60 (+5.49%)</td><td>219.80 (-18.96%)</td><td>493.95 (-5.21%)</td><td>473.11 (-1.88%)</td><td>486.57 (-0.06%)</td><td>446.92 (-0.62%)</td><td>22.50 <b>(-23.44%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>8.46 (n/a)</td><td>7.83 (n/a)</td><td>7.90 (n/a)</td><td>7.30 (n/a)</td><td>0.48 (n/a)</td><td>4775.10 (n/a)</td><td>4466.82 (n/a)</td><td>4410.90 (n/a)</td><td>4121.20 (n/a)</td><td>271.24 (n/a)</td><td>521.08 (n/a)</td><td>482.19 (n/a)</td><td>486.86 (n/a)</td><td>449.73 (n/a)</td><td>29.39 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>7.98 (+4.90%)</td><td>7.68 (+3.44%)</td><td>7.61 (+0.32%)</td><td>7.57 (+11.79%)</td><td>0.17 <b>(-53.27%)</b></td><td>4604.80 (-10.54%)</td><td>4542.98 (-3.48%)</td><td>4584.10 (-0.32%)</td><td>4370.70 (-4.67%)</td><td>97.75 <b>(-60.34%)</b></td><td>491.33 (+4.90%)</td><td>472.88 (+3.44%)</td><td>468.47 (+0.32%)</td><td>466.36 (+11.79%)</td><td>10.45 <b>(-53.27%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>7.60 (n/a)</td><td>7.42 (n/a)</td><td>7.58 (n/a)</td><td>6.77 (n/a)</td><td>0.36 (n/a)</td><td>5147.60 (n/a)</td><td>4706.98 (n/a)</td><td>4598.70 (n/a)</td><td>4585.00 (n/a)</td><td>246.44 (n/a)</td><td>468.38 (n/a)</td><td>457.17 (n/a)</td><td>466.98 (n/a)</td><td>417.18 (n/a)</td><td>22.37 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>7.45 (-3.92%)</td><td>7.40 (+3.11%)</td><td>7.43 (+1.78%)</td><td>7.27 (+8.73%)</td><td>0.07 <b>(-83.33%)</b></td><td>4793.30 (-8.03%)</td><td>4712.88 (-3.30%)</td><td>4693.40 (-1.75%)</td><td>4677.10 (+4.08%)</td><td>47.40 <b>(-84.17%)</b></td><td>459.15 (-3.92%)</td><td>455.70 (+3.11%)</td><td>457.56 (+1.78%)</td><td>448.02 (+8.73%)</td><td>4.54 <b>(-83.33%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>7.76 (n/a)</td><td>7.18 (n/a)</td><td>7.30 (n/a)</td><td>6.69 (n/a)</td><td>0.44 (n/a)</td><td>5211.90 (n/a)</td><td>4873.68 (n/a)</td><td>4776.80 (n/a)</td><td>4493.90 (n/a)</td><td>299.36 (n/a)</td><td>477.87 (n/a)</td><td>441.96 (n/a)</td><td>449.56 (n/a)</td><td>412.04 (n/a)</td><td>27.21 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.79 (-0.34%)</td><td>0.79 (-0.03%)</td><td>0.79 (+0.00%)</td><td>0.79 (+0.12%)</td><td>0.00 <b>(-77.76%)</b></td><td>95489.30 (-0.12%)</td><td>95415.82 (+0.03%)</td><td>95408.40 (-0.00%)</td><td>95377.60 (+0.35%)</td><td>45.42 <b>(-77.71%)</b></td><td>720.50 (-0.34%)</td><td>720.21 (-0.03%)</td><td>720.27 (+0.00%)</td><td>719.66 (+0.12%)</td><td>0.34 <b>(-77.76%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95600.40 (n/a)</td><td>95385.12 (n/a)</td><td>95410.50 (n/a)</td><td>95048.70 (n/a)</td><td>203.77 (n/a)</td><td>722.99 (n/a)</td><td>720.44 (n/a)</td><td>720.25 (n/a)</td><td>718.82 (n/a)</td><td>1.54 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.74 (-0.01%)</td><td>0.74 (+0.02%)</td><td>0.74 (-0.03%)</td><td>0.74 (+0.08%)</td><td>0.00 <b>(-66.34%)</b></td><td>102646.00 (-0.08%)</td><td>102610.64 (-0.02%)</td><td>102610.20 (+0.03%)</td><td>102576.90 (+0.01%)</td><td>24.70 <b>(-66.33%)</b></td><td>669.93 (-0.01%)</td><td>669.71 (+0.02%)</td><td>669.71 (-0.03%)</td><td>669.48 (+0.08%)</td><td>0.16 <b>(-66.34%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>102729.60 (n/a)</td><td>102627.74 (n/a)</td><td>102583.20 (n/a)</td><td>102569.00 (n/a)</td><td>73.36 (n/a)</td><td>669.98 (n/a)</td><td>669.60 (n/a)</td><td>669.89 (n/a)</td><td>668.94 (n/a)</td><td>0.48 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.70 (-0.12%)</td><td>0.70 (-0.04%)</td><td>0.70 (-0.04%)</td><td>0.70 (+0.08%)</td><td>0.00 <b>(-50.63%)</b></td><td>107576.30 (-0.08%)</td><td>107450.88 (+0.04%)</td><td>107406.40 (+0.04%)</td><td>107388.70 (+0.12%)</td><td>79.00 <b>(-50.61%)</b></td><td>639.91 (-0.12%)</td><td>639.54 (-0.04%)</td><td>639.81 (-0.04%)</td><td>638.80 (+0.08%)</td><td>0.47 <b>(-50.63%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>107659.20 (n/a)</td><td>107410.94 (n/a)</td><td>107362.30 (n/a)</td><td>107258.60 (n/a)</td><td>159.98 (n/a)</td><td>640.69 (n/a)</td><td>639.78 (n/a)</td><td>640.07 (n/a)</td><td>638.31 (n/a)</td><td>0.95 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>4.24 (-0.18%)</td><td>3.42 (-9.84%)</td><td>3.30 (-15.81%)</td><td>2.99 (+3.37%)</td><td>0.51 (-1.43%)</td><td>2691.90 (-3.27%)</td><td>2396.32 (+10.74%)</td><td>2441.60 (+18.78%)</td><td>1902.70 (+0.18%)</td><td>326.98 (-7.16%)</td><td>1111.03 (-0.18%)</td><td>896.72 (-9.84%)</td><td>865.79 (-15.81%)</td><td>785.29 (+3.37%)</td><td>134.10 (-1.43%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>4.24 (n/a)</td><td>3.79 (n/a)</td><td>3.92 (n/a)</td><td>2.90 (n/a)</td><td>0.52 (n/a)</td><td>2782.80 (n/a)</td><td>2163.82 (n/a)</td><td>2055.60 (n/a)</td><td>1899.20 (n/a)</td><td>352.18 (n/a)</td><td>1113.06 (n/a)</td><td>994.61 (n/a)</td><td>1028.39 (n/a)</td><td>759.65 (n/a)</td><td>136.05 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.52 (+4.58%)</td><td>0.39 (+11.46%)</td><td>0.35 (+7.10%)</td><td>0.27 (-4.81%)</td><td>0.11 <b>(+26.80%)</b></td><td>4567.80 (+5.05%)</td><td>3370.58 (-8.22%)</td><td>3582.60 (-6.63%)</td><td>2379.30 (-4.38%)</td><td>904.98 <b>(+29.43%)</b></td><td>28.21 (+4.58%)</td><td>21.14 (+11.46%)</td><td>18.73 (+7.10%)</td><td>14.69 (-4.81%)</td><td>5.79 <b>(+26.80%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.50 (n/a)</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.08 (n/a)</td><td>4348.20 (n/a)</td><td>3672.48 (n/a)</td><td>3837.00 (n/a)</td><td>2488.20 (n/a)</td><td>699.18 (n/a)</td><td>26.97 (n/a)</td><td>18.96 (n/a)</td><td>17.49 (n/a)</td><td>15.43 (n/a)</td><td>4.57 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>4.97 <b>(-22.82%)</b></td><td>4.12 (-10.49%)</td><td>3.95 (-16.75%)</td><td>3.39 (+3.75%)</td><td>0.66 <b>(-47.10%)</b></td><td>1964.20 (-3.61%)</td><td>1647.44 (+7.71%)</td><td>1681.90 <b>(+20.12%)</b></td><td>1338.20 <b>(+29.57%)</b></td><td>257.70 <b>(-35.35%)</b></td><td>1535.75 <b>(-22.82%)</b></td><td>1272.81 (-10.49%)</td><td>1221.95 (-16.75%)</td><td>1046.35 (+3.75%)</td><td>203.09 <b>(-47.10%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>6.44 (n/a)</td><td>4.60 (n/a)</td><td>4.75 (n/a)</td><td>3.26 (n/a)</td><td>1.24 (n/a)</td><td>2037.80 (n/a)</td><td>1529.48 (n/a)</td><td>1400.20 (n/a)</td><td>1032.80 (n/a)</td><td>398.60 (n/a)</td><td>1989.93 (n/a)</td><td>1422.04 (n/a)</td><td>1467.78 (n/a)</td><td>1008.52 (n/a)</td><td>383.93 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>13.33 (n/a)</td><td>12.64 (n/a)</td><td>13.17 (n/a)</td><td>10.64 (n/a)</td><td>1.14 (n/a)</td><td>13.33 (n/a)</td><td>12.63 (n/a)</td><td>13.17 (n/a)</td><td>10.64 (n/a)</td><td>1.14 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>25.05 (-0.30%)</td><td>24.14 (-1.59%)</td><td>24.10 (-1.84%)</td><td>23.54 (-2.06%)</td><td>0.57 <b>(+44.01%)</b></td><td>25.04 (-0.30%)</td><td>24.13 (-1.59%)</td><td>24.08 (-1.84%)</td><td>23.53 (-2.06%)</td><td>0.57 <b>(+44.01%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>25.13 (n/a)</td><td>24.53 (n/a)</td><td>24.55 (n/a)</td><td>24.04 (n/a)</td><td>0.40 (n/a)</td><td>25.11 (n/a)</td><td>24.52 (n/a)</td><td>24.53 (n/a)</td><td>24.02 (n/a)</td><td>0.40 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>41.76 (+2.51%)</td><td>39.75 (-0.17%)</td><td>39.33 (-1.52%)</td><td>38.66 (-0.00%)</td><td>1.18 <b>(+58.69%)</b></td><td>41.73 (+2.51%)</td><td>39.72 (-0.17%)</td><td>39.31 (-1.52%)</td><td>38.64 (-0.00%)</td><td>1.18 <b>(+58.69%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>40.73 (n/a)</td><td>39.81 (n/a)</td><td>39.94 (n/a)</td><td>38.66 (n/a)</td><td>0.74 (n/a)</td><td>40.71 (n/a)</td><td>39.79 (n/a)</td><td>39.92 (n/a)</td><td>38.64 (n/a)</td><td>0.74 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>46.22 (+3.68%)</td><td>43.07 (-0.15%)</td><td>42.58 (-0.97%)</td><td>41.32 (-2.09%)</td><td>1.85 <b>(+109.03%)</b></td><td>46.19 (+3.68%)</td><td>43.04 (-0.15%)</td><td>42.55 (-0.97%)</td><td>41.29 (-2.09%)</td><td>1.85 <b>(+109.03%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>44.58 (n/a)</td><td>43.13 (n/a)</td><td>43.00 (n/a)</td><td>42.20 (n/a)</td><td>0.89 (n/a)</td><td>44.55 (n/a)</td><td>43.11 (n/a)</td><td>42.97 (n/a)</td><td>42.17 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>13.23 (n/a)</td><td>12.79 (n/a)</td><td>12.86 (n/a)</td><td>12.10 (n/a)</td><td>0.45 (n/a)</td><td>13.22 (n/a)</td><td>12.78 (n/a)</td><td>12.85 (n/a)</td><td>12.10 (n/a)</td><td>0.45 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>24.55 (-2.42%)</td><td>23.79 (-2.11%)</td><td>23.99 (-1.26%)</td><td>22.50 (-4.63%)</td><td>0.77 <b>(+36.72%)</b></td><td>24.53 (-2.42%)</td><td>23.78 (-2.11%)</td><td>23.97 (-1.26%)</td><td>22.48 (-4.63%)</td><td>0.77 <b>(+36.72%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>25.16 (n/a)</td><td>24.31 (n/a)</td><td>24.29 (n/a)</td><td>23.59 (n/a)</td><td>0.56 (n/a)</td><td>25.14 (n/a)</td><td>24.29 (n/a)</td><td>24.28 (n/a)</td><td>23.57 (n/a)</td><td>0.56 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>40.89 (+1.84%)</td><td>39.55 (+0.16%)</td><td>39.32 (-1.19%)</td><td>38.20 (+0.52%)</td><td>1.19 <b>(+34.91%)</b></td><td>40.86 (+1.84%)</td><td>39.52 (+0.16%)</td><td>39.29 (-1.19%)</td><td>38.17 (+0.52%)</td><td>1.19 <b>(+34.91%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>40.15 (n/a)</td><td>39.48 (n/a)</td><td>39.79 (n/a)</td><td>38.00 (n/a)</td><td>0.88 (n/a)</td><td>40.13 (n/a)</td><td>39.46 (n/a)</td><td>39.77 (n/a)</td><td>37.97 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>45.82 (+1.39%)</td><td>42.06 (-2.04%)</td><td>42.03 (-0.94%)</td><td>40.05 (-3.51%)</td><td>2.36 <b>(+52.81%)</b></td><td>45.79 (+1.39%)</td><td>42.04 (-2.04%)</td><td>42.01 (-0.94%)</td><td>40.02 (-3.51%)</td><td>2.36 <b>(+52.81%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>45.19 (n/a)</td><td>42.94 (n/a)</td><td>42.43 (n/a)</td><td>41.50 (n/a)</td><td>1.55 (n/a)</td><td>45.17 (n/a)</td><td>42.91 (n/a)</td><td>42.40 (n/a)</td><td>41.48 (n/a)</td><td>1.55 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>9.29 (-2.44%)</td><td>8.31 (-3.33%)</td><td>8.53 (-0.07%)</td><td>6.91 (-12.35%)</td><td>0.89 <b>(+48.70%)</b></td><td>9.27 (-2.44%)</td><td>8.30 (-3.33%)</td><td>8.51 (-0.07%)</td><td>6.90 (-12.35%)</td><td>0.88 <b>(+48.70%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>9.52 (n/a)</td><td>8.60 (n/a)</td><td>8.54 (n/a)</td><td>7.88 (n/a)</td><td>0.60 (n/a)</td><td>9.51 (n/a)</td><td>8.58 (n/a)</td><td>8.52 (n/a)</td><td>7.87 (n/a)</td><td>0.59 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.99 (+1.82%)</td><td>0.85 (-4.95%)</td><td>0.79 (-10.86%)</td><td>0.75 (-5.84%)</td><td>0.10 <b>(+60.00%)</b></td><td>0.98 (+1.82%)</td><td>0.83 (-4.95%)</td><td>0.78 (-10.86%)</td><td>0.74 (-5.84%)</td><td>0.10 <b>(+60.00%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.98 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.80 (n/a)</td><td>0.06 (n/a)</td><td>0.96 (n/a)</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.79 (n/a)</td><td>0.06 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>1.13 (-18.55%)</td><td>1.02 (-10.42%)</td><td>1.03 (-1.49%)</td><td>0.89 (-7.93%)</td><td>0.09 <b>(-51.53%)</b></td><td>1.12 (-18.55%)</td><td>1.01 (-10.42%)</td><td>1.02 (-1.49%)</td><td>0.88 (-7.93%)</td><td>0.09 <b>(-51.53%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>1.39 (n/a)</td><td>1.14 (n/a)</td><td>1.05 (n/a)</td><td>0.96 (n/a)</td><td>0.19 (n/a)</td><td>1.37 (n/a)</td><td>1.13 (n/a)</td><td>1.04 (n/a)</td><td>0.95 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>19.38 (+5.48%)</td><td>16.46 (+2.73%)</td><td>16.12 (+2.92%)</td><td>14.78 (+6.03%)</td><td>1.76 (-7.68%)</td><td>19.15 (+5.48%)</td><td>16.27 (+2.73%)</td><td>15.93 (+2.92%)</td><td>14.61 (+6.03%)</td><td>1.74 (-7.68%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>18.37 (n/a)</td><td>16.02 (n/a)</td><td>15.66 (n/a)</td><td>13.94 (n/a)</td><td>1.91 (n/a)</td><td>18.16 (n/a)</td><td>15.84 (n/a)</td><td>15.48 (n/a)</td><td>13.78 (n/a)</td><td>1.89 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>13.45 (-1.78%)</td><td>13.04 (+6.90%)</td><td>12.96 (-1.87%)</td><td>12.69 <b>(+68.54%)</b></td><td>0.30 <b>(-88.63%)</b></td><td>13.22 (-1.78%)</td><td>12.81 (+6.90%)</td><td>12.73 (-1.87%)</td><td>12.47 <b>(+68.54%)</b></td><td>0.29 <b>(-88.63%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>13.70 (n/a)</td><td>12.20 (n/a)</td><td>13.20 (n/a)</td><td>7.53 (n/a)</td><td>2.62 (n/a)</td><td>13.46 (n/a)</td><td>11.98 (n/a)</td><td>12.97 (n/a)</td><td>7.40 (n/a)</td><td>2.57 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>7.80 (-15.89%)</td><td>6.95 (-14.61%)</td><td>7.20 (-9.18%)</td><td>6.01 (-18.61%)</td><td>0.71 (-11.24%)</td><td>7.67 (-15.89%)</td><td>6.83 (-14.61%)</td><td>7.08 (-9.18%)</td><td>5.91 (-18.61%)</td><td>0.69 (-11.24%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>9.28 (n/a)</td><td>8.14 (n/a)</td><td>7.93 (n/a)</td><td>7.39 (n/a)</td><td>0.79 (n/a)</td><td>9.12 (n/a)</td><td>8.00 (n/a)</td><td>7.79 (n/a)</td><td>7.26 (n/a)</td><td>0.78 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>6.06 (-5.65%)</td><td>5.34 (-5.42%)</td><td>5.47 (+1.59%)</td><td>4.62 (-6.62%)</td><td>0.55 (-10.46%)</td><td>5.96 (-5.65%)</td><td>5.25 (-5.42%)</td><td>5.38 (+1.59%)</td><td>4.54 (-6.62%)</td><td>0.55 (-10.46%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>6.42 (n/a)</td><td>5.64 (n/a)</td><td>5.38 (n/a)</td><td>4.94 (n/a)</td><td>0.62 (n/a)</td><td>6.32 (n/a)</td><td>5.55 (n/a)</td><td>5.30 (n/a)</td><td>4.86 (n/a)</td><td>0.61 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>13.34 (n/a)</td><td>12.62 (n/a)</td><td>13.13 (n/a)</td><td>10.88 (n/a)</td><td>1.01 (n/a)</td><td>13.33 (n/a)</td><td>12.61 (n/a)</td><td>13.12 (n/a)</td><td>10.87 (n/a)</td><td>1.01 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>13.37 (n/a)</td><td>11.92 (n/a)</td><td>12.09 (n/a)</td><td>10.48 (n/a)</td><td>1.15 (n/a)</td><td>13.36 (n/a)</td><td>11.91 (n/a)</td><td>12.09 (n/a)</td><td>10.48 (n/a)</td><td>1.15 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>220.90 (n/a)</td><td>168.96 (n/a)</td><td>166.00 (n/a)</td><td>130.50 (n/a)</td><td>33.46 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>198.50 (n/a)</td><td>156.02 (n/a)</td><td>142.70 (n/a)</td><td>131.70 (n/a)</td><td>28.53 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>229.00 (n/a)</td><td>175.50 (n/a)</td><td>167.00 (n/a)</td><td>138.20 (n/a)</td><td>33.18 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>202.10 (n/a)</td><td>182.24 (n/a)</td><td>181.40 (n/a)</td><td>164.10 (n/a)</td><td>13.95 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>190.30 (n/a)</td><td>175.82 (n/a)</td><td>178.20 (n/a)</td><td>152.30 (n/a)</td><td>14.68 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>222.60 (n/a)</td><td>178.82 (n/a)</td><td>183.30 (n/a)</td><td>128.40 (n/a)</td><td>41.88 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>259.70 (n/a)</td><td>215.76 (n/a)</td><td>221.90 (n/a)</td><td>155.70 (n/a)</td><td>44.11 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>327.90 (n/a)</td><td>239.08 (n/a)</td><td>232.30 (n/a)</td><td>150.40 (n/a)</td><td>64.30 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>281.20 (n/a)</td><td>206.80 (n/a)</td><td>187.90 (n/a)</td><td>147.60 (n/a)</td><td>52.83 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>186.30 (n/a)</td><td>165.46 (n/a)</td><td>160.20 (n/a)</td><td>148.70 (n/a)</td><td>14.94 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>164.20 (n/a)</td><td>143.20 (n/a)</td><td>133.90 (n/a)</td><td>127.60 (n/a)</td><td>18.21 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>198.30 (n/a)</td><td>185.60 (n/a)</td><td>188.40 (n/a)</td><td>165.40 (n/a)</td><td>12.49 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>367.40 (n/a)</td><td>218.32 (n/a)</td><td>204.10 (n/a)</td><td>134.20 (n/a)</td><td>91.75 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>295.70 (n/a)</td><td>203.42 (n/a)</td><td>201.00 (n/a)</td><td>130.20 (n/a)</td><td>60.74 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>314.70 (n/a)</td><td>200.98 (n/a)</td><td>184.60 (n/a)</td><td>140.90 (n/a)</td><td>68.27 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>237.40 (n/a)</td><td>219.30 (n/a)</td><td>232.90 (n/a)</td><td>189.30 (n/a)</td><td>22.49 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>203.80 (n/a)</td><td>182.90 (n/a)</td><td>176.20 (n/a)</td><td>163.10 (n/a)</td><td>16.35 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>199.10 (n/a)</td><td>172.06 (n/a)</td><td>173.90 (n/a)</td><td>139.20 (n/a)</td><td>25.94 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.00 (n/a)</td><td>187.40 (n/a)</td><td>181.48 (n/a)</td><td>185.10 (n/a)</td><td>166.60 (n/a)</td><td>8.61 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.00 (n/a)</td><td>200.60 (n/a)</td><td>187.78 (n/a)</td><td>186.20 (n/a)</td><td>176.60 (n/a)</td><td>10.23 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.00 (n/a)</td><td>173.80 (n/a)</td><td>169.56 (n/a)</td><td>171.60 (n/a)</td><td>159.90 (n/a)</td><td>5.56 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.00 (n/a)</td><td>213.50 (n/a)</td><td>204.60 (n/a)</td><td>207.10 (n/a)</td><td>192.50 (n/a)</td><td>9.26 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>224.70 (n/a)</td><td>199.82 (n/a)</td><td>204.50 (n/a)</td><td>161.60 (n/a)</td><td>24.15 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>229.00 (n/a)</td><td>208.08 (n/a)</td><td>222.60 (n/a)</td><td>145.30 (n/a)</td><td>35.44 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>238.60 (n/a)</td><td>189.90 (n/a)</td><td>188.30 (n/a)</td><td>153.90 (n/a)</td><td>34.10 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>217.60 (n/a)</td><td>190.88 (n/a)</td><td>192.50 (n/a)</td><td>173.40 (n/a)</td><td>17.40 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>234.10 (n/a)</td><td>204.96 (n/a)</td><td>195.20 (n/a)</td><td>182.00 (n/a)</td><td>24.80 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>229.10 (n/a)</td><td>173.40 (n/a)</td><td>147.90 (n/a)</td><td>138.20 (n/a)</td><td>42.03 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>193.00 (n/a)</td><td>170.52 (n/a)</td><td>172.40 (n/a)</td><td>145.10 (n/a)</td><td>17.07 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>196.10 (n/a)</td><td>178.72 (n/a)</td><td>189.10 (n/a)</td><td>151.10 (n/a)</td><td>18.68 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>188.00 (n/a)</td><td>170.44 (n/a)</td><td>164.70 (n/a)</td><td>152.90 (n/a)</td><td>14.67 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>237.60 (n/a)</td><td>214.00 (n/a)</td><td>213.80 (n/a)</td><td>193.40 (n/a)</td><td>19.18 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (-15.91%)</td><td>0.02 (-1.05%)</td><td>0.02 (-4.70%)</td><td>0.02 (+13.31%)</td><td>0.00 <b>(-53.98%)</b></td><td>201.80 (-11.76%)</td><td>184.14 (-1.33%)</td><td>186.50 (+4.95%)</td><td>166.60 (+18.92%)</td><td>16.88 <b>(-52.92%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>228.70 (n/a)</td><td>186.62 (n/a)</td><td>177.70 (n/a)</td><td>140.10 (n/a)</td><td>35.86 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 <b>(-21.98%)</b></td><td>0.02 (-3.74%)</td><td>0.02 (+2.01%)</td><td>0.02 (+1.81%)</td><td>0.00 <b>(-57.97%)</b></td><td>217.40 (-1.76%)</td><td>186.92 (+0.96%)</td><td>186.70 (-1.94%)</td><td>162.20 <b>(+28.22%)</b></td><td>19.98 <b>(-44.81%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>221.30 (n/a)</td><td>185.14 (n/a)</td><td>190.40 (n/a)</td><td>126.50 (n/a)</td><td>36.20 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 <b>(-30.09%)</b></td><td>0.02 (-14.80%)</td><td>0.02 (-2.71%)</td><td>0.02 (-6.07%)</td><td>0.00 <b>(-73.78%)</b></td><td>192.40 (+6.47%)</td><td>172.62 (+14.30%)</td><td>168.90 (+2.80%)</td><td>163.30 <b>(+42.99%)</b></td><td>11.38 <b>(-59.12%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>180.70 (n/a)</td><td>151.02 (n/a)</td><td>164.30 (n/a)</td><td>114.20 (n/a)</td><td>27.83 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (+16.95%)</td><td>0.02 (+4.02%)</td><td>0.02 (+5.94%)</td><td>0.02 (+5.44%)</td><td>0.01 <b>(+26.05%)</b></td><td>207.90 (-5.16%)</td><td>176.64 (-3.15%)</td><td>182.60 (-5.58%)</td><td>117.80 (-14.51%)</td><td>34.73 (-1.97%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.20 (n/a)</td><td>182.38 (n/a)</td><td>193.40 (n/a)</td><td>137.80 (n/a)</td><td>35.43 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (+15.27%)</td><td>0.02 (-3.40%)</td><td>0.02 (+0.10%)</td><td>0.02 (-16.89%)</td><td>0.01 <b>(+96.94%)</b></td><td>223.50 <b>(+20.29%)</b></td><td>176.24 (+6.67%)</td><td>171.90 (-0.12%)</td><td>123.70 (-13.25%)</td><td>37.93 <b>(+105.39%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>185.80 (n/a)</td><td>165.22 (n/a)</td><td>172.10 (n/a)</td><td>142.60 (n/a)</td><td>18.47 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (-11.86%)</td><td>0.02 (-10.21%)</td><td>0.02 (-8.66%)</td><td>0.02 (-10.65%)</td><td>0.00 (-16.57%)</td><td>245.80 (+11.93%)</td><td>204.20 (+11.12%)</td><td>194.00 (+9.48%)</td><td>166.30 (+13.52%)</td><td>30.85 (+5.61%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.60 (n/a)</td><td>183.76 (n/a)</td><td>177.20 (n/a)</td><td>146.50 (n/a)</td><td>29.21 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 <b>(-26.87%)</b></td><td>0.02 (-5.91%)</td><td>0.02 (-1.23%)</td><td>0.02 (+15.47%)</td><td>0.00 <b>(-69.92%)</b></td><td>219.80 (-13.40%)</td><td>195.90 (+2.28%)</td><td>190.40 (+1.22%)</td><td>182.50 <b>(+36.70%)</b></td><td>15.67 <b>(-64.01%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>253.80 (n/a)</td><td>191.54 (n/a)</td><td>188.10 (n/a)</td><td>133.50 (n/a)</td><td>43.52 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (-0.01%)</td><td>0.02 (+9.51%)</td><td>0.02 (+6.59%)</td><td>0.02 (+10.58%)</td><td>0.00 <b>(-22.48%)</b></td><td>270.50 (-9.56%)</td><td>222.50 (-9.85%)</td><td>217.80 (-6.20%)</td><td>190.20 (+0.00%)</td><td>31.34 <b>(-31.27%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>299.10 (n/a)</td><td>246.82 (n/a)</td><td>232.20 (n/a)</td><td>190.20 (n/a)</td><td>45.60 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (+15.14%)</td><td>0.05 (-5.87%)</td><td>0.04 (-13.38%)</td><td>0.02 <b>(-48.07%)</b></td><td>0.02 <b>(+204.58%)</b></td><td>364.50 <b>(+92.55%)</b></td><td>202.62 <b>(+20.98%)</b></td><td>187.80 (+15.43%)</td><td>126.60 (-13.17%)</td><td>95.90 <b>(+405.12%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.30 (n/a)</td><td>167.48 (n/a)</td><td>162.70 (n/a)</td><td>145.80 (n/a)</td><td>18.99 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.07 <b>(+29.20%)</b></td><td>0.05 (+6.38%)</td><td>0.04 (-9.79%)</td><td>0.04 (+15.21%)</td><td>0.01 <b>(+66.25%)</b></td><td>212.40 (-13.20%)</td><td>177.82 (-3.56%)</td><td>200.20 (+10.85%)</td><td>111.20 <b>(-22.62%)</b></td><td>41.91 (+9.25%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>244.70 (n/a)</td><td>184.38 (n/a)</td><td>180.60 (n/a)</td><td>143.70 (n/a)</td><td>38.36 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (-16.97%)</td><td>0.05 (-1.98%)</td><td>0.05 (-4.44%)</td><td>0.05 <b>(+32.65%)</b></td><td>0.00 <b>(-77.16%)</b></td><td>179.90 <b>(-24.63%)</b></td><td>168.92 (-1.93%)</td><td>168.70 (+4.65%)</td><td>157.10 <b>(+20.48%)</b></td><td>8.36 <b>(-79.83%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.70 (n/a)</td><td>172.24 (n/a)</td><td>161.20 (n/a)</td><td>130.40 (n/a)</td><td>41.45 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.08 (+12.14%)</td><td>0.05 (-3.89%)</td><td>0.04 (-7.75%)</td><td>0.04 (-2.89%)</td><td>0.01 <b>(+42.55%)</b></td><td>193.90 (+2.97%)</td><td>172.26 (+6.33%)</td><td>188.80 (+8.38%)</td><td>108.70 (-10.83%)</td><td>35.90 <b>(+27.48%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.30 (n/a)</td><td>162.00 (n/a)</td><td>174.20 (n/a)</td><td>121.90 (n/a)</td><td>28.16 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (-15.61%)</td><td>0.05 (+3.94%)</td><td>0.05 (+8.38%)</td><td>0.04 (+9.78%)</td><td>0.00 <b>(-60.78%)</b></td><td>188.80 (-8.92%)</td><td>171.20 (-5.58%)</td><td>170.00 (-7.76%)</td><td>159.70 (+18.47%)</td><td>12.09 <b>(-56.66%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.30 (n/a)</td><td>181.32 (n/a)</td><td>184.30 (n/a)</td><td>134.80 (n/a)</td><td>27.90 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.07 (+10.45%)</td><td>0.05 (+0.47%)</td><td>0.05 (-5.55%)</td><td>0.04 (+1.69%)</td><td>0.01 <b>(+38.21%)</b></td><td>191.60 (-1.69%)</td><td>170.40 (+0.65%)</td><td>176.80 (+5.87%)</td><td>120.80 (-9.51%)</td><td>28.51 <b>(+20.84%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.90 (n/a)</td><td>169.30 (n/a)</td><td>167.00 (n/a)</td><td>133.50 (n/a)</td><td>23.59 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (-1.63%)</td><td>0.05 (-0.74%)</td><td>0.05 (+6.29%)</td><td>0.04 (-3.18%)</td><td>0.01 (+5.82%)</td><td>207.40 (+3.29%)</td><td>179.46 (+1.12%)</td><td>177.10 (-5.90%)</td><td>142.80 (+1.64%)</td><td>28.10 (+14.79%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.80 (n/a)</td><td>177.48 (n/a)</td><td>188.20 (n/a)</td><td>140.50 (n/a)</td><td>24.48 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.08 <b>(+34.55%)</b></td><td>0.05 (+0.08%)</td><td>0.04 (-2.98%)</td><td>0.03 (-17.33%)</td><td>0.02 <b>(+116.63%)</b></td><td>254.40 <b>(+20.97%)</b></td><td>192.18 (+6.24%)</td><td>200.00 (+3.09%)</td><td>108.20 <b>(-25.64%)</b></td><td>53.76 <b>(+84.26%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.30 (n/a)</td><td>180.90 (n/a)</td><td>194.00 (n/a)</td><td>145.50 (n/a)</td><td>29.18 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (-0.95%)</td><td>0.04 (-9.89%)</td><td>0.04 (-15.65%)</td><td>0.03 (-14.74%)</td><td>0.01 <b>(+22.49%)</b></td><td>257.80 (+17.29%)</td><td>199.70 (+13.03%)</td><td>199.20 (+18.50%)</td><td>141.90 (+1.00%)</td><td>45.54 <b>(+43.38%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.80 (n/a)</td><td>176.68 (n/a)</td><td>168.10 (n/a)</td><td>140.50 (n/a)</td><td>31.76 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (+7.06%)</td><td>0.04 (+8.41%)</td><td>0.04 (+1.41%)</td><td>0.03 (+3.66%)</td><td>0.01 (+1.56%)</td><td>279.10 (-3.53%)</td><td>224.38 (-8.00%)</td><td>229.60 (-1.37%)</td><td>177.40 (-6.63%)</td><td>37.98 (-11.52%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>289.30 (n/a)</td><td>243.90 (n/a)</td><td>232.80 (n/a)</td><td>190.00 (n/a)</td><td>42.92 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.11 (-12.99%)</td><td>0.09 (-10.94%)</td><td>0.10 (-7.51%)</td><td>0.07 (-13.44%)</td><td>0.01 (-19.74%)</td><td>222.70 (+15.57%)</td><td>176.84 (+12.02%)</td><td>171.60 (+8.13%)</td><td>146.10 (+14.95%)</td><td>28.00 (+9.82%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>192.70 (n/a)</td><td>157.86 (n/a)</td><td>158.70 (n/a)</td><td>127.10 (n/a)</td><td>25.49 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.13 (-0.76%)</td><td>0.09 (-11.20%)</td><td>0.09 (-10.38%)</td><td>0.06 <b>(-31.34%)</b></td><td>0.02 <b>(+36.21%)</b></td><td>268.90 <b>(+45.67%)</b></td><td>183.72 (+16.83%)</td><td>178.60 (+11.56%)</td><td>127.60 (+0.71%)</td><td>52.75 <b>(+104.14%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>184.60 (n/a)</td><td>157.26 (n/a)</td><td>160.10 (n/a)</td><td>126.70 (n/a)</td><td>25.84 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.09 (-15.25%)</td><td>0.09 (-2.09%)</td><td>0.09 (-11.89%)</td><td>0.08 <b>(+35.50%)</b></td><td>0.00 <b>(-76.73%)</b></td><td>208.10 <b>(-26.18%)</b></td><td>188.84 (-3.14%)</td><td>182.10 (+13.53%)</td><td>181.20 (+18.05%)</td><td>11.46 <b>(-79.36%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>281.90 (n/a)</td><td>194.96 (n/a)</td><td>160.40 (n/a)</td><td>153.50 (n/a)</td><td>55.52 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.12 (+17.22%)</td><td>0.09 (+7.28%)</td><td>0.08 (-8.73%)</td><td>0.05 (-16.12%)</td><td>0.03 <b>(+68.93%)</b></td><td>338.30 (+19.20%)</td><td>204.44 (-0.68%)</td><td>200.00 (+9.59%)</td><td>140.00 (-14.69%)</td><td>80.45 <b>(+66.58%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>283.80 (n/a)</td><td>205.84 (n/a)</td><td>182.50 (n/a)</td><td>164.10 (n/a)</td><td>48.30 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.09 <b>(-33.03%)</b></td><td>0.08 (-19.64%)</td><td>0.08 (-19.89%)</td><td>0.08 (-0.93%)</td><td>0.00 <b>(-77.60%)</b></td><td>211.10 (+0.96%)</td><td>196.38 <b>(+21.21%)</b></td><td>196.40 <b>(+24.86%)</b></td><td>183.50 <b>(+49.31%)</b></td><td>10.41 <b>(-66.28%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>209.10 (n/a)</td><td>162.02 (n/a)</td><td>157.30 (n/a)</td><td>122.90 (n/a)</td><td>30.87 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.12 (+4.05%)</td><td>0.10 (-0.38%)</td><td>0.09 (+0.04%)</td><td>0.08 (-2.66%)</td><td>0.02 (+13.66%)</td><td>203.80 (+2.72%)</td><td>173.92 (+0.75%)</td><td>178.60 (-0.06%)</td><td>133.90 (-3.88%)</td><td>25.58 (+9.70%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>198.40 (n/a)</td><td>172.62 (n/a)</td><td>178.70 (n/a)</td><td>139.30 (n/a)</td><td>23.32 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.10 (+6.35%)</td><td>0.09 (-0.69%)</td><td>0.09 (-4.13%)</td><td>0.07 (-8.53%)</td><td>0.01 <b>(+81.11%)</b></td><td>224.90 (+9.33%)</td><td>189.12 (+1.52%)</td><td>188.00 (+4.33%)</td><td>164.80 (-5.99%)</td><td>23.37 <b>(+86.20%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>205.70 (n/a)</td><td>186.28 (n/a)</td><td>180.20 (n/a)</td><td>175.30 (n/a)</td><td>12.55 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.08 (-12.44%)</td><td>0.07 (-0.54%)</td><td>0.07 (-0.18%)</td><td>0.06 (+3.07%)</td><td>0.01 <b>(-39.67%)</b></td><td>272.80 (-2.95%)</td><td>228.46 (-0.92%)</td><td>223.20 (+0.18%)</td><td>200.30 (+14.26%)</td><td>27.30 <b>(-31.56%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>281.10 (n/a)</td><td>230.58 (n/a)</td><td>222.80 (n/a)</td><td>175.30 (n/a)</td><td>39.89 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.23 (+3.19%)</td><td>0.18 (-8.09%)</td><td>0.18 (-12.18%)</td><td>0.15 (-14.76%)</td><td>0.03 <b>(+97.17%)</b></td><td>215.60 (+17.30%)</td><td>184.76 (+10.75%)</td><td>186.30 (+13.88%)</td><td>144.40 (-3.09%)</td><td>30.43 <b>(+127.10%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>183.80 (n/a)</td><td>166.82 (n/a)</td><td>163.60 (n/a)</td><td>149.00 (n/a)</td><td>13.40 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.23 (-4.43%)</td><td>0.19 (-12.15%)</td><td>0.18 (-17.23%)</td><td>0.15 <b>(-20.16%)</b></td><td>0.04 <b>(+66.23%)</b></td><td>221.10 <b>(+25.27%)</b></td><td>180.20 (+16.15%)</td><td>183.90 <b>(+20.83%)</b></td><td>140.50 (+4.62%)</td><td>33.21 <b>(+116.66%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>176.50 (n/a)</td><td>155.14 (n/a)</td><td>152.20 (n/a)</td><td>134.30 (n/a)</td><td>15.33 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.31 (-5.64%)</td><td>0.22 (+2.44%)</td><td>0.20 (+11.22%)</td><td>0.17 (-4.36%)</td><td>0.05 (-14.02%)</td><td>190.70 (+4.55%)</td><td>158.54 (-3.29%)</td><td>160.20 (-10.10%)</td><td>107.10 (+5.93%)</td><td>34.07 (-3.17%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.32 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>182.40 (n/a)</td><td>163.94 (n/a)</td><td>178.20 (n/a)</td><td>101.10 (n/a)</td><td>35.18 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.24 (-0.60%)</td><td>0.19 (+6.49%)</td><td>0.21 (+6.51%)</td><td>0.13 (+18.59%)</td><td>0.04 (-14.68%)</td><td>255.50 (-15.68%)</td><td>176.16 (-8.68%)</td><td>158.70 (-6.15%)</td><td>136.50 (+0.59%)</td><td>47.00 <b>(-28.23%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>303.00 (n/a)</td><td>192.90 (n/a)</td><td>169.10 (n/a)</td><td>135.70 (n/a)</td><td>65.49 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.33 <b>(+51.92%)</b></td><td>0.24 <b>(+34.57%)</b></td><td>0.22 <b>(+30.13%)</b></td><td>0.18 (+12.20%)</td><td>0.06 <b>(+155.05%)</b></td><td>181.20 (-10.87%)</td><td>141.52 <b>(-23.33%)</b></td><td>148.60 <b>(-23.16%)</b></td><td>99.80 <b>(-34.17%)</b></td><td>31.53 <b>(+47.67%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>203.30 (n/a)</td><td>184.58 (n/a)</td><td>193.40 (n/a)</td><td>151.60 (n/a)</td><td>21.35 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.25 (-6.48%)</td><td>0.18 (-0.95%)</td><td>0.16 (-6.30%)</td><td>0.14 (+16.35%)</td><td>0.04 <b>(-23.49%)</b></td><td>233.60 (-14.09%)</td><td>191.88 (-2.15%)</td><td>200.60 (+6.76%)</td><td>131.40 (+6.92%)</td><td>37.42 <b>(-31.82%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>271.90 (n/a)</td><td>196.10 (n/a)</td><td>187.90 (n/a)</td><td>122.90 (n/a)</td><td>54.89 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.16 <b>(-32.93%)</b></td><td>0.14 (-18.56%)</td><td>0.14 (-6.31%)</td><td>0.10 <b>(-27.13%)</b></td><td>0.02 <b>(-45.24%)</b></td><td>326.80 <b>(+37.25%)</b></td><td>242.88 <b>(+21.15%)</b></td><td>228.60 (+6.72%)</td><td>204.00 <b>(+49.12%)</b></td><td>48.14 (+19.07%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>238.10 (n/a)</td><td>200.48 (n/a)</td><td>214.20 (n/a)</td><td>136.80 (n/a)</td><td>40.43 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 <b>(-21.17%)</b></td><td>0.03 (-2.54%)</td><td>0.02 (+7.17%)</td><td>0.02 (-6.84%)</td><td>0.00 <b>(-38.90%)</b></td><td>193.10 (+7.34%)</td><td>163.36 (+0.37%)</td><td>164.90 (-6.68%)</td><td>131.60 <b>(+26.90%)</b></td><td>27.95 (-15.46%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>179.90 (n/a)</td><td>162.76 (n/a)</td><td>176.70 (n/a)</td><td>103.70 (n/a)</td><td>33.06 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (-10.35%)</td><td>0.03 (+3.40%)</td><td>0.03 (+15.35%)</td><td>0.02 (-2.36%)</td><td>0.00 <b>(-22.42%)</b></td><td>171.10 (+2.46%)</td><td>135.66 (-3.87%)</td><td>127.20 (-13.29%)</td><td>120.20 (+11.50%)</td><td>20.59 (-7.64%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>167.00 (n/a)</td><td>141.12 (n/a)</td><td>146.70 (n/a)</td><td>107.80 (n/a)</td><td>22.29 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (-17.04%)</td><td>0.02 (-10.32%)</td><td>0.02 (+3.78%)</td><td>0.01 <b>(-20.81%)</b></td><td>0.00 (+6.27%)</td><td>320.40 <b>(+26.24%)</b></td><td>251.36 (+13.84%)</td><td>222.60 (-3.64%)</td><td>193.90 <b>(+20.58%)</b></td><td>61.40 <b>(+73.57%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>253.80 (n/a)</td><td>220.80 (n/a)</td><td>231.00 (n/a)</td><td>160.80 (n/a)</td><td>35.38 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 <b>(-24.58%)</b></td><td>0.02 (-19.58%)</td><td>0.02 (-12.80%)</td><td>0.02 <b>(-21.01%)</b></td><td>0.00 <b>(-47.14%)</b></td><td>270.60 <b>(+26.63%)</b></td><td>241.72 <b>(+23.67%)</b></td><td>237.40 (+14.69%)</td><td>222.30 <b>(+32.56%)</b></td><td>19.03 (-11.44%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.70 (n/a)</td><td>195.46 (n/a)</td><td>207.00 (n/a)</td><td>167.70 (n/a)</td><td>21.49 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 <b>(+20.83%)</b></td><td>0.03 (+10.49%)</td><td>0.02 (+8.80%)</td><td>0.02 (+4.38%)</td><td>0.00 <b>(+86.47%)</b></td><td>180.50 (-4.19%)</td><td>161.08 (-8.57%)</td><td>167.20 (-8.08%)</td><td>127.30 (-17.28%)</td><td>21.67 <b>(+46.89%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>188.40 (n/a)</td><td>176.18 (n/a)</td><td>181.90 (n/a)</td><td>153.90 (n/a)</td><td>14.75 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.04 <b>(+42.60%)</b></td><td>0.03 (+15.02%)</td><td>0.03 (+19.43%)</td><td>0.02 <b>(-21.00%)</b></td><td>0.01 <b>(+326.78%)</b></td><td>236.60 <b>(+26.59%)</b></td><td>161.42 (-7.37%)</td><td>150.60 (-16.29%)</td><td>112.00 <b>(-29.91%)</b></td><td>49.01 <b>(+285.13%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>186.90 (n/a)</td><td>174.26 (n/a)</td><td>179.90 (n/a)</td><td>159.80 (n/a)</td><td>12.73 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (-0.17%)</td><td>0.02 (-11.55%)</td><td>0.02 (-15.58%)</td><td>0.02 (-8.72%)</td><td>0.00 <b>(+36.47%)</b></td><td>192.00 (+9.59%)</td><td>171.16 (+14.08%)</td><td>171.90 (+18.47%)</td><td>133.30 (+0.23%)</td><td>23.61 <b>(+47.06%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>175.20 (n/a)</td><td>150.04 (n/a)</td><td>145.10 (n/a)</td><td>133.00 (n/a)</td><td>16.05 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (-5.84%)</td><td>0.02 <b>(-23.30%)</b></td><td>0.02 <b>(-29.05%)</b></td><td>0.02 <b>(-36.51%)</b></td><td>0.01 <b>(+69.41%)</b></td><td>268.80 <b>(+57.47%)</b></td><td>192.30 <b>(+38.88%)</b></td><td>182.00 <b>(+40.98%)</b></td><td>126.30 (+6.22%)</td><td>60.50 <b>(+184.55%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>170.70 (n/a)</td><td>138.46 (n/a)</td><td>129.10 (n/a)</td><td>118.90 (n/a)</td><td>21.26 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (-19.20%)</td><td>0.02 (-15.90%)</td><td>0.03 (-1.63%)</td><td>0.02 <b>(-36.25%)</b></td><td>0.01 (+7.10%)</td><td>272.50 <b>(+56.88%)</b></td><td>175.58 <b>(+23.32%)</b></td><td>144.40 (+1.69%)</td><td>136.00 <b>(+23.75%)</b></td><td>57.50 <b>(+106.24%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>173.70 (n/a)</td><td>142.38 (n/a)</td><td>142.00 (n/a)</td><td>109.90 (n/a)</td><td>27.88 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (-18.97%)</td><td>0.02 (-17.51%)</td><td>0.02 (-17.21%)</td><td>0.02 (-18.54%)</td><td>0.01 (-10.77%)</td><td>233.00 <b>(+22.76%)</b></td><td>177.40 <b>(+22.34%)</b></td><td>177.60 <b>(+20.73%)</b></td><td>125.80 <b>(+23.33%)</b></td><td>43.76 <b>(+36.77%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>189.80 (n/a)</td><td>145.00 (n/a)</td><td>147.10 (n/a)</td><td>102.00 (n/a)</td><td>32.00 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (-0.46%)</td><td>0.02 (+1.70%)</td><td>0.02 (+11.89%)</td><td>0.02 (-4.15%)</td><td>0.00 (+8.29%)</td><td>234.30 (+4.37%)</td><td>182.02 (-1.10%)</td><td>173.90 (-10.64%)</td><td>148.20 (+0.47%)</td><td>36.55 (+14.10%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>224.50 (n/a)</td><td>184.04 (n/a)</td><td>194.60 (n/a)</td><td>147.50 (n/a)</td><td>32.03 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (+12.59%)</td><td>0.02 (-1.97%)</td><td>0.02 (-6.97%)</td><td>0.02 (-8.50%)</td><td>0.00 <b>(+87.13%)</b></td><td>201.60 (+9.33%)</td><td>171.78 (+3.68%)</td><td>178.50 (+7.53%)</td><td>127.80 (-11.13%)</td><td>27.03 <b>(+75.21%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>184.40 (n/a)</td><td>165.68 (n/a)</td><td>166.00 (n/a)</td><td>143.80 (n/a)</td><td>15.43 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (-11.66%)</td><td>0.02 (-7.27%)</td><td>0.02 (-4.46%)</td><td>0.02 (-8.11%)</td><td>0.00 (-10.97%)</td><td>232.00 (+8.87%)</td><td>204.36 (+7.83%)</td><td>198.80 (+4.69%)</td><td>183.10 (+13.23%)</td><td>21.87 (+9.52%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.10 (n/a)</td><td>189.52 (n/a)</td><td>189.90 (n/a)</td><td>161.70 (n/a)</td><td>19.97 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (-7.17%)</td><td>0.02 (-2.43%)</td><td>0.02 (+3.10%)</td><td>0.02 (+8.72%)</td><td>0.00 <b>(-32.49%)</b></td><td>207.50 (-8.02%)</td><td>185.16 (+1.28%)</td><td>184.10 (-3.05%)</td><td>162.50 (+7.69%)</td><td>21.04 <b>(-31.12%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>225.60 (n/a)</td><td>182.82 (n/a)</td><td>189.90 (n/a)</td><td>150.90 (n/a)</td><td>30.55 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (+0.34%)</td><td>0.02 (-17.46%)</td><td>0.02 <b>(-27.84%)</b></td><td>0.02 (-7.98%)</td><td>0.00 (+6.95%)</td><td>261.70 (+8.63%)</td><td>216.70 <b>(+21.93%)</b></td><td>226.30 <b>(+38.58%)</b></td><td>145.30 (-0.34%)</td><td>44.06 (+11.76%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>240.90 (n/a)</td><td>177.72 (n/a)</td><td>163.30 (n/a)</td><td>145.80 (n/a)</td><td>39.42 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 <b>(-30.96%)</b></td><td>0.02 <b>(-20.62%)</b></td><td>0.02 <b>(-22.54%)</b></td><td>0.02 (+6.02%)</td><td>0.00 <b>(-84.00%)</b></td><td>221.10 (-5.67%)</td><td>214.28 <b>(+22.03%)</b></td><td>219.20 <b>(+29.09%)</b></td><td>202.10 <b>(+44.87%)</b></td><td>8.11 <b>(-78.26%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>234.40 (n/a)</td><td>175.60 (n/a)</td><td>169.80 (n/a)</td><td>139.50 (n/a)</td><td>37.33 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (-18.94%)</td><td>0.04 (-10.54%)</td><td>0.04 (-15.41%)</td><td>0.04 (-4.61%)</td><td>0.01 <b>(-36.33%)</b></td><td>215.80 (+4.81%)</td><td>185.04 (+10.23%)</td><td>189.00 (+18.27%)</td><td>159.80 <b>(+23.40%)</b></td><td>24.72 <b>(-21.23%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.90 (n/a)</td><td>167.86 (n/a)</td><td>159.80 (n/a)</td><td>129.50 (n/a)</td><td>31.38 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (-15.95%)</td><td>0.05 (-5.52%)</td><td>0.05 (+4.28%)</td><td>0.04 (+10.32%)</td><td>0.00 <b>(-63.71%)</b></td><td>189.60 (-9.37%)</td><td>175.02 (+3.39%)</td><td>173.40 (-4.09%)</td><td>161.10 (+18.98%)</td><td>12.59 <b>(-59.47%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.20 (n/a)</td><td>169.28 (n/a)</td><td>180.80 (n/a)</td><td>135.40 (n/a)</td><td>31.07 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (+10.20%)</td><td>0.04 (-4.95%)</td><td>0.04 (+0.32%)</td><td>0.02 <b>(-26.85%)</b></td><td>0.01 <b>(+95.98%)</b></td><td>328.70 <b>(+36.67%)</b></td><td>233.12 (+9.05%)</td><td>221.30 (-0.32%)</td><td>171.30 (-9.27%)</td><td>58.77 <b>(+155.42%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>240.50 (n/a)</td><td>213.78 (n/a)</td><td>222.00 (n/a)</td><td>188.80 (n/a)</td><td>23.01 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.04 <b>(-23.55%)</b></td><td>0.04 (-14.06%)</td><td>0.04 (-9.64%)</td><td>0.04 (-10.04%)</td><td>0.00 <b>(-54.54%)</b></td><td>227.90 (+11.17%)</td><td>213.08 (+15.53%)</td><td>210.00 (+10.64%)</td><td>199.80 <b>(+30.84%)</b></td><td>13.62 <b>(-32.88%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.00 (n/a)</td><td>184.44 (n/a)</td><td>189.80 (n/a)</td><td>152.70 (n/a)</td><td>20.29 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 <b>(-27.59%)</b></td><td>0.04 <b>(-29.18%)</b></td><td>0.04 <b>(-25.22%)</b></td><td>0.03 <b>(-36.80%)</b></td><td>0.01 (-6.01%)</td><td>250.10 <b>(+58.29%)</b></td><td>200.02 <b>(+42.63%)</b></td><td>186.40 <b>(+33.72%)</b></td><td>165.90 <b>(+38.02%)</b></td><td>33.53 <b>(+105.43%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>158.00 (n/a)</td><td>140.24 (n/a)</td><td>139.40 (n/a)</td><td>120.20 (n/a)</td><td>16.32 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (-6.52%)</td><td>0.05 (-11.90%)</td><td>0.05 (+3.60%)</td><td>0.03 (-16.27%)</td><td>0.01 (-12.31%)</td><td>234.20 (+19.43%)</td><td>186.96 (+13.46%)</td><td>179.40 (-3.44%)</td><td>132.60 (+6.94%)</td><td>40.94 (+14.65%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.10 (n/a)</td><td>164.78 (n/a)</td><td>185.80 (n/a)</td><td>124.00 (n/a)</td><td>35.71 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (-6.36%)</td><td>0.05 (-11.28%)</td><td>0.05 (-9.96%)</td><td>0.04 (-6.99%)</td><td>0.01 (-13.22%)</td><td>201.20 (+7.54%)</td><td>169.98 (+12.29%)</td><td>174.90 (+11.05%)</td><td>128.70 (+6.80%)</td><td>26.80 (-1.14%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.10 (n/a)</td><td>151.38 (n/a)</td><td>157.50 (n/a)</td><td>120.50 (n/a)</td><td>27.11 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (-16.59%)</td><td>0.04 <b>(-22.95%)</b></td><td>0.05 <b>(-20.64%)</b></td><td>0.02 <b>(-50.90%)</b></td><td>0.01 (+18.53%)</td><td>375.60 <b>(+103.69%)</b></td><td>210.00 <b>(+40.94%)</b></td><td>176.60 <b>(+25.96%)</b></td><td>134.90 (+19.80%)</td><td>94.73 <b>(+207.40%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>184.40 (n/a)</td><td>149.00 (n/a)</td><td>140.20 (n/a)</td><td>112.60 (n/a)</td><td>30.82 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 <b>(-20.67%)</b></td><td>0.04 <b>(-28.66%)</b></td><td>0.04 <b>(-32.47%)</b></td><td>0.03 <b>(-29.07%)</b></td><td>0.01 (+8.26%)</td><td>234.60 <b>(+40.99%)</b></td><td>194.82 <b>(+41.54%)</b></td><td>194.30 <b>(+48.09%)</b></td><td>162.00 <b>(+26.07%)</b></td><td>30.42 <b>(+88.33%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>166.40 (n/a)</td><td>137.64 (n/a)</td><td>131.20 (n/a)</td><td>128.50 (n/a)</td><td>16.15 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (-8.76%)</td><td>0.05 (-17.55%)</td><td>0.05 (-17.89%)</td><td>0.04 (-14.79%)</td><td>0.01 (-3.39%)</td><td>217.50 (+17.31%)</td><td>176.84 <b>(+21.81%)</b></td><td>177.90 <b>(+21.85%)</b></td><td>129.20 (+9.68%)</td><td>32.18 <b>(+21.35%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>185.40 (n/a)</td><td>145.18 (n/a)</td><td>146.00 (n/a)</td><td>117.80 (n/a)</td><td>26.52 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.07 (-3.24%)</td><td>0.05 (-18.21%)</td><td>0.05 <b>(-30.12%)</b></td><td>0.03 <b>(-31.86%)</b></td><td>0.02 <b>(+80.93%)</b></td><td>241.60 <b>(+46.78%)</b></td><td>177.30 <b>(+31.02%)</b></td><td>182.00 <b>(+43.08%)</b></td><td>115.30 (+3.32%)</td><td>56.54 <b>(+167.52%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>164.60 (n/a)</td><td>135.32 (n/a)</td><td>127.20 (n/a)</td><td>111.60 (n/a)</td><td>21.14 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.07 (+5.96%)</td><td>0.05 (-11.05%)</td><td>0.05 (-16.22%)</td><td>0.04 <b>(-28.15%)</b></td><td>0.01 <b>(+128.07%)</b></td><td>232.30 <b>(+39.19%)</b></td><td>176.26 (+18.97%)</td><td>179.70 (+19.32%)</td><td>117.30 (-5.63%)</td><td>48.82 <b>(+204.08%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>166.90 (n/a)</td><td>148.16 (n/a)</td><td>150.60 (n/a)</td><td>124.30 (n/a)</td><td>16.05 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (+6.10%)</td><td>0.04 (-4.96%)</td><td>0.04 (-15.49%)</td><td>0.03 <b>(+24.32%)</b></td><td>0.01 (-10.60%)</td><td>239.50 (-19.55%)</td><td>191.98 (+2.17%)</td><td>199.80 (+18.36%)</td><td>134.10 (-5.76%)</td><td>38.55 <b>(-38.35%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>297.70 (n/a)</td><td>187.90 (n/a)</td><td>168.80 (n/a)</td><td>142.30 (n/a)</td><td>62.52 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (-4.36%)</td><td>0.05 (-9.08%)</td><td>0.05 (-0.78%)</td><td>0.04 (-17.37%)</td><td>0.01 (+19.60%)</td><td>214.70 <b>(+21.03%)</b></td><td>178.46 (+11.12%)</td><td>174.10 (+0.81%)</td><td>145.60 (+4.60%)</td><td>29.95 <b>(+53.82%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>177.40 (n/a)</td><td>160.60 (n/a)</td><td>172.70 (n/a)</td><td>139.20 (n/a)</td><td>19.47 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.07 (+17.08%)</td><td>0.05 (-0.68%)</td><td>0.04 (-17.51%)</td><td>0.04 <b>(+27.01%)</b></td><td>0.01 (+1.56%)</td><td>200.70 <b>(-21.23%)</b></td><td>179.86 (-0.70%)</td><td>190.60 <b>(+21.25%)</b></td><td>124.40 (-14.62%)</td><td>31.60 <b>(-32.17%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>254.80 (n/a)</td><td>181.12 (n/a)</td><td>157.20 (n/a)</td><td>145.70 (n/a)</td><td>46.60 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (-6.94%)</td><td>0.04 (-18.54%)</td><td>0.04 <b>(-23.84%)</b></td><td>0.03 (-17.02%)</td><td>0.01 (-2.04%)</td><td>239.20 <b>(+20.50%)</b></td><td>189.80 <b>(+23.54%)</b></td><td>189.40 <b>(+31.35%)</b></td><td>132.40 (+7.47%)</td><td>39.06 <b>(+23.73%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.50 (n/a)</td><td>153.64 (n/a)</td><td>144.20 (n/a)</td><td>123.20 (n/a)</td><td>31.57 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.11 <b>(-21.50%)</b></td><td>0.10 (-8.98%)</td><td>0.09 (-6.84%)</td><td>0.08 (-7.75%)</td><td>0.01 <b>(-36.37%)</b></td><td>211.80 (+8.39%)</td><td>173.04 (+8.67%)</td><td>174.40 (+7.32%)</td><td>151.10 <b>(+27.40%)</b></td><td>24.54 (-10.52%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>195.40 (n/a)</td><td>159.24 (n/a)</td><td>162.50 (n/a)</td><td>118.60 (n/a)</td><td>27.42 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.14 (+1.02%)</td><td>0.10 (-15.43%)</td><td>0.09 <b>(-21.11%)</b></td><td>0.08 (-16.38%)</td><td>0.02 <b>(+28.77%)</b></td><td>203.00 (+19.62%)</td><td>171.96 <b>(+20.39%)</b></td><td>177.40 <b>(+26.80%)</b></td><td>115.00 (-1.03%)</td><td>33.62 <b>(+43.99%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>169.70 (n/a)</td><td>142.84 (n/a)</td><td>139.90 (n/a)</td><td>116.20 (n/a)</td><td>23.35 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.10 (+11.02%)</td><td>0.08 (+2.02%)</td><td>0.08 (-5.56%)</td><td>0.07 <b>(+38.88%)</b></td><td>0.01 <b>(-27.83%)</b></td><td>245.20 <b>(-28.01%)</b></td><td>215.70 (-5.11%)</td><td>213.60 (+5.85%)</td><td>170.60 (-9.93%)</td><td>29.07 <b>(-54.66%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>340.60 (n/a)</td><td>227.32 (n/a)</td><td>201.80 (n/a)</td><td>189.40 (n/a)</td><td>64.11 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.10 (-8.90%)</td><td>0.08 (-16.59%)</td><td>0.08 <b>(-20.19%)</b></td><td>0.05 <b>(-27.77%)</b></td><td>0.02 <b>(+23.28%)</b></td><td>324.50 <b>(+38.50%)</b></td><td>229.50 <b>(+24.09%)</b></td><td>217.20 <b>(+25.33%)</b></td><td>157.20 (+9.78%)</td><td>64.88 <b>(+87.06%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>234.30 (n/a)</td><td>184.94 (n/a)</td><td>173.30 (n/a)</td><td>143.20 (n/a)</td><td>34.68 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.12 (-13.50%)</td><td>0.10 (-13.62%)</td><td>0.10 <b>(-22.38%)</b></td><td>0.09 (-3.89%)</td><td>0.01 <b>(-34.94%)</b></td><td>192.70 (+4.05%)</td><td>169.22 (+13.83%)</td><td>170.00 <b>(+28.89%)</b></td><td>134.50 (+15.55%)</td><td>23.52 <b>(-23.90%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>185.20 (n/a)</td><td>148.66 (n/a)</td><td>131.90 (n/a)</td><td>116.40 (n/a)</td><td>30.90 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.14 (+1.20%)</td><td>0.11 (-4.83%)</td><td>0.10 (+2.26%)</td><td>0.08 <b>(-20.58%)</b></td><td>0.03 (+9.77%)</td><td>209.10 <b>(+25.96%)</b></td><td>154.52 (+6.54%)</td><td>159.40 (-2.21%)</td><td>113.10 (-1.14%)</td><td>36.63 <b>(+35.90%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>166.00 (n/a)</td><td>145.04 (n/a)</td><td>163.00 (n/a)</td><td>114.40 (n/a)</td><td>26.95 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.12 <b>(-31.53%)</b></td><td>0.11 (-12.91%)</td><td>0.10 (-3.19%)</td><td>0.10 (+8.20%)</td><td>0.01 <b>(-74.34%)</b></td><td>167.90 (-7.59%)</td><td>156.44 (+8.46%)</td><td>162.00 (+3.32%)</td><td>140.60 <b>(+46.00%)</b></td><td>13.04 <b>(-65.58%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>181.70 (n/a)</td><td>144.24 (n/a)</td><td>156.80 (n/a)</td><td>96.30 (n/a)</td><td>37.90 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.11 (+2.27%)</td><td>0.10 (+9.68%)</td><td>0.10 (+13.31%)</td><td>0.10 (+16.09%)</td><td>0.00 <b>(-48.70%)</b></td><td>166.60 (-13.86%)</td><td>160.08 (-9.23%)</td><td>159.50 (-11.73%)</td><td>151.20 (-2.26%)</td><td>6.40 <b>(-56.04%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>193.40 (n/a)</td><td>176.36 (n/a)</td><td>180.70 (n/a)</td><td>154.70 (n/a)</td><td>14.56 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.12 (-7.02%)</td><td>0.11 (+5.67%)</td><td>0.11 (+16.20%)</td><td>0.09 (+3.21%)</td><td>0.01 <b>(-29.05%)</b></td><td>176.70 (-3.07%)</td><td>153.46 (-6.26%)</td><td>148.30 (-13.93%)</td><td>131.30 (+7.53%)</td><td>18.43 <b>(-23.27%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>182.30 (n/a)</td><td>163.70 (n/a)</td><td>172.30 (n/a)</td><td>122.10 (n/a)</td><td>24.02 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.14 (+4.90%)</td><td>0.09 (-7.51%)</td><td>0.08 (-17.88%)</td><td>0.07 (-11.45%)</td><td>0.03 <b>(+28.51%)</b></td><td>230.40 (+12.89%)</td><td>188.48 (+10.73%)</td><td>211.50 <b>(+21.76%)</b></td><td>118.50 (-4.67%)</td><td>45.16 <b>(+33.96%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>204.10 (n/a)</td><td>170.22 (n/a)</td><td>173.70 (n/a)</td><td>124.30 (n/a)</td><td>33.71 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.11 (-18.55%)</td><td>0.09 (-9.71%)</td><td>0.09 (-2.36%)</td><td>0.08 (-10.46%)</td><td>0.01 <b>(-36.41%)</b></td><td>206.30 (+11.69%)</td><td>179.24 (+9.77%)</td><td>175.40 (+2.39%)</td><td>149.80 <b>(+22.79%)</b></td><td>21.79 (-9.35%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>184.70 (n/a)</td><td>163.28 (n/a)</td><td>171.30 (n/a)</td><td>122.00 (n/a)</td><td>24.04 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.12 (-8.01%)</td><td>0.11 (+13.16%)</td><td>0.11 <b>(+20.29%)</b></td><td>0.09 <b>(+39.41%)</b></td><td>0.01 <b>(-50.57%)</b></td><td>175.80 <b>(-28.27%)</b></td><td>156.30 (-14.67%)</td><td>152.40 (-16.90%)</td><td>140.00 (+8.70%)</td><td>16.47 <b>(-61.16%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>245.10 (n/a)</td><td>183.18 (n/a)</td><td>183.40 (n/a)</td><td>128.80 (n/a)</td><td>42.40 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.13 <b>(+21.62%)</b></td><td>0.09 (-7.30%)</td><td>0.08 <b>(-24.98%)</b></td><td>0.08 (+8.41%)</td><td>0.02 <b>(+49.40%)</b></td><td>217.90 (-7.75%)</td><td>189.28 (+9.77%)</td><td>211.60 <b>(+33.25%)</b></td><td>124.70 (-17.74%)</td><td>39.67 (+10.74%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>236.20 (n/a)</td><td>172.44 (n/a)</td><td>158.80 (n/a)</td><td>151.60 (n/a)</td><td>35.82 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.11 (-0.36%)</td><td>0.10 (+3.13%)</td><td>0.10 (+8.48%)</td><td>0.08 (+0.69%)</td><td>0.01 (-2.79%)</td><td>216.60 (-0.69%)</td><td>175.14 (-3.14%)</td><td>165.50 (-7.85%)</td><td>154.00 (+0.33%)</td><td>26.50 (-2.52%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>218.10 (n/a)</td><td>180.82 (n/a)</td><td>179.60 (n/a)</td><td>153.50 (n/a)</td><td>27.18 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.11 (+4.97%)</td><td>0.09 (+1.20%)</td><td>0.09 (+0.55%)</td><td>0.07 (-4.78%)</td><td>0.02 (+18.78%)</td><td>229.50 (+4.99%)</td><td>181.44 (-0.37%)</td><td>179.50 (-0.55%)</td><td>143.00 (-4.73%)</td><td>34.79 (+18.66%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>218.60 (n/a)</td><td>182.12 (n/a)</td><td>180.50 (n/a)</td><td>150.10 (n/a)</td><td>29.32 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.10 <b>(-21.45%)</b></td><td>0.08 (-17.19%)</td><td>0.09 (-11.75%)</td><td>0.07 (-18.18%)</td><td>0.01 <b>(-33.29%)</b></td><td>247.60 <b>(+22.21%)</b></td><td>198.02 (+19.46%)</td><td>184.20 (+13.35%)</td><td>160.20 <b>(+27.34%)</b></td><td>35.04 (+2.51%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>202.60 (n/a)</td><td>165.76 (n/a)</td><td>162.50 (n/a)</td><td>125.80 (n/a)</td><td>34.18 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.24 <b>(-38.65%)</b></td><td>0.21 (-10.45%)</td><td>0.21 (+6.05%)</td><td>0.17 (+4.40%)</td><td>0.03 <b>(-69.61%)</b></td><td>191.20 (-4.21%)</td><td>157.26 (+3.05%)</td><td>153.40 (-5.72%)</td><td>138.20 <b>(+62.97%)</b></td><td>21.94 <b>(-52.50%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.39 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>199.60 (n/a)</td><td>152.60 (n/a)</td><td>162.70 (n/a)</td><td>84.80 (n/a)</td><td>46.20 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.21 (-19.78%)</td><td>0.17 (-19.52%)</td><td>0.17 (-15.79%)</td><td>0.13 <b>(-26.67%)</b></td><td>0.03 (-8.02%)</td><td>259.80 <b>(+36.38%)</b></td><td>194.30 <b>(+25.55%)</b></td><td>190.00 (+18.75%)</td><td>154.20 <b>(+24.66%)</b></td><td>41.76 <b>(+58.21%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>190.50 (n/a)</td><td>154.76 (n/a)</td><td>160.00 (n/a)</td><td>123.70 (n/a)</td><td>26.40 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.20 <b>(+30.13%)</b></td><td>0.17 (+15.72%)</td><td>0.15 (-3.25%)</td><td>0.15 <b>(+41.86%)</b></td><td>0.03 (+16.19%)</td><td>220.90 <b>(-29.51%)</b></td><td>200.72 (-14.13%)</td><td>220.10 (+3.33%)</td><td>160.00 <b>(-23.15%)</b></td><td>28.29 <b>(-36.82%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>313.40 (n/a)</td><td>233.76 (n/a)</td><td>213.00 (n/a)</td><td>208.20 (n/a)</td><td>44.78 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.19 (+2.72%)</td><td>0.17 (+6.62%)</td><td>0.17 (+9.92%)</td><td>0.15 (+4.99%)</td><td>0.02 (-1.61%)</td><td>221.50 (-4.77%)</td><td>197.62 (-6.28%)</td><td>196.10 (-9.00%)</td><td>173.30 (-2.64%)</td><td>19.07 (-7.10%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>232.60 (n/a)</td><td>210.86 (n/a)</td><td>215.50 (n/a)</td><td>178.00 (n/a)</td><td>20.52 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.26 (+16.85%)</td><td>0.19 (-1.78%)</td><td>0.18 (-11.88%)</td><td>0.17 (+4.18%)</td><td>0.04 <b>(+38.98%)</b></td><td>198.30 (-4.02%)</td><td>173.82 (+2.66%)</td><td>182.10 (+13.53%)</td><td>127.70 (-14.41%)</td><td>26.97 (+10.80%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>206.60 (n/a)</td><td>169.32 (n/a)</td><td>160.40 (n/a)</td><td>149.20 (n/a)</td><td>24.34 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.24 <b>(-27.74%)</b></td><td>0.22 (-5.67%)</td><td>0.23 (+11.70%)</td><td>0.16 (-12.61%)</td><td>0.03 <b>(-47.12%)</b></td><td>201.50 (+14.42%)</td><td>155.04 (+3.68%)</td><td>142.80 (-10.47%)</td><td>138.90 <b>(+38.35%)</b></td><td>26.39 (-13.62%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.33 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.06 (n/a)</td><td>176.10 (n/a)</td><td>149.54 (n/a)</td><td>159.50 (n/a)</td><td>100.40 (n/a)</td><td>30.55 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.22 (-17.71%)</td><td>0.18 (-15.06%)</td><td>0.18 (-13.98%)</td><td>0.15 (-12.35%)</td><td>0.03 <b>(-33.71%)</b></td><td>213.50 (+14.05%)</td><td>181.24 (+16.36%)</td><td>183.40 (+16.30%)</td><td>149.70 <b>(+21.51%)</b></td><td>27.09 (-8.50%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>187.20 (n/a)</td><td>155.76 (n/a)</td><td>157.70 (n/a)</td><td>123.20 (n/a)</td><td>29.60 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.19 <b>(-30.28%)</b></td><td>0.17 (-15.89%)</td><td>0.18 (-12.29%)</td><td>0.14 (+1.08%)</td><td>0.02 <b>(-66.11%)</b></td><td>234.30 (-1.10%)</td><td>193.78 (+13.32%)</td><td>184.70 (+14.01%)</td><td>176.10 <b>(+43.40%)</b></td><td>23.18 <b>(-50.54%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>236.90 (n/a)</td><td>171.00 (n/a)</td><td>162.00 (n/a)</td><td>122.80 (n/a)</td><td>46.87 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.25 (+2.21%)</td><td>0.21 (+16.98%)</td><td>0.22 <b>(+25.99%)</b></td><td>0.14 <b>(+47.27%)</b></td><td>0.04 <b>(-26.03%)</b></td><td>232.50 <b>(-32.10%)</b></td><td>166.54 <b>(-20.19%)</b></td><td>149.60 <b>(-20.64%)</b></td><td>129.80 (-2.19%)</td><td>41.62 <b>(-50.41%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>342.40 (n/a)</td><td>208.66 (n/a)</td><td>188.50 (n/a)</td><td>132.70 (n/a)</td><td>83.92 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.20 <b>(-22.64%)</b></td><td>0.18 (-13.89%)</td><td>0.18 (-10.33%)</td><td>0.15 (-7.74%)</td><td>0.02 <b>(-50.06%)</b></td><td>211.50 (+8.35%)</td><td>184.84 (+14.30%)</td><td>183.20 (+11.50%)</td><td>163.80 <b>(+29.28%)</b></td><td>19.39 <b>(-30.15%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>195.20 (n/a)</td><td>161.72 (n/a)</td><td>164.30 (n/a)</td><td>126.70 (n/a)</td><td>27.77 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.30 (+2.46%)</td><td>0.22 (-9.59%)</td><td>0.20 <b>(-23.12%)</b></td><td>0.16 (-10.14%)</td><td>0.06 <b>(+22.47%)</b></td><td>202.30 (+11.28%)</td><td>160.08 (+12.81%)</td><td>163.90 <b>(+30.08%)</b></td><td>109.60 (-2.40%)</td><td>39.19 <b>(+32.54%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>181.80 (n/a)</td><td>141.90 (n/a)</td><td>126.00 (n/a)</td><td>112.30 (n/a)</td><td>29.57 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.30 (+13.98%)</td><td>0.20 (-9.20%)</td><td>0.18 (-13.38%)</td><td>0.14 <b>(-21.33%)</b></td><td>0.06 <b>(+91.23%)</b></td><td>232.00 <b>(+27.12%)</b></td><td>177.58 (+14.98%)</td><td>184.80 (+15.43%)</td><td>111.00 (-12.25%)</td><td>43.55 <b>(+103.54%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>182.50 (n/a)</td><td>154.44 (n/a)</td><td>160.10 (n/a)</td><td>126.50 (n/a)</td><td>21.40 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.21 (-7.71%)</td><td>0.17 (-6.01%)</td><td>0.17 (-6.37%)</td><td>0.14 (+11.51%)</td><td>0.03 <b>(-25.96%)</b></td><td>240.10 (-10.31%)</td><td>198.30 (+4.30%)</td><td>191.80 (+6.79%)</td><td>155.10 (+8.31%)</td><td>31.86 <b>(-31.22%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>267.70 (n/a)</td><td>190.12 (n/a)</td><td>179.60 (n/a)</td><td>143.20 (n/a)</td><td>46.32 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.22 (-10.56%)</td><td>0.17 (-9.31%)</td><td>0.16 (-17.46%)</td><td>0.14 (+14.48%)</td><td>0.03 <b>(-31.59%)</b></td><td>237.40 (-12.62%)</td><td>199.78 (+6.96%)</td><td>205.80 <b>(+21.13%)</b></td><td>152.20 (+11.83%)</td><td>34.56 <b>(-34.72%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>271.70 (n/a)</td><td>186.78 (n/a)</td><td>169.90 (n/a)</td><td>136.10 (n/a)</td><td>52.94 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.23 (-4.75%)</td><td>0.19 (-1.04%)</td><td>0.21 (+8.52%)</td><td>0.15 (+2.02%)</td><td>0.04 (+0.78%)</td><td>219.00 (-1.97%)</td><td>178.16 (+1.30%)</td><td>158.80 (-7.89%)</td><td>143.60 (+4.97%)</td><td>35.62 (+6.78%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>223.40 (n/a)</td><td>175.88 (n/a)</td><td>172.40 (n/a)</td><td>136.80 (n/a)</td><td>33.36 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.21 (-19.24%)</td><td>0.18 (-3.78%)</td><td>0.17 (+1.02%)</td><td>0.14 (-9.49%)</td><td>0.03 <b>(-27.74%)</b></td><td>229.30 (+10.45%)</td><td>187.82 (+2.87%)</td><td>193.00 (-1.03%)</td><td>153.60 <b>(+23.77%)</b></td><td>33.17 (-1.10%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>207.60 (n/a)</td><td>182.58 (n/a)</td><td>195.00 (n/a)</td><td>124.10 (n/a)</td><td>33.54 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.18 (+0.64%)</td><td>0.18 (+0.06%)</td><td>0.18 (-0.01%)</td><td>0.18 (-0.21%)</td><td>0.00 <b>(+251.00%)</b></td><td>47594.30 (+0.21%)</td><td>47369.96 (-0.06%)</td><td>47396.80 (+0.01%)</td><td>47037.90 (-0.64%)</td><td>205.90 <b>(+249.05%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47492.80 (n/a)</td><td>47397.46 (n/a)</td><td>47392.00 (n/a)</td><td>47341.00 (n/a)</td><td>58.99 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.18 (+0.48%)</td><td>0.18 (+0.11%)</td><td>0.18 (+0.09%)</td><td>0.18 (-0.16%)</td><td>0.00 <b>(+114.71%)</b></td><td>47596.10 (+0.16%)</td><td>47388.28 (-0.11%)</td><td>47410.00 (-0.08%)</td><td>47112.70 (-0.48%)</td><td>174.64 <b>(+113.78%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47518.00 (n/a)</td><td>47439.04 (n/a)</td><td>47450.30 (n/a)</td><td>47340.20 (n/a)</td><td>81.69 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.11 (+0.06%)</td><td>0.11 (-0.01%)</td><td>0.11 (-0.04%)</td><td>0.11 (-0.03%)</td><td>0.00 <b>(+70.58%)</b></td><td>374519.40 (+0.03%)</td><td>374279.60 (+0.01%)</td><td>374423.10 (+0.04%)</td><td>373679.70 (-0.06%)</td><td>344.57 <b>(+70.47%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.00 (n/a)</td><td>374411.40 (n/a)</td><td>374254.40 (n/a)</td><td>374284.60 (n/a)</td><td>373916.80 (n/a)</td><td>202.13 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.17 (-3.66%)</td><td>0.14 (-5.60%)</td><td>0.14 (-12.93%)</td><td>0.13 (-0.54%)</td><td>0.02 (-7.62%)</td><td>189.10 (+0.53%)</td><td>171.72 (+5.79%)</td><td>181.80 (+14.85%)</td><td>145.60 (+3.78%)</td><td>19.89 (-3.14%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>188.10 (n/a)</td><td>162.32 (n/a)</td><td>158.30 (n/a)</td><td>140.30 (n/a)</td><td>20.54 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.30 (-16.56%)</td><td>0.27 (-2.17%)</td><td>0.28 (-0.28%)</td><td>0.24 (+7.71%)</td><td>0.02 <b>(-57.18%)</b></td><td>205.30 (-7.15%)</td><td>180.60 (+0.10%)</td><td>177.80 (+0.28%)</td><td>164.70 (+19.87%)</td><td>15.46 <b>(-51.78%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.36 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.05 (n/a)</td><td>221.10 (n/a)</td><td>180.42 (n/a)</td><td>177.30 (n/a)</td><td>137.40 (n/a)</td><td>32.06 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>12.85 (-4.19%)</td><td>12.59 (-0.50%)</td><td>12.73 (+2.01%)</td><td>12.07 (-1.70%)</td><td>0.32 <b>(-33.03%)</b></td><td>868.70 (+1.73%)</td><td>833.04 (+0.44%)</td><td>823.50 (-1.98%)</td><td>815.90 (+4.38%)</td><td>21.41 <b>(-28.76%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>13.41 (n/a)</td><td>12.66 (n/a)</td><td>12.48 (n/a)</td><td>12.28 (n/a)</td><td>0.47 (n/a)</td><td>853.90 (n/a)</td><td>829.38 (n/a)</td><td>840.10 (n/a)</td><td>781.70 (n/a)</td><td>30.05 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.27 (-10.67%)</td><td>0.22 (-11.74%)</td><td>0.22 (-7.67%)</td><td>0.19 (-17.20%)</td><td>0.03 (-1.37%)</td><td>214.80 <b>(+20.74%)</b></td><td>186.90 (+13.59%)</td><td>187.70 (+8.31%)</td><td>153.90 (+11.93%)</td><td>21.68 <b>(+31.63%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.03 (n/a)</td><td>177.90 (n/a)</td><td>164.54 (n/a)</td><td>173.30 (n/a)</td><td>137.50 (n/a)</td><td>16.47 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.04 (-10.49%)</td><td>0.03 (-9.32%)</td><td>0.03 (-10.49%)</td><td>0.02 (-18.95%)</td><td>0.01 <b>(+26.15%)</b></td><td>224.50 <b>(+23.42%)</b></td><td>171.66 (+11.92%)</td><td>168.60 (+11.73%)</td><td>143.00 (+11.72%)</td><td>33.41 <b>(+71.09%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>181.90 (n/a)</td><td>153.38 (n/a)</td><td>150.90 (n/a)</td><td>128.00 (n/a)</td><td>19.53 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (-6.18%)</td><td>0.02 (-8.46%)</td><td>0.02 (-7.30%)</td><td>0.02 (-19.30%)</td><td>0.01 <b>(+31.59%)</b></td><td>240.80 <b>(+23.87%)</b></td><td>182.40 (+13.72%)</td><td>178.70 (+7.85%)</td><td>124.80 (+6.58%)</td><td>53.26 <b>(+78.36%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>194.40 (n/a)</td><td>160.40 (n/a)</td><td>165.70 (n/a)</td><td>117.10 (n/a)</td><td>29.86 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.04 <b>(-22.64%)</b></td><td>0.04 (+7.20%)</td><td>0.04 (-1.14%)</td><td>0.04 <b>(+96.45%)</b></td><td>0.00 <b>(-89.11%)</b></td><td>172.10 <b>(-49.10%)</b></td><td>165.12 <b>(-21.79%)</b></td><td>169.10 (+1.14%)</td><td>155.70 <b>(+29.32%)</b></td><td>7.13 <b>(-92.94%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>338.10 (n/a)</td><td>211.12 (n/a)</td><td>167.20 (n/a)</td><td>120.40 (n/a)</td><td>101.10 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (+9.59%)</td><td>0.03 (+1.75%)</td><td>0.02 (-9.36%)</td><td>0.02 (-2.57%)</td><td>0.00 <b>(+51.81%)</b></td><td>185.90 (+2.65%)</td><td>160.92 (-0.76%)</td><td>165.80 (+10.31%)</td><td>136.00 (-8.72%)</td><td>23.92 <b>(+39.04%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>181.10 (n/a)</td><td>162.16 (n/a)</td><td>150.30 (n/a)</td><td>149.00 (n/a)</td><td>17.20 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 <b>(-25.04%)</b></td><td>0.03 (-15.41%)</td><td>0.03 <b>(-26.27%)</b></td><td>0.03 <b>(+27.26%)</b></td><td>0.00 <b>(-74.01%)</b></td><td>200.40 <b>(-21.44%)</b></td><td>176.22 (+9.41%)</td><td>173.70 <b>(+35.60%)</b></td><td>156.50 <b>(+33.42%)</b></td><td>15.78 <b>(-72.62%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>255.10 (n/a)</td><td>161.06 (n/a)</td><td>128.10 (n/a)</td><td>117.30 (n/a)</td><td>57.63 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (-2.87%)</td><td>0.02 (+7.69%)</td><td>0.02 (+14.58%)</td><td>0.02 (+10.40%)</td><td>0.00 <b>(-23.66%)</b></td><td>212.40 (-9.42%)</td><td>169.72 (-9.13%)</td><td>164.90 (-12.71%)</td><td>128.80 (+2.96%)</td><td>30.69 <b>(-28.62%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>234.50 (n/a)</td><td>186.78 (n/a)</td><td>188.90 (n/a)</td><td>125.10 (n/a)</td><td>43.00 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.04 (-9.85%)</td><td>0.03 (-6.85%)</td><td>0.03 (-14.25%)</td><td>0.02 (-2.97%)</td><td>0.01 <b>(-29.57%)</b></td><td>252.80 (+3.06%)</td><td>174.38 (+4.44%)</td><td>158.00 (+16.61%)</td><td>139.40 (+10.90%)</td><td>45.24 (-14.16%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>245.30 (n/a)</td><td>166.96 (n/a)</td><td>135.50 (n/a)</td><td>125.70 (n/a)</td><td>52.70 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (+5.55%)</td><td>0.02 (+7.00%)</td><td>0.02 (+4.37%)</td><td>0.02 (+8.39%)</td><td>0.00 (-9.65%)</td><td>214.90 (-7.73%)</td><td>188.86 (-6.79%)</td><td>187.10 (-4.20%)</td><td>167.10 (-5.27%)</td><td>17.15 <b>(-20.95%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.90 (n/a)</td><td>202.62 (n/a)</td><td>195.30 (n/a)</td><td>176.40 (n/a)</td><td>21.69 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.04 (+18.73%)</td><td>0.03 (+10.09%)</td><td>0.03 (+11.33%)</td><td>0.02 (-3.79%)</td><td>0.01 <b>(+67.93%)</b></td><td>245.60 (+3.94%)</td><td>172.58 (-6.64%)</td><td>160.80 (-10.17%)</td><td>131.30 (-15.78%)</td><td>44.95 <b>(+45.89%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>236.30 (n/a)</td><td>184.86 (n/a)</td><td>179.00 (n/a)</td><td>155.90 (n/a)</td><td>30.81 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (-10.03%)</td><td>0.02 (+1.90%)</td><td>0.02 (+7.09%)</td><td>0.02 (+10.74%)</td><td>0.00 <b>(-39.26%)</b></td><td>229.90 (-9.70%)</td><td>198.44 (-3.10%)</td><td>190.00 (-6.59%)</td><td>181.10 (+11.17%)</td><td>20.04 <b>(-39.22%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>254.60 (n/a)</td><td>204.78 (n/a)</td><td>203.40 (n/a)</td><td>162.90 (n/a)</td><td>32.97 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (-9.18%)</td><td>0.03 (+4.21%)</td><td>0.03 <b>(+25.02%)</b></td><td>0.02 <b>(+27.03%)</b></td><td>0.00 <b>(-59.18%)</b></td><td>203.20 <b>(-21.27%)</b></td><td>177.62 (-9.99%)</td><td>172.70 <b>(-20.05%)</b></td><td>148.30 (+10.10%)</td><td>21.15 <b>(-63.20%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>258.10 (n/a)</td><td>197.34 (n/a)</td><td>216.00 (n/a)</td><td>134.70 (n/a)</td><td>57.48 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (+5.27%)</td><td>0.02 (+11.05%)</td><td>0.02 (+6.15%)</td><td>0.02 <b>(+22.56%)</b></td><td>0.00 (-8.88%)</td><td>201.00 (-18.43%)</td><td>179.14 (-10.67%)</td><td>192.30 (-5.78%)</td><td>144.90 (-4.98%)</td><td>24.52 <b>(-27.72%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>246.40 (n/a)</td><td>200.54 (n/a)</td><td>204.10 (n/a)</td><td>152.50 (n/a)</td><td>33.92 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (+10.98%)</td><td>0.02 (+4.22%)</td><td>0.03 (-3.80%)</td><td>0.01 (+6.67%)</td><td>0.01 (-5.91%)</td><td>319.10 (-6.26%)</td><td>199.94 (-5.55%)</td><td>173.90 (+3.95%)</td><td>142.50 (-9.87%)</td><td>68.84 (-12.47%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>340.40 (n/a)</td><td>211.68 (n/a)</td><td>167.30 (n/a)</td><td>158.10 (n/a)</td><td>78.64 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (-3.58%)</td><td>0.02 (-11.19%)</td><td>0.02 (-13.82%)</td><td>0.02 <b>(-25.00%)</b></td><td>0.00 <b>(+60.50%)</b></td><td>269.60 <b>(+33.33%)</b></td><td>206.62 (+16.30%)</td><td>211.40 (+16.03%)</td><td>150.40 (+3.72%)</td><td>48.48 <b>(+121.37%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>202.20 (n/a)</td><td>177.66 (n/a)</td><td>182.20 (n/a)</td><td>145.00 (n/a)</td><td>21.90 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (-16.02%)</td><td>0.02 (+2.06%)</td><td>0.02 (+11.65%)</td><td>0.02 (+2.83%)</td><td>0.00 <b>(-51.55%)</b></td><td>217.20 (-2.78%)</td><td>188.42 (-4.14%)</td><td>185.60 (-10.42%)</td><td>163.40 (+19.10%)</td><td>19.85 <b>(-41.47%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>223.40 (n/a)</td><td>196.56 (n/a)</td><td>207.20 (n/a)</td><td>137.20 (n/a)</td><td>33.92 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.02 (+0.65%)</td><td>0.02 (-6.78%)</td><td>0.02 (-1.17%)</td><td>0.01 <b>(-22.30%)</b></td><td>0.00 <b>(+63.30%)</b></td><td>328.80 <b>(+28.69%)</b></td><td>241.72 (+10.64%)</td><td>223.70 (+1.18%)</td><td>179.10 (-0.67%)</td><td>58.34 <b>(+113.53%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>255.50 (n/a)</td><td>218.48 (n/a)</td><td>221.10 (n/a)</td><td>180.30 (n/a)</td><td>27.32 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.07 (+1.62%)</td><td>0.05 (-9.27%)</td><td>0.04 (-15.86%)</td><td>0.04 (-13.91%)</td><td>0.01 <b>(+37.65%)</b></td><td>212.20 (+16.15%)</td><td>182.30 (+12.42%)</td><td>195.30 (+18.87%)</td><td>122.60 (-1.61%)</td><td>34.69 <b>(+54.29%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.70 (n/a)</td><td>162.16 (n/a)</td><td>164.30 (n/a)</td><td>124.60 (n/a)</td><td>22.49 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.10 (+14.64%)</td><td>0.08 (+1.64%)</td><td>0.08 (-5.97%)</td><td>0.07 (+4.61%)</td><td>0.01 <b>(+45.00%)</b></td><td>183.10 (-4.39%)</td><td>159.66 (-0.68%)</td><td>162.90 (+6.33%)</td><td>118.10 (-12.71%)</td><td>24.76 (+15.64%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>191.50 (n/a)</td><td>160.76 (n/a)</td><td>153.20 (n/a)</td><td>135.30 (n/a)</td><td>21.41 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (-17.47%)</td><td>0.04 (-11.95%)</td><td>0.05 (-16.57%)</td><td>0.04 (+15.92%)</td><td>0.00 <b>(-61.04%)</b></td><td>207.50 (-13.72%)</td><td>183.86 (+8.47%)</td><td>177.70 (+19.91%)</td><td>158.00 <b>(+21.17%)</b></td><td>19.57 <b>(-58.44%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.50 (n/a)</td><td>169.50 (n/a)</td><td>148.20 (n/a)</td><td>130.40 (n/a)</td><td>47.08 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.07 (-15.27%)</td><td>0.06 (-15.81%)</td><td>0.06 (-13.86%)</td><td>0.05 (-18.26%)</td><td>0.01 (-13.15%)</td><td>197.00 <b>(+22.28%)</b></td><td>169.86 (+18.87%)</td><td>166.60 (+16.10%)</td><td>146.00 (+18.03%)</td><td>18.36 <b>(+25.79%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>161.10 (n/a)</td><td>142.90 (n/a)</td><td>143.50 (n/a)</td><td>123.70 (n/a)</td><td>14.59 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.07 (-1.26%)</td><td>0.05 (-5.05%)</td><td>0.04 (-16.28%)</td><td>0.04 <b>(+49.97%)</b></td><td>0.01 <b>(-34.88%)</b></td><td>195.70 <b>(-33.32%)</b></td><td>175.98 (-1.41%)</td><td>195.30 (+19.45%)</td><td>126.00 (+1.29%)</td><td>30.47 <b>(-55.62%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>293.50 (n/a)</td><td>178.50 (n/a)</td><td>163.50 (n/a)</td><td>124.40 (n/a)</td><td>68.67 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.08 (-16.43%)</td><td>0.07 (-12.11%)</td><td>0.07 (-6.22%)</td><td>0.06 (-14.06%)</td><td>0.01 <b>(-25.69%)</b></td><td>182.30 (+16.41%)</td><td>149.38 (+13.42%)</td><td>143.80 (+6.60%)</td><td>130.40 (+19.74%)</td><td>19.66 (+6.82%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>156.60 (n/a)</td><td>131.70 (n/a)</td><td>134.90 (n/a)</td><td>108.90 (n/a)</td><td>18.40 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 <b>(-24.83%)</b></td><td>0.04 <b>(-27.07%)</b></td><td>0.04 <b>(-33.44%)</b></td><td>0.04 <b>(-29.47%)</b></td><td>0.01 (-11.19%)</td><td>231.60 <b>(+41.82%)</b></td><td>191.80 <b>(+39.55%)</b></td><td>210.50 <b>(+50.25%)</b></td><td>128.90 <b>(+33.02%)</b></td><td>43.84 <b>(+75.48%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>163.30 (n/a)</td><td>137.44 (n/a)</td><td>140.10 (n/a)</td><td>96.90 (n/a)</td><td>24.98 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.07 (-5.01%)</td><td>0.05 (-10.50%)</td><td>0.06 (-8.07%)</td><td>0.04 <b>(-22.51%)</b></td><td>0.01 <b>(+49.43%)</b></td><td>214.30 <b>(+29.02%)</b></td><td>172.98 (+13.76%)</td><td>166.80 (+8.74%)</td><td>133.50 (+5.28%)</td><td>31.49 <b>(+107.49%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>166.10 (n/a)</td><td>152.06 (n/a)</td><td>153.40 (n/a)</td><td>126.80 (n/a)</td><td>15.17 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (-15.76%)</td><td>0.05 (-2.90%)</td><td>0.05 (+10.93%)</td><td>0.04 (+10.93%)</td><td>0.01 <b>(-38.55%)</b></td><td>213.00 (-9.86%)</td><td>167.70 (-1.81%)</td><td>149.40 (-9.84%)</td><td>129.60 (+18.68%)</td><td>35.69 <b>(-33.36%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>236.30 (n/a)</td><td>170.80 (n/a)</td><td>165.70 (n/a)</td><td>109.20 (n/a)</td><td>53.56 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 <b>(-31.66%)</b></td><td>0.05 <b>(-23.44%)</b></td><td>0.05 (-16.95%)</td><td>0.04 (-18.25%)</td><td>0.01 <b>(-61.29%)</b></td><td>225.70 <b>(+22.33%)</b></td><td>190.68 <b>(+27.34%)</b></td><td>186.00 <b>(+20.39%)</b></td><td>171.50 <b>(+46.33%)</b></td><td>21.94 <b>(-28.82%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>184.50 (n/a)</td><td>149.74 (n/a)</td><td>154.50 (n/a)</td><td>117.20 (n/a)</td><td>30.82 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 <b>(-20.50%)</b></td><td>0.04 <b>(-21.11%)</b></td><td>0.05 (-14.23%)</td><td>0.03 <b>(-38.28%)</b></td><td>0.01 <b>(+43.66%)</b></td><td>263.70 <b>(+61.98%)</b></td><td>189.38 <b>(+30.18%)</b></td><td>171.90 (+16.54%)</td><td>157.60 <b>(+25.78%)</b></td><td>43.57 <b>(+198.42%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>162.80 (n/a)</td><td>145.48 (n/a)</td><td>147.50 (n/a)</td><td>125.30 (n/a)</td><td>14.60 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (-12.83%)</td><td>0.04 (-18.89%)</td><td>0.04 (-19.63%)</td><td>0.04 <b>(-20.07%)</b></td><td>0.00 (+19.41%)</td><td>237.30 <b>(+25.09%)</b></td><td>210.06 <b>(+23.87%)</b></td><td>207.50 <b>(+24.40%)</b></td><td>176.80 (+14.73%)</td><td>22.36 <b>(+68.18%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>189.70 (n/a)</td><td>169.58 (n/a)</td><td>166.80 (n/a)</td><td>154.10 (n/a)</td><td>13.29 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (-14.62%)</td><td>0.04 (-10.32%)</td><td>0.04 (-9.02%)</td><td>0.03 (-17.57%)</td><td>0.01 (-3.32%)</td><td>248.60 <b>(+21.33%)</b></td><td>191.36 (+12.56%)</td><td>183.20 (+9.90%)</td><td>146.90 (+17.15%)</td><td>41.96 <b>(+39.47%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.90 (n/a)</td><td>170.00 (n/a)</td><td>166.70 (n/a)</td><td>125.40 (n/a)</td><td>30.08 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.06 (-5.03%)</td><td>0.05 (-1.26%)</td><td>0.05 (-8.17%)</td><td>0.04 <b>(+51.17%)</b></td><td>0.01 <b>(-44.21%)</b></td><td>245.40 <b>(-33.85%)</b></td><td>192.68 (-7.32%)</td><td>189.90 (+8.89%)</td><td>150.10 (+5.33%)</td><td>34.12 <b>(-63.33%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>371.00 (n/a)</td><td>207.90 (n/a)</td><td>174.40 (n/a)</td><td>142.50 (n/a)</td><td>93.03 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.05 (-0.45%)</td><td>0.04 (-4.99%)</td><td>0.04 (-18.31%)</td><td>0.03 (+14.48%)</td><td>0.01 <b>(-26.82%)</b></td><td>259.00 (-12.65%)</td><td>212.96 (+3.03%)</td><td>219.70 <b>(+22.40%)</b></td><td>175.20 (+0.46%)</td><td>32.70 <b>(-36.85%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>296.50 (n/a)</td><td>206.70 (n/a)</td><td>179.50 (n/a)</td><td>174.40 (n/a)</td><td>51.79 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.14 (+14.85%)</td><td>0.10 (-4.66%)</td><td>0.08 (-19.94%)</td><td>0.08 <b>(-20.30%)</b></td><td>0.03 <b>(+169.10%)</b></td><td>212.90 <b>(+25.46%)</b></td><td>167.76 (+11.26%)</td><td>193.40 <b>(+24.85%)</b></td><td>114.90 (-12.89%)</td><td>45.91 <b>(+189.73%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>169.70 (n/a)</td><td>150.78 (n/a)</td><td>154.90 (n/a)</td><td>131.90 (n/a)</td><td>15.85 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.16 (-14.86%)</td><td>0.14 (-14.30%)</td><td>0.14 (-10.76%)</td><td>0.12 (-6.39%)</td><td>0.02 <b>(-36.59%)</b></td><td>209.20 (+6.84%)</td><td>176.34 (+15.45%)</td><td>170.80 (+12.07%)</td><td>152.40 (+17.41%)</td><td>21.34 (-19.37%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>195.80 (n/a)</td><td>152.74 (n/a)</td><td>152.40 (n/a)</td><td>129.80 (n/a)</td><td>26.47 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.14 (+3.91%)</td><td>0.10 (-19.65%)</td><td>0.09 <b>(-29.44%)</b></td><td>0.07 <b>(-25.56%)</b></td><td>0.03 <b>(+58.99%)</b></td><td>220.20 <b>(+34.35%)</b></td><td>178.66 <b>(+28.31%)</b></td><td>184.30 <b>(+41.77%)</b></td><td>118.20 (-3.75%)</td><td>38.31 <b>(+98.77%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>163.90 (n/a)</td><td>139.24 (n/a)</td><td>130.00 (n/a)</td><td>122.80 (n/a)</td><td>19.27 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.13 (-18.56%)</td><td>0.11 (-17.47%)</td><td>0.10 <b>(-20.73%)</b></td><td>0.09 (-6.38%)</td><td>0.01 <b>(-45.37%)</b></td><td>219.00 (+6.78%)</td><td>191.28 (+18.87%)</td><td>197.40 <b>(+26.13%)</b></td><td>157.20 <b>(+22.81%)</b></td><td>23.15 <b>(-28.49%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>205.10 (n/a)</td><td>160.92 (n/a)</td><td>156.50 (n/a)</td><td>128.00 (n/a)</td><td>32.37 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.15 <b>(+42.99%)</b></td><td>0.11 <b>(+21.73%)</b></td><td>0.11 (+10.65%)</td><td>0.09 (+16.16%)</td><td>0.03 <b>(+96.50%)</b></td><td>187.80 (-13.93%)</td><td>150.34 (-15.59%)</td><td>151.90 (-9.64%)</td><td>106.00 <b>(-30.08%)</b></td><td>35.39 <b>(+21.51%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>218.20 (n/a)</td><td>178.10 (n/a)</td><td>168.10 (n/a)</td><td>151.60 (n/a)</td><td>29.13 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.12 <b>(-28.02%)</b></td><td>0.12 (-10.79%)</td><td>0.12 (-8.19%)</td><td>0.11 (+1.06%)</td><td>0.00 <b>(-84.21%)</b></td><td>184.50 (-1.02%)</td><td>176.44 (+10.11%)</td><td>174.70 (+8.92%)</td><td>172.30 <b>(+38.95%)</b></td><td>5.15 <b>(-77.72%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>186.40 (n/a)</td><td>160.24 (n/a)</td><td>160.40 (n/a)</td><td>124.00 (n/a)</td><td>23.11 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.15 <b>(+41.70%)</b></td><td>0.11 <b>(+32.79%)</b></td><td>0.09 (+10.66%)</td><td>0.09 <b>(+44.24%)</b></td><td>0.03 <b>(+65.45%)</b></td><td>190.30 <b>(-30.67%)</b></td><td>157.12 <b>(-23.43%)</b></td><td>184.50 (-9.60%)</td><td>109.80 <b>(-29.39%)</b></td><td>40.28 (-16.96%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>274.50 (n/a)</td><td>205.20 (n/a)</td><td>204.10 (n/a)</td><td>155.50 (n/a)</td><td>48.50 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.14 (-8.63%)</td><td>0.12 (+6.66%)</td><td>0.13 <b>(+26.01%)</b></td><td>0.09 (-2.27%)</td><td>0.02 <b>(-22.25%)</b></td><td>206.80 (+2.33%)</td><td>161.06 (-7.23%)</td><td>146.90 <b>(-20.64%)</b></td><td>131.20 (+9.52%)</td><td>29.81 (-10.30%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>202.10 (n/a)</td><td>173.62 (n/a)</td><td>185.10 (n/a)</td><td>119.80 (n/a)</td><td>33.24 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.14 (+7.65%)</td><td>0.12 (+15.78%)</td><td>0.13 <b>(+32.89%)</b></td><td>0.10 (+1.99%)</td><td>0.02 <b>(+48.83%)</b></td><td>171.50 (-1.94%)</td><td>142.72 (-12.45%)</td><td>129.80 <b>(-24.75%)</b></td><td>120.30 (-7.10%)</td><td>26.50 <b>(+38.85%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>174.90 (n/a)</td><td>163.02 (n/a)</td><td>172.50 (n/a)</td><td>129.50 (n/a)</td><td>19.09 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.12 (-10.88%)</td><td>0.09 <b>(-21.76%)</b></td><td>0.09 <b>(-23.04%)</b></td><td>0.05 <b>(-47.63%)</b></td><td>0.03 <b>(+80.52%)</b></td><td>378.10 <b>(+90.96%)</b></td><td>229.74 <b>(+38.80%)</b></td><td>216.10 <b>(+29.95%)</b></td><td>152.80 (+12.19%)</td><td>88.64 <b>(+297.94%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>198.00 (n/a)</td><td>165.52 (n/a)</td><td>166.30 (n/a)</td><td>136.20 (n/a)</td><td>22.27 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.14 <b>(+24.84%)</b></td><td>0.09 (-2.31%)</td><td>0.08 (-13.54%)</td><td>0.06 (+5.99%)</td><td>0.03 <b>(+29.74%)</b></td><td>286.60 (-5.66%)</td><td>206.68 (+3.74%)</td><td>213.80 (+15.69%)</td><td>115.20 (-19.94%)</td><td>61.05 (-6.66%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>303.80 (n/a)</td><td>199.22 (n/a)</td><td>184.80 (n/a)</td><td>143.90 (n/a)</td><td>65.40 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.10 (-4.55%)</td><td>0.08 (-11.45%)</td><td>0.09 (-15.35%)</td><td>0.05 <b>(-28.75%)</b></td><td>0.02 <b>(+27.89%)</b></td><td>320.20 <b>(+40.32%)</b></td><td>216.34 (+16.51%)</td><td>199.00 (+18.17%)</td><td>167.70 (+4.75%)</td><td>61.74 <b>(+93.39%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>228.20 (n/a)</td><td>185.68 (n/a)</td><td>168.40 (n/a)</td><td>160.10 (n/a)</td><td>31.92 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.10 (+5.39%)</td><td>0.09 (+4.28%)</td><td>0.08 (-0.82%)</td><td>0.07 (+15.69%)</td><td>0.01 (-15.82%)</td><td>224.50 (-13.59%)</td><td>194.26 (-5.03%)</td><td>200.70 (+0.80%)</td><td>161.60 (-5.11%)</td><td>24.68 <b>(-31.31%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>259.80 (n/a)</td><td>204.54 (n/a)</td><td>199.10 (n/a)</td><td>170.30 (n/a)</td><td>35.93 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.10 (-14.25%)</td><td>0.09 (-4.19%)</td><td>0.09 (+4.33%)</td><td>0.08 (+4.63%)</td><td>0.01 <b>(-52.71%)</b></td><td>228.70 (-4.43%)</td><td>198.94 (+1.50%)</td><td>202.80 (-4.16%)</td><td>172.80 (+16.60%)</td><td>21.79 <b>(-46.60%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>239.30 (n/a)</td><td>196.00 (n/a)</td><td>211.60 (n/a)</td><td>148.20 (n/a)</td><td>40.81 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.08 <b>(-20.21%)</b></td><td>0.08 (-1.87%)</td><td>0.08 (-5.81%)</td><td>0.07 <b>(+57.75%)</b></td><td>0.00 <b>(-80.52%)</b></td><td>220.40 <b>(-36.61%)</b></td><td>212.82 (-4.80%)</td><td>216.20 (+6.19%)</td><td>194.10 <b>(+25.31%)</b></td><td>10.61 <b>(-85.51%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>347.70 (n/a)</td><td>223.56 (n/a)</td><td>203.60 (n/a)</td><td>154.90 (n/a)</td><td>73.20 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.20 (-19.51%)</td><td>0.18 (-5.95%)</td><td>0.17 (-0.89%)</td><td>0.15 (-9.76%)</td><td>0.02 <b>(-39.72%)</b></td><td>218.90 (+10.78%)</td><td>187.16 (+5.02%)</td><td>188.00 (+0.91%)</td><td>160.30 <b>(+24.26%)</b></td><td>23.76 (-16.25%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>197.60 (n/a)</td><td>178.22 (n/a)</td><td>186.30 (n/a)</td><td>129.00 (n/a)</td><td>28.37 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.20 <b>(-24.11%)</b></td><td>0.18 <b>(-23.71%)</b></td><td>0.18 (-19.33%)</td><td>0.15 <b>(-21.69%)</b></td><td>0.02 <b>(-36.74%)</b></td><td>216.40 <b>(+27.67%)</b></td><td>187.40 <b>(+30.45%)</b></td><td>182.20 <b>(+23.95%)</b></td><td>160.50 <b>(+31.77%)</b></td><td>21.16 (+8.29%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>169.50 (n/a)</td><td>143.66 (n/a)</td><td>147.00 (n/a)</td><td>121.80 (n/a)</td><td>19.54 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.25 (-19.70%)</td><td>0.22 <b>(-25.38%)</b></td><td>0.22 <b>(-26.89%)</b></td><td>0.19 <b>(-22.31%)</b></td><td>0.02 (-15.93%)</td><td>210.70 <b>(+28.71%)</b></td><td>189.54 <b>(+34.14%)</b></td><td>187.70 <b>(+36.81%)</b></td><td>161.30 <b>(+24.56%)</b></td><td>18.60 <b>(+33.33%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.03 (n/a)</td><td>163.70 (n/a)</td><td>141.30 (n/a)</td><td>137.20 (n/a)</td><td>129.50 (n/a)</td><td>13.95 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.21 <b>(-20.36%)</b></td><td>0.17 <b>(-24.75%)</b></td><td>0.15 <b>(-32.84%)</b></td><td>0.13 (-17.28%)</td><td>0.03 (-18.93%)</td><td>251.00 <b>(+20.91%)</b></td><td>203.64 <b>(+32.72%)</b></td><td>212.50 <b>(+48.91%)</b></td><td>158.20 <b>(+25.56%)</b></td><td>37.62 (+17.59%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>207.60 (n/a)</td><td>153.44 (n/a)</td><td>142.70 (n/a)</td><td>126.00 (n/a)</td><td>31.99 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.32 (+3.83%)</td><td>0.24 (+5.20%)</td><td>0.22 (+4.06%)</td><td>0.15 (-4.20%)</td><td>0.07 <b>(+28.33%)</b></td><td>270.60 (+4.40%)</td><td>187.42 (-2.13%)</td><td>182.80 (-3.89%)</td><td>129.30 (-3.72%)</td><td>59.67 <b>(+24.49%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>259.20 (n/a)</td><td>191.50 (n/a)</td><td>190.20 (n/a)</td><td>134.30 (n/a)</td><td>47.93 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.21 (+0.48%)</td><td>0.18 (-2.98%)</td><td>0.17 (-2.33%)</td><td>0.15 (-4.06%)</td><td>0.02 (-4.45%)</td><td>214.40 (+4.23%)</td><td>187.66 (+3.01%)</td><td>189.50 (+2.38%)</td><td>158.30 (-0.50%)</td><td>22.42 (+0.28%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>205.70 (n/a)</td><td>182.18 (n/a)</td><td>185.10 (n/a)</td><td>159.10 (n/a)</td><td>22.35 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.30 (-0.09%)</td><td>0.22 (+0.90%)</td><td>0.19 (-12.07%)</td><td>0.17 (+8.70%)</td><td>0.06 (-6.55%)</td><td>219.00 (-8.02%)</td><td>177.16 (-2.12%)</td><td>190.20 (+13.69%)</td><td>123.40 (+0.08%)</td><td>40.44 (-16.56%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>238.10 (n/a)</td><td>181.00 (n/a)</td><td>167.30 (n/a)</td><td>123.30 (n/a)</td><td>48.46 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.25 (-2.04%)</td><td>0.16 (-16.91%)</td><td>0.15 <b>(-25.20%)</b></td><td>0.11 (-9.37%)</td><td>0.05 (+8.57%)</td><td>289.10 (+10.34%)</td><td>215.76 <b>(+22.23%)</b></td><td>224.60 <b>(+33.69%)</b></td><td>132.10 (+2.09%)</td><td>60.99 (+17.64%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>262.00 (n/a)</td><td>176.52 (n/a)</td><td>168.00 (n/a)</td><td>129.40 (n/a)</td><td>51.85 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.27 (+12.99%)</td><td>0.23 (+15.22%)</td><td>0.22 <b>(+24.19%)</b></td><td>0.18 (+5.92%)</td><td>0.04 <b>(+27.66%)</b></td><td>199.90 (-5.57%)</td><td>165.98 (-12.76%)</td><td>165.00 (-19.51%)</td><td>135.90 (-11.52%)</td><td>26.46 (+5.70%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>211.70 (n/a)</td><td>190.26 (n/a)</td><td>205.00 (n/a)</td><td>153.60 (n/a)</td><td>25.04 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.19 <b>(-26.02%)</b></td><td>0.17 (-10.01%)</td><td>0.17 (-5.65%)</td><td>0.16 (-5.79%)</td><td>0.01 <b>(-65.95%)</b></td><td>209.60 (+6.13%)</td><td>189.94 (+9.04%)</td><td>187.90 (+5.98%)</td><td>175.00 <b>(+35.14%)</b></td><td>13.45 <b>(-50.07%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>197.50 (n/a)</td><td>174.20 (n/a)</td><td>177.30 (n/a)</td><td>129.50 (n/a)</td><td>26.95 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.20 <b>(-27.51%)</b></td><td>0.17 (-7.33%)</td><td>0.17 (+5.55%)</td><td>0.15 <b>(+40.00%)</b></td><td>0.02 <b>(-65.34%)</b></td><td>238.60 <b>(-28.58%)</b></td><td>207.98 (-1.72%)</td><td>205.10 (-5.27%)</td><td>171.70 <b>(+37.91%)</b></td><td>27.22 <b>(-65.52%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>334.10 (n/a)</td><td>211.62 (n/a)</td><td>216.50 (n/a)</td><td>124.50 (n/a)</td><td>78.96 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.19 (-10.70%)</td><td>0.17 (-1.37%)</td><td>0.16 (+7.85%)</td><td>0.15 (+8.65%)</td><td>0.02 <b>(-51.85%)</b></td><td>220.90 (-7.96%)</td><td>198.76 (-1.13%)</td><td>203.90 (-7.28%)</td><td>175.20 (+12.02%)</td><td>19.94 <b>(-49.70%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>240.00 (n/a)</td><td>201.04 (n/a)</td><td>219.90 (n/a)</td><td>156.40 (n/a)</td><td>39.64 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.21 (-1.19%)</td><td>0.18 (+0.85%)</td><td>0.17 (-8.85%)</td><td>0.14 <b>(+24.19%)</b></td><td>0.03 <b>(-22.22%)</b></td><td>245.00 (-19.46%)</td><td>201.36 (-3.35%)</td><td>206.40 (+9.73%)</td><td>164.80 (+1.23%)</td><td>34.59 <b>(-39.43%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>304.20 (n/a)</td><td>208.34 (n/a)</td><td>188.10 (n/a)</td><td>162.80 (n/a)</td><td>57.12 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.18 (-3.92%)</td><td>0.16 (-10.88%)</td><td>0.16 (-9.02%)</td><td>0.13 (-16.56%)</td><td>0.02 <b>(+42.95%)</b></td><td>258.00 (+19.83%)</td><td>213.28 (+13.41%)</td><td>198.60 (+9.91%)</td><td>179.30 (+4.06%)</td><td>32.36 <b>(+80.48%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>215.30 (n/a)</td><td>188.06 (n/a)</td><td>180.70 (n/a)</td><td>172.30 (n/a)</td><td>17.93 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.12 <b>(-29.63%)</b></td><td>0.11 (-9.93%)</td><td>0.11 (-3.13%)</td><td>0.09 <b>(+54.79%)</b></td><td>0.01 <b>(-72.82%)</b></td><td>218.80 <b>(-35.40%)</b></td><td>189.22 (-0.80%)</td><td>179.20 (+3.29%)</td><td>171.00 <b>(+42.14%)</b></td><td>20.02 <b>(-76.65%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>338.70 (n/a)</td><td>190.74 (n/a)</td><td>173.50 (n/a)</td><td>120.30 (n/a)</td><td>85.76 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.16 (-0.37%)</td><td>0.12 (+4.29%)</td><td>0.11 (-0.23%)</td><td>0.10 (+7.08%)</td><td>0.02 (-7.50%)</td><td>199.80 (-6.59%)</td><td>170.54 (-4.54%)</td><td>181.80 (+0.22%)</td><td>131.30 (+0.38%)</td><td>26.77 (-10.89%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>213.90 (n/a)</td><td>178.66 (n/a)</td><td>181.40 (n/a)</td><td>130.80 (n/a)</td><td>30.04 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.16 (+0.45%)</td><td>0.14 (+4.49%)</td><td>0.14 (+10.89%)</td><td>0.10 (-8.21%)</td><td>0.02 <b>(+20.43%)</b></td><td>212.60 (+8.97%)</td><td>153.60 (-3.13%)</td><td>145.60 (-9.79%)</td><td>130.50 (-0.46%)</td><td>33.88 <b>(+34.49%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>195.10 (n/a)</td><td>158.56 (n/a)</td><td>161.40 (n/a)</td><td>131.10 (n/a)</td><td>25.19 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.17 (+9.49%)</td><td>0.12 (-12.14%)</td><td>0.11 <b>(-28.47%)</b></td><td>0.10 (-14.16%)</td><td>0.03 <b>(+61.23%)</b></td><td>211.20 (+16.49%)</td><td>173.48 (+17.11%)</td><td>190.50 <b>(+39.87%)</b></td><td>118.30 (-8.72%)</td><td>38.07 <b>(+71.53%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>181.30 (n/a)</td><td>148.14 (n/a)</td><td>136.20 (n/a)</td><td>129.60 (n/a)</td><td>22.19 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.14 (+8.85%)</td><td>0.11 (+5.31%)</td><td>0.12 (+15.05%)</td><td>0.07 (-16.14%)</td><td>0.03 <b>(+81.49%)</b></td><td>274.40 (+19.25%)</td><td>199.50 (-0.82%)</td><td>176.70 (-13.04%)</td><td>149.50 (-8.11%)</td><td>56.81 <b>(+92.71%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>230.10 (n/a)</td><td>201.14 (n/a)</td><td>203.20 (n/a)</td><td>162.70 (n/a)</td><td>29.48 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.12 (-9.45%)</td><td>0.12 (-2.07%)</td><td>0.11 (-7.89%)</td><td>0.11 (+11.48%)</td><td>0.01 <b>(-63.31%)</b></td><td>188.60 (-10.32%)</td><td>178.26 (+0.52%)</td><td>180.10 (+8.56%)</td><td>166.40 (+10.42%)</td><td>9.69 <b>(-64.10%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>210.30 (n/a)</td><td>177.34 (n/a)</td><td>165.90 (n/a)</td><td>150.70 (n/a)</td><td>27.00 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.18 (+12.81%)</td><td>0.12 (+8.63%)</td><td>0.11 (+15.34%)</td><td>0.08 (-5.60%)</td><td>0.04 <b>(+24.73%)</b></td><td>246.20 (+5.94%)</td><td>182.16 (-6.16%)</td><td>183.00 (-13.31%)</td><td>115.80 (-11.40%)</td><td>51.18 (+13.59%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>232.40 (n/a)</td><td>194.12 (n/a)</td><td>211.10 (n/a)</td><td>130.70 (n/a)</td><td>45.06 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.15 <b>(+24.40%)</b></td><td>0.12 <b>(+22.84%)</b></td><td>0.12 (+13.71%)</td><td>0.10 <b>(+75.89%)</b></td><td>0.02 (-17.16%)</td><td>205.50 <b>(-43.14%)</b></td><td>173.52 <b>(-22.50%)</b></td><td>173.00 (-12.09%)</td><td>139.70 (-19.62%)</td><td>28.98 <b>(-62.97%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>361.40 (n/a)</td><td>223.90 (n/a)</td><td>196.80 (n/a)</td><td>173.80 (n/a)</td><td>78.28 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.21 (+7.28%)</td><td>0.16 (-2.53%)</td><td>0.16 (-12.54%)</td><td>0.13 (+9.98%)</td><td>0.03 (-5.88%)</td><td>184.60 (-9.06%)</td><td>157.26 (+1.63%)</td><td>154.90 (+14.40%)</td><td>115.50 (-6.78%)</td><td>26.82 <b>(-21.64%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>203.00 (n/a)</td><td>154.74 (n/a)</td><td>135.40 (n/a)</td><td>123.90 (n/a)</td><td>34.23 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.16 (-16.56%)</td><td>0.14 (-9.43%)</td><td>0.14 (-11.27%)</td><td>0.13 (+10.56%)</td><td>0.01 <b>(-55.92%)</b></td><td>196.50 (-9.57%)</td><td>177.54 (+7.80%)</td><td>174.60 (+12.72%)</td><td>156.30 (+19.86%)</td><td>15.90 <b>(-52.74%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>217.30 (n/a)</td><td>164.70 (n/a)</td><td>154.90 (n/a)</td><td>130.40 (n/a)</td><td>33.65 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.17 (-16.86%)</td><td>0.13 <b>(-20.35%)</b></td><td>0.11 <b>(-30.62%)</b></td><td>0.10 (-18.84%)</td><td>0.03 (-15.40%)</td><td>242.80 <b>(+23.25%)</b></td><td>196.08 <b>(+25.77%)</b></td><td>215.70 <b>(+44.18%)</b></td><td>144.80 <b>(+20.27%)</b></td><td>42.91 <b>(+22.85%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>197.00 (n/a)</td><td>155.90 (n/a)</td><td>149.60 (n/a)</td><td>120.40 (n/a)</td><td>34.93 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.20 (-10.18%)</td><td>0.15 (+2.95%)</td><td>0.14 (+6.79%)</td><td>0.12 <b>(+27.88%)</b></td><td>0.03 <b>(-35.19%)</b></td><td>200.00 <b>(-21.81%)</b></td><td>169.42 (-7.29%)</td><td>173.30 (-6.37%)</td><td>121.50 (+11.26%)</td><td>30.20 <b>(-42.68%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>255.80 (n/a)</td><td>182.74 (n/a)</td><td>185.10 (n/a)</td><td>109.20 (n/a)</td><td>52.68 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.14 (+7.72%)</td><td>0.13 (-0.66%)</td><td>0.13 (-0.36%)</td><td>0.10 (-17.96%)</td><td>0.02 <b>(+236.00%)</b></td><td>242.70 <b>(+21.90%)</b></td><td>194.44 (+2.34%)</td><td>185.70 (+0.38%)</td><td>169.60 (-7.17%)</td><td>30.36 <b>(+275.58%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>199.10 (n/a)</td><td>190.00 (n/a)</td><td>185.00 (n/a)</td><td>182.70 (n/a)</td><td>8.08 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.15 <b>(-29.50%)</b></td><td>0.13 (-8.35%)</td><td>0.13 (-4.34%)</td><td>0.11 (+8.21%)</td><td>0.02 <b>(-57.96%)</b></td><td>228.70 (-7.60%)</td><td>195.70 (+3.85%)</td><td>192.10 (+4.52%)</td><td>165.60 <b>(+41.90%)</b></td><td>28.09 <b>(-43.52%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>247.50 (n/a)</td><td>188.44 (n/a)</td><td>183.80 (n/a)</td><td>116.70 (n/a)</td><td>49.73 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.17 (+15.31%)</td><td>0.15 (+13.05%)</td><td>0.16 <b>(+26.97%)</b></td><td>0.11 (+0.58%)</td><td>0.02 <b>(+41.41%)</b></td><td>219.10 (-0.54%)</td><td>168.40 (-10.63%)</td><td>153.90 <b>(-21.24%)</b></td><td>142.60 (-13.26%)</td><td>30.48 <b>(+27.94%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>220.30 (n/a)</td><td>188.42 (n/a)</td><td>195.40 (n/a)</td><td>164.40 (n/a)</td><td>23.83 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.17 (+5.59%)</td><td>0.14 (-0.28%)</td><td>0.15 (+9.22%)</td><td>0.11 (-13.62%)</td><td>0.03 <b>(+99.34%)</b></td><td>223.30 (+15.76%)</td><td>180.48 (+2.93%)</td><td>165.70 (-8.40%)</td><td>141.80 (-5.34%)</td><td>37.51 <b>(+128.51%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>192.90 (n/a)</td><td>175.34 (n/a)</td><td>180.90 (n/a)</td><td>149.80 (n/a)</td><td>16.41 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.13 (-11.95%)</td><td>0.11 (-4.97%)</td><td>0.12 (-17.76%)</td><td>0.09 <b>(+58.51%)</b></td><td>0.02 <b>(-55.69%)</b></td><td>214.70 <b>(-36.91%)</b></td><td>165.98 (-6.71%)</td><td>157.90 <b>(+21.65%)</b></td><td>143.90 (+13.58%)</td><td>28.96 <b>(-68.52%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>340.30 (n/a)</td><td>177.92 (n/a)</td><td>129.80 (n/a)</td><td>126.70 (n/a)</td><td>91.99 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.12 (-18.28%)</td><td>0.10 (-11.13%)</td><td>0.11 (-5.67%)</td><td>0.06 <b>(-20.39%)</b></td><td>0.03 (-4.05%)</td><td>322.30 <b>(+25.60%)</b></td><td>199.18 (+14.93%)</td><td>173.60 (+5.98%)</td><td>151.10 <b>(+22.35%)</b></td><td>71.35 <b>(+42.94%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>256.60 (n/a)</td><td>173.30 (n/a)</td><td>163.80 (n/a)</td><td>123.50 (n/a)</td><td>49.92 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.16 (+16.79%)</td><td>0.13 (+13.09%)</td><td>0.14 <b>(+24.33%)</b></td><td>0.10 (-2.93%)</td><td>0.03 <b>(+81.65%)</b></td><td>189.20 (+2.99%)</td><td>146.56 (-9.62%)</td><td>131.90 (-19.57%)</td><td>114.00 (-14.41%)</td><td>30.44 <b>(+66.70%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>183.70 (n/a)</td><td>162.16 (n/a)</td><td>164.00 (n/a)</td><td>133.20 (n/a)</td><td>18.26 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.15 (+3.40%)</td><td>0.12 (+13.93%)</td><td>0.14 <b>(+28.83%)</b></td><td>0.09 (+4.59%)</td><td>0.03 <b>(+22.93%)</b></td><td>199.70 (-4.36%)</td><td>155.52 (-11.21%)</td><td>131.70 <b>(-22.39%)</b></td><td>125.40 (-3.32%)</td><td>36.31 (+13.11%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>208.80 (n/a)</td><td>175.16 (n/a)</td><td>169.70 (n/a)</td><td>129.70 (n/a)</td><td>32.10 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.16 <b>(+31.58%)</b></td><td>0.14 (+16.10%)</td><td>0.14 (+13.98%)</td><td>0.11 (-4.36%)</td><td>0.02 <b>(+340.46%)</b></td><td>173.20 (+4.59%)</td><td>136.86 (-12.20%)</td><td>134.00 (-12.25%)</td><td>114.50 <b>(-24.02%)</b></td><td>22.78 <b>(+255.32%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.00 (n/a)</td><td>165.60 (n/a)</td><td>155.88 (n/a)</td><td>152.70 (n/a)</td><td>150.70 (n/a)</td><td>6.41 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.15 (-1.50%)</td><td>0.12 (+11.39%)</td><td>0.13 <b>(+23.61%)</b></td><td>0.10 (+8.72%)</td><td>0.02 <b>(-25.28%)</b></td><td>182.30 (-8.02%)</td><td>150.52 (-11.40%)</td><td>145.50 (-19.08%)</td><td>124.60 (+1.47%)</td><td>21.20 <b>(-27.92%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>198.20 (n/a)</td><td>169.88 (n/a)</td><td>179.80 (n/a)</td><td>122.80 (n/a)</td><td>29.40 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.13 (-5.24%)</td><td>0.09 (-4.44%)</td><td>0.09 (-2.57%)</td><td>0.07 (+11.53%)</td><td>0.02 <b>(-22.11%)</b></td><td>275.40 (-10.35%)</td><td>207.08 (+1.56%)</td><td>201.60 (+2.65%)</td><td>147.30 (+5.52%)</td><td>45.67 <b>(-28.46%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>307.20 (n/a)</td><td>203.90 (n/a)</td><td>196.40 (n/a)</td><td>139.60 (n/a)</td><td>63.84 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.13 (-7.31%)</td><td>0.11 (+6.68%)</td><td>0.12 <b>(+25.56%)</b></td><td>0.09 (+9.30%)</td><td>0.02 <b>(-24.01%)</b></td><td>212.30 (-8.53%)</td><td>173.36 (-7.74%)</td><td>155.60 <b>(-20.33%)</b></td><td>145.80 (+7.84%)</td><td>29.68 <b>(-24.14%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>232.10 (n/a)</td><td>187.90 (n/a)</td><td>195.30 (n/a)</td><td>135.20 (n/a)</td><td>39.12 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.93 <b>(+26.47%)</b></td><td>0.66 (+18.68%)</td><td>0.63 (+14.30%)</td><td>0.54 <b>(+25.06%)</b></td><td>0.16 <b>(+40.79%)</b></td><td>181.40 <b>(-20.02%)</b></td><td>155.84 (-15.05%)</td><td>157.00 (-12.53%)</td><td>105.40 <b>(-20.93%)</b></td><td>30.87 (-10.10%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.74 (n/a)</td><td>0.55 (n/a)</td><td>0.55 (n/a)</td><td>0.43 (n/a)</td><td>0.11 (n/a)</td><td>226.80 (n/a)</td><td>183.44 (n/a)</td><td>179.50 (n/a)</td><td>133.30 (n/a)</td><td>34.34 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.81 (+18.49%)</td><td>0.57 (-0.17%)</td><td>0.56 (-0.23%)</td><td>0.40 (-13.52%)</td><td>0.15 <b>(+86.32%)</b></td><td>244.20 (+15.62%)</td><td>183.68 (+4.01%)</td><td>175.20 (+0.23%)</td><td>121.50 (-15.62%)</td><td>45.96 <b>(+79.67%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.68 (n/a)</td><td>0.57 (n/a)</td><td>0.56 (n/a)</td><td>0.47 (n/a)</td><td>0.08 (n/a)</td><td>211.20 (n/a)</td><td>176.60 (n/a)</td><td>174.80 (n/a)</td><td>144.00 (n/a)</td><td>25.58 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.58 (-16.26%)</td><td>0.50 (-15.53%)</td><td>0.47 <b>(-23.91%)</b></td><td>0.41 (-9.42%)</td><td>0.07 (-18.77%)</td><td>239.90 (+10.40%)</td><td>199.20 (+17.97%)</td><td>207.00 <b>(+31.43%)</b></td><td>170.30 (+19.42%)</td><td>29.19 (+1.04%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.69 (n/a)</td><td>0.59 (n/a)</td><td>0.62 (n/a)</td><td>0.45 (n/a)</td><td>0.09 (n/a)</td><td>217.30 (n/a)</td><td>168.86 (n/a)</td><td>157.50 (n/a)</td><td>142.60 (n/a)</td><td>28.89 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.64 (-7.18%)</td><td>0.56 (+6.96%)</td><td>0.61 <b>(+22.89%)</b></td><td>0.43 (+2.21%)</td><td>0.09 (-19.95%)</td><td>226.20 (-2.16%)</td><td>178.88 (-7.59%)</td><td>160.30 (-18.59%)</td><td>152.60 (+7.77%)</td><td>31.76 (-18.17%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.69 (n/a)</td><td>0.53 (n/a)</td><td>0.50 (n/a)</td><td>0.43 (n/a)</td><td>0.11 (n/a)</td><td>231.20 (n/a)</td><td>193.58 (n/a)</td><td>196.90 (n/a)</td><td>141.60 (n/a)</td><td>38.81 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.52 (+0.15%)</td><td>0.42 (-10.16%)</td><td>0.41 (-13.74%)</td><td>0.38 (-11.33%)</td><td>0.06 <b>(+76.04%)</b></td><td>194.60 (+12.81%)</td><td>176.30 (+12.34%)</td><td>180.60 (+15.92%)</td><td>142.20 (-0.14%)</td><td>21.03 <b>(+96.46%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.52 (n/a)</td><td>0.47 (n/a)</td><td>0.47 (n/a)</td><td>0.43 (n/a)</td><td>0.03 (n/a)</td><td>172.50 (n/a)</td><td>156.94 (n/a)</td><td>155.80 (n/a)</td><td>142.40 (n/a)</td><td>10.70 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.49 <b>(-28.95%)</b></td><td>0.44 (-18.88%)</td><td>0.44 (-14.84%)</td><td>0.37 (-14.46%)</td><td>0.05 <b>(-58.40%)</b></td><td>201.20 (+16.91%)</td><td>169.28 <b>(+20.31%)</b></td><td>166.90 (+17.45%)</td><td>149.40 <b>(+40.81%)</b></td><td>19.67 <b>(-31.24%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.69 (n/a)</td><td>0.54 (n/a)</td><td>0.52 (n/a)</td><td>0.43 (n/a)</td><td>0.11 (n/a)</td><td>172.10 (n/a)</td><td>140.70 (n/a)</td><td>142.10 (n/a)</td><td>106.10 (n/a)</td><td>28.60 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.49 (+1.52%)</td><td>0.40 (-5.08%)</td><td>0.40 (-0.87%)</td><td>0.31 (-19.78%)</td><td>0.08 <b>(+104.40%)</b></td><td>237.90 <b>(+24.69%)</b></td><td>191.94 (+8.32%)</td><td>184.20 (+0.88%)</td><td>149.30 (-1.45%)</td><td>39.66 <b>(+158.15%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.49 (n/a)</td><td>0.42 (n/a)</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.04 (n/a)</td><td>190.80 (n/a)</td><td>177.20 (n/a)</td><td>182.60 (n/a)</td><td>151.50 (n/a)</td><td>15.36 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.49 (-4.25%)</td><td>0.44 (+13.98%)</td><td>0.43 (+7.71%)</td><td>0.36 <b>(+66.38%)</b></td><td>0.05 <b>(-49.77%)</b></td><td>204.10 <b>(-39.90%)</b></td><td>169.92 (-18.15%)</td><td>171.50 (-7.15%)</td><td>150.10 (+4.45%)</td><td>22.02 <b>(-71.06%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.51 (n/a)</td><td>0.39 (n/a)</td><td>0.40 (n/a)</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>339.60 (n/a)</td><td>207.60 (n/a)</td><td>184.70 (n/a)</td><td>143.70 (n/a)</td><td>76.09 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.32 (-7.78%)</td><td>0.24 (-17.11%)</td><td>0.22 <b>(-22.38%)</b></td><td>0.20 (-18.75%)</td><td>0.05 <b>(+35.22%)</b></td><td>182.60 <b>(+23.13%)</b></td><td>160.46 <b>(+22.62%)</b></td><td>171.10 <b>(+28.84%)</b></td><td>116.50 (+8.47%)</td><td>27.01 <b>(+83.21%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.34 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.04 (n/a)</td><td>148.30 (n/a)</td><td>130.86 (n/a)</td><td>132.80 (n/a)</td><td>107.40 (n/a)</td><td>14.74 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.28 (-16.49%)</td><td>0.25 (+12.80%)</td><td>0.26 (+11.14%)</td><td>0.20 <b>(+97.02%)</b></td><td>0.04 <b>(-58.42%)</b></td><td>183.60 <b>(-49.25%)</b></td><td>152.74 <b>(-23.34%)</b></td><td>141.10 (-10.01%)</td><td>130.20 (+19.78%)</td><td>24.14 <b>(-75.64%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.34 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>361.80 (n/a)</td><td>199.24 (n/a)</td><td>156.80 (n/a)</td><td>108.70 (n/a)</td><td>99.11 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.30 (+1.55%)</td><td>0.25 (+11.44%)</td><td>0.28 <b>(+26.25%)</b></td><td>0.15 (-12.57%)</td><td>0.06 <b>(+35.78%)</b></td><td>238.50 (+14.39%)</td><td>156.18 (-7.50%)</td><td>132.00 <b>(-20.77%)</b></td><td>124.80 (-1.58%)</td><td>47.52 <b>(+58.19%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>208.50 (n/a)</td><td>168.84 (n/a)</td><td>166.60 (n/a)</td><td>126.80 (n/a)</td><td>30.04 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.30 (+4.83%)</td><td>0.25 <b>(+26.11%)</b></td><td>0.26 <b>(+41.04%)</b></td><td>0.21 <b>(+38.19%)</b></td><td>0.04 <b>(-38.69%)</b></td><td>173.40 <b>(-27.66%)</b></td><td>146.84 <b>(-24.09%)</b></td><td>144.60 <b>(-29.08%)</b></td><td>122.10 (-4.61%)</td><td>20.33 <b>(-58.67%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>239.70 (n/a)</td><td>193.44 (n/a)</td><td>203.90 (n/a)</td><td>128.00 (n/a)</td><td>49.18 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.32 <b>(+32.45%)</b></td><td>0.26 <b>(+20.69%)</b></td><td>0.25 (+19.45%)</td><td>0.22 (+11.74%)</td><td>0.04 <b>(+121.04%)</b></td><td>168.90 (-10.49%)</td><td>146.48 (-16.20%)</td><td>146.10 (-16.32%)</td><td>115.90 <b>(-24.50%)</b></td><td>20.05 <b>(+48.39%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>188.70 (n/a)</td><td>174.80 (n/a)</td><td>174.60 (n/a)</td><td>153.50 (n/a)</td><td>13.51 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.31 <b>(+48.22%)</b></td><td>0.26 <b>(+32.31%)</b></td><td>0.26 <b>(+30.36%)</b></td><td>0.23 (+17.56%)</td><td>0.03 <b>(+370.44%)</b></td><td>161.80 (-14.93%)</td><td>140.68 <b>(-23.75%)</b></td><td>142.80 <b>(-23.27%)</b></td><td>120.10 <b>(-32.53%)</b></td><td>15.29 <b>(+168.54%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.01 (n/a)</td><td>190.20 (n/a)</td><td>184.50 (n/a)</td><td>186.10 (n/a)</td><td>178.00 (n/a)</td><td>5.69 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.31 <b>(+28.44%)</b></td><td>0.22 (+15.51%)</td><td>0.20 (+6.52%)</td><td>0.18 <b>(+23.04%)</b></td><td>0.05 <b>(+26.79%)</b></td><td>200.30 (-18.71%)</td><td>170.94 (-13.43%)</td><td>182.90 (-6.11%)</td><td>118.10 <b>(-22.15%)</b></td><td>33.03 <b>(-21.07%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>246.40 (n/a)</td><td>197.46 (n/a)</td><td>194.80 (n/a)</td><td>151.70 (n/a)</td><td>41.84 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.28 (-0.29%)</td><td>0.21 (+0.24%)</td><td>0.21 (-3.11%)</td><td>0.16 (+2.18%)</td><td>0.04 (+0.31%)</td><td>232.60 (-2.10%)</td><td>179.84 (-0.26%)</td><td>177.80 (+3.25%)</td><td>132.50 (+0.30%)</td><td>37.45 (-1.95%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>237.60 (n/a)</td><td>180.30 (n/a)</td><td>172.20 (n/a)</td><td>132.10 (n/a)</td><td>38.19 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.35 (+1.30%)</td><td>0.28 (+3.67%)</td><td>0.26 (-6.54%)</td><td>0.22 <b>(+26.23%)</b></td><td>0.06 (-16.61%)</td><td>187.20 <b>(-20.78%)</b></td><td>150.36 (-6.15%)</td><td>158.40 (+6.95%)</td><td>118.30 (-1.25%)</td><td>29.60 <b>(-37.06%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.34 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.17 (n/a)</td><td>0.07 (n/a)</td><td>236.30 (n/a)</td><td>160.22 (n/a)</td><td>148.10 (n/a)</td><td>119.80 (n/a)</td><td>47.02 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.33 (+5.81%)</td><td>0.28 (+13.94%)</td><td>0.28 (+14.95%)</td><td>0.22 (+8.59%)</td><td>0.05 (+11.09%)</td><td>188.80 (-7.90%)</td><td>150.92 (-12.06%)</td><td>147.70 (-13.02%)</td><td>123.70 (-5.50%)</td><td>26.71 (-2.36%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>205.00 (n/a)</td><td>171.62 (n/a)</td><td>169.80 (n/a)</td><td>130.90 (n/a)</td><td>27.36 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.34 (+5.92%)</td><td>0.31 <b>(+23.84%)</b></td><td>0.31 <b>(+32.95%)</b></td><td>0.27 <b>(+61.72%)</b></td><td>0.03 <b>(-51.18%)</b></td><td>151.50 <b>(-38.16%)</b></td><td>134.30 <b>(-22.89%)</b></td><td>131.90 <b>(-24.76%)</b></td><td>120.00 (-5.59%)</td><td>13.46 <b>(-71.13%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>245.00 (n/a)</td><td>174.16 (n/a)</td><td>175.30 (n/a)</td><td>127.10 (n/a)</td><td>46.63 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.33 (-2.98%)</td><td>0.26 (+1.80%)</td><td>0.25 (+7.13%)</td><td>0.20 (+1.20%)</td><td>0.05 <b>(-23.35%)</b></td><td>204.20 (-1.16%)</td><td>160.88 (-3.53%)</td><td>164.70 (-6.63%)</td><td>125.20 (+3.05%)</td><td>29.88 <b>(-21.83%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.34 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>206.60 (n/a)</td><td>166.76 (n/a)</td><td>176.40 (n/a)</td><td>121.50 (n/a)</td><td>38.22 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.39 <b>(+29.13%)</b></td><td>0.29 <b>(+21.09%)</b></td><td>0.29 <b>(+29.05%)</b></td><td>0.21 (+6.48%)</td><td>0.07 <b>(+81.48%)</b></td><td>191.10 (-6.09%)</td><td>151.40 (-14.81%)</td><td>143.60 <b>(-22.50%)</b></td><td>104.90 <b>(-22.53%)</b></td><td>37.65 <b>(+39.27%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>203.50 (n/a)</td><td>177.72 (n/a)</td><td>185.30 (n/a)</td><td>135.40 (n/a)</td><td>27.03 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.34 (+4.04%)</td><td>0.27 (+5.57%)</td><td>0.26 (+7.50%)</td><td>0.18 (+2.46%)</td><td>0.07 (+5.07%)</td><td>224.30 (-2.39%)</td><td>157.52 (-5.11%)</td><td>159.50 (-7.00%)</td><td>119.90 (-3.93%)</td><td>42.17 (-0.62%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>229.80 (n/a)</td><td>166.00 (n/a)</td><td>171.50 (n/a)</td><td>124.80 (n/a)</td><td>42.43 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.34 (+16.39%)</td><td>0.26 (+11.58%)</td><td>0.24 (-3.57%)</td><td>0.20 (+12.94%)</td><td>0.06 (+11.63%)</td><td>204.10 (-11.45%)</td><td>165.06 (-10.73%)</td><td>169.20 (+3.74%)</td><td>121.40 (-14.02%)</td><td>33.91 (-19.38%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>230.50 (n/a)</td><td>184.90 (n/a)</td><td>163.10 (n/a)</td><td>141.20 (n/a)</td><td>42.06 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.31 (+0.54%)</td><td>0.25 (+6.84%)</td><td>0.26 (+19.69%)</td><td>0.21 (+9.33%)</td><td>0.04 (-10.79%)</td><td>196.30 (-8.57%)</td><td>166.26 (-7.04%)</td><td>159.20 (-16.43%)</td><td>130.90 (-0.53%)</td><td>26.37 (-15.92%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>214.70 (n/a)</td><td>178.86 (n/a)</td><td>190.50 (n/a)</td><td>131.60 (n/a)</td><td>31.36 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.39 <b>(+45.80%)</b></td><td>0.26 <b>(+23.17%)</b></td><td>0.25 <b>(+36.46%)</b></td><td>0.16 (-6.04%)</td><td>0.09 <b>(+90.21%)</b></td><td>220.00 (+6.43%)</td><td>150.56 (-13.86%)</td><td>141.50 <b>(-26.72%)</b></td><td>88.50 <b>(-31.40%)</b></td><td>51.64 <b>(+37.62%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>206.70 (n/a)</td><td>174.78 (n/a)</td><td>193.10 (n/a)</td><td>129.00 (n/a)</td><td>37.52 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.28 (-2.26%)</td><td>0.21 (-14.31%)</td><td>0.19 <b>(-28.09%)</b></td><td>0.18 (-1.01%)</td><td>0.04 (+8.23%)</td><td>191.10 (+1.00%)</td><td>170.26 (+17.19%)</td><td>187.70 <b>(+39.04%)</b></td><td>123.90 (+2.31%)</td><td>28.88 (+9.45%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>189.20 (n/a)</td><td>145.28 (n/a)</td><td>135.00 (n/a)</td><td>121.10 (n/a)</td><td>26.38 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.29 (+4.39%)</td><td>0.24 (+18.48%)</td><td>0.27 <b>(+36.76%)</b></td><td>0.18 (+7.01%)</td><td>0.05 <b>(+22.44%)</b></td><td>193.30 (-6.57%)</td><td>148.60 (-14.67%)</td><td>129.70 <b>(-26.89%)</b></td><td>119.90 (-4.23%)</td><td>34.73 (+11.44%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>206.90 (n/a)</td><td>174.14 (n/a)</td><td>177.40 (n/a)</td><td>125.20 (n/a)</td><td>31.16 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.29 (+2.03%)</td><td>0.22 (-3.38%)</td><td>0.21 (-8.74%)</td><td>0.12 <b>(-25.95%)</b></td><td>0.06 <b>(+45.31%)</b></td><td>287.40 <b>(+35.06%)</b></td><td>174.80 (+9.50%)</td><td>163.70 (+9.57%)</td><td>121.20 (-1.94%)</td><td>65.96 <b>(+95.86%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>212.80 (n/a)</td><td>159.64 (n/a)</td><td>149.40 (n/a)</td><td>123.60 (n/a)</td><td>33.68 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.28 (+12.24%)</td><td>0.19 (-5.85%)</td><td>0.18 (-11.79%)</td><td>0.15 (-17.27%)</td><td>0.05 <b>(+86.18%)</b></td><td>237.40 <b>(+20.88%)</b></td><td>192.10 (+10.48%)</td><td>196.40 (+13.39%)</td><td>122.80 (-10.95%)</td><td>45.21 <b>(+100.45%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>196.40 (n/a)</td><td>173.88 (n/a)</td><td>173.20 (n/a)</td><td>137.90 (n/a)</td><td>22.56 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.28 <b>(+22.89%)</b></td><td>0.24 <b>(+25.29%)</b></td><td>0.25 <b>(+27.03%)</b></td><td>0.18 <b>(+23.65%)</b></td><td>0.04 <b>(+29.38%)</b></td><td>189.50 (-19.12%)</td><td>147.20 <b>(-20.03%)</b></td><td>140.40 <b>(-21.30%)</b></td><td>123.00 (-18.65%)</td><td>27.60 (-16.07%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>234.30 (n/a)</td><td>184.06 (n/a)</td><td>178.40 (n/a)</td><td>151.20 (n/a)</td><td>32.88 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.27 <b>(+23.95%)</b></td><td>0.20 (+2.55%)</td><td>0.18 (-11.60%)</td><td>0.15 (-14.51%)</td><td>0.06 <b>(+218.22%)</b></td><td>232.10 (+16.99%)</td><td>183.02 (+3.48%)</td><td>197.50 (+13.12%)</td><td>127.20 (-19.29%)</td><td>50.15 <b>(+195.78%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>198.40 (n/a)</td><td>176.86 (n/a)</td><td>174.60 (n/a)</td><td>157.60 (n/a)</td><td>16.96 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.26 <b>(+26.62%)</b></td><td>0.21 <b>(+21.69%)</b></td><td>0.20 (+9.53%)</td><td>0.17 <b>(+53.04%)</b></td><td>0.04 (+16.22%)</td><td>206.00 <b>(-34.67%)</b></td><td>172.94 (-19.05%)</td><td>178.20 (-8.71%)</td><td>134.10 <b>(-21.02%)</b></td><td>33.01 <b>(-42.96%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>315.30 (n/a)</td><td>213.64 (n/a)</td><td>195.20 (n/a)</td><td>169.80 (n/a)</td><td>57.87 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.85 (-16.15%)</td><td>0.64 <b>(-22.83%)</b></td><td>0.62 <b>(-25.83%)</b></td><td>0.51 <b>(-22.55%)</b></td><td>0.13 (-12.99%)</td><td>258.30 <b>(+29.09%)</b></td><td>212.68 <b>(+30.02%)</b></td><td>210.50 <b>(+34.76%)</b></td><td>155.00 (+19.23%)</td><td>39.94 <b>(+30.85%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>1.01 (n/a)</td><td>0.82 (n/a)</td><td>0.84 (n/a)</td><td>0.66 (n/a)</td><td>0.15 (n/a)</td><td>200.10 (n/a)</td><td>163.58 (n/a)</td><td>156.20 (n/a)</td><td>130.00 (n/a)</td><td>30.52 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.87 (-8.82%)</td><td>0.69 (-19.05%)</td><td>0.69 <b>(-23.46%)</b></td><td>0.51 (-19.58%)</td><td>0.13 (-0.66%)</td><td>258.90 <b>(+24.35%)</b></td><td>195.54 <b>(+24.42%)</b></td><td>190.80 <b>(+30.68%)</b></td><td>150.90 (+9.67%)</td><td>39.19 <b>(+35.10%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.95 (n/a)</td><td>0.85 (n/a)</td><td>0.90 (n/a)</td><td>0.63 (n/a)</td><td>0.13 (n/a)</td><td>208.20 (n/a)</td><td>157.16 (n/a)</td><td>146.00 (n/a)</td><td>137.60 (n/a)</td><td>29.01 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.66 <b>(-27.92%)</b></td><td>0.59 <b>(-25.71%)</b></td><td>0.62 (-18.69%)</td><td>0.47 <b>(-35.63%)</b></td><td>0.08 (+8.94%)</td><td>277.10 <b>(+55.33%)</b></td><td>227.44 <b>(+35.91%)</b></td><td>211.20 <b>(+23.01%)</b></td><td>198.50 <b>(+38.71%)</b></td><td>33.23 <b>(+138.44%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.92 (n/a)</td><td>0.79 (n/a)</td><td>0.76 (n/a)</td><td>0.73 (n/a)</td><td>0.07 (n/a)</td><td>178.40 (n/a)</td><td>167.34 (n/a)</td><td>171.70 (n/a)</td><td>143.10 (n/a)</td><td>13.94 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (+6.71%)</td><td>0.03 (+4.84%)</td><td>0.03 (+1.84%)</td><td>0.02 (+10.94%)</td><td>0.00 (-1.43%)</td><td>209.20 (-9.87%)</td><td>164.96 (-5.10%)</td><td>160.10 (-1.84%)</td><td>137.40 (-6.28%)</td><td>27.80 (-18.20%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.10 (n/a)</td><td>173.82 (n/a)</td><td>163.10 (n/a)</td><td>146.60 (n/a)</td><td>33.98 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (-12.20%)</td><td>0.02 (-9.98%)</td><td>0.02 (-11.88%)</td><td>0.02 (+2.49%)</td><td>0.00 <b>(-29.44%)</b></td><td>219.60 (-2.44%)</td><td>183.80 (+9.25%)</td><td>187.20 (+13.52%)</td><td>142.30 (+13.84%)</td><td>27.86 <b>(-24.15%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>225.10 (n/a)</td><td>168.24 (n/a)</td><td>164.90 (n/a)</td><td>125.00 (n/a)</td><td>36.73 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (+0.60%)</td><td>0.02 (-5.56%)</td><td>0.02 (-9.79%)</td><td>0.02 (+9.69%)</td><td>0.01 (-3.66%)</td><td>222.10 (-8.83%)</td><td>179.64 (+5.16%)</td><td>183.10 (+10.84%)</td><td>134.60 (-0.59%)</td><td>37.84 (-13.15%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>243.60 (n/a)</td><td>170.82 (n/a)</td><td>165.20 (n/a)</td><td>135.40 (n/a)</td><td>43.58 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>14.04 (-13.98%)</td><td>12.56 (-9.62%)</td><td>12.97 (+0.35%)</td><td>10.70 (-6.12%)</td><td>1.55 <b>(-28.24%)</b></td><td>196.10 (+6.52%)</td><td>169.24 (+9.94%)</td><td>161.80 (-0.31%)</td><td>149.40 (+16.26%)</td><td>21.51 (-8.90%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>16.33 (n/a)</td><td>13.89 (n/a)</td><td>12.93 (n/a)</td><td>11.40 (n/a)</td><td>2.16 (n/a)</td><td>184.10 (n/a)</td><td>153.94 (n/a)</td><td>162.30 (n/a)</td><td>128.50 (n/a)</td><td>23.61 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.88 (-16.61%)</td><td>0.70 <b>(-21.61%)</b></td><td>0.72 (-17.21%)</td><td>0.43 <b>(-40.59%)</b></td><td>0.16 (+7.11%)</td><td>306.80 <b>(+68.29%)</b></td><td>200.56 <b>(+31.96%)</b></td><td>183.50 <b>(+20.72%)</b></td><td>151.00 (+19.94%)</td><td>60.92 <b>(+135.32%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>1.05 (n/a)</td><td>0.89 (n/a)</td><td>0.87 (n/a)</td><td>0.72 (n/a)</td><td>0.15 (n/a)</td><td>182.30 (n/a)</td><td>151.98 (n/a)</td><td>152.00 (n/a)</td><td>125.90 (n/a)</td><td>25.89 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.93 (-11.68%)</td><td>0.74 (-8.60%)</td><td>0.71 (-13.48%)</td><td>0.56 (-8.93%)</td><td>0.17 (+8.02%)</td><td>234.80 (+9.82%)</td><td>185.42 (+10.84%)</td><td>185.10 (+15.62%)</td><td>142.30 (+13.21%)</td><td>42.87 <b>(+31.04%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>1.05 (n/a)</td><td>0.81 (n/a)</td><td>0.82 (n/a)</td><td>0.62 (n/a)</td><td>0.16 (n/a)</td><td>213.80 (n/a)</td><td>167.28 (n/a)</td><td>160.10 (n/a)</td><td>125.70 (n/a)</td><td>32.71 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>1.07 (+8.24%)</td><td>0.85 (+6.08%)</td><td>0.78 (-6.28%)</td><td>0.70 (+15.42%)</td><td>0.16 (+12.72%)</td><td>187.80 (-13.38%)</td><td>159.90 (-5.69%)</td><td>169.10 (+6.69%)</td><td>123.00 (-7.59%)</td><td>28.85 (-10.29%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.99 (n/a)</td><td>0.80 (n/a)</td><td>0.83 (n/a)</td><td>0.61 (n/a)</td><td>0.15 (n/a)</td><td>216.80 (n/a)</td><td>169.54 (n/a)</td><td>158.50 (n/a)</td><td>133.10 (n/a)</td><td>32.16 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.97 (-13.61%)</td><td>0.71 <b>(-24.77%)</b></td><td>0.72 <b>(-21.49%)</b></td><td>0.48 <b>(-32.99%)</b></td><td>0.18 (+5.76%)</td><td>272.70 <b>(+49.18%)</b></td><td>195.80 <b>(+36.18%)</b></td><td>182.30 <b>(+27.39%)</b></td><td>135.80 (+15.77%)</td><td>50.01 <b>(+87.17%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>1.13 (n/a)</td><td>0.94 (n/a)</td><td>0.92 (n/a)</td><td>0.72 (n/a)</td><td>0.17 (n/a)</td><td>182.80 (n/a)</td><td>143.78 (n/a)</td><td>143.10 (n/a)</td><td>117.30 (n/a)</td><td>26.72 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.94 (-9.06%)</td><td>0.83 (-0.74%)</td><td>0.78 (-7.65%)</td><td>0.75 (+17.77%)</td><td>0.10 <b>(-44.38%)</b></td><td>176.90 (-15.12%)</td><td>160.88 (-1.87%)</td><td>169.90 (+8.29%)</td><td>140.40 (+9.95%)</td><td>18.39 <b>(-48.37%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>1.03 (n/a)</td><td>0.84 (n/a)</td><td>0.84 (n/a)</td><td>0.63 (n/a)</td><td>0.18 (n/a)</td><td>208.40 (n/a)</td><td>163.94 (n/a)</td><td>156.90 (n/a)</td><td>127.70 (n/a)</td><td>35.62 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 (-19.28%)</td><td>0.02 <b>(-24.67%)</b></td><td>0.02 <b>(-33.04%)</b></td><td>0.02 (-3.48%)</td><td>0.00 <b>(-32.03%)</b></td><td>247.60 (+3.60%)</td><td>202.60 <b>(+29.49%)</b></td><td>213.10 <b>(+49.33%)</b></td><td>148.00 <b>(+23.95%)</b></td><td>39.76 (-16.97%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>239.00 (n/a)</td><td>156.46 (n/a)</td><td>142.70 (n/a)</td><td>119.40 (n/a)</td><td>47.88 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.03 <b>(-29.77%)</b></td><td>0.02 <b>(-28.18%)</b></td><td>0.02 <b>(-31.18%)</b></td><td>0.02 <b>(-21.40%)</b></td><td>0.00 <b>(-48.23%)</b></td><td>197.90 <b>(+27.19%)</b></td><td>186.42 <b>(+38.44%)</b></td><td>194.20 <b>(+45.25%)</b></td><td>162.70 <b>(+42.47%)</b></td><td>14.82 (-6.37%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>155.60 (n/a)</td><td>134.66 (n/a)</td><td>133.70 (n/a)</td><td>114.20 (n/a)</td><td>15.83 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.00 (+4.65%)</td><td>0.00 (+5.29%)</td><td>0.00 (+4.76%)</td><td>0.00 (+10.53%)</td><td>0.00 <b>(-37.12%)</b></td><td>965.66 (-9.39%)</td><td>935.46 (-4.83%)</td><td>934.99 (-3.56%)</td><td>906.61 (-4.62%)</td><td>26.71 <b>(-43.16%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1065.68 (n/a)</td><td>982.89 (n/a)</td><td>969.53 (n/a)</td><td>950.49 (n/a)</td><td>46.99 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.01 (+1.18%)</td><td>0.01 (-3.69%)</td><td>0.01 (-1.25%)</td><td>0.01 (-9.09%)</td><td>0.00 <b>(+74.82%)</b></td><td>1172.87 (+10.28%)</td><td>1052.48 (+4.25%)</td><td>1041.34 (+1.75%)</td><td>952.51 (-1.23%)</td><td>78.78 <b>(+90.39%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1063.55 (n/a)</td><td>1009.58 (n/a)</td><td>1023.40 (n/a)</td><td>964.41 (n/a)</td><td>41.38 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.95 (-2.59%)</td><td>0.94 (-2.66%)</td><td>0.94 (-2.53%)</td><td>0.92 (-2.78%)</td><td>0.01 (+4.54%)</td><td>2268.56 (+2.85%)</td><td>2225.69 (+2.74%)</td><td>2222.94 (+2.59%)</td><td>2198.58 (+2.66%)</td><td>26.98 (+10.06%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.98 (n/a)</td><td>0.97 (n/a)</td><td>0.97 (n/a)</td><td>0.95 (n/a)</td><td>0.01 (n/a)</td><td>2205.73 (n/a)</td><td>2166.42 (n/a)</td><td>2166.78 (n/a)</td><td>2141.55 (n/a)</td><td>24.51 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.40 (-5.31%)</td><td>0.39 (-2.88%)</td><td>0.39 (-1.25%)</td><td>0.38 (-2.62%)</td><td>0.01 <b>(-36.34%)</b></td><td>1381.55 (+2.69%)</td><td>1339.37 (+2.93%)</td><td>1327.98 (+1.28%)</td><td>1319.01 (+5.62%)</td><td>24.78 <b>(-30.53%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.42 (n/a)</td><td>0.40 (n/a)</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.01 (n/a)</td><td>1345.32 (n/a)</td><td>1301.22 (n/a)</td><td>1311.24 (n/a)</td><td>1248.84 (n/a)</td><td>35.68 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.25 (-6.32%)</td><td>0.25 (-2.14%)</td><td>0.25 (-1.54%)</td><td>0.24 (+1.33%)</td><td>0.00 <b>(-74.74%)</b></td><td>2144.14 (-1.31%)</td><td>2110.26 (+2.08%)</td><td>2108.65 (+1.56%)</td><td>2092.80 (+6.75%)</td><td>20.91 <b>(-73.49%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.01 (n/a)</td><td>2172.68 (n/a)</td><td>2067.21 (n/a)</td><td>2076.18 (n/a)</td><td>1960.40 (n/a)</td><td>78.88 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.37 (-2.41%)</td><td>0.36 (-1.63%)</td><td>0.36 (-1.74%)</td><td>0.35 (-2.85%)</td><td>0.01 (+6.45%)</td><td>1477.08 (+2.91%)</td><td>1442.05 (+1.65%)</td><td>1452.58 (+1.76%)</td><td>1407.08 (+2.46%)</td><td>28.80 (+12.19%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.01 (n/a)</td><td>1435.30 (n/a)</td><td>1418.68 (n/a)</td><td>1427.39 (n/a)</td><td>1373.30 (n/a)</td><td>25.67 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>6.00 (+5.47%)</td><td>4.83 (+3.23%)</td><td>4.84 (+8.71%)</td><td>3.53 (-9.20%)</td><td>1.18 <b>(+50.95%)</b></td><td>296.90 (+10.13%)</td><td>228.42 (-0.36%)</td><td>216.50 (-7.99%)</td><td>174.70 (-5.21%)</td><td>57.34 <b>(+54.99%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>5.69 (n/a)</td><td>4.68 (n/a)</td><td>4.46 (n/a)</td><td>3.89 (n/a)</td><td>0.78 (n/a)</td><td>269.60 (n/a)</td><td>229.24 (n/a)</td><td>235.30 (n/a)</td><td>184.30 (n/a)</td><td>36.99 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>7.03 <b>(+41.47%)</b></td><td>5.33 <b>(+28.15%)</b></td><td>5.55 <b>(+30.72%)</b></td><td>3.65 <b>(+20.69%)</b></td><td>1.24 <b>(+71.59%)</b></td><td>287.50 (-17.17%)</td><td>205.94 <b>(-20.52%)</b></td><td>189.00 <b>(-23.48%)</b></td><td>149.20 <b>(-29.32%)</b></td><td>51.69 (-0.88%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>4.97 (n/a)</td><td>4.16 (n/a)</td><td>4.24 (n/a)</td><td>3.02 (n/a)</td><td>0.72 (n/a)</td><td>347.10 (n/a)</td><td>259.10 (n/a)</td><td>247.00 (n/a)</td><td>211.10 (n/a)</td><td>52.15 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>5.17 (-12.83%)</td><td>4.54 (-9.74%)</td><td>4.66 (-9.74%)</td><td>3.82 (-2.70%)</td><td>0.59 <b>(-32.13%)</b></td><td>274.70 (+2.81%)</td><td>234.24 (+9.55%)</td><td>225.00 (+10.78%)</td><td>203.00 (+14.75%)</td><td>31.56 (-19.12%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>5.93 (n/a)</td><td>5.03 (n/a)</td><td>5.16 (n/a)</td><td>3.92 (n/a)</td><td>0.87 (n/a)</td><td>267.20 (n/a)</td><td>213.82 (n/a)</td><td>203.10 (n/a)</td><td>176.90 (n/a)</td><td>39.02 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>6.11 (-2.08%)</td><td>5.26 (+8.43%)</td><td>5.43 (+18.66%)</td><td>4.43 (+15.42%)</td><td>0.72 <b>(-21.71%)</b></td><td>236.70 (-13.36%)</td><td>202.50 (-8.85%)</td><td>193.00 (-15.72%)</td><td>171.60 (+2.14%)</td><td>28.25 <b>(-28.80%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>6.24 (n/a)</td><td>4.85 (n/a)</td><td>4.58 (n/a)</td><td>3.84 (n/a)</td><td>0.92 (n/a)</td><td>273.20 (n/a)</td><td>222.16 (n/a)</td><td>229.00 (n/a)</td><td>168.00 (n/a)</td><td>39.68 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>9.12 (-5.55%)</td><td>8.33 (+6.15%)</td><td>8.29 (+10.35%)</td><td>7.71 (+6.62%)</td><td>0.60 <b>(-41.57%)</b></td><td>272.00 (-6.24%)</td><td>252.86 (-6.53%)</td><td>253.00 (-9.38%)</td><td>230.00 (+5.84%)</td><td>17.92 <b>(-40.91%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>9.65 (n/a)</td><td>7.84 (n/a)</td><td>7.51 (n/a)</td><td>7.23 (n/a)</td><td>1.02 (n/a)</td><td>290.10 (n/a)</td><td>270.52 (n/a)</td><td>279.20 (n/a)</td><td>217.30 (n/a)</td><td>30.33 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>9.12 (+5.45%)</td><td>7.95 (-2.06%)</td><td>7.65 (-6.79%)</td><td>7.06 (-5.59%)</td><td>0.89 <b>(+105.38%)</b></td><td>297.10 (+5.92%)</td><td>266.32 (+2.87%)</td><td>274.30 (+7.27%)</td><td>229.90 (-5.16%)</td><td>28.85 <b>(+104.40%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>8.65 (n/a)</td><td>8.12 (n/a)</td><td>8.20 (n/a)</td><td>7.48 (n/a)</td><td>0.43 (n/a)</td><td>280.50 (n/a)</td><td>258.88 (n/a)</td><td>255.70 (n/a)</td><td>242.40 (n/a)</td><td>14.12 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>8.22 (+1.90%)</td><td>7.55 (-1.88%)</td><td>7.60 (-0.29%)</td><td>6.36 (-15.36%)</td><td>0.75 <b>(+249.82%)</b></td><td>329.80 (+18.12%)</td><td>280.08 (+2.74%)</td><td>276.00 (+0.29%)</td><td>255.10 (-1.85%)</td><td>30.26 <b>(+307.07%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>8.07 (n/a)</td><td>7.70 (n/a)</td><td>7.62 (n/a)</td><td>7.51 (n/a)</td><td>0.22 (n/a)</td><td>279.20 (n/a)</td><td>272.62 (n/a)</td><td>275.20 (n/a)</td><td>259.90 (n/a)</td><td>7.43 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>9.76 (+10.71%)</td><td>8.50 (+12.65%)</td><td>8.19 (+3.95%)</td><td>7.32 (+18.14%)</td><td>1.06 (+0.12%)</td><td>286.60 (-15.36%)</td><td>249.86 (-11.59%)</td><td>256.20 (-3.79%)</td><td>214.80 (-9.67%)</td><td>30.66 <b>(-25.18%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>8.82 (n/a)</td><td>7.54 (n/a)</td><td>7.87 (n/a)</td><td>6.19 (n/a)</td><td>1.06 (n/a)</td><td>338.60 (n/a)</td><td>282.60 (n/a)</td><td>266.30 (n/a)</td><td>237.80 (n/a)</td><td>40.98 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>9.06 (-15.03%)</td><td>8.22 (-7.18%)</td><td>8.42 (-5.44%)</td><td>7.14 (+9.49%)</td><td>0.75 <b>(-52.77%)</b></td><td>293.60 (-8.65%)</td><td>256.94 (+5.42%)</td><td>249.20 (+5.77%)</td><td>231.40 (+17.64%)</td><td>24.53 <b>(-49.49%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>10.66 (n/a)</td><td>8.86 (n/a)</td><td>8.90 (n/a)</td><td>6.52 (n/a)</td><td>1.59 (n/a)</td><td>321.40 (n/a)</td><td>243.74 (n/a)</td><td>235.60 (n/a)</td><td>196.70 (n/a)</td><td>48.57 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>10.00 (+7.13%)</td><td>8.31 (+0.51%)</td><td>7.93 (-5.26%)</td><td>7.09 (+8.27%)</td><td>1.23 (+5.38%)</td><td>295.90 (-7.65%)</td><td>256.60 (-0.56%)</td><td>264.30 (+5.55%)</td><td>209.80 (-6.67%)</td><td>36.31 (-8.15%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>9.33 (n/a)</td><td>8.27 (n/a)</td><td>8.37 (n/a)</td><td>6.54 (n/a)</td><td>1.16 (n/a)</td><td>320.40 (n/a)</td><td>258.04 (n/a)</td><td>250.40 (n/a)</td><td>224.80 (n/a)</td><td>39.53 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>13.39 (-1.50%)</td><td>12.16 (+2.96%)</td><td>12.14 (+6.12%)</td><td>11.17 (+7.31%)</td><td>0.80 <b>(-36.13%)</b></td><td>375.50 (-6.82%)</td><td>346.22 (-3.38%)</td><td>345.60 (-5.75%)</td><td>313.30 (+1.52%)</td><td>22.17 <b>(-39.67%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>13.59 (n/a)</td><td>11.81 (n/a)</td><td>11.44 (n/a)</td><td>10.41 (n/a)</td><td>1.25 (n/a)</td><td>403.00 (n/a)</td><td>358.34 (n/a)</td><td>366.70 (n/a)</td><td>308.60 (n/a)</td><td>36.75 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>13.00 (-11.38%)</td><td>12.08 (-0.20%)</td><td>12.11 (+1.48%)</td><td>11.42 (+17.04%)</td><td>0.62 <b>(-65.76%)</b></td><td>367.20 (-14.56%)</td><td>347.98 (-1.38%)</td><td>346.40 (-1.45%)</td><td>322.60 (+12.88%)</td><td>17.47 <b>(-67.04%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>14.67 (n/a)</td><td>12.10 (n/a)</td><td>11.93 (n/a)</td><td>9.76 (n/a)</td><td>1.81 (n/a)</td><td>429.80 (n/a)</td><td>352.84 (n/a)</td><td>351.50 (n/a)</td><td>285.80 (n/a)</td><td>53.00 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>12.68 (-14.13%)</td><td>11.69 (-2.82%)</td><td>11.19 (-7.33%)</td><td>10.96 (+7.67%)</td><td>0.80 <b>(-53.64%)</b></td><td>382.60 (-7.11%)</td><td>360.00 (+1.69%)</td><td>374.70 (+7.92%)</td><td>330.80 (+16.48%)</td><td>24.10 <b>(-49.44%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>14.77 (n/a)</td><td>12.03 (n/a)</td><td>12.08 (n/a)</td><td>10.18 (n/a)</td><td>1.73 (n/a)</td><td>411.90 (n/a)</td><td>354.00 (n/a)</td><td>347.20 (n/a)</td><td>284.00 (n/a)</td><td>47.66 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>15.35 (-0.26%)</td><td>12.48 (-5.80%)</td><td>11.95 (-12.87%)</td><td>9.88 (-12.63%)</td><td>2.06 <b>(+20.80%)</b></td><td>424.50 (+14.45%)</td><td>343.56 (+7.04%)</td><td>351.10 (+14.78%)</td><td>273.20 (+0.26%)</td><td>56.71 <b>(+35.89%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>15.39 (n/a)</td><td>13.24 (n/a)</td><td>13.71 (n/a)</td><td>11.31 (n/a)</td><td>1.70 (n/a)</td><td>370.90 (n/a)</td><td>320.96 (n/a)</td><td>305.90 (n/a)</td><td>272.50 (n/a)</td><td>41.74 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>14.89 (+8.57%)</td><td>12.87 (+9.21%)</td><td>13.15 (+8.85%)</td><td>10.94 <b>(+21.31%)</b></td><td>1.47 <b>(-20.40%)</b></td><td>383.40 (-17.57%)</td><td>329.44 (-9.46%)</td><td>319.00 (-8.12%)</td><td>281.70 (-7.91%)</td><td>37.93 <b>(-39.87%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>13.71 (n/a)</td><td>11.78 (n/a)</td><td>12.08 (n/a)</td><td>9.02 (n/a)</td><td>1.84 (n/a)</td><td>465.10 (n/a)</td><td>363.86 (n/a)</td><td>347.20 (n/a)</td><td>305.90 (n/a)</td><td>63.08 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>15.06 (-0.53%)</td><td>12.91 (+0.47%)</td><td>12.58 (-1.84%)</td><td>11.43 (+2.74%)</td><td>1.37 (-6.45%)</td><td>367.00 (-2.65%)</td><td>327.72 (-0.61%)</td><td>333.30 (+1.86%)</td><td>278.50 (+0.54%)</td><td>32.86 (-8.46%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>15.14 (n/a)</td><td>12.85 (n/a)</td><td>12.82 (n/a)</td><td>11.13 (n/a)</td><td>1.46 (n/a)</td><td>377.00 (n/a)</td><td>329.72 (n/a)</td><td>327.20 (n/a)</td><td>277.00 (n/a)</td><td>35.89 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>15.22 (-1.77%)</td><td>14.38 (+12.42%)</td><td>14.44 (+14.13%)</td><td>13.55 <b>(+26.42%)</b></td><td>0.67 <b>(-64.32%)</b></td><td>309.40 <b>(-20.91%)</b></td><td>292.20 (-12.36%)</td><td>290.40 (-12.37%)</td><td>275.60 (+1.81%)</td><td>13.54 <b>(-71.28%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>15.49 (n/a)</td><td>12.79 (n/a)</td><td>12.65 (n/a)</td><td>10.72 (n/a)</td><td>1.87 (n/a)</td><td>391.20 (n/a)</td><td>333.40 (n/a)</td><td>331.40 (n/a)</td><td>270.70 (n/a)</td><td>47.16 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>12.86 (-5.19%)</td><td>12.49 (+0.53%)</td><td>12.76 (+2.16%)</td><td>11.74 (+2.42%)</td><td>0.48 <b>(-36.74%)</b></td><td>357.20 (-2.38%)</td><td>336.12 (-0.70%)</td><td>328.80 (-2.11%)</td><td>326.10 (+5.47%)</td><td>13.33 <b>(-34.84%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>13.57 (n/a)</td><td>12.43 (n/a)</td><td>12.49 (n/a)</td><td>11.46 (n/a)</td><td>0.76 (n/a)</td><td>365.90 (n/a)</td><td>338.50 (n/a)</td><td>335.90 (n/a)</td><td>309.20 (n/a)</td><td>20.45 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>2.84 (-14.90%)</td><td>2.43 (-14.10%)</td><td>2.40 (-10.84%)</td><td>2.15 (-10.38%)</td><td>0.29 <b>(-33.26%)</b></td><td>244.30 (+11.55%)</td><td>218.36 (+15.52%)</td><td>218.40 (+12.17%)</td><td>184.50 (+17.52%)</td><td>25.59 (-10.56%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>3.34 (n/a)</td><td>2.83 (n/a)</td><td>2.69 (n/a)</td><td>2.39 (n/a)</td><td>0.44 (n/a)</td><td>219.00 (n/a)</td><td>189.02 (n/a)</td><td>194.70 (n/a)</td><td>157.00 (n/a)</td><td>28.61 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>5.21 (-7.09%)</td><td>4.60 (-6.83%)</td><td>4.66 (-7.24%)</td><td>3.44 (-19.83%)</td><td>0.71 <b>(+41.12%)</b></td><td>304.80 <b>(+24.71%)</b></td><td>233.08 (+8.83%)</td><td>225.10 (+7.81%)</td><td>201.10 (+7.66%)</td><td>42.05 <b>(+91.09%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>5.61 (n/a)</td><td>4.94 (n/a)</td><td>5.02 (n/a)</td><td>4.29 (n/a)</td><td>0.50 (n/a)</td><td>244.40 (n/a)</td><td>214.16 (n/a)</td><td>208.80 (n/a)</td><td>186.80 (n/a)</td><td>22.00 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>7.99 (-9.50%)</td><td>7.87 (+4.20%)</td><td>7.88 (-1.78%)</td><td>7.76 <b>(+24.55%)</b></td><td>0.09 <b>(-91.52%)</b></td><td>270.10 (-19.71%)</td><td>266.40 (-5.69%)</td><td>266.30 (+1.80%)</td><td>262.60 (+10.48%)</td><td>3.15 <b>(-92.54%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>8.82 (n/a)</td><td>7.56 (n/a)</td><td>8.02 (n/a)</td><td>6.23 (n/a)</td><td>1.09 (n/a)</td><td>336.40 (n/a)</td><td>282.46 (n/a)</td><td>261.60 (n/a)</td><td>237.70 (n/a)</td><td>42.23 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>3.24 (-7.58%)</td><td>2.84 (+8.68%)</td><td>2.76 (+8.88%)</td><td>2.67 <b>(+32.01%)</b></td><td>0.23 <b>(-61.94%)</b></td><td>196.30 <b>(-24.27%)</b></td><td>185.38 (-11.25%)</td><td>189.90 (-8.17%)</td><td>161.70 (+8.16%)</td><td>13.84 <b>(-69.61%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>3.51 (n/a)</td><td>2.61 (n/a)</td><td>2.54 (n/a)</td><td>2.02 (n/a)</td><td>0.61 (n/a)</td><td>259.20 (n/a)</td><td>208.88 (n/a)</td><td>206.80 (n/a)</td><td>149.50 (n/a)</td><td>45.54 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.25 (+12.36%)</td><td>0.21 (+15.02%)</td><td>0.20 (+8.88%)</td><td>0.19 <b>(+78.35%)</b></td><td>0.02 <b>(-48.88%)</b></td><td>174.90 <b>(-43.92%)</b></td><td>158.78 (-18.43%)</td><td>162.80 (-8.18%)</td><td>131.70 (-11.01%)</td><td>16.56 <b>(-75.50%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>311.90 (n/a)</td><td>194.66 (n/a)</td><td>177.30 (n/a)</td><td>148.00 (n/a)</td><td>67.60 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.25 <b>(+26.87%)</b></td><td>0.21 (+12.86%)</td><td>0.21 (+14.64%)</td><td>0.15 (-13.92%)</td><td>0.04 <b>(+341.43%)</b></td><td>212.60 (+16.17%)</td><td>160.70 (-9.13%)</td><td>158.30 (-12.78%)</td><td>131.00 <b>(-21.18%)</b></td><td>31.37 <b>(+313.56%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>183.00 (n/a)</td><td>176.84 (n/a)</td><td>181.50 (n/a)</td><td>166.20 (n/a)</td><td>7.59 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.45 (+0.96%)</td><td>0.38 (-2.31%)</td><td>0.40 (+1.55%)</td><td>0.25 <b>(-24.03%)</b></td><td>0.08 <b>(+71.53%)</b></td><td>263.70 <b>(+31.65%)</b></td><td>179.90 (+5.84%)</td><td>165.10 (-1.55%)</td><td>146.00 (-0.95%)</td><td>48.03 <b>(+131.28%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.44 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.33 (n/a)</td><td>0.05 (n/a)</td><td>200.30 (n/a)</td><td>169.98 (n/a)</td><td>167.70 (n/a)</td><td>147.40 (n/a)</td><td>20.77 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.51 (-2.81%)</td><td>0.40 (+10.91%)</td><td>0.44 (+18.02%)</td><td>0.27 <b>(+21.22%)</b></td><td>0.11 (-1.21%)</td><td>243.10 (-17.51%)</td><td>175.62 (-10.87%)</td><td>148.70 (-15.27%)</td><td>129.30 (+2.86%)</td><td>52.77 (-16.94%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.52 (n/a)</td><td>0.36 (n/a)</td><td>0.37 (n/a)</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>294.70 (n/a)</td><td>197.04 (n/a)</td><td>175.50 (n/a)</td><td>125.70 (n/a)</td><td>63.53 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.56 <b>(+21.57%)</b></td><td>0.46 (+19.04%)</td><td>0.46 <b>(+24.42%)</b></td><td>0.38 (+19.19%)</td><td>0.07 (+8.31%)</td><td>174.70 (-16.09%)</td><td>143.62 (-16.32%)</td><td>142.90 (-19.63%)</td><td>116.40 (-17.80%)</td><td>21.92 <b>(-22.93%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.46 (n/a)</td><td>0.39 (n/a)</td><td>0.37 (n/a)</td><td>0.31 (n/a)</td><td>0.07 (n/a)</td><td>208.20 (n/a)</td><td>171.62 (n/a)</td><td>177.80 (n/a)</td><td>141.60 (n/a)</td><td>28.44 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>1.01 (+17.73%)</td><td>0.85 (+8.97%)</td><td>0.85 (+10.77%)</td><td>0.74 (+4.01%)</td><td>0.11 <b>(+63.52%)</b></td><td>178.10 (-3.83%)</td><td>157.00 (-7.55%)</td><td>155.00 (-9.73%)</td><td>129.30 (-15.05%)</td><td>20.01 <b>(+34.66%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.86 (n/a)</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.71 (n/a)</td><td>0.07 (n/a)</td><td>185.20 (n/a)</td><td>169.82 (n/a)</td><td>171.70 (n/a)</td><td>152.20 (n/a)</td><td>14.86 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>1.10 <b>(+31.18%)</b></td><td>0.86 (+15.92%)</td><td>0.98 <b>(+37.52%)</b></td><td>0.54 (-15.23%)</td><td>0.23 <b>(+192.54%)</b></td><td>243.10 (+18.01%)</td><td>164.42 (-8.25%)</td><td>133.70 <b>(-27.30%)</b></td><td>119.50 <b>(-23.74%)</b></td><td>52.11 <b>(+166.53%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.84 (n/a)</td><td>0.74 (n/a)</td><td>0.71 (n/a)</td><td>0.64 (n/a)</td><td>0.08 (n/a)</td><td>206.00 (n/a)</td><td>179.20 (n/a)</td><td>183.90 (n/a)</td><td>156.70 (n/a)</td><td>19.55 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>1.00 (+3.37%)</td><td>0.85 (+6.74%)</td><td>0.81 (+2.19%)</td><td>0.67 (+12.26%)</td><td>0.15 (+13.15%)</td><td>195.40 (-10.90%)</td><td>158.90 (-6.22%)</td><td>160.90 (-2.19%)</td><td>131.50 (-3.24%)</td><td>27.85 (-8.46%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.96 (n/a)</td><td>0.79 (n/a)</td><td>0.80 (n/a)</td><td>0.60 (n/a)</td><td>0.13 (n/a)</td><td>219.30 (n/a)</td><td>169.44 (n/a)</td><td>164.50 (n/a)</td><td>135.90 (n/a)</td><td>30.43 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>1.07 (+3.41%)</td><td>0.77 (+12.14%)</td><td>0.82 <b>(+29.40%)</b></td><td>0.54 (+5.78%)</td><td>0.22 (+6.67%)</td><td>240.60 (-5.46%)</td><td>182.16 (-10.10%)</td><td>159.80 <b>(-22.73%)</b></td><td>122.60 (-3.31%)</td><td>50.93 (+7.99%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>1.03 (n/a)</td><td>0.68 (n/a)</td><td>0.63 (n/a)</td><td>0.52 (n/a)</td><td>0.20 (n/a)</td><td>254.50 (n/a)</td><td>202.62 (n/a)</td><td>206.80 (n/a)</td><td>126.80 (n/a)</td><td>47.16 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.12 (-5.95%)</td><td>0.11 (+7.74%)</td><td>0.10 (+9.23%)</td><td>0.10 (+17.65%)</td><td>0.01 <b>(-45.71%)</b></td><td>169.90 (-15.01%)</td><td>153.68 (-8.44%)</td><td>156.90 (-8.46%)</td><td>138.90 (+6.36%)</td><td>12.36 <b>(-50.05%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:49</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>199.90 (n/a)</td><td>167.84 (n/a)</td><td>171.40 (n/a)</td><td>130.60 (n/a)</td><td>24.74 (n/a)</td>
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
