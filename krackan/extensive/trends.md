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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 <b>(-31.87%)</b></td><td>0.03 (-18.19%)</td><td>0.03 (-6.77%)</td><td>0.03 <b>(-25.61%)</b></td><td>0.00 <b>(-47.09%)</b></td><td>238.10 <b>(+34.44%)</b></td><td>195.72 <b>(+21.22%)</b></td><td>185.90 (+7.27%)</td><td>179.10 <b>(+46.80%)</b></td><td>24.54 (+6.35%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>177.10 (n/a)</td><td>161.46 (n/a)</td><td>173.30 (n/a)</td><td>122.00 (n/a)</td><td>23.08 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (-11.62%)</td><td>0.03 (-19.67%)</td><td>0.03 <b>(-22.45%)</b></td><td>0.03 (-17.79%)</td><td>0.01 (-5.12%)</td><td>239.40 <b>(+21.65%)</b></td><td>185.62 <b>(+25.11%)</b></td><td>187.40 <b>(+28.89%)</b></td><td>139.10 (+13.18%)</td><td>36.86 <b>(+27.42%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>196.80 (n/a)</td><td>148.36 (n/a)</td><td>145.40 (n/a)</td><td>122.90 (n/a)</td><td>28.92 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 <b>(-32.76%)</b></td><td>0.03 (-14.97%)</td><td>0.03 (-6.81%)</td><td>0.03 (-0.67%)</td><td>0.00 <b>(-69.71%)</b></td><td>213.60 (+0.71%)</td><td>186.82 (+12.99%)</td><td>185.90 (+7.33%)</td><td>165.80 <b>(+48.70%)</b></td><td>17.65 <b>(-53.06%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>212.10 (n/a)</td><td>165.34 (n/a)</td><td>173.20 (n/a)</td><td>111.50 (n/a)</td><td>37.60 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (+7.02%)</td><td>0.03 (-10.41%)</td><td>0.03 (-19.12%)</td><td>0.03 <b>(-24.65%)</b></td><td>0.01 <b>(+147.98%)</b></td><td>242.80 <b>(+32.75%)</b></td><td>188.06 (+15.52%)</td><td>196.30 <b>(+23.61%)</b></td><td>136.70 (-6.56%)</td><td>41.06 <b>(+202.17%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>182.90 (n/a)</td><td>162.80 (n/a)</td><td>158.80 (n/a)</td><td>146.30 (n/a)</td><td>13.59 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 <b>(-20.12%)</b></td><td>0.04 (+4.68%)</td><td>0.04 (+17.25%)</td><td>0.03 (+8.46%)</td><td>0.00 <b>(-52.89%)</b></td><td>203.60 (-7.83%)</td><td>173.20 (-7.64%)</td><td>173.00 (-14.69%)</td><td>151.40 <b>(+25.23%)</b></td><td>21.81 <b>(-44.03%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>220.90 (n/a)</td><td>187.52 (n/a)</td><td>202.80 (n/a)</td><td>120.90 (n/a)</td><td>38.97 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (+1.43%)</td><td>0.04 (-1.29%)</td><td>0.04 (+10.83%)</td><td>0.03 (-14.73%)</td><td>0.01 <b>(+36.34%)</b></td><td>229.40 (+17.28%)</td><td>175.78 (+3.12%)</td><td>161.70 (-9.82%)</td><td>135.60 (-1.38%)</td><td>36.60 <b>(+61.48%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>195.60 (n/a)</td><td>170.46 (n/a)</td><td>179.30 (n/a)</td><td>137.50 (n/a)</td><td>22.66 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 <b>(-22.81%)</b></td><td>0.03 (-17.99%)</td><td>0.03 <b>(-20.86%)</b></td><td>0.02 (-15.56%)</td><td>0.00 <b>(-41.93%)</b></td><td>248.10 (+18.42%)</td><td>198.86 <b>(+20.04%)</b></td><td>193.00 <b>(+26.31%)</b></td><td>172.30 <b>(+29.55%)</b></td><td>30.37 (-10.89%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>209.50 (n/a)</td><td>165.66 (n/a)</td><td>152.80 (n/a)</td><td>133.00 (n/a)</td><td>34.08 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (-6.66%)</td><td>0.03 (+1.12%)</td><td>0.03 (+9.17%)</td><td>0.03 (+10.13%)</td><td>0.00 <b>(-48.50%)</b></td><td>207.10 (-9.21%)</td><td>186.16 (-2.48%)</td><td>184.90 (-8.37%)</td><td>171.00 (+7.14%)</td><td>15.01 <b>(-48.77%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>228.10 (n/a)</td><td>190.90 (n/a)</td><td>201.80 (n/a)</td><td>159.60 (n/a)</td><td>29.29 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.07 <b>(-21.42%)</b></td><td>0.07 (-16.35%)</td><td>0.07 (-11.92%)</td><td>0.06 (-9.41%)</td><td>0.01 <b>(-24.18%)</b></td><td>210.70 (+10.43%)</td><td>183.78 (+19.18%)</td><td>167.60 (+13.55%)</td><td>166.10 <b>(+27.28%)</b></td><td>23.41 (+3.97%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>190.80 (n/a)</td><td>154.20 (n/a)</td><td>147.60 (n/a)</td><td>130.50 (n/a)</td><td>22.52 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.09 (+13.37%)</td><td>0.08 (+10.05%)</td><td>0.07 (+4.88%)</td><td>0.07 (+15.64%)</td><td>0.01 (+15.72%)</td><td>178.00 (-13.51%)</td><td>163.02 (-9.10%)</td><td>173.00 (-4.68%)</td><td>132.60 (-11.78%)</td><td>19.20 (-11.28%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>205.80 (n/a)</td><td>179.34 (n/a)</td><td>181.50 (n/a)</td><td>150.30 (n/a)</td><td>21.64 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.09 (+1.47%)</td><td>0.08 (+2.49%)</td><td>0.08 (+6.27%)</td><td>0.07 (-3.44%)</td><td>0.01 <b>(+35.17%)</b></td><td>185.30 (+3.58%)</td><td>159.20 (-1.59%)</td><td>160.70 (-5.91%)</td><td>134.20 (-1.47%)</td><td>24.34 <b>(+36.55%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>178.90 (n/a)</td><td>161.78 (n/a)</td><td>170.80 (n/a)</td><td>136.20 (n/a)</td><td>17.83 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.07 <b>(-24.68%)</b></td><td>0.07 (-12.95%)</td><td>0.07 (-12.53%)</td><td>0.07 (-0.70%)</td><td>0.00 <b>(-79.38%)</b></td><td>181.30 (+0.72%)</td><td>175.14 (+13.15%)</td><td>173.80 (+14.34%)</td><td>166.90 <b>(+32.78%)</b></td><td>5.95 <b>(-72.33%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>180.00 (n/a)</td><td>154.78 (n/a)</td><td>152.00 (n/a)</td><td>125.70 (n/a)</td><td>21.50 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.08 (-1.99%)</td><td>0.07 (-0.19%)</td><td>0.08 (+0.45%)</td><td>0.04 <b>(-26.03%)</b></td><td>0.02 <b>(+21.23%)</b></td><td>320.30 <b>(+35.20%)</b></td><td>196.48 (+3.87%)</td><td>163.40 (-0.49%)</td><td>158.90 (+1.99%)</td><td>69.73 <b>(+69.46%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>236.90 (n/a)</td><td>189.16 (n/a)</td><td>164.20 (n/a)</td><td>155.80 (n/a)</td><td>41.15 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.10 (+3.33%)</td><td>0.07 (+2.23%)</td><td>0.07 (+2.39%)</td><td>0.05 (-9.07%)</td><td>0.02 (+12.43%)</td><td>241.20 (+9.99%)</td><td>173.60 (-1.01%)</td><td>168.90 (-2.31%)</td><td>124.10 (-3.20%)</td><td>43.11 <b>(+21.47%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>219.30 (n/a)</td><td>175.38 (n/a)</td><td>172.90 (n/a)</td><td>128.20 (n/a)</td><td>35.49 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.08 (-4.19%)</td><td>0.07 (-0.57%)</td><td>0.07 (+2.25%)</td><td>0.05 (-0.96%)</td><td>0.01 <b>(-24.47%)</b></td><td>227.80 (+0.98%)</td><td>186.56 (-0.61%)</td><td>183.10 (-2.24%)</td><td>151.40 (+4.41%)</td><td>27.70 <b>(-21.39%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>225.60 (n/a)</td><td>187.70 (n/a)</td><td>187.30 (n/a)</td><td>145.00 (n/a)</td><td>35.24 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.09 (+3.38%)</td><td>0.07 (-0.32%)</td><td>0.07 (-9.31%)</td><td>0.06 (+17.68%)</td><td>0.01 (-9.73%)</td><td>209.10 (-15.00%)</td><td>177.68 (-0.88%)</td><td>178.00 (+10.22%)</td><td>137.40 (-3.24%)</td><td>31.11 <b>(-25.32%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>246.00 (n/a)</td><td>179.26 (n/a)</td><td>161.50 (n/a)</td><td>142.00 (n/a)</td><td>41.66 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.18 (+1.45%)</td><td>0.16 (+3.44%)</td><td>0.15 (-4.44%)</td><td>0.13 <b>(+24.80%)</b></td><td>0.02 <b>(-27.38%)</b></td><td>195.70 (-19.89%)</td><td>159.72 (-5.74%)</td><td>162.90 (+4.62%)</td><td>134.50 (-1.39%)</td><td>24.08 <b>(-44.71%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>244.30 (n/a)</td><td>169.44 (n/a)</td><td>155.70 (n/a)</td><td>136.40 (n/a)</td><td>43.55 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.19 (-1.73%)</td><td>0.14 (-12.62%)</td><td>0.14 (-11.39%)</td><td>0.06 <b>(-44.50%)</b></td><td>0.05 <b>(+32.23%)</b></td><td>390.80 <b>(+80.18%)</b></td><td>206.74 <b>(+26.43%)</b></td><td>171.00 (+12.87%)</td><td>129.00 (+1.82%)</td><td>105.10 <b>(+166.91%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>216.90 (n/a)</td><td>163.52 (n/a)</td><td>151.50 (n/a)</td><td>126.70 (n/a)</td><td>39.38 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.14 <b>(-32.98%)</b></td><td>0.13 <b>(-30.04%)</b></td><td>0.13 <b>(-30.39%)</b></td><td>0.12 (-14.45%)</td><td>0.01 <b>(-67.03%)</b></td><td>211.80 (+16.89%)</td><td>193.10 <b>(+39.64%)</b></td><td>187.90 <b>(+43.65%)</b></td><td>171.60 <b>(+49.22%)</b></td><td>16.21 <b>(-41.24%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>181.20 (n/a)</td><td>138.28 (n/a)</td><td>130.80 (n/a)</td><td>115.00 (n/a)</td><td>27.59 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.19 (-2.45%)</td><td>0.15 (-3.38%)</td><td>0.15 (-8.98%)</td><td>0.12 (+5.09%)</td><td>0.03 (-15.64%)</td><td>199.40 (-4.82%)</td><td>166.92 (+2.43%)</td><td>168.60 (+9.84%)</td><td>128.50 (+2.47%)</td><td>26.92 (-19.36%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>209.50 (n/a)</td><td>162.96 (n/a)</td><td>153.50 (n/a)</td><td>125.40 (n/a)</td><td>33.39 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.20 <b>(+24.03%)</b></td><td>0.16 (+11.15%)</td><td>0.15 (+6.02%)</td><td>0.11 (-3.05%)</td><td>0.04 <b>(+132.02%)</b></td><td>214.20 (+3.13%)</td><td>164.32 (-6.73%)</td><td>164.30 (-5.68%)</td><td>122.40 (-19.37%)</td><td>39.50 <b>(+87.95%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>207.70 (n/a)</td><td>176.18 (n/a)</td><td>174.20 (n/a)</td><td>151.80 (n/a)</td><td>21.02 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.21 <b>(+32.15%)</b></td><td>0.16 (+12.10%)</td><td>0.16 (+10.35%)</td><td>0.09 <b>(-22.96%)</b></td><td>0.05 <b>(+209.09%)</b></td><td>269.30 <b>(+29.78%)</b></td><td>172.38 (-3.92%)</td><td>156.10 (-9.40%)</td><td>118.30 <b>(-24.31%)</b></td><td>60.17 <b>(+204.65%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>207.50 (n/a)</td><td>179.42 (n/a)</td><td>172.30 (n/a)</td><td>156.30 (n/a)</td><td>19.75 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.19 <b>(+36.06%)</b></td><td>0.14 (+13.21%)</td><td>0.13 (+9.12%)</td><td>0.10 (-14.13%)</td><td>0.03 <b>(+271.06%)</b></td><td>254.40 (+16.48%)</td><td>185.50 (-7.46%)</td><td>183.00 (-8.36%)</td><td>131.10 <b>(-26.51%)</b></td><td>47.22 <b>(+219.98%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>218.40 (n/a)</td><td>200.46 (n/a)</td><td>199.70 (n/a)</td><td>178.40 (n/a)</td><td>14.76 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.16 (+10.47%)</td><td>0.14 <b>(+21.36%)</b></td><td>0.13 (+9.98%)</td><td>0.12 <b>(+62.59%)</b></td><td>0.02 <b>(-33.95%)</b></td><td>202.30 <b>(-38.47%)</b></td><td>182.06 <b>(-20.46%)</b></td><td>189.90 (-9.05%)</td><td>158.30 (-9.49%)</td><td>21.25 <b>(-64.65%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>328.80 (n/a)</td><td>228.88 (n/a)</td><td>208.80 (n/a)</td><td>174.90 (n/a)</td><td>60.10 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.34 (+15.65%)</td><td>0.30 (+11.35%)</td><td>0.32 (+11.50%)</td><td>0.21 (-3.66%)</td><td>0.05 <b>(+74.10%)</b></td><td>229.00 (+3.76%)</td><td>166.04 (-8.48%)</td><td>155.80 (-10.31%)</td><td>142.60 (-13.52%)</td><td>35.68 <b>(+57.90%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>220.70 (n/a)</td><td>181.42 (n/a)</td><td>173.70 (n/a)</td><td>164.90 (n/a)</td><td>22.60 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.37 (+10.64%)</td><td>0.27 (-7.86%)</td><td>0.26 (-9.27%)</td><td>0.18 <b>(-25.41%)</b></td><td>0.08 <b>(+114.06%)</b></td><td>266.90 <b>(+34.05%)</b></td><td>197.44 (+14.94%)</td><td>192.70 (+10.24%)</td><td>131.70 (-9.61%)</td><td>57.27 <b>(+163.36%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.34 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.04 (n/a)</td><td>199.10 (n/a)</td><td>171.78 (n/a)</td><td>174.80 (n/a)</td><td>145.70 (n/a)</td><td>21.75 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.36 (-9.16%)</td><td>0.31 (+1.40%)</td><td>0.34 <b>(+21.22%)</b></td><td>0.21 <b>(-21.73%)</b></td><td>0.06 <b>(+21.21%)</b></td><td>233.40 <b>(+27.75%)</b></td><td>166.36 (+0.79%)</td><td>143.50 (-17.48%)</td><td>136.00 (+10.12%)</td><td>41.25 <b>(+74.21%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.40 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.05 (n/a)</td><td>182.70 (n/a)</td><td>165.06 (n/a)</td><td>173.90 (n/a)</td><td>123.50 (n/a)</td><td>23.68 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.39 (+0.68%)</td><td>0.31 (+13.38%)</td><td>0.33 <b>(+31.83%)</b></td><td>0.21 (+9.43%)</td><td>0.07 (-10.35%)</td><td>232.30 (-8.62%)</td><td>164.02 (-12.93%)</td><td>148.20 <b>(-24.16%)</b></td><td>125.70 (-0.63%)</td><td>41.43 (-14.87%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.39 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.08 (n/a)</td><td>254.20 (n/a)</td><td>188.38 (n/a)</td><td>195.40 (n/a)</td><td>126.50 (n/a)</td><td>48.66 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.37 (+4.70%)</td><td>0.28 (-4.23%)</td><td>0.26 (-6.82%)</td><td>0.23 (-4.61%)</td><td>0.06 (+12.65%)</td><td>214.40 (+4.79%)</td><td>181.50 (+5.23%)</td><td>191.70 (+7.33%)</td><td>132.20 (-4.48%)</td><td>35.65 (+15.72%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.36 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>204.60 (n/a)</td><td>172.48 (n/a)</td><td>178.60 (n/a)</td><td>138.40 (n/a)</td><td>30.81 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.47 <b>(+20.43%)</b></td><td>0.31 (-7.96%)</td><td>0.26 <b>(-28.18%)</b></td><td>0.22 <b>(-20.37%)</b></td><td>0.11 <b>(+105.28%)</b></td><td>228.00 <b>(+25.55%)</b></td><td>176.64 (+16.64%)</td><td>192.20 <b>(+39.28%)</b></td><td>105.50 (-16.93%)</td><td>55.29 <b>(+115.84%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.39 (n/a)</td><td>0.33 (n/a)</td><td>0.36 (n/a)</td><td>0.27 (n/a)</td><td>0.05 (n/a)</td><td>181.60 (n/a)</td><td>151.44 (n/a)</td><td>138.00 (n/a)</td><td>127.00 (n/a)</td><td>25.62 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.44 <b>(+47.23%)</b></td><td>0.30 (+2.32%)</td><td>0.29 (-0.26%)</td><td>0.22 <b>(-22.35%)</b></td><td>0.09 <b>(+893.97%)</b></td><td>224.30 <b>(+28.76%)</b></td><td>175.36 (+4.10%)</td><td>166.70 (+0.30%)</td><td>110.50 <b>(-32.08%)</b></td><td>45.97 <b>(+766.63%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.01 (n/a)</td><td>174.20 (n/a)</td><td>168.46 (n/a)</td><td>166.20 (n/a)</td><td>162.70 (n/a)</td><td>5.30 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.37 <b>(+26.47%)</b></td><td>0.27 (+1.65%)</td><td>0.24 (-9.32%)</td><td>0.18 <b>(-21.24%)</b></td><td>0.08 <b>(+196.01%)</b></td><td>280.50 <b>(+26.98%)</b></td><td>196.20 (+4.36%)</td><td>203.10 (+10.32%)</td><td>132.70 <b>(-20.92%)</b></td><td>57.32 <b>(+187.81%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>220.90 (n/a)</td><td>188.00 (n/a)</td><td>184.10 (n/a)</td><td>167.80 (n/a)</td><td>19.92 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (-14.53%)</td><td>0.02 (-8.58%)</td><td>0.02 (+7.75%)</td><td>0.01 <b>(-52.82%)</b></td><td>0.01 <b>(+42.13%)</b></td><td>358.00 <b>(+111.96%)</b></td><td>185.70 <b>(+22.85%)</b></td><td>150.40 (-7.22%)</td><td>125.30 (+16.99%)</td><td>97.38 <b>(+281.59%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>168.90 (n/a)</td><td>151.16 (n/a)</td><td>162.10 (n/a)</td><td>107.10 (n/a)</td><td>25.52 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (-13.47%)</td><td>0.02 (-2.94%)</td><td>0.02 (-0.26%)</td><td>0.02 (+1.14%)</td><td>0.00 <b>(-48.70%)</b></td><td>171.90 (-1.15%)</td><td>148.92 (+1.43%)</td><td>144.00 (+0.28%)</td><td>136.00 (+15.55%)</td><td>14.09 <b>(-41.83%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>173.90 (n/a)</td><td>146.82 (n/a)</td><td>143.60 (n/a)</td><td>117.70 (n/a)</td><td>24.22 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (+10.87%)</td><td>0.02 (+10.29%)</td><td>0.02 (+7.40%)</td><td>0.01 (+8.64%)</td><td>0.00 <b>(+41.91%)</b></td><td>190.30 (-7.98%)</td><td>155.44 (-8.50%)</td><td>155.20 (-6.90%)</td><td>127.60 (-9.76%)</td><td>26.77 (+13.97%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>206.80 (n/a)</td><td>169.88 (n/a)</td><td>166.70 (n/a)</td><td>141.40 (n/a)</td><td>23.49 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (-11.65%)</td><td>0.02 (+0.10%)</td><td>0.02 (+7.37%)</td><td>0.01 (+11.51%)</td><td>0.00 <b>(-32.19%)</b></td><td>213.20 (-10.31%)</td><td>165.56 (-4.07%)</td><td>168.20 (-6.87%)</td><td>117.90 (+13.15%)</td><td>35.21 <b>(-30.50%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>237.70 (n/a)</td><td>172.58 (n/a)</td><td>180.60 (n/a)</td><td>104.20 (n/a)</td><td>50.65 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (-1.66%)</td><td>0.02 (+11.54%)</td><td>0.02 (+14.97%)</td><td>0.01 (+7.72%)</td><td>0.00 <b>(-24.08%)</b></td><td>200.30 (-7.18%)</td><td>165.58 (-11.85%)</td><td>167.60 (-13.03%)</td><td>128.70 (+1.66%)</td><td>26.06 <b>(-27.41%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>215.80 (n/a)</td><td>187.84 (n/a)</td><td>192.70 (n/a)</td><td>126.60 (n/a)</td><td>35.89 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 <b>(+28.91%)</b></td><td>0.02 <b>(+21.57%)</b></td><td>0.02 <b>(+23.01%)</b></td><td>0.01 (+3.37%)</td><td>0.00 <b>(+92.26%)</b></td><td>223.80 (-3.28%)</td><td>161.68 (-15.00%)</td><td>151.10 (-18.72%)</td><td>117.20 <b>(-22.44%)</b></td><td>42.17 <b>(+46.13%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>231.40 (n/a)</td><td>190.22 (n/a)</td><td>185.90 (n/a)</td><td>151.10 (n/a)</td><td>28.86 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 <b>(+42.40%)</b></td><td>0.02 <b>(+39.42%)</b></td><td>0.02 <b>(+45.12%)</b></td><td>0.02 <b>(+40.48%)</b></td><td>0.00 <b>(+29.86%)</b></td><td>165.60 <b>(-28.84%)</b></td><td>151.94 <b>(-28.34%)</b></td><td>150.30 <b>(-31.09%)</b></td><td>134.90 <b>(-29.78%)</b></td><td>12.19 <b>(-33.86%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>232.70 (n/a)</td><td>212.02 (n/a)</td><td>218.10 (n/a)</td><td>192.10 (n/a)</td><td>18.43 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (+3.70%)</td><td>0.01 (+1.84%)</td><td>0.01 (+3.86%)</td><td>0.01 (+3.79%)</td><td>0.00 (+6.30%)</td><td>223.40 (-3.67%)</td><td>206.96 (-1.77%)</td><td>211.30 (-3.69%)</td><td>172.60 (-3.58%)</td><td>20.07 (-1.81%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>231.90 (n/a)</td><td>210.68 (n/a)</td><td>219.40 (n/a)</td><td>179.00 (n/a)</td><td>20.44 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 <b>(+26.61%)</b></td><td>0.03 (+14.95%)</td><td>0.03 (+10.35%)</td><td>0.03 (+14.48%)</td><td>0.01 <b>(+44.82%)</b></td><td>206.80 (-12.67%)</td><td>160.80 (-12.18%)</td><td>157.20 (-9.39%)</td><td>119.50 <b>(-21.02%)</b></td><td>32.50 (-2.11%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>236.80 (n/a)</td><td>183.10 (n/a)</td><td>173.50 (n/a)</td><td>151.30 (n/a)</td><td>33.20 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (+10.09%)</td><td>0.03 (-10.69%)</td><td>0.03 (-9.22%)</td><td>0.02 <b>(-41.28%)</b></td><td>0.01 <b>(+95.60%)</b></td><td>338.30 <b>(+70.34%)</b></td><td>209.54 <b>(+21.30%)</b></td><td>201.20 (+10.19%)</td><td>128.60 (-9.18%)</td><td>78.08 <b>(+215.07%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>198.60 (n/a)</td><td>172.74 (n/a)</td><td>182.60 (n/a)</td><td>141.60 (n/a)</td><td>24.78 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (-9.04%)</td><td>0.03 (+14.96%)</td><td>0.03 <b>(+27.52%)</b></td><td>0.03 <b>(+57.01%)</b></td><td>0.00 <b>(-59.32%)</b></td><td>182.60 <b>(-36.33%)</b></td><td>161.08 (-18.25%)</td><td>157.60 <b>(-21.59%)</b></td><td>140.10 (+9.97%)</td><td>16.93 <b>(-71.34%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>286.80 (n/a)</td><td>197.04 (n/a)</td><td>201.00 (n/a)</td><td>127.40 (n/a)</td><td>59.07 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 <b>(-23.50%)</b></td><td>0.03 (-7.64%)</td><td>0.03 (-7.99%)</td><td>0.02 (+11.74%)</td><td>0.00 <b>(-47.56%)</b></td><td>217.80 (-10.48%)</td><td>171.42 (+3.73%)</td><td>159.80 (+8.63%)</td><td>149.10 <b>(+30.79%)</b></td><td>29.07 <b>(-40.85%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>243.30 (n/a)</td><td>165.26 (n/a)</td><td>147.10 (n/a)</td><td>114.00 (n/a)</td><td>49.14 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (+4.09%)</td><td>0.03 (-3.66%)</td><td>0.03 (-3.57%)</td><td>0.02 (-2.81%)</td><td>0.01 (+7.53%)</td><td>219.10 (+2.91%)</td><td>177.66 (+4.32%)</td><td>184.20 (+3.72%)</td><td>123.00 (-3.98%)</td><td>37.82 (+6.69%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>212.90 (n/a)</td><td>170.30 (n/a)</td><td>177.60 (n/a)</td><td>128.10 (n/a)</td><td>35.44 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 <b>(-32.43%)</b></td><td>0.03 (-19.93%)</td><td>0.03 (-7.73%)</td><td>0.02 (-5.35%)</td><td>0.00 <b>(-70.23%)</b></td><td>210.70 (+5.67%)</td><td>192.80 <b>(+20.44%)</b></td><td>191.10 (+8.39%)</td><td>169.30 <b>(+47.99%)</b></td><td>16.61 <b>(-52.65%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>199.40 (n/a)</td><td>160.08 (n/a)</td><td>176.30 (n/a)</td><td>114.40 (n/a)</td><td>35.09 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (-18.78%)</td><td>0.02 (-12.67%)</td><td>0.03 (-12.36%)</td><td>0.02 (-8.81%)</td><td>0.00 <b>(-40.88%)</b></td><td>234.90 (+9.66%)</td><td>212.14 (+13.65%)</td><td>207.10 (+14.10%)</td><td>187.30 <b>(+23.14%)</b></td><td>19.65 (-19.76%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.20 (n/a)</td><td>186.66 (n/a)</td><td>181.50 (n/a)</td><td>152.10 (n/a)</td><td>24.49 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (-4.60%)</td><td>0.02 (-5.74%)</td><td>0.02 (-10.04%)</td><td>0.02 (-3.84%)</td><td>0.00 (+7.54%)</td><td>242.60 (+3.99%)</td><td>225.58 (+6.20%)</td><td>233.60 (+11.19%)</td><td>207.30 (+4.86%)</td><td>16.48 (+15.57%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>233.30 (n/a)</td><td>212.42 (n/a)</td><td>210.10 (n/a)</td><td>197.70 (n/a)</td><td>14.26 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.08 (+5.60%)</td><td>0.06 (-4.81%)</td><td>0.06 (-6.60%)</td><td>0.05 (+2.68%)</td><td>0.01 (+2.12%)</td><td>232.00 (-2.60%)</td><td>179.64 (+4.87%)</td><td>168.70 (+7.04%)</td><td>129.50 (-5.27%)</td><td>38.86 (-6.04%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>238.20 (n/a)</td><td>171.30 (n/a)</td><td>157.60 (n/a)</td><td>136.70 (n/a)</td><td>41.36 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.08 (+16.49%)</td><td>0.06 (+9.72%)</td><td>0.06 (+5.22%)</td><td>0.04 (-17.66%)</td><td>0.02 <b>(+112.06%)</b></td><td>258.10 <b>(+21.46%)</b></td><td>175.62 (-4.15%)</td><td>178.60 (-4.95%)</td><td>126.90 (-14.14%)</td><td>52.41 <b>(+120.75%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>212.50 (n/a)</td><td>183.22 (n/a)</td><td>187.90 (n/a)</td><td>147.80 (n/a)</td><td>23.74 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.08 (+20.00%)</td><td>0.07 (+19.91%)</td><td>0.07 <b>(+23.00%)</b></td><td>0.06 (+16.76%)</td><td>0.01 <b>(+22.80%)</b></td><td>167.90 (-14.34%)</td><td>146.20 (-16.54%)</td><td>150.60 (-18.68%)</td><td>127.60 (-16.71%)</td><td>17.51 (-12.39%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>196.00 (n/a)</td><td>175.18 (n/a)</td><td>185.20 (n/a)</td><td>153.20 (n/a)</td><td>19.98 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.09 (-1.07%)</td><td>0.07 (+18.80%)</td><td>0.08 <b>(+35.94%)</b></td><td>0.05 (+17.18%)</td><td>0.02 (+1.19%)</td><td>195.30 (-14.64%)</td><td>154.14 (-15.98%)</td><td>134.60 <b>(-26.45%)</b></td><td>123.10 (+1.15%)</td><td>36.52 (-7.10%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>228.80 (n/a)</td><td>183.46 (n/a)</td><td>183.00 (n/a)</td><td>121.70 (n/a)</td><td>39.31 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.08 (+9.45%)</td><td>0.07 (+7.95%)</td><td>0.07 (+7.25%)</td><td>0.06 (-0.17%)</td><td>0.01 <b>(+62.05%)</b></td><td>185.10 (+0.22%)</td><td>152.14 (-5.96%)</td><td>149.40 (-6.74%)</td><td>125.40 (-8.67%)</td><td>27.64 <b>(+45.05%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>184.70 (n/a)</td><td>161.78 (n/a)</td><td>160.20 (n/a)</td><td>137.30 (n/a)</td><td>19.05 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.09 <b>(+32.89%)</b></td><td>0.07 <b>(+28.01%)</b></td><td>0.07 <b>(+26.75%)</b></td><td>0.06 <b>(+27.53%)</b></td><td>0.01 <b>(+47.31%)</b></td><td>164.50 <b>(-21.59%)</b></td><td>149.04 <b>(-21.71%)</b></td><td>155.80 <b>(-21.11%)</b></td><td>122.30 <b>(-24.74%)</b></td><td>16.62 (-14.13%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>209.80 (n/a)</td><td>190.36 (n/a)</td><td>197.50 (n/a)</td><td>162.50 (n/a)</td><td>19.36 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.08 <b>(+20.63%)</b></td><td>0.07 (+18.43%)</td><td>0.07 (+14.36%)</td><td>0.06 (+17.75%)</td><td>0.01 <b>(+55.02%)</b></td><td>166.40 (-15.10%)</td><td>152.72 (-15.43%)</td><td>157.40 (-12.60%)</td><td>137.90 (-17.13%)</td><td>11.53 (+8.34%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>196.00 (n/a)</td><td>180.58 (n/a)</td><td>180.10 (n/a)</td><td>166.40 (n/a)</td><td>10.64 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (+0.32%)</td><td>0.05 (-6.34%)</td><td>0.05 (-3.95%)</td><td>0.03 <b>(-26.95%)</b></td><td>0.01 <b>(+101.02%)</b></td><td>316.80 <b>(+36.91%)</b></td><td>219.42 (+10.94%)</td><td>207.40 (+4.12%)</td><td>175.10 (-0.28%)</td><td>58.16 <b>(+171.65%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>231.40 (n/a)</td><td>197.78 (n/a)</td><td>199.20 (n/a)</td><td>175.60 (n/a)</td><td>21.41 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.15 (-13.49%)</td><td>0.12 (+3.22%)</td><td>0.13 (+14.63%)</td><td>0.09 (+2.51%)</td><td>0.02 <b>(-23.69%)</b></td><td>223.20 (-2.45%)</td><td>174.06 (-4.35%)</td><td>164.60 (-12.77%)</td><td>144.60 (+15.59%)</td><td>33.36 (-12.39%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>228.80 (n/a)</td><td>181.98 (n/a)</td><td>188.70 (n/a)</td><td>125.10 (n/a)</td><td>38.07 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.14 (-4.43%)</td><td>0.12 (+11.23%)</td><td>0.12 (+0.70%)</td><td>0.12 <b>(+91.05%)</b></td><td>0.01 <b>(-73.74%)</b></td><td>182.10 <b>(-47.67%)</b></td><td>170.16 (-18.82%)</td><td>174.20 (-0.68%)</td><td>151.00 (+4.64%)</td><td>12.22 <b>(-85.58%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>348.00 (n/a)</td><td>209.62 (n/a)</td><td>175.40 (n/a)</td><td>144.30 (n/a)</td><td>84.71 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.15 (-14.17%)</td><td>0.11 (-10.32%)</td><td>0.11 (+2.25%)</td><td>0.07 <b>(-36.43%)</b></td><td>0.03 (+1.15%)</td><td>310.40 <b>(+57.32%)</b></td><td>205.70 (+14.84%)</td><td>188.30 (-2.23%)</td><td>143.70 (+16.55%)</td><td>62.21 <b>(+97.89%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>197.30 (n/a)</td><td>179.12 (n/a)</td><td>192.60 (n/a)</td><td>123.30 (n/a)</td><td>31.44 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.13 (-6.76%)</td><td>0.12 (-2.73%)</td><td>0.12 (+2.40%)</td><td>0.10 (-3.01%)</td><td>0.01 (-12.15%)</td><td>213.30 (+3.09%)</td><td>183.56 (+2.65%)</td><td>176.40 (-2.33%)</td><td>156.70 (+7.26%)</td><td>21.69 (-0.57%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>206.90 (n/a)</td><td>178.82 (n/a)</td><td>180.60 (n/a)</td><td>146.10 (n/a)</td><td>21.82 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.14 (-17.02%)</td><td>0.12 (-0.65%)</td><td>0.12 (+9.18%)</td><td>0.10 (+2.03%)</td><td>0.02 <b>(-47.29%)</b></td><td>215.10 (-2.00%)</td><td>175.94 (-2.14%)</td><td>170.40 (-8.39%)</td><td>148.80 <b>(+20.49%)</b></td><td>24.58 <b>(-36.45%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>219.50 (n/a)</td><td>179.78 (n/a)</td><td>186.00 (n/a)</td><td>123.50 (n/a)</td><td>38.68 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.16 (+2.25%)</td><td>0.12 (+10.84%)</td><td>0.11 (+13.44%)</td><td>0.09 (+14.16%)</td><td>0.03 (+1.34%)</td><td>227.20 (-12.38%)</td><td>185.34 (-9.92%)</td><td>184.90 (-11.83%)</td><td>134.00 (-2.19%)</td><td>41.58 (-6.06%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>259.30 (n/a)</td><td>205.74 (n/a)</td><td>209.70 (n/a)</td><td>137.00 (n/a)</td><td>44.26 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.15 (-15.72%)</td><td>0.11 (-6.76%)</td><td>0.11 (-6.22%)</td><td>0.08 (+5.31%)</td><td>0.03 <b>(-30.30%)</b></td><td>247.20 (-5.03%)</td><td>196.76 (+4.17%)</td><td>197.80 (+6.63%)</td><td>137.00 (+18.61%)</td><td>41.71 (-19.65%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>260.30 (n/a)</td><td>188.88 (n/a)</td><td>185.50 (n/a)</td><td>115.50 (n/a)</td><td>51.91 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (+5.34%)</td><td>0.10 (+2.43%)</td><td>0.10 (+1.98%)</td><td>0.09 (-6.83%)</td><td>0.01 <b>(+48.40%)</b></td><td>238.80 (+7.33%)</td><td>203.10 (-1.77%)</td><td>206.40 (-1.95%)</td><td>178.20 (-5.11%)</td><td>24.64 <b>(+48.87%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>222.50 (n/a)</td><td>206.76 (n/a)</td><td>210.50 (n/a)</td><td>187.80 (n/a)</td><td>16.55 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>203.40 (n/a)</td><td>166.10 (n/a)</td><td>170.20 (n/a)</td><td>120.80 (n/a)</td><td>33.25 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>195.30 (n/a)</td><td>158.68 (n/a)</td><td>163.20 (n/a)</td><td>117.80 (n/a)</td><td>28.32 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>215.50 (n/a)</td><td>182.80 (n/a)</td><td>194.90 (n/a)</td><td>127.10 (n/a)</td><td>33.52 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>212.40 (n/a)</td><td>180.72 (n/a)</td><td>198.60 (n/a)</td><td>125.70 (n/a)</td><td>35.76 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>209.30 (n/a)</td><td>174.90 (n/a)</td><td>172.50 (n/a)</td><td>148.50 (n/a)</td><td>26.07 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>183.10 (n/a)</td><td>163.80 (n/a)</td><td>154.60 (n/a)</td><td>148.10 (n/a)</td><td>16.46 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>210.60 (n/a)</td><td>147.84 (n/a)</td><td>133.90 (n/a)</td><td>119.70 (n/a)</td><td>36.60 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>239.10 (n/a)</td><td>201.42 (n/a)</td><td>216.20 (n/a)</td><td>164.10 (n/a)</td><td>34.19 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>185.30 (n/a)</td><td>148.44 (n/a)</td><td>133.70 (n/a)</td><td>117.70 (n/a)</td><td>30.12 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>221.50 (n/a)</td><td>147.08 (n/a)</td><td>131.10 (n/a)</td><td>123.80 (n/a)</td><td>41.73 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>203.40 (n/a)</td><td>179.50 (n/a)</td><td>188.70 (n/a)</td><td>141.30 (n/a)</td><td>25.61 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>217.70 (n/a)</td><td>194.92 (n/a)</td><td>196.60 (n/a)</td><td>169.00 (n/a)</td><td>21.19 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.40 (+11.96%)</td><td>0.31 (+0.63%)</td><td>0.31 (+3.87%)</td><td>0.21 (-16.23%)</td><td>0.08 <b>(+102.96%)</b></td><td>229.40 (+19.35%)</td><td>169.98 (+4.12%)</td><td>159.20 (-3.69%)</td><td>123.00 (-10.68%)</td><td>47.18 <b>(+117.19%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.36 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.04 (n/a)</td><td>192.20 (n/a)</td><td>163.26 (n/a)</td><td>165.30 (n/a)</td><td>137.70 (n/a)</td><td>21.72 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.34 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.04 (n/a)</td><td>206.30 (n/a)</td><td>175.74 (n/a)</td><td>178.00 (n/a)</td><td>142.80 (n/a)</td><td>23.03 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.02 (n/a)</td><td>211.00 (n/a)</td><td>193.86 (n/a)</td><td>201.10 (n/a)</td><td>177.00 (n/a)</td><td>15.50 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>228.10 (n/a)</td><td>204.42 (n/a)</td><td>220.60 (n/a)</td><td>154.50 (n/a)</td><td>30.15 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>198.20 (n/a)</td><td>163.44 (n/a)</td><td>155.70 (n/a)</td><td>145.10 (n/a)</td><td>20.44 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>185.10 (n/a)</td><td>159.36 (n/a)</td><td>169.50 (n/a)</td><td>124.60 (n/a)</td><td>26.88 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>186.90 (n/a)</td><td>157.90 (n/a)</td><td>151.20 (n/a)</td><td>133.20 (n/a)</td><td>22.64 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.80 (n/a)</td><td>167.80 (n/a)</td><td>161.80 (n/a)</td><td>134.90 (n/a)</td><td>40.60 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>219.00 (n/a)</td><td>185.86 (n/a)</td><td>194.00 (n/a)</td><td>154.60 (n/a)</td><td>25.51 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>271.30 (n/a)</td><td>200.74 (n/a)</td><td>202.80 (n/a)</td><td>123.80 (n/a)</td><td>59.70 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>230.70 (n/a)</td><td>166.54 (n/a)</td><td>154.50 (n/a)</td><td>127.50 (n/a)</td><td>41.51 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>209.10 (n/a)</td><td>163.66 (n/a)</td><td>154.80 (n/a)</td><td>142.00 (n/a)</td><td>26.13 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>143.60 (n/a)</td><td>137.00 (n/a)</td><td>139.90 (n/a)</td><td>124.40 (n/a)</td><td>7.80 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>204.10 (n/a)</td><td>161.46 (n/a)</td><td>166.00 (n/a)</td><td>126.50 (n/a)</td><td>33.55 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>188.00 (n/a)</td><td>159.60 (n/a)</td><td>172.20 (n/a)</td><td>128.30 (n/a)</td><td>26.59 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>235.20 (n/a)</td><td>188.18 (n/a)</td><td>175.00 (n/a)</td><td>154.00 (n/a)</td><td>31.87 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.04 (n/a)</td><td>196.60 (n/a)</td><td>176.50 (n/a)</td><td>188.20 (n/a)</td><td>147.90 (n/a)</td><td>22.96 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.38 (n/a)</td><td>0.35 (n/a)</td><td>0.35 (n/a)</td><td>0.31 (n/a)</td><td>0.03 (n/a)</td><td>158.20 (n/a)</td><td>143.04 (n/a)</td><td>139.00 (n/a)</td><td>127.80 (n/a)</td><td>11.95 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.42 (n/a)</td><td>0.31 (n/a)</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.07 (n/a)</td><td>206.80 (n/a)</td><td>163.38 (n/a)</td><td>155.60 (n/a)</td><td>118.20 (n/a)</td><td>37.59 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>214.60 (n/a)</td><td>164.04 (n/a)</td><td>175.80 (n/a)</td><td>123.70 (n/a)</td><td>37.88 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>171.70 (n/a)</td><td>134.78 (n/a)</td><td>122.10 (n/a)</td><td>118.00 (n/a)</td><td>23.23 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>220.60 (n/a)</td><td>171.82 (n/a)</td><td>159.10 (n/a)</td><td>145.50 (n/a)</td><td>31.05 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>174.50 (n/a)</td><td>146.60 (n/a)</td><td>144.50 (n/a)</td><td>123.20 (n/a)</td><td>21.86 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>197.80 (n/a)</td><td>169.24 (n/a)</td><td>170.80 (n/a)</td><td>123.10 (n/a)</td><td>29.34 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.70 (n/a)</td><td>181.48 (n/a)</td><td>182.50 (n/a)</td><td>156.80 (n/a)</td><td>18.83 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.80 (n/a)</td><td>161.90 (n/a)</td><td>159.40 (n/a)</td><td>128.60 (n/a)</td><td>29.91 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.10 (n/a)</td><td>199.74 (n/a)</td><td>197.70 (n/a)</td><td>170.80 (n/a)</td><td>19.49 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.70 (n/a)</td><td>161.60 (n/a)</td><td>149.70 (n/a)</td><td>120.30 (n/a)</td><td>33.72 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>181.70 (n/a)</td><td>161.28 (n/a)</td><td>162.30 (n/a)</td><td>132.10 (n/a)</td><td>18.19 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>272.20 (n/a)</td><td>183.38 (n/a)</td><td>179.80 (n/a)</td><td>117.40 (n/a)</td><td>55.95 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.30 (n/a)</td><td>162.60 (n/a)</td><td>165.60 (n/a)</td><td>124.00 (n/a)</td><td>27.79 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.10 (n/a)</td><td>182.66 (n/a)</td><td>191.40 (n/a)</td><td>129.40 (n/a)</td><td>41.13 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>260.90 (n/a)</td><td>187.62 (n/a)</td><td>189.20 (n/a)</td><td>143.20 (n/a)</td><td>47.94 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.00 (n/a)</td><td>187.42 (n/a)</td><td>197.80 (n/a)</td><td>157.10 (n/a)</td><td>26.81 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.70 (n/a)</td><td>213.08 (n/a)</td><td>224.40 (n/a)</td><td>163.60 (n/a)</td><td>27.87 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>205.80 (n/a)</td><td>167.48 (n/a)</td><td>168.50 (n/a)</td><td>133.30 (n/a)</td><td>27.11 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>192.70 (n/a)</td><td>173.18 (n/a)</td><td>172.50 (n/a)</td><td>153.40 (n/a)</td><td>16.02 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>191.50 (n/a)</td><td>181.34 (n/a)</td><td>185.20 (n/a)</td><td>166.30 (n/a)</td><td>9.90 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>214.10 (n/a)</td><td>179.76 (n/a)</td><td>192.10 (n/a)</td><td>136.40 (n/a)</td><td>32.91 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>256.00 (n/a)</td><td>186.32 (n/a)</td><td>185.90 (n/a)</td><td>132.40 (n/a)</td><td>45.58 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>224.60 (n/a)</td><td>177.36 (n/a)</td><td>163.60 (n/a)</td><td>154.30 (n/a)</td><td>28.24 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>209.70 (n/a)</td><td>163.34 (n/a)</td><td>165.50 (n/a)</td><td>106.10 (n/a)</td><td>37.95 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>284.80 (n/a)</td><td>225.92 (n/a)</td><td>212.60 (n/a)</td><td>196.00 (n/a)</td><td>35.58 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>166.90 (n/a)</td><td>145.20 (n/a)</td><td>141.40 (n/a)</td><td>126.00 (n/a)</td><td>19.55 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>220.40 (n/a)</td><td>174.78 (n/a)</td><td>157.40 (n/a)</td><td>132.80 (n/a)</td><td>42.42 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>241.80 (n/a)</td><td>167.58 (n/a)</td><td>141.70 (n/a)</td><td>133.40 (n/a)</td><td>45.63 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>229.40 (n/a)</td><td>167.02 (n/a)</td><td>148.80 (n/a)</td><td>120.10 (n/a)</td><td>45.83 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>226.20 (n/a)</td><td>177.00 (n/a)</td><td>187.20 (n/a)</td><td>118.20 (n/a)</td><td>41.10 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>215.10 (n/a)</td><td>192.52 (n/a)</td><td>190.40 (n/a)</td><td>172.40 (n/a)</td><td>19.68 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>211.00 (n/a)</td><td>183.88 (n/a)</td><td>172.20 (n/a)</td><td>165.80 (n/a)</td><td>19.79 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>333.40 (n/a)</td><td>227.92 (n/a)</td><td>202.50 (n/a)</td><td>161.40 (n/a)</td><td>72.56 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>4.34 (-2.02%)</td><td>4.08 (+2.72%)</td><td>4.18 (+3.31%)</td><td>3.52 (-2.10%)</td><td>0.32 (-12.68%)</td><td>2668.20 (+2.15%)</td><td>2315.36 (-2.78%)</td><td>2251.30 (-3.20%)</td><td>2166.00 (+2.06%)</td><td>200.71 (-9.07%)</td><td>1707.97 (-2.02%)</td><td>1606.49 (+2.72%)</td><td>1643.18 (+3.31%)</td><td>1386.49 (-2.10%)</td><td>126.16 (-12.68%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>4.43 (n/a)</td><td>3.98 (n/a)</td><td>4.04 (n/a)</td><td>3.60 (n/a)</td><td>0.37 (n/a)</td><td>2612.10 (n/a)</td><td>2381.68 (n/a)</td><td>2325.80 (n/a)</td><td>2122.20 (n/a)</td><td>220.74 (n/a)</td><td>1743.20 (n/a)</td><td>1563.97 (n/a)</td><td>1590.59 (n/a)</td><td>1416.25 (n/a)</td><td>144.49 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>1.34 (+3.64%)</td><td>0.96 (+12.10%)</td><td>0.92 (+14.00%)</td><td>0.71 (+9.01%)</td><td>0.27 (+2.07%)</td><td>313.30 (-8.28%)</td><td>245.18 (-11.05%)</td><td>239.60 (-12.27%)</td><td>164.50 (-3.52%)</td><td>65.68 (-7.15%)</td><td>57.36 (+3.64%)</td><td>40.93 (+12.10%)</td><td>39.39 (+14.00%)</td><td>30.12 (+9.01%)</td><td>11.57 (+2.07%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>1.30 (n/a)</td><td>0.86 (n/a)</td><td>0.81 (n/a)</td><td>0.65 (n/a)</td><td>0.27 (n/a)</td><td>341.60 (n/a)</td><td>275.64 (n/a)</td><td>273.10 (n/a)</td><td>170.50 (n/a)</td><td>70.74 (n/a)</td><td>55.35 (n/a)</td><td>36.51 (n/a)</td><td>34.55 (n/a)</td><td>27.63 (n/a)</td><td>11.34 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>1.23 (+16.66%)</td><td>0.98 (-0.23%)</td><td>0.95 (-3.13%)</td><td>0.67 <b>(-21.17%)</b></td><td>0.25 <b>(+206.51%)</b></td><td>330.00 <b>(+26.87%)</b></td><td>238.66 (+5.27%)</td><td>232.70 (+3.24%)</td><td>179.70 (-14.27%)</td><td>63.76 <b>(+217.38%)</b></td><td>52.52 (+16.66%)</td><td>41.78 (-0.23%)</td><td>40.55 (-3.13%)</td><td>28.60 <b>(-21.17%)</b></td><td>10.60 <b>(+206.51%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>1.06 (n/a)</td><td>0.98 (n/a)</td><td>0.98 (n/a)</td><td>0.85 (n/a)</td><td>0.08 (n/a)</td><td>260.10 (n/a)</td><td>226.72 (n/a)</td><td>225.40 (n/a)</td><td>209.60 (n/a)</td><td>20.09 (n/a)</td><td>45.02 (n/a)</td><td>41.87 (n/a)</td><td>41.86 (n/a)</td><td>36.28 (n/a)</td><td>3.46 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.52 (-0.02%)</td><td>0.52 (+0.07%)</td><td>0.52 (+0.01%)</td><td>0.52 (+0.27%)</td><td>0.00 <b>(-62.48%)</b></td><td>48502.80 (-0.27%)</td><td>48469.48 (-0.07%)</td><td>48482.90 (-0.01%)</td><td>48430.00 (+0.02%)</td><td>29.63 <b>(-62.57%)</b></td><td>354.74 (-0.02%)</td><td>354.45 (+0.07%)</td><td>354.35 (+0.01%)</td><td>354.20 (+0.27%)</td><td>0.22 <b>(-62.48%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48635.70 (n/a)</td><td>48503.20 (n/a)</td><td>48486.80 (n/a)</td><td>48422.10 (n/a)</td><td>79.17 (n/a)</td><td>354.79 (n/a)</td><td>354.20 (n/a)</td><td>354.32 (n/a)</td><td>353.24 (n/a)</td><td>0.58 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.21 (-0.71%)</td><td>0.21 (-0.32%)</td><td>0.21 (+0.10%)</td><td>0.21 (-1.23%)</td><td>0.00 <b>(+41.96%)</b></td><td>120542.50 (+1.24%)</td><td>118808.90 (+0.33%)</td><td>118484.50 (-0.10%)</td><td>118117.30 (+0.71%)</td><td>999.90 <b>(+45.01%)</b></td><td>145.45 (-0.71%)</td><td>144.61 (-0.32%)</td><td>145.00 (+0.10%)</td><td>142.52 (-1.23%)</td><td>1.21 <b>(+41.95%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>119063.00 (n/a)</td><td>118423.08 (n/a)</td><td>118604.60 (n/a)</td><td>117281.00 (n/a)</td><td>689.55 (n/a)</td><td>146.48 (n/a)</td><td>145.08 (n/a)</td><td>144.85 (n/a)</td><td>144.29 (n/a)</td><td>0.85 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.89 (-1.07%)</td><td>0.89 (-0.66%)</td><td>0.89 (-0.69%)</td><td>0.88 (+0.32%)</td><td>0.01 <b>(-43.25%)</b></td><td>28661.60 (-0.32%)</td><td>28360.88 (+0.66%)</td><td>28327.10 (+0.69%)</td><td>28184.60 (+1.08%)</td><td>194.88 <b>(-42.95%)</b></td><td>609.55 (-1.07%)</td><td>605.78 (-0.66%)</td><td>606.48 (-0.69%)</td><td>599.40 (+0.32%)</td><td>4.15 <b>(-43.25%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28754.00 (n/a)</td><td>28175.68 (n/a)</td><td>28132.30 (n/a)</td><td>27884.00 (n/a)</td><td>341.57 (n/a)</td><td>616.12 (n/a)</td><td>609.81 (n/a)</td><td>610.68 (n/a)</td><td>597.48 (n/a)</td><td>7.31 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>3.63 (+1.67%)</td><td>3.48 (+1.20%)</td><td>3.52 (+3.02%)</td><td>3.34 (-0.30%)</td><td>0.13 <b>(+40.74%)</b></td><td>7544.30 (+0.30%)</td><td>7242.62 (-1.13%)</td><td>7146.70 (-2.93%)</td><td>6932.70 (-1.64%)</td><td>276.76 <b>(+39.67%)</b></td><td>2478.09 (+1.67%)</td><td>2374.81 (+1.20%)</td><td>2403.87 (+3.02%)</td><td>2277.19 (-0.30%)</td><td>90.25 <b>(+40.74%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>3.57 (n/a)</td><td>3.44 (n/a)</td><td>3.42 (n/a)</td><td>3.35 (n/a)</td><td>0.09 (n/a)</td><td>7521.80 (n/a)</td><td>7325.30 (n/a)</td><td>7362.30 (n/a)</td><td>7048.30 (n/a)</td><td>198.15 (n/a)</td><td>2437.45 (n/a)</td><td>2346.66 (n/a)</td><td>2333.50 (n/a)</td><td>2284.00 (n/a)</td><td>64.13 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>2.89 (+1.93%)</td><td>2.82 (+1.07%)</td><td>2.82 (+0.30%)</td><td>2.73 (-0.29%)</td><td>0.06 <b>(+42.46%)</b></td><td>9232.30 (+0.29%)</td><td>8920.56 (-1.04%)</td><td>8932.40 (-0.29%)</td><td>8697.30 (-1.89%)</td><td>206.44 <b>(+40.20%)</b></td><td>1975.32 (+1.93%)</td><td>1926.69 (+1.07%)</td><td>1923.33 (+0.30%)</td><td>1860.84 (-0.29%)</td><td>44.15 <b>(+42.46%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>2.84 (n/a)</td><td>2.79 (n/a)</td><td>2.81 (n/a)</td><td>2.73 (n/a)</td><td>0.05 (n/a)</td><td>9205.80 (n/a)</td><td>9014.08 (n/a)</td><td>8958.80 (n/a)</td><td>8864.80 (n/a)</td><td>147.25 (n/a)</td><td>1938.00 (n/a)</td><td>1906.30 (n/a)</td><td>1917.65 (n/a)</td><td>1866.20 (n/a)</td><td>30.99 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>3.34 (+0.10%)</td><td>3.25 (+1.01%)</td><td>3.26 (+1.82%)</td><td>3.16 (+2.80%)</td><td>0.08 <b>(-22.41%)</b></td><td>7962.70 (-2.72%)</td><td>7747.12 (-1.03%)</td><td>7709.00 (-1.78%)</td><td>7542.80 (-0.10%)</td><td>194.59 <b>(-24.26%)</b></td><td>2277.64 (+0.10%)</td><td>2218.69 (+1.01%)</td><td>2228.55 (+1.82%)</td><td>2157.53 (+2.80%)</td><td>55.55 <b>(-22.41%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>3.33 (n/a)</td><td>3.22 (n/a)</td><td>3.21 (n/a)</td><td>3.07 (n/a)</td><td>0.10 (n/a)</td><td>8185.40 (n/a)</td><td>7828.12 (n/a)</td><td>7849.10 (n/a)</td><td>7550.60 (n/a)</td><td>256.91 (n/a)</td><td>2275.31 (n/a)</td><td>2196.51 (n/a)</td><td>2188.77 (n/a)</td><td>2098.84 (n/a)</td><td>71.60 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.79 (+0.26%)</td><td>0.79 (+0.09%)</td><td>0.79 (+0.03%)</td><td>0.79 (+0.13%)</td><td>0.00 <b>(+56.82%)</b></td><td>96163.80 (-0.13%)</td><td>96067.28 (-0.09%)</td><td>96102.00 (-0.03%)</td><td>95854.20 (-0.26%)</td><td>121.94 <b>(+56.20%)</b></td><td>716.92 (+0.26%)</td><td>715.33 (+0.09%)</td><td>715.07 (+0.03%)</td><td>714.61 (+0.13%)</td><td>0.91 <b>(+56.82%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.00 (n/a)</td><td>96293.50 (n/a)</td><td>96155.28 (n/a)</td><td>96126.60 (n/a)</td><td>96107.60 (n/a)</td><td>78.06 (n/a)</td><td>715.03 (n/a)</td><td>714.67 (n/a)</td><td>714.89 (n/a)</td><td>713.65 (n/a)</td><td>0.58 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.73 (-0.01%)</td><td>0.73 (-0.02%)</td><td>0.73 (-0.01%)</td><td>0.73 (-0.10%)</td><td>0.00 <b>(+79.41%)</b></td><td>103542.70 (+0.10%)</td><td>103366.20 (+0.02%)</td><td>103331.60 (+0.01%)</td><td>103303.50 (+0.01%)</td><td>100.16 <b>(+79.54%)</b></td><td>665.22 (-0.01%)</td><td>664.82 (-0.02%)</td><td>665.04 (-0.01%)</td><td>663.68 (-0.10%)</td><td>0.64 <b>(+79.41%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103435.30 (n/a)</td><td>103340.78 (n/a)</td><td>103316.50 (n/a)</td><td>103295.30 (n/a)</td><td>55.79 (n/a)</td><td>665.27 (n/a)</td><td>664.98 (n/a)</td><td>665.14 (n/a)</td><td>664.37 (n/a)</td><td>0.36 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.70 (+0.13%)</td><td>0.69 (+0.13%)</td><td>0.69 (+0.20%)</td><td>0.69 (+0.21%)</td><td>0.00 <b>(-25.09%)</b></td><td>108917.00 (-0.21%)</td><td>108757.52 (-0.13%)</td><td>108760.20 (-0.20%)</td><td>108541.80 (-0.12%)</td><td>154.04 <b>(-25.30%)</b></td><td>633.12 (+0.12%)</td><td>631.86 (+0.13%)</td><td>631.84 (+0.20%)</td><td>630.93 (+0.21%)</td><td>0.90 <b>(-25.09%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.69 (n/a)</td><td>0.00 (n/a)</td><td>109147.40 (n/a)</td><td>108899.30 (n/a)</td><td>108975.90 (n/a)</td><td>108677.50 (n/a)</td><td>206.23 (n/a)</td><td>632.33 (n/a)</td><td>631.04 (n/a)</td><td>630.59 (n/a)</td><td>629.60 (n/a)</td><td>1.20 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>7.58 (-2.65%)</td><td>7.09 (+1.13%)</td><td>7.03 (+2.97%)</td><td>6.56 (+1.39%)</td><td>0.38 <b>(-33.20%)</b></td><td>1358.80 (-1.37%)</td><td>1260.70 (-1.39%)</td><td>1267.50 (-2.89%)</td><td>1175.50 (+2.72%)</td><td>67.55 <b>(-32.40%)</b></td><td>456.72 (-2.65%)</td><td>426.82 (+1.13%)</td><td>423.55 (+2.97%)</td><td>395.11 (+1.39%)</td><td>22.67 <b>(-33.20%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>7.79 (n/a)</td><td>7.01 (n/a)</td><td>6.83 (n/a)</td><td>6.47 (n/a)</td><td>0.56 (n/a)</td><td>1377.70 (n/a)</td><td>1278.46 (n/a)</td><td>1305.20 (n/a)</td><td>1144.40 (n/a)</td><td>99.92 (n/a)</td><td>469.13 (n/a)</td><td>422.05 (n/a)</td><td>411.32 (n/a)</td><td>389.68 (n/a)</td><td>33.94 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>6.83 (-3.48%)</td><td>6.66 (-1.38%)</td><td>6.69 (-2.84%)</td><td>6.38 (+0.26%)</td><td>0.17 <b>(-40.09%)</b></td><td>1396.30 (-0.26%)</td><td>1338.46 (+1.31%)</td><td>1332.20 (+2.92%)</td><td>1304.90 (+3.60%)</td><td>35.09 <b>(-37.99%)</b></td><td>411.41 (-3.48%)</td><td>401.32 (-1.38%)</td><td>402.98 (-2.84%)</td><td>384.50 (+0.26%)</td><td>10.29 <b>(-40.08%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>7.08 (n/a)</td><td>6.76 (n/a)</td><td>6.89 (n/a)</td><td>6.37 (n/a)</td><td>0.29 (n/a)</td><td>1399.90 (n/a)</td><td>1321.16 (n/a)</td><td>1294.40 (n/a)</td><td>1259.50 (n/a)</td><td>56.60 (n/a)</td><td>426.26 (n/a)</td><td>406.95 (n/a)</td><td>414.77 (n/a)</td><td>383.51 (n/a)</td><td>17.18 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>7.04 (+5.31%)</td><td>6.21 (+2.54%)</td><td>6.04 (-2.65%)</td><td>5.24 (+10.68%)</td><td>0.74 (-4.48%)</td><td>1700.90 (-9.65%)</td><td>1451.76 (-2.84%)</td><td>1474.80 (+2.72%)</td><td>1266.00 (-5.05%)</td><td>176.24 <b>(-20.85%)</b></td><td>424.07 (+5.31%)</td><td>374.11 (+2.54%)</td><td>364.02 (-2.65%)</td><td>315.64 (+10.68%)</td><td>44.50 (-4.48%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>6.69 (n/a)</td><td>6.06 (n/a)</td><td>6.21 (n/a)</td><td>4.73 (n/a)</td><td>0.77 (n/a)</td><td>1882.50 (n/a)</td><td>1494.16 (n/a)</td><td>1435.70 (n/a)</td><td>1333.30 (n/a)</td><td>222.66 (n/a)</td><td>402.67 (n/a)</td><td>364.85 (n/a)</td><td>373.94 (n/a)</td><td>285.19 (n/a)</td><td>46.59 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>8.11 (+0.23%)</td><td>7.82 (-1.66%)</td><td>7.92 (-1.05%)</td><td>7.36 (-5.20%)</td><td>0.29 <b>(+119.90%)</b></td><td>4736.30 (+5.49%)</td><td>4464.74 (+1.79%)</td><td>4403.00 (+1.06%)</td><td>4301.10 (-0.23%)</td><td>172.62 <b>(+131.93%)</b></td><td>499.29 (+0.23%)</td><td>481.55 (-1.66%)</td><td>487.73 (-1.05%)</td><td>453.41 (-5.20%)</td><td>18.15 <b>(+119.90%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>8.09 (n/a)</td><td>7.95 (n/a)</td><td>8.00 (n/a)</td><td>7.77 (n/a)</td><td>0.13 (n/a)</td><td>4490.00 (n/a)</td><td>4386.42 (n/a)</td><td>4357.00 (n/a)</td><td>4310.90 (n/a)</td><td>74.43 (n/a)</td><td>498.15 (n/a)</td><td>489.69 (n/a)</td><td>492.89 (n/a)</td><td>478.28 (n/a)</td><td>8.25 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>7.55 (-0.02%)</td><td>7.39 (+0.22%)</td><td>7.53 (+0.02%)</td><td>7.12 (+0.29%)</td><td>0.22 (-7.96%)</td><td>4899.90 (-0.29%)</td><td>4722.68 (-0.23%)</td><td>4629.20 (-0.02%)</td><td>4615.30 (+0.02%)</td><td>141.58 (-8.40%)</td><td>465.30 (-0.02%)</td><td>455.04 (+0.22%)</td><td>463.90 (+0.02%)</td><td>438.27 (+0.29%)</td><td>13.48 (-7.96%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>7.56 (n/a)</td><td>7.37 (n/a)</td><td>7.53 (n/a)</td><td>7.09 (n/a)</td><td>0.24 (n/a)</td><td>4914.30 (n/a)</td><td>4733.46 (n/a)</td><td>4630.00 (n/a)</td><td>4614.30 (n/a)</td><td>154.56 (n/a)</td><td>465.40 (n/a)</td><td>454.06 (n/a)</td><td>463.82 (n/a)</td><td>436.98 (n/a)</td><td>14.65 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>7.59 (+3.36%)</td><td>6.99 (-2.94%)</td><td>6.90 (-5.08%)</td><td>6.30 (-7.76%)</td><td>0.55 <b>(+161.24%)</b></td><td>5530.40 (+8.41%)</td><td>5014.06 (+3.46%)</td><td>5049.80 (+5.35%)</td><td>4592.20 (-3.25%)</td><td>395.33 <b>(+170.31%)</b></td><td>467.64 (+3.36%)</td><td>430.42 (-2.94%)</td><td>425.26 (-5.08%)</td><td>388.30 (-7.76%)</td><td>33.76 <b>(+161.24%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>7.35 (n/a)</td><td>7.20 (n/a)</td><td>7.27 (n/a)</td><td>6.83 (n/a)</td><td>0.21 (n/a)</td><td>5101.40 (n/a)</td><td>4846.16 (n/a)</td><td>4793.30 (n/a)</td><td>4746.60 (n/a)</td><td>146.25 (n/a)</td><td>452.42 (n/a)</td><td>443.44 (n/a)</td><td>448.02 (n/a)</td><td>420.96 (n/a)</td><td>12.92 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.79 (+0.06%)</td><td>0.79 (+0.10%)</td><td>0.79 (+0.13%)</td><td>0.79 (+0.16%)</td><td>0.00 <b>(-33.09%)</b></td><td>95525.90 (-0.16%)</td><td>95420.38 (-0.10%)</td><td>95389.00 (-0.13%)</td><td>95350.60 (-0.06%)</td><td>73.82 <b>(-33.25%)</b></td><td>720.70 (+0.06%)</td><td>720.18 (+0.10%)</td><td>720.41 (+0.13%)</td><td>719.38 (+0.16%)</td><td>0.56 <b>(-33.09%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95679.50 (n/a)</td><td>95516.90 (n/a)</td><td>95516.70 (n/a)</td><td>95409.70 (n/a)</td><td>110.59 (n/a)</td><td>720.26 (n/a)</td><td>719.45 (n/a)</td><td>719.45 (n/a)</td><td>718.23 (n/a)</td><td>0.83 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.74 (-0.03%)</td><td>0.74 (-0.05%)</td><td>0.74 (-0.05%)</td><td>0.73 (-0.06%)</td><td>0.00 (+12.63%)</td><td>102817.60 (+0.06%)</td><td>102672.56 (+0.05%)</td><td>102638.60 (+0.05%)</td><td>102574.10 (+0.03%)</td><td>96.49 (+12.75%)</td><td>669.95 (-0.03%)</td><td>669.31 (-0.05%)</td><td>669.53 (-0.05%)</td><td>668.36 (-0.06%)</td><td>0.63 (+12.62%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>102755.40 (n/a)</td><td>102624.24 (n/a)</td><td>102585.90 (n/a)</td><td>102539.80 (n/a)</td><td>85.57 (n/a)</td><td>670.17 (n/a)</td><td>669.62 (n/a)</td><td>669.87 (n/a)</td><td>668.77 (n/a)</td><td>0.56 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.71 (+0.24%)</td><td>0.70 (+0.08%)</td><td>0.70 (+0.20%)</td><td>0.70 (-0.07%)</td><td>0.00 <b>(+82.85%)</b></td><td>107776.80 (+0.07%)</td><td>107352.14 (-0.08%)</td><td>107213.40 (-0.20%)</td><td>107004.80 (-0.24%)</td><td>313.66 <b>(+82.60%)</b></td><td>642.21 (+0.24%)</td><td>640.14 (+0.08%)</td><td>640.96 (+0.20%)</td><td>637.61 (-0.07%)</td><td>1.87 <b>(+82.85%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.70 (n/a)</td><td>0.00 (n/a)</td><td>107698.80 (n/a)</td><td>107437.62 (n/a)</td><td>107426.60 (n/a)</td><td>107257.20 (n/a)</td><td>171.77 (n/a)</td><td>640.70 (n/a)</td><td>639.62 (n/a)</td><td>639.69 (n/a)</td><td>638.07 (n/a)</td><td>1.02 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>3.64 (-14.35%)</td><td>3.36 (-5.79%)</td><td>3.60 (-3.47%)</td><td>2.96 (+0.07%)</td><td>0.35 <b>(-31.69%)</b></td><td>2719.70 (-0.07%)</td><td>2420.08 (+5.36%)</td><td>2241.70 (+3.60%)</td><td>2215.90 (+16.75%)</td><td>259.72 <b>(-21.11%)</b></td><td>954.00 (-14.35%)</td><td>881.31 (-5.80%)</td><td>943.00 (-3.47%)</td><td>777.27 (+0.07%)</td><td>91.02 <b>(-31.69%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>4.25 (n/a)</td><td>3.57 (n/a)</td><td>3.73 (n/a)</td><td>2.96 (n/a)</td><td>0.51 (n/a)</td><td>2721.50 (n/a)</td><td>2296.92 (n/a)</td><td>2163.90 (n/a)</td><td>1898.00 (n/a)</td><td>329.22 (n/a)</td><td>1113.77 (n/a)</td><td>935.53 (n/a)</td><td>976.89 (n/a)</td><td>776.75 (n/a)</td><td>133.25 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.43 (+5.04%)</td><td>0.34 (+3.37%)</td><td>0.33 (+4.65%)</td><td>0.29 (+6.17%)</td><td>0.05 (+6.70%)</td><td>4278.30 (-5.81%)</td><td>3732.78 (-3.23%)</td><td>3792.50 (-4.45%)</td><td>2884.00 (-4.80%)</td><td>517.67 (-5.13%)</td><td>23.27 (+5.04%)</td><td>18.30 (+3.37%)</td><td>17.70 (+4.65%)</td><td>15.69 (+6.17%)</td><td>2.91 (+6.70%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.41 (n/a)</td><td>0.33 (n/a)</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.05 (n/a)</td><td>4542.10 (n/a)</td><td>3857.44 (n/a)</td><td>3969.00 (n/a)</td><td>3029.50 (n/a)</td><td>545.66 (n/a)</td><td>22.15 (n/a)</td><td>17.70 (n/a)</td><td>16.91 (n/a)</td><td>14.77 (n/a)</td><td>2.73 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>4.92 (-1.66%)</td><td>4.03 (-12.16%)</td><td>3.66 <b>(-23.99%)</b></td><td>3.16 (-10.56%)</td><td>0.78 <b>(+31.23%)</b></td><td>2104.10 (+11.81%)</td><td>1701.08 (+15.39%)</td><td>1817.20 <b>(+31.56%)</b></td><td>1352.70 (+1.69%)</td><td>322.60 <b>(+40.62%)</b></td><td>1519.33 (-1.66%)</td><td>1244.60 (-12.16%)</td><td>1130.96 <b>(-23.99%)</b></td><td>976.77 (-10.56%)</td><td>241.45 <b>(+31.23%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>5.00 (n/a)</td><td>4.59 (n/a)</td><td>4.82 (n/a)</td><td>3.53 (n/a)</td><td>0.60 (n/a)</td><td>1881.80 (n/a)</td><td>1474.26 (n/a)</td><td>1381.30 (n/a)</td><td>1330.20 (n/a)</td><td>229.41 (n/a)</td><td>1545.02 (n/a)</td><td>1416.94 (n/a)</td><td>1487.89 (n/a)</td><td>1092.13 (n/a)</td><td>183.99 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>13.17 (n/a)</td><td>12.17 (n/a)</td><td>12.30 (n/a)</td><td>10.71 (n/a)</td><td>1.06 (n/a)</td><td>13.16 (n/a)</td><td>12.17 (n/a)</td><td>12.29 (n/a)</td><td>10.71 (n/a)</td><td>1.06 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>25.04 (-1.97%)</td><td>24.36 (+1.70%)</td><td>24.46 (+0.96%)</td><td>23.36 (+8.50%)</td><td>0.70 <b>(-52.50%)</b></td><td>25.02 (-1.97%)</td><td>24.35 (+1.70%)</td><td>24.44 (+0.96%)</td><td>23.35 (+8.50%)</td><td>0.70 <b>(-52.50%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>25.54 (n/a)</td><td>23.95 (n/a)</td><td>24.22 (n/a)</td><td>21.53 (n/a)</td><td>1.48 (n/a)</td><td>25.53 (n/a)</td><td>23.94 (n/a)</td><td>24.21 (n/a)</td><td>21.52 (n/a)</td><td>1.48 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>43.17 (-1.12%)</td><td>40.98 (-0.22%)</td><td>40.76 (+0.63%)</td><td>38.70 (-0.99%)</td><td>1.67 (-1.62%)</td><td>43.14 (-1.12%)</td><td>40.95 (-0.22%)</td><td>40.73 (+0.63%)</td><td>38.68 (-0.99%)</td><td>1.67 (-1.62%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>43.66 (n/a)</td><td>41.06 (n/a)</td><td>40.50 (n/a)</td><td>39.09 (n/a)</td><td>1.70 (n/a)</td><td>43.63 (n/a)</td><td>41.04 (n/a)</td><td>40.48 (n/a)</td><td>39.07 (n/a)</td><td>1.70 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>44.93 (-1.13%)</td><td>43.10 (+1.04%)</td><td>43.12 (+1.73%)</td><td>42.09 (+4.35%)</td><td>1.16 <b>(-39.04%)</b></td><td>44.90 (-1.13%)</td><td>43.07 (+1.04%)</td><td>43.09 (+1.73%)</td><td>42.06 (+4.35%)</td><td>1.16 <b>(-39.04%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>45.44 (n/a)</td><td>42.65 (n/a)</td><td>42.39 (n/a)</td><td>40.34 (n/a)</td><td>1.90 (n/a)</td><td>45.42 (n/a)</td><td>42.63 (n/a)</td><td>42.36 (n/a)</td><td>40.31 (n/a)</td><td>1.90 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>13.14 (n/a)</td><td>12.42 (n/a)</td><td>12.41 (n/a)</td><td>11.24 (n/a)</td><td>0.78 (n/a)</td><td>13.13 (n/a)</td><td>12.41 (n/a)</td><td>12.41 (n/a)</td><td>11.24 (n/a)</td><td>0.78 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>24.49 (-2.65%)</td><td>23.89 (-2.11%)</td><td>24.01 (-1.64%)</td><td>22.79 (-3.90%)</td><td>0.65 <b>(+22.01%)</b></td><td>24.48 (-2.65%)</td><td>23.88 (-2.11%)</td><td>23.99 (-1.64%)</td><td>22.77 (-3.90%)</td><td>0.65 <b>(+22.01%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>25.16 (n/a)</td><td>24.41 (n/a)</td><td>24.41 (n/a)</td><td>23.71 (n/a)</td><td>0.54 (n/a)</td><td>25.14 (n/a)</td><td>24.39 (n/a)</td><td>24.39 (n/a)</td><td>23.70 (n/a)</td><td>0.54 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>40.93 (-2.01%)</td><td>39.05 (+0.36%)</td><td>40.14 (-0.60%)</td><td>34.04 (-0.03%)</td><td>2.85 (-8.21%)</td><td>40.90 (-2.01%)</td><td>39.02 (+0.36%)</td><td>40.11 (-0.60%)</td><td>34.02 (-0.03%)</td><td>2.85 (-8.21%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>41.76 (n/a)</td><td>38.91 (n/a)</td><td>40.38 (n/a)</td><td>34.05 (n/a)</td><td>3.10 (n/a)</td><td>41.74 (n/a)</td><td>38.88 (n/a)</td><td>40.35 (n/a)</td><td>34.03 (n/a)</td><td>3.10 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>45.55 (+4.74%)</td><td>43.80 (+5.58%)</td><td>43.92 (+3.26%)</td><td>41.76 (+10.97%)</td><td>1.36 <b>(-40.82%)</b></td><td>45.52 (+4.74%)</td><td>43.77 (+5.58%)</td><td>43.90 (+3.26%)</td><td>41.74 (+10.97%)</td><td>1.36 <b>(-40.82%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>43.49 (n/a)</td><td>41.48 (n/a)</td><td>42.54 (n/a)</td><td>37.63 (n/a)</td><td>2.30 (n/a)</td><td>43.46 (n/a)</td><td>41.46 (n/a)</td><td>42.51 (n/a)</td><td>37.61 (n/a)</td><td>2.30 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>9.84 (+6.90%)</td><td>8.72 (+0.56%)</td><td>8.41 (-2.99%)</td><td>7.97 (+0.62%)</td><td>0.85 <b>(+76.80%)</b></td><td>9.82 (+6.90%)</td><td>8.71 (+0.56%)</td><td>8.39 (-2.99%)</td><td>7.96 (+0.62%)</td><td>0.84 <b>(+76.79%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>9.20 (n/a)</td><td>8.67 (n/a)</td><td>8.67 (n/a)</td><td>7.93 (n/a)</td><td>0.48 (n/a)</td><td>9.19 (n/a)</td><td>8.66 (n/a)</td><td>8.65 (n/a)</td><td>7.91 (n/a)</td><td>0.48 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.98 (-12.31%)</td><td>0.87 (-6.91%)</td><td>0.92 (-0.78%)</td><td>0.74 (-11.17%)</td><td>0.12 (+3.26%)</td><td>0.97 (-12.31%)</td><td>0.86 (-6.91%)</td><td>0.90 (-0.78%)</td><td>0.73 (-11.17%)</td><td>0.11 (+3.26%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>1.12 (n/a)</td><td>0.94 (n/a)</td><td>0.93 (n/a)</td><td>0.84 (n/a)</td><td>0.11 (n/a)</td><td>1.10 (n/a)</td><td>0.92 (n/a)</td><td>0.91 (n/a)</td><td>0.82 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>1.51 (+13.05%)</td><td>1.14 (-5.53%)</td><td>1.05 (-14.81%)</td><td>0.83 <b>(-21.94%)</b></td><td>0.26 <b>(+145.59%)</b></td><td>1.49 (+13.05%)</td><td>1.13 (-5.53%)</td><td>1.04 (-14.81%)</td><td>0.82 <b>(-21.94%)</b></td><td>0.26 <b>(+145.59%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>1.33 (n/a)</td><td>1.21 (n/a)</td><td>1.24 (n/a)</td><td>1.06 (n/a)</td><td>0.11 (n/a)</td><td>1.32 (n/a)</td><td>1.19 (n/a)</td><td>1.22 (n/a)</td><td>1.05 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>18.40 (+12.94%)</td><td>16.70 (+12.80%)</td><td>16.91 (+11.17%)</td><td>14.22 (+14.06%)</td><td>1.67 (+3.03%)</td><td>18.19 (+12.94%)</td><td>16.50 (+12.80%)</td><td>16.71 (+11.17%)</td><td>14.05 (+14.06%)</td><td>1.65 (+3.03%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>16.30 (n/a)</td><td>14.80 (n/a)</td><td>15.21 (n/a)</td><td>12.46 (n/a)</td><td>1.62 (n/a)</td><td>16.11 (n/a)</td><td>14.63 (n/a)</td><td>15.03 (n/a)</td><td>12.32 (n/a)</td><td>1.60 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>13.70 (-4.18%)</td><td>13.12 (-2.97%)</td><td>13.28 (-2.74%)</td><td>12.52 (+2.95%)</td><td>0.56 <b>(-33.47%)</b></td><td>13.46 (-4.18%)</td><td>12.89 (-2.97%)</td><td>13.05 (-2.74%)</td><td>12.30 (+2.95%)</td><td>0.55 <b>(-33.47%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>14.29 (n/a)</td><td>13.53 (n/a)</td><td>13.66 (n/a)</td><td>12.16 (n/a)</td><td>0.84 (n/a)</td><td>14.04 (n/a)</td><td>13.29 (n/a)</td><td>13.42 (n/a)</td><td>11.95 (n/a)</td><td>0.83 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>8.19 (-7.19%)</td><td>7.27 (-5.32%)</td><td>7.21 (+1.04%)</td><td>6.26 (-8.43%)</td><td>0.71 <b>(-29.07%)</b></td><td>8.05 (-7.19%)</td><td>7.14 (-5.32%)</td><td>7.08 (+1.04%)</td><td>6.15 (-8.43%)</td><td>0.70 <b>(-29.07%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>8.83 (n/a)</td><td>7.68 (n/a)</td><td>7.13 (n/a)</td><td>6.84 (n/a)</td><td>1.00 (n/a)</td><td>8.68 (n/a)</td><td>7.55 (n/a)</td><td>7.01 (n/a)</td><td>6.72 (n/a)</td><td>0.98 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>6.98 (+7.55%)</td><td>5.40 (-4.99%)</td><td>5.27 (-3.86%)</td><td>4.36 (-12.40%)</td><td>1.10 <b>(+87.24%)</b></td><td>6.86 (+7.55%)</td><td>5.31 (-4.99%)</td><td>5.18 (-3.86%)</td><td>4.29 (-12.40%)</td><td>1.09 <b>(+87.24%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>6.49 (n/a)</td><td>5.68 (n/a)</td><td>5.48 (n/a)</td><td>4.98 (n/a)</td><td>0.59 (n/a)</td><td>6.38 (n/a)</td><td>5.59 (n/a)</td><td>5.39 (n/a)</td><td>4.90 (n/a)</td><td>0.58 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>13.14 (n/a)</td><td>12.82 (n/a)</td><td>12.96 (n/a)</td><td>12.31 (n/a)</td><td>0.35 (n/a)</td><td>13.13 (n/a)</td><td>12.81 (n/a)</td><td>12.95 (n/a)</td><td>12.30 (n/a)</td><td>0.35 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>13.17 (n/a)</td><td>12.63 (n/a)</td><td>12.83 (n/a)</td><td>11.71 (n/a)</td><td>0.57 (n/a)</td><td>13.16 (n/a)</td><td>12.63 (n/a)</td><td>12.82 (n/a)</td><td>11.71 (n/a)</td><td>0.57 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.90 (n/a)</td><td>176.00 (n/a)</td><td>172.80 (n/a)</td><td>150.30 (n/a)</td><td>25.28 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.60 (n/a)</td><td>173.16 (n/a)</td><td>164.10 (n/a)</td><td>130.00 (n/a)</td><td>33.66 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>177.00 (n/a)</td><td>151.12 (n/a)</td><td>145.50 (n/a)</td><td>134.50 (n/a)</td><td>17.97 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>226.10 (n/a)</td><td>179.60 (n/a)</td><td>179.60 (n/a)</td><td>123.90 (n/a)</td><td>37.52 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>188.00 (n/a)</td><td>168.52 (n/a)</td><td>174.40 (n/a)</td><td>135.00 (n/a)</td><td>21.07 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>260.90 (n/a)</td><td>205.92 (n/a)</td><td>196.00 (n/a)</td><td>172.60 (n/a)</td><td>33.14 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>319.30 (n/a)</td><td>223.84 (n/a)</td><td>217.00 (n/a)</td><td>177.70 (n/a)</td><td>57.20 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>314.20 (n/a)</td><td>233.58 (n/a)</td><td>224.90 (n/a)</td><td>175.00 (n/a)</td><td>50.77 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.20 (n/a)</td><td>156.36 (n/a)</td><td>148.30 (n/a)</td><td>123.30 (n/a)</td><td>32.44 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.20 (n/a)</td><td>159.84 (n/a)</td><td>159.50 (n/a)</td><td>125.80 (n/a)</td><td>24.40 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>177.70 (n/a)</td><td>153.54 (n/a)</td><td>169.90 (n/a)</td><td>115.00 (n/a)</td><td>29.68 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.70 (n/a)</td><td>172.96 (n/a)</td><td>176.20 (n/a)</td><td>121.80 (n/a)</td><td>33.05 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.70 (n/a)</td><td>177.54 (n/a)</td><td>185.20 (n/a)</td><td>135.90 (n/a)</td><td>25.93 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.70 (n/a)</td><td>177.12 (n/a)</td><td>179.20 (n/a)</td><td>130.50 (n/a)</td><td>41.72 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>193.20 (n/a)</td><td>182.02 (n/a)</td><td>189.10 (n/a)</td><td>154.70 (n/a)</td><td>15.69 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.30 (n/a)</td><td>189.58 (n/a)</td><td>199.60 (n/a)</td><td>130.10 (n/a)</td><td>46.01 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>198.60 (n/a)</td><td>168.70 (n/a)</td><td>170.80 (n/a)</td><td>135.40 (n/a)</td><td>25.34 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>253.30 (n/a)</td><td>179.36 (n/a)</td><td>165.90 (n/a)</td><td>153.80 (n/a)</td><td>41.92 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>192.30 (n/a)</td><td>157.10 (n/a)</td><td>169.80 (n/a)</td><td>116.50 (n/a)</td><td>32.06 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>189.70 (n/a)</td><td>165.88 (n/a)</td><td>174.20 (n/a)</td><td>138.60 (n/a)</td><td>22.97 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>215.30 (n/a)</td><td>166.40 (n/a)</td><td>163.00 (n/a)</td><td>124.80 (n/a)</td><td>32.32 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>202.10 (n/a)</td><td>177.12 (n/a)</td><td>188.70 (n/a)</td><td>136.20 (n/a)</td><td>27.76 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>211.90 (n/a)</td><td>189.04 (n/a)</td><td>202.40 (n/a)</td><td>150.40 (n/a)</td><td>26.16 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>311.60 (n/a)</td><td>235.04 (n/a)</td><td>237.90 (n/a)</td><td>171.60 (n/a)</td><td>52.39 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>210.20 (n/a)</td><td>185.58 (n/a)</td><td>183.70 (n/a)</td><td>170.70 (n/a)</td><td>15.44 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>191.90 (n/a)</td><td>171.96 (n/a)</td><td>178.50 (n/a)</td><td>148.80 (n/a)</td><td>16.99 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>206.20 (n/a)</td><td>150.86 (n/a)</td><td>141.50 (n/a)</td><td>124.40 (n/a)</td><td>33.67 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>332.30 (n/a)</td><td>203.78 (n/a)</td><td>173.20 (n/a)</td><td>142.00 (n/a)</td><td>79.74 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>190.50 (n/a)</td><td>169.84 (n/a)</td><td>168.70 (n/a)</td><td>132.00 (n/a)</td><td>23.73 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>216.20 (n/a)</td><td>169.22 (n/a)</td><td>157.50 (n/a)</td><td>130.10 (n/a)</td><td>32.92 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>305.90 (n/a)</td><td>221.60 (n/a)</td><td>210.90 (n/a)</td><td>171.10 (n/a)</td><td>50.14 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>231.90 (n/a)</td><td>207.00 (n/a)</td><td>206.30 (n/a)</td><td>188.60 (n/a)</td><td>16.87 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (-4.99%)</td><td>0.03 (-9.07%)</td><td>0.03 (-10.09%)</td><td>0.02 (-11.41%)</td><td>0.00 (-6.76%)</td><td>197.40 (+12.93%)</td><td>163.00 (+10.02%)</td><td>162.30 (+11.24%)</td><td>131.50 (+5.20%)</td><td>23.64 (+11.02%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>174.80 (n/a)</td><td>148.16 (n/a)</td><td>145.90 (n/a)</td><td>125.00 (n/a)</td><td>21.29 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (+10.90%)</td><td>0.02 (-3.33%)</td><td>0.02 (-11.15%)</td><td>0.02 (-4.74%)</td><td>0.00 <b>(+93.78%)</b></td><td>197.40 (+5.00%)</td><td>180.32 (+4.45%)</td><td>190.30 (+12.54%)</td><td>145.40 (-9.86%)</td><td>22.20 <b>(+85.48%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>188.00 (n/a)</td><td>172.64 (n/a)</td><td>169.10 (n/a)</td><td>161.30 (n/a)</td><td>11.97 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 <b>(+23.99%)</b></td><td>0.03 (+15.77%)</td><td>0.02 (+8.85%)</td><td>0.02 (+8.47%)</td><td>0.01 <b>(+81.68%)</b></td><td>195.70 (-7.78%)</td><td>158.56 (-11.65%)</td><td>166.40 (-8.12%)</td><td>116.70 (-19.35%)</td><td>33.42 <b>(+36.27%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.20 (n/a)</td><td>179.46 (n/a)</td><td>181.10 (n/a)</td><td>144.70 (n/a)</td><td>24.53 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 <b>(+55.71%)</b></td><td>0.02 (+7.16%)</td><td>0.02 (-8.11%)</td><td>0.02 (-0.83%)</td><td>0.01 <b>(+182.88%)</b></td><td>240.90 (+0.84%)</td><td>185.00 (-0.17%)</td><td>191.20 (+8.82%)</td><td>102.50 <b>(-35.78%)</b></td><td>52.06 <b>(+67.56%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>238.90 (n/a)</td><td>185.32 (n/a)</td><td>175.70 (n/a)</td><td>159.60 (n/a)</td><td>31.07 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (-6.83%)</td><td>0.02 (-13.35%)</td><td>0.02 (-9.31%)</td><td>0.01 <b>(-38.10%)</b></td><td>0.01 <b>(+50.44%)</b></td><td>322.90 <b>(+61.53%)</b></td><td>204.96 <b>(+22.04%)</b></td><td>181.40 (+10.27%)</td><td>142.00 (+7.33%)</td><td>69.63 <b>(+177.58%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>199.90 (n/a)</td><td>167.94 (n/a)</td><td>164.50 (n/a)</td><td>132.30 (n/a)</td><td>25.08 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (+4.94%)</td><td>0.02 (+3.24%)</td><td>0.02 (-5.88%)</td><td>0.02 <b>(+31.53%)</b></td><td>0.00 <b>(-35.48%)</b></td><td>218.40 <b>(-23.98%)</b></td><td>192.58 (-6.76%)</td><td>203.70 (+6.26%)</td><td>149.80 (-4.71%)</td><td>26.60 <b>(-52.68%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>287.30 (n/a)</td><td>206.54 (n/a)</td><td>191.70 (n/a)</td><td>157.20 (n/a)</td><td>56.20 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (+17.58%)</td><td>0.02 (-6.89%)</td><td>0.02 (-14.32%)</td><td>0.01 <b>(-28.73%)</b></td><td>0.01 <b>(+116.35%)</b></td><td>310.80 <b>(+40.32%)</b></td><td>208.78 (+13.84%)</td><td>198.30 (+16.72%)</td><td>137.40 (-14.92%)</td><td>64.78 <b>(+161.33%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.50 (n/a)</td><td>183.40 (n/a)</td><td>169.90 (n/a)</td><td>161.50 (n/a)</td><td>24.79 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (+13.24%)</td><td>0.02 (+14.29%)</td><td>0.02 (+3.41%)</td><td>0.02 (+17.86%)</td><td>0.00 <b>(+23.08%)</b></td><td>230.40 (-15.14%)</td><td>206.78 (-12.34%)</td><td>224.00 (-3.28%)</td><td>172.20 (-11.69%)</td><td>27.46 (-7.34%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>271.50 (n/a)</td><td>235.88 (n/a)</td><td>231.60 (n/a)</td><td>195.00 (n/a)</td><td>29.63 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (-8.72%)</td><td>0.04 (-8.81%)</td><td>0.04 (-19.10%)</td><td>0.04 <b>(+76.15%)</b></td><td>0.01 <b>(-58.46%)</b></td><td>211.70 <b>(-43.23%)</b></td><td>188.88 (-2.99%)</td><td>187.30 <b>(+23.63%)</b></td><td>150.50 (+9.53%)</td><td>24.52 <b>(-75.54%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>372.90 (n/a)</td><td>194.70 (n/a)</td><td>151.50 (n/a)</td><td>137.40 (n/a)</td><td>100.24 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.07 (+2.32%)</td><td>0.05 (-4.01%)</td><td>0.05 (+7.13%)</td><td>0.04 <b>(-24.68%)</b></td><td>0.01 <b>(+59.09%)</b></td><td>227.10 <b>(+32.81%)</b></td><td>163.86 (+7.80%)</td><td>149.20 (-6.69%)</td><td>121.20 (-2.26%)</td><td>42.44 <b>(+107.50%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>171.00 (n/a)</td><td>152.00 (n/a)</td><td>159.90 (n/a)</td><td>124.00 (n/a)</td><td>20.45 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (-3.87%)</td><td>0.05 (-4.37%)</td><td>0.05 (+0.25%)</td><td>0.04 (-4.34%)</td><td>0.01 (+4.59%)</td><td>208.50 (+4.56%)</td><td>167.68 (+5.04%)</td><td>159.20 (-0.25%)</td><td>130.50 (+3.98%)</td><td>30.71 (+14.77%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.40 (n/a)</td><td>159.64 (n/a)</td><td>159.60 (n/a)</td><td>125.50 (n/a)</td><td>26.76 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.07 (-12.92%)</td><td>0.05 (-15.49%)</td><td>0.05 (-6.37%)</td><td>0.03 <b>(-25.80%)</b></td><td>0.01 (-6.15%)</td><td>237.90 <b>(+34.79%)</b></td><td>176.90 (+19.69%)</td><td>175.60 (+6.75%)</td><td>124.60 (+14.84%)</td><td>42.61 <b>(+44.67%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>176.50 (n/a)</td><td>147.80 (n/a)</td><td>164.50 (n/a)</td><td>108.50 (n/a)</td><td>29.45 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 <b>(-25.98%)</b></td><td>0.05 (-11.94%)</td><td>0.05 (-8.37%)</td><td>0.04 (+6.78%)</td><td>0.00 <b>(-71.65%)</b></td><td>199.10 (-6.35%)</td><td>180.24 (+10.25%)</td><td>178.10 (+9.13%)</td><td>165.60 <b>(+35.07%)</b></td><td>12.09 <b>(-63.83%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.60 (n/a)</td><td>163.48 (n/a)</td><td>163.20 (n/a)</td><td>122.60 (n/a)</td><td>33.43 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (+0.67%)</td><td>0.05 (+4.55%)</td><td>0.05 (+1.43%)</td><td>0.04 (+10.42%)</td><td>0.00 <b>(-26.74%)</b></td><td>182.30 (-9.44%)</td><td>169.44 (-4.93%)</td><td>176.30 (-1.40%)</td><td>147.90 (-0.67%)</td><td>13.70 <b>(-34.66%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.30 (n/a)</td><td>178.22 (n/a)</td><td>178.80 (n/a)</td><td>148.90 (n/a)</td><td>20.98 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.07 (+3.60%)</td><td>0.05 (+2.85%)</td><td>0.05 <b>(+25.14%)</b></td><td>0.03 (-14.69%)</td><td>0.01 (+9.20%)</td><td>242.20 (+17.23%)</td><td>170.56 (-1.38%)</td><td>157.90 <b>(-20.09%)</b></td><td>119.50 (-3.47%)</td><td>47.81 <b>(+23.64%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.60 (n/a)</td><td>172.94 (n/a)</td><td>197.60 (n/a)</td><td>123.80 (n/a)</td><td>38.67 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (-7.85%)</td><td>0.04 (-9.93%)</td><td>0.05 (-6.41%)</td><td>0.03 (-9.28%)</td><td>0.01 (+0.86%)</td><td>258.90 (+10.22%)</td><td>206.38 (+11.81%)</td><td>177.10 (+6.88%)</td><td>168.50 (+8.57%)</td><td>44.51 <b>(+23.89%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.90 (n/a)</td><td>184.58 (n/a)</td><td>165.70 (n/a)</td><td>155.20 (n/a)</td><td>35.93 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 <b>(-34.67%)</b></td><td>0.04 (-4.57%)</td><td>0.04 (+2.62%)</td><td>0.04 <b>(+45.77%)</b></td><td>0.00 <b>(-89.57%)</b></td><td>208.80 <b>(-31.41%)</b></td><td>198.92 (-5.74%)</td><td>198.20 (-2.56%)</td><td>190.90 <b>(+53.09%)</b></td><td>8.06 <b>(-89.21%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>304.40 (n/a)</td><td>211.04 (n/a)</td><td>203.40 (n/a)</td><td>124.70 (n/a)</td><td>74.65 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (-3.47%)</td><td>0.04 (-1.26%)</td><td>0.04 (-8.86%)</td><td>0.03 <b>(+34.87%)</b></td><td>0.00 <b>(-38.12%)</b></td><td>241.50 <b>(-25.85%)</b></td><td>222.08 (-1.84%)</td><td>231.10 (+9.73%)</td><td>178.40 (+3.60%)</td><td>25.94 <b>(-55.37%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>325.70 (n/a)</td><td>226.24 (n/a)</td><td>210.60 (n/a)</td><td>172.20 (n/a)</td><td>58.11 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 (-19.46%)</td><td>0.09 (-15.25%)</td><td>0.10 (-6.53%)</td><td>0.06 <b>(-24.77%)</b></td><td>0.02 (-9.71%)</td><td>256.20 <b>(+32.95%)</b></td><td>185.38 (+19.11%)</td><td>169.50 (+7.01%)</td><td>152.80 <b>(+24.13%)</b></td><td>40.70 <b>(+56.55%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>192.70 (n/a)</td><td>155.64 (n/a)</td><td>158.40 (n/a)</td><td>123.10 (n/a)</td><td>26.00 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.10 <b>(-20.65%)</b></td><td>0.09 (-10.92%)</td><td>0.10 (-4.58%)</td><td>0.05 <b>(-21.63%)</b></td><td>0.02 <b>(-24.26%)</b></td><td>308.50 <b>(+27.58%)</b></td><td>195.90 (+12.15%)</td><td>172.40 (+4.80%)</td><td>159.60 <b>(+26.07%)</b></td><td>63.18 <b>(+28.55%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>241.80 (n/a)</td><td>174.68 (n/a)</td><td>164.50 (n/a)</td><td>126.60 (n/a)</td><td>49.14 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.10 <b>(-30.05%)</b></td><td>0.08 <b>(-36.63%)</b></td><td>0.08 <b>(-38.11%)</b></td><td>0.06 <b>(-47.02%)</b></td><td>0.01 <b>(+60.51%)</b></td><td>272.70 <b>(+88.72%)</b></td><td>210.06 <b>(+61.81%)</b></td><td>210.40 <b>(+61.60%)</b></td><td>171.10 <b>(+42.94%)</b></td><td>41.55 <b>(+324.47%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>144.50 (n/a)</td><td>129.82 (n/a)</td><td>130.20 (n/a)</td><td>119.70 (n/a)</td><td>9.79 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 (-13.26%)</td><td>0.09 (-5.22%)</td><td>0.09 (+8.19%)</td><td>0.06 <b>(-20.10%)</b></td><td>0.02 (-15.48%)</td><td>258.10 <b>(+25.17%)</b></td><td>185.30 (+5.75%)</td><td>173.80 (-7.55%)</td><td>146.80 (+15.32%)</td><td>42.45 <b>(+27.40%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>206.20 (n/a)</td><td>175.22 (n/a)</td><td>188.00 (n/a)</td><td>127.30 (n/a)</td><td>33.32 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 <b>(+35.08%)</b></td><td>0.10 (+9.94%)</td><td>0.09 (+1.91%)</td><td>0.07 (-9.01%)</td><td>0.02 <b>(+208.82%)</b></td><td>235.60 (+9.89%)</td><td>178.70 (-6.07%)</td><td>180.40 (-1.85%)</td><td>131.90 <b>(-25.98%)</b></td><td>38.73 <b>(+152.01%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>214.40 (n/a)</td><td>190.24 (n/a)</td><td>183.80 (n/a)</td><td>178.20 (n/a)</td><td>15.37 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.15 (+12.39%)</td><td>0.10 (-12.06%)</td><td>0.09 (-18.91%)</td><td>0.07 <b>(-25.96%)</b></td><td>0.03 <b>(+101.34%)</b></td><td>240.50 <b>(+35.04%)</b></td><td>182.48 (+19.42%)</td><td>181.70 <b>(+23.27%)</b></td><td>112.30 (-11.01%)</td><td>46.67 <b>(+128.98%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>178.10 (n/a)</td><td>152.80 (n/a)</td><td>147.40 (n/a)</td><td>126.20 (n/a)</td><td>20.38 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (+15.83%)</td><td>0.10 (+10.95%)</td><td>0.10 (+14.06%)</td><td>0.07 (-0.40%)</td><td>0.02 <b>(+48.39%)</b></td><td>227.70 (+0.40%)</td><td>174.56 (-8.48%)</td><td>167.90 (-12.32%)</td><td>131.10 (-13.69%)</td><td>35.18 <b>(+31.52%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>226.80 (n/a)</td><td>190.74 (n/a)</td><td>191.50 (n/a)</td><td>151.90 (n/a)</td><td>26.75 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.09 (-17.53%)</td><td>0.07 (-14.38%)</td><td>0.07 (-10.91%)</td><td>0.05 <b>(-30.33%)</b></td><td>0.02 (+4.23%)</td><td>322.80 <b>(+43.53%)</b></td><td>234.02 (+18.99%)</td><td>232.90 (+12.30%)</td><td>183.60 <b>(+21.27%)</b></td><td>55.84 <b>(+77.79%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>224.90 (n/a)</td><td>196.68 (n/a)</td><td>207.40 (n/a)</td><td>151.40 (n/a)</td><td>31.41 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.19 <b>(-24.90%)</b></td><td>0.17 (-14.82%)</td><td>0.17 (-10.70%)</td><td>0.16 (-0.26%)</td><td>0.01 <b>(-70.30%)</b></td><td>199.90 (+0.25%)</td><td>187.98 (+15.38%)</td><td>187.60 (+12.00%)</td><td>176.80 <b>(+33.13%)</b></td><td>10.23 <b>(-60.09%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>199.40 (n/a)</td><td>162.92 (n/a)</td><td>167.50 (n/a)</td><td>132.80 (n/a)</td><td>25.64 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.25 (-2.91%)</td><td>0.20 (+1.43%)</td><td>0.18 (-2.98%)</td><td>0.17 <b>(+31.48%)</b></td><td>0.03 <b>(-29.68%)</b></td><td>187.70 <b>(-23.98%)</b></td><td>169.50 (-4.23%)</td><td>183.80 (+3.08%)</td><td>130.70 (+2.99%)</td><td>24.58 <b>(-45.10%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>246.90 (n/a)</td><td>176.98 (n/a)</td><td>178.30 (n/a)</td><td>126.90 (n/a)</td><td>44.78 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.21 (-17.94%)</td><td>0.19 (-5.77%)</td><td>0.21 (+5.58%)</td><td>0.14 (+1.72%)</td><td>0.03 <b>(-27.88%)</b></td><td>236.60 (-1.66%)</td><td>180.08 (+4.33%)</td><td>157.50 (-5.29%)</td><td>154.00 <b>(+21.84%)</b></td><td>35.75 (-16.43%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>240.60 (n/a)</td><td>172.60 (n/a)</td><td>166.30 (n/a)</td><td>126.40 (n/a)</td><td>42.77 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.27 (+16.54%)</td><td>0.21 (+4.69%)</td><td>0.19 (-12.54%)</td><td>0.17 <b>(+30.68%)</b></td><td>0.05 (+9.64%)</td><td>192.80 <b>(-23.46%)</b></td><td>161.36 (-5.43%)</td><td>171.80 (+14.38%)</td><td>119.40 (-14.16%)</td><td>33.35 <b>(-28.77%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>251.90 (n/a)</td><td>170.62 (n/a)</td><td>150.20 (n/a)</td><td>139.10 (n/a)</td><td>46.82 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.25 (-0.48%)</td><td>0.19 (-1.49%)</td><td>0.18 (-4.96%)</td><td>0.15 <b>(+25.29%)</b></td><td>0.04 <b>(-29.56%)</b></td><td>217.50 <b>(-20.18%)</b></td><td>176.76 (-3.16%)</td><td>183.10 (+5.23%)</td><td>128.70 (+0.47%)</td><td>35.77 <b>(-40.95%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>272.50 (n/a)</td><td>182.52 (n/a)</td><td>174.00 (n/a)</td><td>128.10 (n/a)</td><td>60.58 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.19 (-19.86%)</td><td>0.17 (-8.37%)</td><td>0.17 (-7.71%)</td><td>0.16 <b>(+27.95%)</b></td><td>0.01 <b>(-68.45%)</b></td><td>211.10 <b>(-21.84%)</b></td><td>192.04 (+4.08%)</td><td>187.30 (+8.33%)</td><td>173.50 <b>(+24.82%)</b></td><td>15.60 <b>(-69.74%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>270.10 (n/a)</td><td>184.52 (n/a)</td><td>172.90 (n/a)</td><td>139.00 (n/a)</td><td>51.56 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.21 (+16.03%)</td><td>0.17 (+4.25%)</td><td>0.17 (-0.49%)</td><td>0.14 (+2.33%)</td><td>0.02 <b>(+44.81%)</b></td><td>226.50 (-2.24%)</td><td>194.54 (-3.49%)</td><td>193.10 (+0.52%)</td><td>156.80 (-13.85%)</td><td>25.30 <b>(+20.06%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>231.70 (n/a)</td><td>201.58 (n/a)</td><td>192.10 (n/a)</td><td>182.00 (n/a)</td><td>21.07 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (+13.79%)</td><td>0.03 (+10.06%)</td><td>0.03 (+5.68%)</td><td>0.02 (+11.85%)</td><td>0.00 (+18.30%)</td><td>183.80 (-10.60%)</td><td>157.56 (-8.98%)</td><td>151.90 (-5.36%)</td><td>132.00 (-12.06%)</td><td>22.53 (-6.24%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.60 (n/a)</td><td>173.10 (n/a)</td><td>160.50 (n/a)</td><td>150.10 (n/a)</td><td>24.03 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (+11.01%)</td><td>0.03 (+4.21%)</td><td>0.02 (-3.27%)</td><td>0.02 (+19.95%)</td><td>0.01 (+13.27%)</td><td>196.70 (-16.65%)</td><td>166.68 (-4.27%)</td><td>174.00 (+3.39%)</td><td>112.30 (-9.87%)</td><td>32.45 (-18.91%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>236.00 (n/a)</td><td>174.12 (n/a)</td><td>168.30 (n/a)</td><td>124.60 (n/a)</td><td>40.02 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (-9.80%)</td><td>0.02 (+3.46%)</td><td>0.02 (+8.57%)</td><td>0.02 <b>(+45.76%)</b></td><td>0.00 <b>(-65.43%)</b></td><td>239.90 <b>(-31.40%)</b></td><td>215.80 (-8.44%)</td><td>216.00 (-7.89%)</td><td>191.10 (+10.91%)</td><td>17.99 <b>(-74.13%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>349.70 (n/a)</td><td>235.70 (n/a)</td><td>234.50 (n/a)</td><td>172.30 (n/a)</td><td>69.55 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (+5.57%)</td><td>0.02 (+8.97%)</td><td>0.02 (+18.27%)</td><td>0.01 (-9.92%)</td><td>0.00 <b>(+44.20%)</b></td><td>276.90 (+10.98%)</td><td>203.32 (-5.91%)</td><td>178.70 (-15.47%)</td><td>157.30 (-5.24%)</td><td>51.41 <b>(+49.31%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>249.50 (n/a)</td><td>216.10 (n/a)</td><td>211.40 (n/a)</td><td>166.00 (n/a)</td><td>34.43 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 <b>(+28.85%)</b></td><td>0.02 (+5.80%)</td><td>0.02 (+8.33%)</td><td>0.02 (-19.21%)</td><td>0.01 <b>(+129.09%)</b></td><td>254.10 <b>(+23.77%)</b></td><td>184.22 (-1.50%)</td><td>181.80 (-7.67%)</td><td>124.80 <b>(-22.39%)</b></td><td>46.80 <b>(+117.33%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.30 (n/a)</td><td>187.02 (n/a)</td><td>196.90 (n/a)</td><td>160.80 (n/a)</td><td>21.53 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 <b>(-22.86%)</b></td><td>0.03 (+7.30%)</td><td>0.03 (+19.58%)</td><td>0.03 <b>(+37.43%)</b></td><td>0.00 <b>(-79.44%)</b></td><td>160.50 <b>(-27.24%)</b></td><td>147.26 (-12.16%)</td><td>143.70 (-16.36%)</td><td>138.20 <b>(+29.64%)</b></td><td>8.64 <b>(-80.09%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>220.60 (n/a)</td><td>167.64 (n/a)</td><td>171.80 (n/a)</td><td>106.60 (n/a)</td><td>43.37 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 <b>(-24.45%)</b></td><td>0.02 <b>(-24.01%)</b></td><td>0.02 (-19.26%)</td><td>0.01 <b>(-30.49%)</b></td><td>0.01 (-13.12%)</td><td>286.90 <b>(+43.88%)</b></td><td>213.46 <b>(+34.90%)</b></td><td>190.30 <b>(+23.89%)</b></td><td>142.80 <b>(+32.34%)</b></td><td>67.85 <b>(+67.93%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>199.40 (n/a)</td><td>158.24 (n/a)</td><td>153.60 (n/a)</td><td>107.90 (n/a)</td><td>40.40 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (-10.25%)</td><td>0.03 (+1.53%)</td><td>0.03 (+1.69%)</td><td>0.02 (+15.00%)</td><td>0.00 <b>(-33.07%)</b></td><td>194.70 (-13.04%)</td><td>163.46 (-3.23%)</td><td>161.50 (-1.64%)</td><td>143.90 (+11.38%)</td><td>21.42 <b>(-37.61%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>223.90 (n/a)</td><td>168.92 (n/a)</td><td>164.20 (n/a)</td><td>129.20 (n/a)</td><td>34.34 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (-0.22%)</td><td>0.02 (+4.59%)</td><td>0.02 (+15.56%)</td><td>0.02 (+7.36%)</td><td>0.00 <b>(-26.67%)</b></td><td>221.10 (-6.87%)</td><td>174.44 (-6.51%)</td><td>177.20 (-13.48%)</td><td>138.10 (+0.22%)</td><td>31.06 <b>(-28.76%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>237.40 (n/a)</td><td>186.58 (n/a)</td><td>204.80 (n/a)</td><td>137.80 (n/a)</td><td>43.60 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (+15.56%)</td><td>0.02 (+7.06%)</td><td>0.02 (+2.01%)</td><td>0.02 (+6.86%)</td><td>0.00 <b>(+68.57%)</b></td><td>195.30 (-6.42%)</td><td>177.30 (-5.88%)</td><td>187.20 (-1.99%)</td><td>145.80 (-13.47%)</td><td>21.95 <b>(+38.91%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>208.70 (n/a)</td><td>188.38 (n/a)</td><td>191.00 (n/a)</td><td>168.50 (n/a)</td><td>15.80 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (+9.06%)</td><td>0.03 (+4.08%)</td><td>0.02 (-2.91%)</td><td>0.02 (+16.85%)</td><td>0.00 (-6.19%)</td><td>182.00 (-14.43%)</td><td>160.08 (-4.51%)</td><td>167.90 (+2.94%)</td><td>131.20 (-8.25%)</td><td>19.74 <b>(-28.13%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.70 (n/a)</td><td>167.64 (n/a)</td><td>163.10 (n/a)</td><td>143.00 (n/a)</td><td>27.47 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 <b>(-27.27%)</b></td><td>0.02 (-17.08%)</td><td>0.02 (-1.06%)</td><td>0.02 (-14.47%)</td><td>0.00 <b>(-54.36%)</b></td><td>251.40 (+16.93%)</td><td>195.32 (+16.55%)</td><td>184.30 (+1.10%)</td><td>167.00 <b>(+37.56%)</b></td><td>32.84 <b>(-21.33%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>215.00 (n/a)</td><td>167.58 (n/a)</td><td>182.30 (n/a)</td><td>121.40 (n/a)</td><td>41.74 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 <b>(-30.90%)</b></td><td>0.02 (-7.36%)</td><td>0.02 (+5.71%)</td><td>0.02 (-3.16%)</td><td>0.00 <b>(-74.75%)</b></td><td>218.60 (+3.26%)</td><td>195.58 (+4.61%)</td><td>190.50 (-5.37%)</td><td>185.30 <b>(+44.77%)</b></td><td>13.38 <b>(-61.26%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>211.70 (n/a)</td><td>186.96 (n/a)</td><td>201.30 (n/a)</td><td>128.00 (n/a)</td><td>34.53 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 <b>(+22.98%)</b></td><td>0.02 (+12.08%)</td><td>0.02 (+11.42%)</td><td>0.02 (+4.90%)</td><td>0.00 <b>(+76.29%)</b></td><td>211.90 (-4.68%)</td><td>185.98 (-9.40%)</td><td>189.90 (-10.26%)</td><td>135.30 (-18.69%)</td><td>30.82 <b>(+36.97%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.30 (n/a)</td><td>205.28 (n/a)</td><td>211.60 (n/a)</td><td>166.40 (n/a)</td><td>22.50 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 <b>(+40.91%)</b></td><td>0.03 <b>(+34.73%)</b></td><td>0.02 <b>(+20.85%)</b></td><td>0.02 <b>(+34.13%)</b></td><td>0.00 <b>(+93.53%)</b></td><td>182.60 <b>(-25.44%)</b></td><td>159.20 <b>(-24.81%)</b></td><td>175.20 (-17.24%)</td><td>128.30 <b>(-29.00%)</b></td><td>27.57 (+1.70%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>244.90 (n/a)</td><td>211.74 (n/a)</td><td>211.70 (n/a)</td><td>180.70 (n/a)</td><td>27.11 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (+2.60%)</td><td>0.02 (+11.82%)</td><td>0.02 (+6.29%)</td><td>0.02 <b>(+28.45%)</b></td><td>0.00 <b>(-57.77%)</b></td><td>199.90 <b>(-22.16%)</b></td><td>179.22 (-12.44%)</td><td>175.00 (-5.91%)</td><td>168.50 (-2.54%)</td><td>12.12 <b>(-67.30%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>256.80 (n/a)</td><td>204.68 (n/a)</td><td>186.00 (n/a)</td><td>172.90 (n/a)</td><td>37.07 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (-10.97%)</td><td>0.05 (+17.79%)</td><td>0.05 (+1.75%)</td><td>0.04 <b>(+100.89%)</b></td><td>0.01 <b>(-58.66%)</b></td><td>199.00 <b>(-50.23%)</b></td><td>168.04 <b>(-27.02%)</b></td><td>177.00 (-1.72%)</td><td>138.50 (+12.33%)</td><td>24.56 <b>(-77.86%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>399.80 (n/a)</td><td>230.24 (n/a)</td><td>180.10 (n/a)</td><td>123.30 (n/a)</td><td>110.94 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (+8.64%)</td><td>0.06 (+9.89%)</td><td>0.06 (+8.84%)</td><td>0.05 (+16.82%)</td><td>0.01 (-11.86%)</td><td>158.30 (-14.39%)</td><td>144.82 (-9.37%)</td><td>143.70 (-8.12%)</td><td>127.50 (-7.94%)</td><td>13.00 <b>(-29.99%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>184.90 (n/a)</td><td>159.80 (n/a)</td><td>156.40 (n/a)</td><td>138.50 (n/a)</td><td>18.56 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 <b>(-34.49%)</b></td><td>0.03 <b>(-26.30%)</b></td><td>0.03 <b>(-21.61%)</b></td><td>0.02 <b>(-33.70%)</b></td><td>0.01 <b>(-27.55%)</b></td><td>336.10 <b>(+50.85%)</b></td><td>269.86 <b>(+36.72%)</b></td><td>264.70 <b>(+27.57%)</b></td><td>209.00 <b>(+52.67%)</b></td><td>59.26 <b>(+72.36%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.80 (n/a)</td><td>197.38 (n/a)</td><td>207.50 (n/a)</td><td>136.90 (n/a)</td><td>34.38 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 <b>(+21.94%)</b></td><td>0.04 (+8.01%)</td><td>0.04 (+1.64%)</td><td>0.03 (-14.35%)</td><td>0.01 <b>(+116.47%)</b></td><td>275.40 (+16.74%)</td><td>197.76 (-3.09%)</td><td>205.10 (-1.63%)</td><td>143.20 (-17.98%)</td><td>54.56 <b>(+101.51%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.90 (n/a)</td><td>204.06 (n/a)</td><td>208.50 (n/a)</td><td>174.60 (n/a)</td><td>27.08 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (+3.04%)</td><td>0.05 (+3.13%)</td><td>0.05 (+1.43%)</td><td>0.03 (-14.31%)</td><td>0.01 <b>(+31.43%)</b></td><td>281.50 (+16.71%)</td><td>181.98 (+0.52%)</td><td>176.80 (-1.45%)</td><td>127.10 (-2.98%)</td><td>60.13 <b>(+52.29%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.20 (n/a)</td><td>181.04 (n/a)</td><td>179.40 (n/a)</td><td>131.00 (n/a)</td><td>39.49 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.07 (-5.42%)</td><td>0.05 (+4.45%)</td><td>0.06 (+14.04%)</td><td>0.04 (+4.06%)</td><td>0.01 (-18.38%)</td><td>202.10 (-3.90%)</td><td>154.36 (-5.46%)</td><td>139.60 (-12.31%)</td><td>125.00 (+5.66%)</td><td>30.55 (-16.02%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.30 (n/a)</td><td>163.28 (n/a)</td><td>159.20 (n/a)</td><td>118.30 (n/a)</td><td>36.37 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.07 (+5.53%)</td><td>0.05 (-14.20%)</td><td>0.05 (-18.85%)</td><td>0.04 (-14.54%)</td><td>0.01 <b>(+53.83%)</b></td><td>216.00 (+17.01%)</td><td>172.56 <b>(+20.03%)</b></td><td>169.70 <b>(+23.15%)</b></td><td>118.20 (-5.21%)</td><td>40.54 <b>(+69.81%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>184.60 (n/a)</td><td>143.76 (n/a)</td><td>137.80 (n/a)</td><td>124.70 (n/a)</td><td>23.88 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.07 (-7.47%)</td><td>0.05 (+1.31%)</td><td>0.05 (+8.69%)</td><td>0.04 (+3.88%)</td><td>0.01 <b>(-24.93%)</b></td><td>200.70 (-3.74%)</td><td>167.60 (-3.19%)</td><td>166.50 (-8.01%)</td><td>125.30 (+8.02%)</td><td>29.96 <b>(-22.37%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.50 (n/a)</td><td>173.12 (n/a)</td><td>181.00 (n/a)</td><td>116.00 (n/a)</td><td>38.59 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (+9.25%)</td><td>0.05 (+13.48%)</td><td>0.05 <b>(+25.77%)</b></td><td>0.04 <b>(+27.38%)</b></td><td>0.01 (-6.22%)</td><td>210.30 <b>(-21.50%)</b></td><td>169.52 (-13.32%)</td><td>159.90 <b>(-20.53%)</b></td><td>129.50 (-8.48%)</td><td>34.32 <b>(-30.25%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>267.90 (n/a)</td><td>195.58 (n/a)</td><td>201.20 (n/a)</td><td>141.50 (n/a)</td><td>49.21 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (-4.68%)</td><td>0.05 (-5.55%)</td><td>0.05 (-2.23%)</td><td>0.03 (-19.02%)</td><td>0.01 (+14.52%)</td><td>252.80 <b>(+23.50%)</b></td><td>176.74 (+7.83%)</td><td>163.00 (+2.26%)</td><td>140.30 (+4.94%)</td><td>45.28 <b>(+52.48%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.70 (n/a)</td><td>163.90 (n/a)</td><td>159.40 (n/a)</td><td>133.70 (n/a)</td><td>29.70 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (-14.18%)</td><td>0.05 (-2.26%)</td><td>0.05 (-0.83%)</td><td>0.04 <b>(+21.72%)</b></td><td>0.01 <b>(-47.22%)</b></td><td>182.90 (-17.83%)</td><td>163.30 (-1.09%)</td><td>164.60 (+0.80%)</td><td>131.00 (+16.55%)</td><td>19.58 <b>(-49.85%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.60 (n/a)</td><td>165.10 (n/a)</td><td>163.30 (n/a)</td><td>112.40 (n/a)</td><td>39.03 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (-7.32%)</td><td>0.04 (-19.23%)</td><td>0.04 (-18.29%)</td><td>0.02 <b>(-47.14%)</b></td><td>0.01 <b>(+67.26%)</b></td><td>338.20 <b>(+89.15%)</b></td><td>208.98 <b>(+33.31%)</b></td><td>191.80 <b>(+22.40%)</b></td><td>133.80 (+7.90%)</td><td>76.82 <b>(+263.32%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.80 (n/a)</td><td>156.76 (n/a)</td><td>156.70 (n/a)</td><td>124.00 (n/a)</td><td>21.14 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (-12.51%)</td><td>0.05 (+4.65%)</td><td>0.05 (+12.30%)</td><td>0.04 (+10.41%)</td><td>0.00 <b>(-44.15%)</b></td><td>200.00 (-9.42%)</td><td>176.46 (-6.12%)</td><td>178.20 (-10.94%)</td><td>157.30 (+14.32%)</td><td>18.54 <b>(-41.52%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.80 (n/a)</td><td>187.96 (n/a)</td><td>200.10 (n/a)</td><td>137.60 (n/a)</td><td>31.70 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (-16.62%)</td><td>0.05 (-3.24%)</td><td>0.05 (-0.93%)</td><td>0.04 (+7.64%)</td><td>0.00 <b>(-61.34%)</b></td><td>186.30 (-7.08%)</td><td>171.94 (+1.00%)</td><td>174.00 (+0.93%)</td><td>153.20 (+19.97%)</td><td>12.84 <b>(-57.62%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.50 (n/a)</td><td>170.24 (n/a)</td><td>172.40 (n/a)</td><td>127.70 (n/a)</td><td>30.30 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 <b>(-20.38%)</b></td><td>0.05 (-3.78%)</td><td>0.05 (+0.34%)</td><td>0.04 (+8.96%)</td><td>0.00 <b>(-66.04%)</b></td><td>192.30 (-8.21%)</td><td>179.42 (+1.93%)</td><td>174.60 (-0.34%)</td><td>167.10 <b>(+25.64%)</b></td><td>11.41 <b>(-59.42%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.50 (n/a)</td><td>176.02 (n/a)</td><td>175.20 (n/a)</td><td>133.00 (n/a)</td><td>28.12 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (-2.73%)</td><td>0.04 (-5.17%)</td><td>0.04 (+1.10%)</td><td>0.04 (-8.65%)</td><td>0.00 (-12.09%)</td><td>225.30 (+9.48%)</td><td>194.36 (+5.34%)</td><td>192.70 (-1.08%)</td><td>166.90 (+2.83%)</td><td>20.73 (+1.32%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.80 (n/a)</td><td>184.50 (n/a)</td><td>194.80 (n/a)</td><td>162.30 (n/a)</td><td>20.46 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 (-3.18%)</td><td>0.09 (-7.69%)</td><td>0.09 (-10.00%)</td><td>0.08 (-11.43%)</td><td>0.01 <b>(+43.00%)</b></td><td>192.80 (+12.88%)</td><td>175.02 (+8.78%)</td><td>176.60 (+11.07%)</td><td>152.20 (+3.26%)</td><td>16.31 <b>(+65.13%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>170.80 (n/a)</td><td>160.90 (n/a)</td><td>159.00 (n/a)</td><td>147.40 (n/a)</td><td>9.88 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.13 (-5.54%)</td><td>0.10 (-8.84%)</td><td>0.09 (-6.82%)</td><td>0.08 (-17.65%)</td><td>0.02 (+13.06%)</td><td>214.80 <b>(+21.42%)</b></td><td>171.62 (+10.81%)</td><td>173.90 (+7.35%)</td><td>129.60 (+5.88%)</td><td>30.32 <b>(+46.13%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>176.90 (n/a)</td><td>154.88 (n/a)</td><td>162.00 (n/a)</td><td>122.40 (n/a)</td><td>20.75 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 <b>(+28.46%)</b></td><td>0.09 <b>(+24.94%)</b></td><td>0.08 (+15.15%)</td><td>0.08 <b>(+41.47%)</b></td><td>0.01 (+8.60%)</td><td>208.80 <b>(-29.32%)</b></td><td>186.58 <b>(-20.71%)</b></td><td>195.00 (-13.14%)</td><td>145.90 <b>(-22.19%)</b></td><td>25.77 <b>(-40.77%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>295.40 (n/a)</td><td>235.32 (n/a)</td><td>224.50 (n/a)</td><td>187.50 (n/a)</td><td>43.51 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 (-3.94%)</td><td>0.08 (-1.79%)</td><td>0.08 (-2.77%)</td><td>0.07 <b>(+30.26%)</b></td><td>0.01 <b>(-34.21%)</b></td><td>240.80 <b>(-23.24%)</b></td><td>204.12 (-2.33%)</td><td>203.10 (+2.89%)</td><td>155.50 (+4.08%)</td><td>31.93 <b>(-49.80%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>313.70 (n/a)</td><td>209.00 (n/a)</td><td>197.40 (n/a)</td><td>149.40 (n/a)</td><td>63.60 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.13 (+9.57%)</td><td>0.10 (-0.49%)</td><td>0.11 (+9.30%)</td><td>0.07 (-13.04%)</td><td>0.03 <b>(+100.05%)</b></td><td>230.90 (+14.99%)</td><td>173.00 (+5.84%)</td><td>145.20 (-8.51%)</td><td>129.80 (-8.72%)</td><td>51.85 <b>(+115.57%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>200.80 (n/a)</td><td>163.46 (n/a)</td><td>158.70 (n/a)</td><td>142.20 (n/a)</td><td>24.05 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 (-13.92%)</td><td>0.10 (-6.34%)</td><td>0.10 (-1.17%)</td><td>0.09 (-4.62%)</td><td>0.01 <b>(-31.70%)</b></td><td>186.00 (+4.85%)</td><td>169.08 (+6.30%)</td><td>166.40 (+1.16%)</td><td>155.00 (+16.19%)</td><td>14.49 (-16.69%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>177.40 (n/a)</td><td>159.06 (n/a)</td><td>164.50 (n/a)</td><td>133.40 (n/a)</td><td>17.40 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.13 (+2.83%)</td><td>0.11 (+9.34%)</td><td>0.10 (+9.34%)</td><td>0.08 (-1.96%)</td><td>0.02 <b>(+26.86%)</b></td><td>205.40 (+1.99%)</td><td>158.56 (-7.55%)</td><td>159.60 (-8.54%)</td><td>129.60 (-2.78%)</td><td>31.18 <b>(+25.76%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>201.40 (n/a)</td><td>171.50 (n/a)</td><td>174.50 (n/a)</td><td>133.30 (n/a)</td><td>24.80 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.13 (-2.73%)</td><td>0.11 (+8.94%)</td><td>0.11 (+15.87%)</td><td>0.10 (+10.31%)</td><td>0.01 <b>(-27.79%)</b></td><td>169.80 (-9.34%)</td><td>146.76 (-9.43%)</td><td>142.90 (-13.66%)</td><td>121.80 (+2.78%)</td><td>18.79 <b>(-31.65%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>187.30 (n/a)</td><td>162.04 (n/a)</td><td>165.50 (n/a)</td><td>118.50 (n/a)</td><td>27.49 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 <b>(+22.51%)</b></td><td>0.11 <b>(+24.41%)</b></td><td>0.12 <b>(+35.94%)</b></td><td>0.07 (-0.91%)</td><td>0.02 <b>(+108.73%)</b></td><td>225.00 (+0.90%)</td><td>158.12 (-17.26%)</td><td>134.70 <b>(-26.47%)</b></td><td>133.20 (-18.38%)</td><td>39.58 <b>(+68.53%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>223.00 (n/a)</td><td>191.10 (n/a)</td><td>183.20 (n/a)</td><td>163.20 (n/a)</td><td>23.49 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 <b>(-23.94%)</b></td><td>0.10 (-12.42%)</td><td>0.10 (-2.85%)</td><td>0.08 (+5.60%)</td><td>0.01 <b>(-65.83%)</b></td><td>193.30 (-5.34%)</td><td>169.98 (+9.59%)</td><td>171.30 (+2.94%)</td><td>152.50 <b>(+31.47%)</b></td><td>16.63 <b>(-55.73%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>204.20 (n/a)</td><td>155.10 (n/a)</td><td>166.40 (n/a)</td><td>116.00 (n/a)</td><td>37.55 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (-7.80%)</td><td>0.10 (-3.24%)</td><td>0.10 (-0.19%)</td><td>0.08 (-3.02%)</td><td>0.02 <b>(-21.42%)</b></td><td>206.70 (+3.14%)</td><td>171.66 (+2.41%)</td><td>170.10 (+0.18%)</td><td>133.40 (+8.46%)</td><td>26.26 (-12.77%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>200.40 (n/a)</td><td>167.62 (n/a)</td><td>169.80 (n/a)</td><td>123.00 (n/a)</td><td>30.11 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (-6.54%)</td><td>0.10 (-8.27%)</td><td>0.11 (+8.16%)</td><td>0.07 <b>(-29.76%)</b></td><td>0.02 <b>(+61.07%)</b></td><td>231.40 <b>(+42.31%)</b></td><td>165.18 (+12.17%)</td><td>144.10 (-7.51%)</td><td>134.70 (+6.99%)</td><td>39.53 <b>(+149.33%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>162.60 (n/a)</td><td>147.26 (n/a)</td><td>155.80 (n/a)</td><td>125.90 (n/a)</td><td>15.85 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 (-12.71%)</td><td>0.09 (-11.35%)</td><td>0.09 (-0.65%)</td><td>0.06 <b>(-32.32%)</b></td><td>0.02 (+10.71%)</td><td>280.00 <b>(+47.76%)</b></td><td>193.14 (+15.78%)</td><td>177.00 (+0.63%)</td><td>142.60 (+14.54%)</td><td>51.73 <b>(+99.33%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>189.50 (n/a)</td><td>166.82 (n/a)</td><td>175.90 (n/a)</td><td>124.50 (n/a)</td><td>25.95 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.13 <b>(+26.66%)</b></td><td>0.10 (+11.13%)</td><td>0.10 (+9.80%)</td><td>0.07 (-9.48%)</td><td>0.02 <b>(+174.36%)</b></td><td>222.50 (+10.48%)</td><td>167.48 (-7.27%)</td><td>160.30 (-8.92%)</td><td>130.80 <b>(-21.06%)</b></td><td>36.58 <b>(+139.64%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>201.40 (n/a)</td><td>180.62 (n/a)</td><td>176.00 (n/a)</td><td>165.70 (n/a)</td><td>15.26 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.13 (-0.92%)</td><td>0.10 (-2.88%)</td><td>0.09 (-4.11%)</td><td>0.07 (-11.23%)</td><td>0.02 (-3.19%)</td><td>233.60 (+12.63%)</td><td>177.38 (+3.04%)</td><td>180.20 (+4.28%)</td><td>130.20 (+0.93%)</td><td>37.74 (+7.02%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>207.40 (n/a)</td><td>172.14 (n/a)</td><td>172.80 (n/a)</td><td>129.00 (n/a)</td><td>35.26 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.14 <b>(+37.06%)</b></td><td>0.11 <b>(+21.49%)</b></td><td>0.12 <b>(+29.57%)</b></td><td>0.07 (-13.49%)</td><td>0.02 <b>(+326.58%)</b></td><td>222.60 (+15.58%)</td><td>154.18 (-14.37%)</td><td>140.80 <b>(-22.85%)</b></td><td>120.90 <b>(-27.04%)</b></td><td>39.44 <b>(+281.81%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>192.60 (n/a)</td><td>180.06 (n/a)</td><td>182.50 (n/a)</td><td>165.70 (n/a)</td><td>10.33 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.29 (+8.42%)</td><td>0.21 (+5.81%)</td><td>0.21 (+7.06%)</td><td>0.14 (-17.90%)</td><td>0.07 <b>(+75.39%)</b></td><td>238.90 <b>(+21.76%)</b></td><td>169.56 (+0.51%)</td><td>159.00 (-6.64%)</td><td>114.10 (-7.76%)</td><td>55.93 <b>(+99.31%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>196.20 (n/a)</td><td>168.70 (n/a)</td><td>170.30 (n/a)</td><td>123.70 (n/a)</td><td>28.06 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.26 (+2.78%)</td><td>0.22 (-5.64%)</td><td>0.25 (-1.63%)</td><td>0.15 (-19.72%)</td><td>0.05 <b>(+64.21%)</b></td><td>216.10 <b>(+24.55%)</b></td><td>155.40 (+9.19%)</td><td>132.80 (+1.68%)</td><td>124.70 (-2.73%)</td><td>38.67 <b>(+99.32%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>173.50 (n/a)</td><td>142.32 (n/a)</td><td>130.60 (n/a)</td><td>128.20 (n/a)</td><td>19.40 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.18 (-7.22%)</td><td>0.14 (-11.12%)</td><td>0.15 (+6.02%)</td><td>0.09 <b>(-37.35%)</b></td><td>0.04 <b>(+45.01%)</b></td><td>370.60 <b>(+59.60%)</b></td><td>248.04 (+17.48%)</td><td>217.50 (-5.64%)</td><td>180.90 (+7.81%)</td><td>74.23 <b>(+152.62%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>232.20 (n/a)</td><td>211.14 (n/a)</td><td>230.50 (n/a)</td><td>167.80 (n/a)</td><td>29.38 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.21 <b>(+24.02%)</b></td><td>0.16 (+6.09%)</td><td>0.15 (-8.77%)</td><td>0.13 <b>(+21.76%)</b></td><td>0.03 (+18.65%)</td><td>254.20 (-17.87%)</td><td>206.88 (-6.10%)</td><td>216.60 (+9.62%)</td><td>152.70 (-19.33%)</td><td>37.88 <b>(-24.95%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>309.50 (n/a)</td><td>220.32 (n/a)</td><td>197.60 (n/a)</td><td>189.30 (n/a)</td><td>50.47 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.26 (-0.81%)</td><td>0.20 (+12.19%)</td><td>0.20 (+9.62%)</td><td>0.15 <b>(+36.35%)</b></td><td>0.04 <b>(-35.31%)</b></td><td>217.60 <b>(-26.64%)</b></td><td>171.50 (-16.67%)</td><td>166.40 (-8.77%)</td><td>128.10 (+0.79%)</td><td>33.09 <b>(-53.80%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>296.60 (n/a)</td><td>205.82 (n/a)</td><td>182.40 (n/a)</td><td>127.10 (n/a)</td><td>71.63 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.28 (+7.08%)</td><td>0.21 (+7.70%)</td><td>0.19 (+6.54%)</td><td>0.18 <b>(+32.64%)</b></td><td>0.04 <b>(-21.78%)</b></td><td>178.00 <b>(-24.58%)</b></td><td>159.52 (-9.89%)</td><td>171.20 (-6.09%)</td><td>117.30 (-6.61%)</td><td>25.50 <b>(-43.92%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>236.00 (n/a)</td><td>177.02 (n/a)</td><td>182.30 (n/a)</td><td>125.60 (n/a)</td><td>45.46 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.27 (+15.49%)</td><td>0.22 (+16.11%)</td><td>0.22 (+6.50%)</td><td>0.18 <b>(+25.06%)</b></td><td>0.03 (+3.00%)</td><td>177.60 <b>(-20.07%)</b></td><td>149.32 (-14.51%)</td><td>149.50 (-6.09%)</td><td>123.30 (-13.47%)</td><td>23.10 <b>(-29.74%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>222.20 (n/a)</td><td>174.66 (n/a)</td><td>159.20 (n/a)</td><td>142.50 (n/a)</td><td>32.88 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.26 <b>(+20.77%)</b></td><td>0.24 <b>(+53.18%)</b></td><td>0.25 <b>(+59.29%)</b></td><td>0.19 <b>(+108.05%)</b></td><td>0.03 <b>(-38.44%)</b></td><td>170.10 <b>(-51.92%)</b></td><td>136.90 <b>(-38.96%)</b></td><td>129.20 <b>(-37.25%)</b></td><td>126.40 (-17.17%)</td><td>18.61 <b>(-76.05%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>353.80 (n/a)</td><td>224.28 (n/a)</td><td>205.90 (n/a)</td><td>152.60 (n/a)</td><td>77.70 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.26 (+11.52%)</td><td>0.20 (-5.80%)</td><td>0.22 (+2.33%)</td><td>0.13 <b>(-29.78%)</b></td><td>0.06 <b>(+285.89%)</b></td><td>244.60 <b>(+42.37%)</b></td><td>178.44 (+15.30%)</td><td>151.90 (-2.32%)</td><td>125.60 (-10.35%)</td><td>60.19 <b>(+405.64%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>171.80 (n/a)</td><td>154.76 (n/a)</td><td>155.50 (n/a)</td><td>140.10 (n/a)</td><td>11.90 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.26 (+1.57%)</td><td>0.21 (+14.45%)</td><td>0.23 <b>(+40.68%)</b></td><td>0.15 (-1.24%)</td><td>0.04 (-2.34%)</td><td>218.90 (+1.25%)</td><td>158.60 (-12.67%)</td><td>142.60 <b>(-28.91%)</b></td><td>125.30 (-1.57%)</td><td>36.52 (+1.16%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>216.20 (n/a)</td><td>181.62 (n/a)</td><td>200.60 (n/a)</td><td>127.30 (n/a)</td><td>36.10 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.25 (-3.40%)</td><td>0.21 (+0.12%)</td><td>0.21 (+3.13%)</td><td>0.13 <b>(-20.55%)</b></td><td>0.05 <b>(+34.19%)</b></td><td>247.00 <b>(+25.83%)</b></td><td>164.60 (+2.90%)</td><td>154.80 (-3.07%)</td><td>131.30 (+3.55%)</td><td>47.35 <b>(+80.35%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>196.30 (n/a)</td><td>159.96 (n/a)</td><td>159.70 (n/a)</td><td>126.80 (n/a)</td><td>26.26 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.24 (-9.82%)</td><td>0.19 (-7.68%)</td><td>0.19 (+0.45%)</td><td>0.14 <b>(-21.71%)</b></td><td>0.04 (+5.45%)</td><td>230.40 <b>(+27.72%)</b></td><td>177.38 (+9.62%)</td><td>176.50 (-0.45%)</td><td>135.30 (+10.90%)</td><td>37.03 <b>(+48.00%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>180.40 (n/a)</td><td>161.82 (n/a)</td><td>177.30 (n/a)</td><td>122.00 (n/a)</td><td>25.02 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.26 (+18.09%)</td><td>0.20 (+7.51%)</td><td>0.19 (-7.81%)</td><td>0.16 <b>(+28.53%)</b></td><td>0.04 (-5.23%)</td><td>199.10 <b>(-22.20%)</b></td><td>168.46 (-8.49%)</td><td>169.30 (+8.46%)</td><td>128.50 (-15.29%)</td><td>29.64 <b>(-35.05%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>255.90 (n/a)</td><td>184.08 (n/a)</td><td>156.10 (n/a)</td><td>151.70 (n/a)</td><td>45.64 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.22 (-5.22%)</td><td>0.19 (+3.74%)</td><td>0.18 (+10.56%)</td><td>0.16 <b>(+23.17%)</b></td><td>0.02 <b>(-49.31%)</b></td><td>203.80 (-18.84%)</td><td>173.72 (-7.52%)</td><td>179.30 (-9.54%)</td><td>146.90 (+5.53%)</td><td>22.03 <b>(-54.32%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>251.10 (n/a)</td><td>187.84 (n/a)</td><td>198.20 (n/a)</td><td>139.20 (n/a)</td><td>48.22 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.24 (-12.02%)</td><td>0.20 (+4.14%)</td><td>0.20 (+16.94%)</td><td>0.17 (+18.41%)</td><td>0.03 <b>(-41.13%)</b></td><td>194.00 (-15.54%)</td><td>167.28 (-7.06%)</td><td>162.10 (-14.46%)</td><td>138.00 (+13.58%)</td><td>25.03 <b>(-41.18%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>229.70 (n/a)</td><td>179.98 (n/a)</td><td>189.50 (n/a)</td><td>121.50 (n/a)</td><td>42.55 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.24 (+5.61%)</td><td>0.18 (-15.09%)</td><td>0.17 <b>(-23.88%)</b></td><td>0.12 <b>(-38.70%)</b></td><td>0.05 <b>(+169.76%)</b></td><td>281.60 <b>(+63.15%)</b></td><td>193.74 <b>(+24.53%)</b></td><td>196.90 <b>(+31.35%)</b></td><td>135.50 (-5.31%)</td><td>55.95 <b>(+318.80%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>172.60 (n/a)</td><td>155.58 (n/a)</td><td>149.90 (n/a)</td><td>143.10 (n/a)</td><td>13.36 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.18 (-1.05%)</td><td>0.18 (-0.34%)</td><td>0.18 (-0.06%)</td><td>0.18 (-0.25%)</td><td>0.00 <b>(-68.71%)</b></td><td>47576.60 (+0.25%)</td><td>47461.04 (+0.34%)</td><td>47439.20 (+0.06%)</td><td>47365.90 (+1.06%)</td><td>78.38 <b>(-68.28%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47457.20 (n/a)</td><td>47299.24 (n/a)</td><td>47412.90 (n/a)</td><td>46868.90 (n/a)</td><td>247.09 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.18 (-0.11%)</td><td>0.18 (-0.08%)</td><td>0.18 (-0.03%)</td><td>0.18 (-0.09%)</td><td>0.00 (-5.13%)</td><td>47527.20 (+0.09%)</td><td>47427.68 (+0.08%)</td><td>47408.60 (+0.03%)</td><td>47362.70 (+0.11%)</td><td>61.95 (-5.00%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47485.90 (n/a)</td><td>47391.12 (n/a)</td><td>47392.80 (n/a)</td><td>47312.20 (n/a)</td><td>65.21 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 (+0.00%)</td><td>0.11 (+0.03%)</td><td>0.11 (+0.05%)</td><td>0.11 (+0.05%)</td><td>0.00 <b>(-50.96%)</b></td><td>374445.90 (-0.05%)</td><td>374332.68 (-0.03%)</td><td>374287.60 (-0.05%)</td><td>374264.20 (-0.00%)</td><td>84.66 <b>(-51.00%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.00 (n/a)</td><td>374624.10 (n/a)</td><td>374448.72 (n/a)</td><td>374463.50 (n/a)</td><td>374264.70 (n/a)</td><td>172.78 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.14 <b>(-25.73%)</b></td><td>0.12 <b>(-26.05%)</b></td><td>0.13 <b>(-29.68%)</b></td><td>0.09 <b>(-23.90%)</b></td><td>0.02 <b>(-31.54%)</b></td><td>261.30 <b>(+31.44%)</b></td><td>201.50 <b>(+34.69%)</b></td><td>190.50 <b>(+42.16%)</b></td><td>176.40 <b>(+34.66%)</b></td><td>35.17 <b>(+21.89%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>198.80 (n/a)</td><td>149.60 (n/a)</td><td>134.00 (n/a)</td><td>131.00 (n/a)</td><td>28.86 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.35 (-9.38%)</td><td>0.29 (-4.47%)</td><td>0.28 (-16.63%)</td><td>0.26 <b>(+39.49%)</b></td><td>0.04 <b>(-58.13%)</b></td><td>186.70 <b>(-28.33%)</b></td><td>170.06 (-1.63%)</td><td>173.70 (+19.96%)</td><td>139.80 (+10.34%)</td><td>18.24 <b>(-67.44%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.39 (n/a)</td><td>0.31 (n/a)</td><td>0.34 (n/a)</td><td>0.19 (n/a)</td><td>0.08 (n/a)</td><td>260.50 (n/a)</td><td>172.88 (n/a)</td><td>144.80 (n/a)</td><td>126.70 (n/a)</td><td>56.04 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>12.76 (-4.32%)</td><td>12.50 (-4.54%)</td><td>12.66 (-3.34%)</td><td>12.04 (-6.27%)</td><td>0.31 <b>(+41.52%)</b></td><td>870.80 (+6.69%)</td><td>839.48 (+4.78%)</td><td>828.50 (+3.46%)</td><td>822.00 (+4.53%)</td><td>21.25 <b>(+57.57%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>13.33 (n/a)</td><td>13.09 (n/a)</td><td>13.09 (n/a)</td><td>12.85 (n/a)</td><td>0.22 (n/a)</td><td>816.20 (n/a)</td><td>801.16 (n/a)</td><td>800.80 (n/a)</td><td>786.40 (n/a)</td><td>13.49 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.23 <b>(-23.91%)</b></td><td>0.21 (-18.53%)</td><td>0.21 (-10.68%)</td><td>0.16 <b>(-27.04%)</b></td><td>0.03 (-12.96%)</td><td>248.70 <b>(+37.02%)</b></td><td>201.94 <b>(+23.25%)</b></td><td>193.90 (+11.95%)</td><td>176.80 <b>(+31.35%)</b></td><td>29.73 <b>(+56.75%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.03 (n/a)</td><td>181.50 (n/a)</td><td>163.84 (n/a)</td><td>173.20 (n/a)</td><td>134.60 (n/a)</td><td>18.97 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 <b>(-25.10%)</b></td><td>0.03 (-7.26%)</td><td>0.03 (+3.15%)</td><td>0.03 (+15.97%)</td><td>0.00 <b>(-85.52%)</b></td><td>192.80 (-13.74%)</td><td>181.64 (+2.44%)</td><td>176.80 (-3.02%)</td><td>176.00 <b>(+33.54%)</b></td><td>7.52 <b>(-83.00%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>223.50 (n/a)</td><td>177.32 (n/a)</td><td>182.30 (n/a)</td><td>131.80 (n/a)</td><td>44.23 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (-16.07%)</td><td>0.03 (-11.43%)</td><td>0.02 (-9.25%)</td><td>0.02 (-8.46%)</td><td>0.00 <b>(-27.03%)</b></td><td>188.00 (+9.24%)</td><td>161.64 (+11.91%)</td><td>171.00 (+10.18%)</td><td>132.20 (+19.10%)</td><td>24.88 (-5.54%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>172.10 (n/a)</td><td>144.44 (n/a)</td><td>155.20 (n/a)</td><td>111.00 (n/a)</td><td>26.34 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (+5.72%)</td><td>0.04 (+11.35%)</td><td>0.04 <b>(+20.36%)</b></td><td>0.03 (+4.84%)</td><td>0.01 (+3.44%)</td><td>181.10 (-4.63%)</td><td>145.68 (-10.26%)</td><td>141.60 (-16.90%)</td><td>125.40 (-5.43%)</td><td>23.18 (-7.02%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>189.90 (n/a)</td><td>162.34 (n/a)</td><td>170.40 (n/a)</td><td>132.60 (n/a)</td><td>24.93 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (+12.05%)</td><td>0.03 (+11.59%)</td><td>0.03 <b>(+28.18%)</b></td><td>0.02 (-8.56%)</td><td>0.01 (+11.82%)</td><td>200.60 (+9.32%)</td><td>143.48 (-9.74%)</td><td>138.40 <b>(-21.98%)</b></td><td>110.20 (-10.77%)</td><td>34.08 (+12.93%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>183.50 (n/a)</td><td>158.96 (n/a)</td><td>177.40 (n/a)</td><td>123.50 (n/a)</td><td>30.18 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (-7.46%)</td><td>0.03 (-10.59%)</td><td>0.03 <b>(-23.10%)</b></td><td>0.03 (+5.70%)</td><td>0.00 <b>(-39.67%)</b></td><td>193.30 (-5.38%)</td><td>173.14 (+8.88%)</td><td>179.00 <b>(+30.09%)</b></td><td>136.00 (+8.02%)</td><td>22.26 <b>(-40.64%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>204.30 (n/a)</td><td>159.02 (n/a)</td><td>137.60 (n/a)</td><td>125.90 (n/a)</td><td>37.51 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (+13.33%)</td><td>0.03 (+2.45%)</td><td>0.03 (-3.68%)</td><td>0.02 (+3.81%)</td><td>0.01 <b>(+45.61%)</b></td><td>177.70 (-3.69%)</td><td>155.28 (-1.30%)</td><td>161.80 (+3.78%)</td><td>112.40 (-11.77%)</td><td>25.34 <b>(+20.93%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>184.50 (n/a)</td><td>157.32 (n/a)</td><td>155.90 (n/a)</td><td>127.40 (n/a)</td><td>20.96 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (-5.74%)</td><td>0.03 (-15.35%)</td><td>0.03 <b>(-24.23%)</b></td><td>0.02 (-12.69%)</td><td>0.01 (-4.24%)</td><td>208.60 (+14.55%)</td><td>175.92 (+18.35%)</td><td>183.70 <b>(+31.97%)</b></td><td>135.90 (+6.09%)</td><td>27.16 (+15.43%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>182.10 (n/a)</td><td>148.64 (n/a)</td><td>139.20 (n/a)</td><td>128.10 (n/a)</td><td>23.53 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (-0.98%)</td><td>0.03 (+4.95%)</td><td>0.02 (+11.99%)</td><td>0.02 (+17.46%)</td><td>0.00 <b>(-35.39%)</b></td><td>174.20 (-14.86%)</td><td>163.98 (-6.34%)</td><td>170.20 (-10.70%)</td><td>134.40 (+0.98%)</td><td>16.76 <b>(-45.08%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.60 (n/a)</td><td>175.08 (n/a)</td><td>190.60 (n/a)</td><td>133.10 (n/a)</td><td>30.51 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 <b>(+28.84%)</b></td><td>0.03 (+2.01%)</td><td>0.02 (-14.75%)</td><td>0.02 <b>(+25.58%)</b></td><td>0.01 <b>(+20.58%)</b></td><td>235.60 <b>(-20.38%)</b></td><td>184.74 (-2.88%)</td><td>185.90 (+17.29%)</td><td>119.60 <b>(-22.39%)</b></td><td>42.90 <b>(-29.06%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>295.90 (n/a)</td><td>190.22 (n/a)</td><td>158.50 (n/a)</td><td>154.10 (n/a)</td><td>60.47 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (+11.69%)</td><td>0.03 (+8.24%)</td><td>0.02 (+12.86%)</td><td>0.02 (+8.32%)</td><td>0.00 (+9.47%)</td><td>179.00 (-7.68%)</td><td>158.58 (-7.62%)</td><td>164.70 (-11.40%)</td><td>124.50 (-10.43%)</td><td>23.37 (-9.03%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>193.90 (n/a)</td><td>171.66 (n/a)</td><td>185.90 (n/a)</td><td>139.00 (n/a)</td><td>25.69 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (-12.47%)</td><td>0.03 (-7.74%)</td><td>0.03 (-5.21%)</td><td>0.02 (+2.43%)</td><td>0.00 <b>(-38.09%)</b></td><td>211.30 (-2.36%)</td><td>177.16 (+5.92%)</td><td>179.10 (+5.48%)</td><td>144.40 (+14.33%)</td><td>26.55 <b>(-29.75%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>216.40 (n/a)</td><td>167.26 (n/a)</td><td>169.80 (n/a)</td><td>126.30 (n/a)</td><td>37.79 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (-19.19%)</td><td>0.02 (-9.18%)</td><td>0.02 (-14.97%)</td><td>0.02 <b>(+22.76%)</b></td><td>0.00 <b>(-87.17%)</b></td><td>188.90 (-18.54%)</td><td>183.58 (+7.17%)</td><td>183.70 (+17.61%)</td><td>178.30 <b>(+23.73%)</b></td><td>4.34 <b>(-87.57%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>231.90 (n/a)</td><td>171.30 (n/a)</td><td>156.20 (n/a)</td><td>144.10 (n/a)</td><td>34.93 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (-5.80%)</td><td>0.02 (+16.83%)</td><td>0.02 <b>(+20.05%)</b></td><td>0.02 <b>(+56.99%)</b></td><td>0.00 <b>(-57.52%)</b></td><td>211.60 <b>(-36.28%)</b></td><td>192.28 (-18.57%)</td><td>189.90 (-16.67%)</td><td>170.70 (+6.16%)</td><td>18.62 <b>(-70.94%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>332.10 (n/a)</td><td>236.14 (n/a)</td><td>227.90 (n/a)</td><td>160.80 (n/a)</td><td>64.07 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (-8.58%)</td><td>0.02 (+2.50%)</td><td>0.02 (-5.61%)</td><td>0.02 <b>(+57.21%)</b></td><td>0.00 <b>(-58.81%)</b></td><td>193.00 <b>(-36.39%)</b></td><td>179.98 (-9.11%)</td><td>190.90 (+5.94%)</td><td>148.20 (+9.37%)</td><td>19.05 <b>(-71.55%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>303.40 (n/a)</td><td>198.02 (n/a)</td><td>180.20 (n/a)</td><td>135.50 (n/a)</td><td>66.95 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (-18.54%)</td><td>0.02 (-7.54%)</td><td>0.02 (-5.58%)</td><td>0.02 (+9.72%)</td><td>0.00 <b>(-60.92%)</b></td><td>223.10 (-8.86%)</td><td>203.18 (+4.33%)</td><td>211.80 (+5.90%)</td><td>175.70 <b>(+22.78%)</b></td><td>19.38 <b>(-56.22%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>244.80 (n/a)</td><td>194.74 (n/a)</td><td>200.00 (n/a)</td><td>143.10 (n/a)</td><td>44.28 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 (-7.62%)</td><td>0.02 (-7.97%)</td><td>0.02 (-7.57%)</td><td>0.01 (+5.25%)</td><td>0.00 <b>(-30.99%)</b></td><td>300.30 (-4.97%)</td><td>236.58 (+6.12%)</td><td>237.20 (+8.21%)</td><td>187.40 (+8.26%)</td><td>42.41 <b>(-27.17%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>316.00 (n/a)</td><td>222.94 (n/a)</td><td>219.20 (n/a)</td><td>173.10 (n/a)</td><td>58.23 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.07 (+3.68%)</td><td>0.05 (-2.09%)</td><td>0.05 (-13.75%)</td><td>0.04 (+19.11%)</td><td>0.01 <b>(-25.74%)</b></td><td>183.60 (-16.05%)</td><td>160.76 (-0.22%)</td><td>164.30 (+15.95%)</td><td>123.30 (-3.60%)</td><td>22.40 <b>(-41.86%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.70 (n/a)</td><td>161.12 (n/a)</td><td>141.70 (n/a)</td><td>127.90 (n/a)</td><td>38.52 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.08 (-18.83%)</td><td>0.07 (+1.17%)</td><td>0.07 (+18.73%)</td><td>0.06 (+14.35%)</td><td>0.01 <b>(-49.03%)</b></td><td>203.60 (-12.54%)</td><td>177.30 (-4.01%)</td><td>166.40 (-15.75%)</td><td>157.30 <b>(+23.18%)</b></td><td>22.48 <b>(-43.28%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>232.80 (n/a)</td><td>184.70 (n/a)</td><td>197.50 (n/a)</td><td>127.70 (n/a)</td><td>39.63 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (-6.10%)</td><td>0.05 (-15.24%)</td><td>0.04 (-17.72%)</td><td>0.04 (-4.94%)</td><td>0.01 (-18.13%)</td><td>209.10 (+5.18%)</td><td>185.22 (+17.02%)</td><td>194.50 <b>(+21.56%)</b></td><td>134.40 (+6.50%)</td><td>29.14 (-8.60%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.80 (n/a)</td><td>158.28 (n/a)</td><td>160.00 (n/a)</td><td>126.20 (n/a)</td><td>31.89 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (-1.50%)</td><td>0.05 (+4.76%)</td><td>0.06 (+5.66%)</td><td>0.03 (-7.19%)</td><td>0.01 (-3.44%)</td><td>307.10 (+7.72%)</td><td>202.86 (-4.28%)</td><td>177.20 (-5.34%)</td><td>168.00 (+1.51%)</td><td>58.87 (+9.70%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>285.10 (n/a)</td><td>211.92 (n/a)</td><td>187.20 (n/a)</td><td>165.50 (n/a)</td><td>53.66 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (-16.25%)</td><td>0.05 (-14.45%)</td><td>0.05 (-15.57%)</td><td>0.04 (-13.46%)</td><td>0.00 (-16.32%)</td><td>187.50 (+15.53%)</td><td>175.90 (+16.86%)</td><td>177.60 (+18.40%)</td><td>161.70 (+19.42%)</td><td>12.13 (+15.75%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>162.30 (n/a)</td><td>150.52 (n/a)</td><td>150.00 (n/a)</td><td>135.40 (n/a)</td><td>10.48 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.07 (+8.53%)</td><td>0.06 (+6.02%)</td><td>0.06 (+2.17%)</td><td>0.05 (+11.20%)</td><td>0.01 (+8.15%)</td><td>207.60 (-10.09%)</td><td>179.38 (-5.74%)</td><td>184.80 (-2.12%)</td><td>153.00 (-7.83%)</td><td>21.47 (-12.86%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.90 (n/a)</td><td>190.30 (n/a)</td><td>188.80 (n/a)</td><td>166.00 (n/a)</td><td>24.63 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (-8.72%)</td><td>0.05 (-10.46%)</td><td>0.04 (-11.89%)</td><td>0.04 (+3.86%)</td><td>0.01 <b>(-23.15%)</b></td><td>205.10 (-3.71%)</td><td>176.46 (+10.18%)</td><td>188.20 (+13.51%)</td><td>134.50 (+9.53%)</td><td>28.97 (-18.23%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.00 (n/a)</td><td>160.16 (n/a)</td><td>165.80 (n/a)</td><td>122.80 (n/a)</td><td>35.43 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.07 (+17.33%)</td><td>0.05 (+0.20%)</td><td>0.05 (-11.52%)</td><td>0.04 (+11.80%)</td><td>0.01 <b>(+27.43%)</b></td><td>237.10 (-10.56%)</td><td>192.14 (+0.25%)</td><td>200.10 (+12.99%)</td><td>133.90 (-14.82%)</td><td>38.50 (-9.51%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>265.10 (n/a)</td><td>191.66 (n/a)</td><td>177.10 (n/a)</td><td>157.20 (n/a)</td><td>42.55 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (-6.49%)</td><td>0.05 (-6.46%)</td><td>0.05 (-5.46%)</td><td>0.04 (-12.03%)</td><td>0.00 <b>(+27.92%)</b></td><td>188.70 (+13.74%)</td><td>167.04 (+7.15%)</td><td>163.40 (+5.83%)</td><td>158.70 (+6.94%)</td><td>12.44 <b>(+57.78%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>165.90 (n/a)</td><td>155.90 (n/a)</td><td>154.40 (n/a)</td><td>148.40 (n/a)</td><td>7.89 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (+0.84%)</td><td>0.05 (+8.49%)</td><td>0.05 (+4.16%)</td><td>0.05 <b>(+43.41%)</b></td><td>0.00 <b>(-56.17%)</b></td><td>193.00 <b>(-30.27%)</b></td><td>179.48 (-10.58%)</td><td>180.20 (-4.00%)</td><td>158.10 (-0.82%)</td><td>13.07 <b>(-71.16%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>276.80 (n/a)</td><td>200.72 (n/a)</td><td>187.70 (n/a)</td><td>159.40 (n/a)</td><td>45.32 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (-4.63%)</td><td>0.05 (-4.13%)</td><td>0.04 (+0.69%)</td><td>0.04 (-2.81%)</td><td>0.01 (-5.37%)</td><td>213.30 (+2.89%)</td><td>186.14 (+4.28%)</td><td>188.30 (-0.69%)</td><td>137.30 (+4.89%)</td><td>30.92 (+4.30%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.30 (n/a)</td><td>178.50 (n/a)</td><td>189.60 (n/a)</td><td>130.90 (n/a)</td><td>29.64 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (+0.55%)</td><td>0.04 (-12.72%)</td><td>0.04 (-14.49%)</td><td>0.03 <b>(-26.16%)</b></td><td>0.01 <b>(+66.35%)</b></td><td>312.00 <b>(+35.42%)</b></td><td>226.00 (+17.97%)</td><td>217.10 (+16.91%)</td><td>169.10 (-0.53%)</td><td>53.24 <b>(+126.35%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.40 (n/a)</td><td>191.58 (n/a)</td><td>185.70 (n/a)</td><td>170.00 (n/a)</td><td>23.52 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.05 (-14.63%)</td><td>0.05 (-4.13%)</td><td>0.05 (+5.97%)</td><td>0.04 (+6.18%)</td><td>0.00 <b>(-56.15%)</b></td><td>191.60 (-5.85%)</td><td>176.28 (+2.75%)</td><td>169.00 (-5.64%)</td><td>164.30 (+17.11%)</td><td>12.86 <b>(-50.66%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.50 (n/a)</td><td>171.56 (n/a)</td><td>179.10 (n/a)</td><td>140.30 (n/a)</td><td>26.07 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.06 (-8.05%)</td><td>0.04 <b>(-23.34%)</b></td><td>0.04 <b>(-25.93%)</b></td><td>0.03 <b>(-29.64%)</b></td><td>0.01 <b>(+31.75%)</b></td><td>321.20 <b>(+42.12%)</b></td><td>240.06 <b>(+36.91%)</b></td><td>223.50 <b>(+35.05%)</b></td><td>146.60 (+8.75%)</td><td>71.07 <b>(+105.70%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.00 (n/a)</td><td>175.34 (n/a)</td><td>165.50 (n/a)</td><td>134.80 (n/a)</td><td>34.55 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.04 (-6.64%)</td><td>0.04 (-10.19%)</td><td>0.04 (-13.72%)</td><td>0.03 (-11.10%)</td><td>0.00 (-3.91%)</td><td>242.60 (+12.52%)</td><td>217.26 (+11.45%)</td><td>218.80 (+15.95%)</td><td>190.80 (+7.13%)</td><td>20.65 (+15.15%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>215.60 (n/a)</td><td>194.94 (n/a)</td><td>188.70 (n/a)</td><td>178.10 (n/a)</td><td>17.94 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (-15.27%)</td><td>0.10 (-5.40%)</td><td>0.10 (+4.84%)</td><td>0.07 (-12.67%)</td><td>0.02 <b>(-20.71%)</b></td><td>230.60 (+14.50%)</td><td>169.42 (+5.35%)</td><td>160.90 (-4.62%)</td><td>133.50 (+18.04%)</td><td>36.89 (+14.01%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>201.40 (n/a)</td><td>160.82 (n/a)</td><td>168.70 (n/a)</td><td>113.10 (n/a)</td><td>32.36 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.16 <b>(-20.47%)</b></td><td>0.15 (-14.09%)</td><td>0.15 (-13.16%)</td><td>0.13 (-0.39%)</td><td>0.01 <b>(-55.18%)</b></td><td>186.90 (+0.43%)</td><td>166.02 (+14.53%)</td><td>164.50 (+15.12%)</td><td>150.80 <b>(+25.67%)</b></td><td>13.95 <b>(-44.35%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>186.10 (n/a)</td><td>144.96 (n/a)</td><td>142.90 (n/a)</td><td>120.00 (n/a)</td><td>25.06 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 (-15.37%)</td><td>0.09 <b>(-21.22%)</b></td><td>0.09 <b>(-25.59%)</b></td><td>0.06 <b>(-34.08%)</b></td><td>0.02 (+2.64%)</td><td>295.40 <b>(+51.72%)</b></td><td>200.04 <b>(+30.13%)</b></td><td>187.30 <b>(+34.36%)</b></td><td>146.70 (+18.12%)</td><td>56.08 <b>(+92.01%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>194.70 (n/a)</td><td>153.72 (n/a)</td><td>139.40 (n/a)</td><td>124.20 (n/a)</td><td>29.20 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.13 <b>(-30.47%)</b></td><td>0.11 <b>(-22.18%)</b></td><td>0.12 (-10.79%)</td><td>0.06 <b>(-40.38%)</b></td><td>0.03 (-12.49%)</td><td>325.20 <b>(+67.72%)</b></td><td>196.42 <b>(+33.35%)</b></td><td>169.30 (+12.12%)</td><td>154.60 <b>(+43.81%)</b></td><td>72.41 <b>(+121.13%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>193.90 (n/a)</td><td>147.30 (n/a)</td><td>151.00 (n/a)</td><td>107.50 (n/a)</td><td>32.75 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (-7.54%)</td><td>0.10 (-1.63%)</td><td>0.11 (+16.13%)</td><td>0.08 (-8.41%)</td><td>0.02 (-9.65%)</td><td>203.20 (+9.19%)</td><td>160.90 (+1.59%)</td><td>147.60 (-13.89%)</td><td>132.10 (+8.19%)</td><td>28.93 (+8.19%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>186.10 (n/a)</td><td>158.38 (n/a)</td><td>171.40 (n/a)</td><td>122.10 (n/a)</td><td>26.74 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 <b>(-23.62%)</b></td><td>0.11 <b>(-23.66%)</b></td><td>0.11 <b>(-22.06%)</b></td><td>0.07 <b>(-33.51%)</b></td><td>0.02 (-1.97%)</td><td>285.10 <b>(+50.45%)</b></td><td>199.22 <b>(+33.42%)</b></td><td>181.50 <b>(+28.36%)</b></td><td>164.20 <b>(+30.94%)</b></td><td>48.72 <b>(+98.20%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>189.50 (n/a)</td><td>149.32 (n/a)</td><td>141.40 (n/a)</td><td>125.40 (n/a)</td><td>24.58 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 (+5.07%)</td><td>0.09 (+2.00%)</td><td>0.10 (+6.14%)</td><td>0.07 (-1.03%)</td><td>0.01 (+14.81%)</td><td>229.20 (+1.01%)</td><td>181.14 (-1.57%)</td><td>172.40 (-5.79%)</td><td>150.90 (-4.79%)</td><td>29.45 (+11.55%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>226.90 (n/a)</td><td>184.02 (n/a)</td><td>183.00 (n/a)</td><td>158.50 (n/a)</td><td>26.40 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (-5.86%)</td><td>0.09 (-6.79%)</td><td>0.10 (-12.74%)</td><td>0.07 (+10.87%)</td><td>0.02 <b>(-34.64%)</b></td><td>257.10 (-9.79%)</td><td>201.32 (+3.55%)</td><td>192.90 (+14.62%)</td><td>156.00 (+6.27%)</td><td>36.68 <b>(-36.58%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>285.00 (n/a)</td><td>194.42 (n/a)</td><td>168.30 (n/a)</td><td>146.80 (n/a)</td><td>57.84 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.10 <b>(-21.39%)</b></td><td>0.08 <b>(-21.75%)</b></td><td>0.08 (-19.04%)</td><td>0.06 <b>(-30.31%)</b></td><td>0.02 (-3.04%)</td><td>280.40 <b>(+43.50%)</b></td><td>214.98 <b>(+29.71%)</b></td><td>196.80 <b>(+23.46%)</b></td><td>169.30 <b>(+27.20%)</b></td><td>48.34 <b>(+71.18%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>195.40 (n/a)</td><td>165.74 (n/a)</td><td>159.40 (n/a)</td><td>133.10 (n/a)</td><td>28.24 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.17 (+17.09%)</td><td>0.10 (-10.95%)</td><td>0.10 (-10.74%)</td><td>0.06 <b>(-41.91%)</b></td><td>0.04 <b>(+123.43%)</b></td><td>320.30 <b>(+72.20%)</b></td><td>201.96 <b>(+23.69%)</b></td><td>192.80 (+12.03%)</td><td>111.30 (-14.58%)</td><td>75.87 <b>(+225.77%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>186.00 (n/a)</td><td>163.28 (n/a)</td><td>172.10 (n/a)</td><td>130.30 (n/a)</td><td>23.29 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (-12.73%)</td><td>0.09 (-18.05%)</td><td>0.10 (-11.04%)</td><td>0.05 <b>(-30.83%)</b></td><td>0.03 (+4.59%)</td><td>335.10 <b>(+44.56%)</b></td><td>207.44 <b>(+27.61%)</b></td><td>171.90 (+12.43%)</td><td>132.60 (+14.61%)</td><td>79.72 <b>(+76.71%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>231.80 (n/a)</td><td>162.56 (n/a)</td><td>152.90 (n/a)</td><td>115.70 (n/a)</td><td>45.11 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.09 <b>(-22.80%)</b></td><td>0.07 <b>(-22.34%)</b></td><td>0.08 (-2.58%)</td><td>0.05 <b>(-33.09%)</b></td><td>0.02 (+6.67%)</td><td>345.10 <b>(+49.46%)</b></td><td>257.14 <b>(+32.75%)</b></td><td>213.00 (+2.65%)</td><td>195.00 <b>(+29.48%)</b></td><td>69.75 <b>(+111.94%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>230.90 (n/a)</td><td>193.70 (n/a)</td><td>207.50 (n/a)</td><td>150.60 (n/a)</td><td>32.91 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 (-1.60%)</td><td>0.09 (-2.29%)</td><td>0.09 (+8.23%)</td><td>0.06 (-15.08%)</td><td>0.02 (+1.00%)</td><td>256.00 (+17.76%)</td><td>194.68 (+2.84%)</td><td>188.80 (-7.63%)</td><td>145.20 (+1.61%)</td><td>40.05 (+19.31%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>217.40 (n/a)</td><td>189.30 (n/a)</td><td>204.40 (n/a)</td><td>142.90 (n/a)</td><td>33.57 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.09 <b>(-32.49%)</b></td><td>0.08 (-18.83%)</td><td>0.08 (-12.09%)</td><td>0.05 (-0.66%)</td><td>0.01 <b>(-49.38%)</b></td><td>327.30 (+0.68%)</td><td>239.26 (+16.94%)</td><td>211.80 (+13.75%)</td><td>193.40 <b>(+48.20%)</b></td><td>53.71 <b>(-26.13%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>325.10 (n/a)</td><td>204.60 (n/a)</td><td>186.20 (n/a)</td><td>130.50 (n/a)</td><td>72.72 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.10 (+8.50%)</td><td>0.08 (+0.58%)</td><td>0.08 (-2.96%)</td><td>0.08 (+14.53%)</td><td>0.01 (-4.20%)</td><td>218.40 (-12.67%)</td><td>196.24 (-1.02%)</td><td>196.70 (+3.09%)</td><td>160.70 (-7.86%)</td><td>22.05 <b>(-26.27%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>250.10 (n/a)</td><td>198.26 (n/a)</td><td>190.80 (n/a)</td><td>174.40 (n/a)</td><td>29.90 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.21 (-15.48%)</td><td>0.18 (-11.24%)</td><td>0.19 (-11.54%)</td><td>0.16 (-1.74%)</td><td>0.02 <b>(-43.00%)</b></td><td>210.30 (+1.74%)</td><td>180.08 (+10.97%)</td><td>177.10 (+13.02%)</td><td>157.20 (+18.37%)</td><td>20.47 <b>(-31.03%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>206.70 (n/a)</td><td>162.28 (n/a)</td><td>156.70 (n/a)</td><td>132.80 (n/a)</td><td>29.68 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.25 (+0.06%)</td><td>0.19 (+14.82%)</td><td>0.17 (-1.63%)</td><td>0.17 <b>(+74.77%)</b></td><td>0.04 <b>(-30.97%)</b></td><td>197.90 <b>(-42.79%)</b></td><td>174.74 (-18.56%)</td><td>195.50 (+1.66%)</td><td>133.10 (+0.00%)</td><td>31.05 <b>(-60.96%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>345.90 (n/a)</td><td>214.56 (n/a)</td><td>192.30 (n/a)</td><td>133.10 (n/a)</td><td>79.53 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.32 (-4.53%)</td><td>0.24 (-12.24%)</td><td>0.26 (-3.64%)</td><td>0.16 <b>(-28.37%)</b></td><td>0.06 <b>(+56.50%)</b></td><td>253.40 <b>(+39.61%)</b></td><td>178.28 (+19.23%)</td><td>156.20 (+3.79%)</td><td>129.30 (+4.78%)</td><td>52.23 <b>(+130.89%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.04 (n/a)</td><td>181.50 (n/a)</td><td>149.52 (n/a)</td><td>150.50 (n/a)</td><td>123.40 (n/a)</td><td>22.62 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.18 (-10.52%)</td><td>0.17 (-6.84%)</td><td>0.17 (-5.38%)</td><td>0.16 (-3.82%)</td><td>0.01 <b>(-30.69%)</b></td><td>210.00 (+3.96%)</td><td>194.88 (+7.04%)</td><td>191.40 (+5.69%)</td><td>177.40 (+11.78%)</td><td>13.33 (-18.62%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>202.00 (n/a)</td><td>182.06 (n/a)</td><td>181.10 (n/a)</td><td>158.70 (n/a)</td><td>16.39 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.31 (-1.64%)</td><td>0.23 (-8.27%)</td><td>0.23 (-1.99%)</td><td>0.18 (-12.05%)</td><td>0.05 (+12.56%)</td><td>226.00 (+13.68%)</td><td>183.40 (+10.00%)</td><td>178.90 (+2.00%)</td><td>134.10 (+1.67%)</td><td>33.94 <b>(+28.97%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>198.80 (n/a)</td><td>166.72 (n/a)</td><td>175.40 (n/a)</td><td>131.90 (n/a)</td><td>26.31 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.25 (-16.75%)</td><td>0.21 (+6.82%)</td><td>0.19 (+1.51%)</td><td>0.19 <b>(+23.20%)</b></td><td>0.03 <b>(-49.89%)</b></td><td>170.40 (-18.82%)</td><td>154.96 (-10.08%)</td><td>168.30 (-1.52%)</td><td>131.80 <b>(+20.15%)</b></td><td>19.95 <b>(-50.56%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>209.90 (n/a)</td><td>172.34 (n/a)</td><td>170.90 (n/a)</td><td>109.70 (n/a)</td><td>40.35 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.31 (+9.52%)</td><td>0.20 (-17.98%)</td><td>0.18 <b>(-26.21%)</b></td><td>0.14 <b>(-33.15%)</b></td><td>0.07 <b>(+133.96%)</b></td><td>272.00 <b>(+49.61%)</b></td><td>197.48 <b>(+29.97%)</b></td><td>199.40 <b>(+35.55%)</b></td><td>120.40 (-8.72%)</td><td>56.82 <b>(+206.76%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>181.80 (n/a)</td><td>151.94 (n/a)</td><td>147.10 (n/a)</td><td>131.90 (n/a)</td><td>18.52 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.26 (+4.00%)</td><td>0.22 (+7.70%)</td><td>0.22 (+11.29%)</td><td>0.18 (+13.08%)</td><td>0.03 <b>(-22.19%)</b></td><td>181.90 (-11.57%)</td><td>152.14 (-8.37%)</td><td>149.10 (-10.13%)</td><td>126.40 (-3.88%)</td><td>20.68 <b>(-33.02%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>205.70 (n/a)</td><td>166.04 (n/a)</td><td>165.90 (n/a)</td><td>131.50 (n/a)</td><td>30.88 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.22 <b>(-23.61%)</b></td><td>0.20 (-19.35%)</td><td>0.20 <b>(-20.75%)</b></td><td>0.17 (-6.17%)</td><td>0.02 <b>(-54.85%)</b></td><td>217.30 (+6.57%)</td><td>187.50 <b>(+21.64%)</b></td><td>185.80 <b>(+26.22%)</b></td><td>166.60 <b>(+30.87%)</b></td><td>18.88 <b>(-37.41%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>203.90 (n/a)</td><td>154.14 (n/a)</td><td>147.20 (n/a)</td><td>127.30 (n/a)</td><td>30.16 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.21 (-17.01%)</td><td>0.18 (-9.58%)</td><td>0.18 (-15.27%)</td><td>0.15 (+6.18%)</td><td>0.02 <b>(-50.60%)</b></td><td>213.10 (-5.83%)</td><td>189.50 (+6.92%)</td><td>184.50 (+18.04%)</td><td>156.40 <b>(+20.49%)</b></td><td>23.39 <b>(-45.69%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>226.30 (n/a)</td><td>177.24 (n/a)</td><td>156.30 (n/a)</td><td>129.80 (n/a)</td><td>43.07 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.19 (-18.22%)</td><td>0.17 <b>(-20.47%)</b></td><td>0.17 <b>(-22.13%)</b></td><td>0.13 (-17.53%)</td><td>0.02 (-19.95%)</td><td>269.80 <b>(+21.26%)</b></td><td>212.08 <b>(+25.55%)</b></td><td>205.00 <b>(+28.45%)</b></td><td>183.70 <b>(+22.22%)</b></td><td>35.13 (+16.12%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>222.50 (n/a)</td><td>168.92 (n/a)</td><td>159.60 (n/a)</td><td>150.30 (n/a)</td><td>30.26 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.29 <b>(+23.01%)</b></td><td>0.19 (-8.55%)</td><td>0.18 (-15.98%)</td><td>0.09 <b>(-48.39%)</b></td><td>0.08 <b>(+161.07%)</b></td><td>378.20 <b>(+93.75%)</b></td><td>202.18 <b>(+26.49%)</b></td><td>181.80 (+18.98%)</td><td>111.30 (-18.70%)</td><td>103.21 <b>(+336.05%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>195.20 (n/a)</td><td>159.84 (n/a)</td><td>152.80 (n/a)</td><td>136.90 (n/a)</td><td>23.67 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.20 (-11.06%)</td><td>0.17 (-7.97%)</td><td>0.17 (-13.90%)</td><td>0.16 <b>(+23.27%)</b></td><td>0.01 <b>(-61.01%)</b></td><td>216.20 (-18.87%)</td><td>202.10 (+5.16%)</td><td>203.30 (+16.17%)</td><td>176.50 (+12.42%)</td><td>16.14 <b>(-64.39%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>266.50 (n/a)</td><td>192.18 (n/a)</td><td>175.00 (n/a)</td><td>157.00 (n/a)</td><td>45.31 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.17 (-10.24%)</td><td>0.15 (-2.21%)</td><td>0.16 (+2.63%)</td><td>0.14 (+8.68%)</td><td>0.01 <b>(-50.96%)</b></td><td>230.10 (-7.96%)</td><td>213.10 (+0.94%)</td><td>209.70 (-2.60%)</td><td>192.20 (+11.42%)</td><td>15.77 <b>(-48.82%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>250.00 (n/a)</td><td>211.12 (n/a)</td><td>215.30 (n/a)</td><td>172.50 (n/a)</td><td>30.82 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.16 (+9.58%)</td><td>0.13 (-0.01%)</td><td>0.13 (+0.75%)</td><td>0.09 (-7.95%)</td><td>0.03 <b>(+41.02%)</b></td><td>217.10 (+8.66%)</td><td>164.00 (+1.76%)</td><td>159.80 (-0.75%)</td><td>125.20 (-8.75%)</td><td>35.44 <b>(+41.61%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>199.80 (n/a)</td><td>161.16 (n/a)</td><td>161.00 (n/a)</td><td>137.20 (n/a)</td><td>25.03 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.14 (-9.64%)</td><td>0.13 (+2.90%)</td><td>0.13 (+9.58%)</td><td>0.11 (+13.11%)</td><td>0.01 <b>(-47.68%)</b></td><td>190.80 (-11.58%)</td><td>163.10 (-5.06%)</td><td>162.00 (-8.73%)</td><td>143.30 (+10.66%)</td><td>17.79 <b>(-47.74%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>215.80 (n/a)</td><td>171.80 (n/a)</td><td>177.50 (n/a)</td><td>129.50 (n/a)</td><td>34.04 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (-13.36%)</td><td>0.10 (-13.11%)</td><td>0.11 (-8.13%)</td><td>0.06 <b>(-34.98%)</b></td><td>0.02 <b>(+37.54%)</b></td><td>341.50 <b>(+53.83%)</b></td><td>216.36 <b>(+20.67%)</b></td><td>193.60 (+8.89%)</td><td>164.90 (+15.40%)</td><td>71.78 <b>(+154.37%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>222.00 (n/a)</td><td>179.30 (n/a)</td><td>177.80 (n/a)</td><td>142.90 (n/a)</td><td>28.22 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.13 (+16.92%)</td><td>0.12 (+16.60%)</td><td>0.12 (+13.45%)</td><td>0.10 (+14.94%)</td><td>0.01 (+11.86%)</td><td>205.60 (-12.99%)</td><td>171.54 (-14.28%)</td><td>165.90 (-11.85%)</td><td>154.00 (-14.49%)</td><td>19.89 (-14.75%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>236.30 (n/a)</td><td>200.12 (n/a)</td><td>188.20 (n/a)</td><td>180.10 (n/a)</td><td>23.34 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.15 (-12.28%)</td><td>0.12 (-8.36%)</td><td>0.12 (-10.54%)</td><td>0.10 (-13.84%)</td><td>0.02 (-15.17%)</td><td>215.50 (+16.11%)</td><td>168.24 (+8.98%)</td><td>169.40 (+11.74%)</td><td>135.90 (+14.01%)</td><td>30.43 (+11.68%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>185.60 (n/a)</td><td>154.38 (n/a)</td><td>151.60 (n/a)</td><td>119.20 (n/a)</td><td>27.24 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.14 (-14.55%)</td><td>0.12 (-7.69%)</td><td>0.11 (-4.45%)</td><td>0.10 (-8.62%)</td><td>0.02 <b>(-32.16%)</b></td><td>207.80 (+9.43%)</td><td>177.02 (+7.25%)</td><td>179.40 (+4.67%)</td><td>142.30 (+17.02%)</td><td>23.29 (-12.94%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>189.90 (n/a)</td><td>165.06 (n/a)</td><td>171.40 (n/a)</td><td>121.60 (n/a)</td><td>26.76 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.13 (-6.09%)</td><td>0.11 (-5.91%)</td><td>0.12 (-2.95%)</td><td>0.09 (-5.79%)</td><td>0.02 (+11.53%)</td><td>221.60 (+6.13%)</td><td>189.18 (+6.91%)</td><td>176.10 (+3.04%)</td><td>162.00 (+6.51%)</td><td>29.83 <b>(+27.94%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>208.80 (n/a)</td><td>176.96 (n/a)</td><td>170.90 (n/a)</td><td>152.10 (n/a)</td><td>23.32 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.13 (-19.55%)</td><td>0.10 (-18.32%)</td><td>0.10 (-16.23%)</td><td>0.09 (-19.70%)</td><td>0.02 (-18.62%)</td><td>236.90 <b>(+24.49%)</b></td><td>201.70 <b>(+22.49%)</b></td><td>208.60 (+19.40%)</td><td>159.30 <b>(+24.26%)</b></td><td>31.02 <b>(+26.82%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>190.30 (n/a)</td><td>164.66 (n/a)</td><td>174.70 (n/a)</td><td>128.20 (n/a)</td><td>24.46 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.17 (-10.03%)</td><td>0.13 (-15.67%)</td><td>0.14 (-16.46%)</td><td>0.06 <b>(-47.28%)</b></td><td>0.04 <b>(+46.43%)</b></td><td>380.50 <b>(+89.68%)</b></td><td>209.06 <b>(+30.26%)</b></td><td>177.50 (+19.69%)</td><td>141.20 (+11.09%)</td><td>97.54 <b>(+226.58%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>200.60 (n/a)</td><td>160.50 (n/a)</td><td>148.30 (n/a)</td><td>127.10 (n/a)</td><td>29.87 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.15 (-7.92%)</td><td>0.13 (-5.01%)</td><td>0.13 (-6.47%)</td><td>0.11 (-0.62%)</td><td>0.02 (-17.78%)</td><td>219.80 (+0.59%)</td><td>187.54 (+4.77%)</td><td>193.00 (+6.93%)</td><td>160.50 (+8.59%)</td><td>24.02 (-11.27%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>218.50 (n/a)</td><td>179.00 (n/a)</td><td>180.50 (n/a)</td><td>147.80 (n/a)</td><td>27.08 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.15 (-8.16%)</td><td>0.14 (+4.96%)</td><td>0.14 (+6.35%)</td><td>0.13 <b>(+22.07%)</b></td><td>0.01 <b>(-66.89%)</b></td><td>190.10 (-18.10%)</td><td>176.18 (-6.13%)</td><td>174.30 (-5.99%)</td><td>169.40 (+8.94%)</td><td>8.11 <b>(-70.77%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>232.10 (n/a)</td><td>187.68 (n/a)</td><td>185.40 (n/a)</td><td>155.50 (n/a)</td><td>27.76 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.18 (+9.18%)</td><td>0.15 (+11.94%)</td><td>0.16 <b>(+23.55%)</b></td><td>0.12 (+9.74%)</td><td>0.02 (+9.34%)</td><td>196.90 (-8.88%)</td><td>163.26 (-10.64%)</td><td>150.00 (-19.05%)</td><td>133.80 (-8.42%)</td><td>27.00 (-6.97%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>216.10 (n/a)</td><td>182.70 (n/a)</td><td>185.30 (n/a)</td><td>146.10 (n/a)</td><td>29.02 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.19 (+2.97%)</td><td>0.15 (-1.83%)</td><td>0.12 (-11.81%)</td><td>0.11 (-18.10%)</td><td>0.04 <b>(+86.09%)</b></td><td>223.40 <b>(+22.14%)</b></td><td>177.64 (+5.51%)</td><td>197.80 (+13.42%)</td><td>131.30 (-2.88%)</td><td>41.40 <b>(+117.61%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>182.90 (n/a)</td><td>168.36 (n/a)</td><td>174.40 (n/a)</td><td>135.20 (n/a)</td><td>19.02 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.20 <b>(+29.07%)</b></td><td>0.16 <b>(+28.67%)</b></td><td>0.16 <b>(+33.69%)</b></td><td>0.12 (+10.12%)</td><td>0.03 <b>(+80.03%)</b></td><td>201.90 (-9.18%)</td><td>155.52 <b>(-20.85%)</b></td><td>150.00 <b>(-25.22%)</b></td><td>122.60 <b>(-22.50%)</b></td><td>32.11 <b>(+27.07%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>222.30 (n/a)</td><td>196.50 (n/a)</td><td>200.60 (n/a)</td><td>158.20 (n/a)</td><td>25.27 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.16 (-2.55%)</td><td>0.14 (+9.05%)</td><td>0.14 (+14.46%)</td><td>0.12 (+8.99%)</td><td>0.01 <b>(-32.54%)</b></td><td>197.10 (-8.24%)</td><td>175.94 (-9.03%)</td><td>174.60 (-12.66%)</td><td>156.40 (+2.62%)</td><td>15.65 <b>(-34.34%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>214.80 (n/a)</td><td>193.40 (n/a)</td><td>199.90 (n/a)</td><td>152.40 (n/a)</td><td>23.83 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.18 <b>(+21.39%)</b></td><td>0.15 (+16.59%)</td><td>0.16 <b>(+26.80%)</b></td><td>0.11 (+4.06%)</td><td>0.02 <b>(+67.18%)</b></td><td>217.00 (-3.90%)</td><td>169.74 (-13.14%)</td><td>157.40 <b>(-21.14%)</b></td><td>138.70 (-17.59%)</td><td>29.94 <b>(+35.45%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>225.80 (n/a)</td><td>195.42 (n/a)</td><td>199.60 (n/a)</td><td>168.30 (n/a)</td><td>22.10 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.14 (-12.51%)</td><td>0.12 (-11.59%)</td><td>0.12 (-15.28%)</td><td>0.11 (-2.96%)</td><td>0.01 <b>(-32.16%)</b></td><td>172.70 (+3.04%)</td><td>156.22 (+12.13%)</td><td>157.60 (+18.05%)</td><td>130.90 (+14.22%)</td><td>17.13 <b>(-20.30%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>167.60 (n/a)</td><td>139.32 (n/a)</td><td>133.50 (n/a)</td><td>114.60 (n/a)</td><td>21.49 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.15 (+5.09%)</td><td>0.13 (+3.86%)</td><td>0.13 (+11.67%)</td><td>0.11 (-2.41%)</td><td>0.02 <b>(+35.69%)</b></td><td>168.40 (+2.50%)</td><td>143.68 (-2.88%)</td><td>138.10 (-10.44%)</td><td>120.40 (-4.82%)</td><td>22.25 <b>(+34.66%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>164.30 (n/a)</td><td>147.94 (n/a)</td><td>154.20 (n/a)</td><td>126.50 (n/a)</td><td>16.53 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.15 (-9.83%)</td><td>0.12 (+5.13%)</td><td>0.12 (+17.15%)</td><td>0.08 (-2.94%)</td><td>0.03 (-11.39%)</td><td>222.60 (+3.06%)</td><td>160.92 (-5.11%)</td><td>148.60 (-14.65%)</td><td>126.60 (+10.96%)</td><td>39.06 (+5.19%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>216.00 (n/a)</td><td>169.58 (n/a)</td><td>174.10 (n/a)</td><td>114.10 (n/a)</td><td>37.14 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.14 <b>(+29.43%)</b></td><td>0.11 <b>(+20.77%)</b></td><td>0.11 <b>(+33.11%)</b></td><td>0.09 (+7.27%)</td><td>0.02 <b>(+33.33%)</b></td><td>213.50 (-6.77%)</td><td>169.82 (-16.80%)</td><td>168.50 <b>(-24.88%)</b></td><td>129.30 <b>(-22.76%)</b></td><td>29.85 (-5.22%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>229.00 (n/a)</td><td>204.10 (n/a)</td><td>224.30 (n/a)</td><td>167.40 (n/a)</td><td>31.49 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 (-5.71%)</td><td>0.11 (+2.26%)</td><td>0.11 (+1.74%)</td><td>0.09 <b>(+20.44%)</b></td><td>0.01 <b>(-47.53%)</b></td><td>194.10 (-16.98%)</td><td>173.60 (-3.99%)</td><td>175.00 (-1.69%)</td><td>157.70 (+6.05%)</td><td>14.94 <b>(-54.76%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>233.80 (n/a)</td><td>180.82 (n/a)</td><td>178.00 (n/a)</td><td>148.70 (n/a)</td><td>33.03 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 <b>(-27.43%)</b></td><td>0.10 (-12.77%)</td><td>0.11 (-2.30%)</td><td>0.07 <b>(-20.90%)</b></td><td>0.02 <b>(-37.82%)</b></td><td>271.50 <b>(+26.46%)</b></td><td>189.90 (+13.09%)</td><td>175.00 (+2.40%)</td><td>151.60 <b>(+37.82%)</b></td><td>46.80 (+16.92%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>214.70 (n/a)</td><td>167.92 (n/a)</td><td>170.90 (n/a)</td><td>110.00 (n/a)</td><td>40.03 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 (-16.00%)</td><td>0.10 (-8.67%)</td><td>0.10 (-7.19%)</td><td>0.09 (-2.80%)</td><td>0.01 <b>(-49.44%)</b></td><td>202.00 (+2.90%)</td><td>183.50 (+8.36%)</td><td>187.20 (+7.77%)</td><td>165.20 (+19.11%)</td><td>14.28 <b>(-38.11%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>196.30 (n/a)</td><td>169.34 (n/a)</td><td>173.70 (n/a)</td><td>138.70 (n/a)</td><td>23.07 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.11 (-1.14%)</td><td>0.10 (+0.28%)</td><td>0.10 (+6.35%)</td><td>0.06 <b>(-25.59%)</b></td><td>0.02 <b>(+61.82%)</b></td><td>320.00 <b>(+34.40%)</b></td><td>204.04 (+4.07%)</td><td>175.80 (-5.99%)</td><td>167.00 (+1.15%)</td><td>65.07 <b>(+126.32%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>238.10 (n/a)</td><td>196.06 (n/a)</td><td>187.00 (n/a)</td><td>165.10 (n/a)</td><td>28.75 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.82 (+19.14%)</td><td>0.62 (+13.96%)</td><td>0.63 (+19.50%)</td><td>0.49 (+13.75%)</td><td>0.13 (+7.44%)</td><td>201.00 (-12.11%)</td><td>162.32 (-12.78%)</td><td>155.20 (-16.33%)</td><td>120.20 (-16.12%)</td><td>30.79 <b>(-21.33%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.69 (n/a)</td><td>0.55 (n/a)</td><td>0.53 (n/a)</td><td>0.43 (n/a)</td><td>0.12 (n/a)</td><td>228.70 (n/a)</td><td>186.10 (n/a)</td><td>185.50 (n/a)</td><td>143.30 (n/a)</td><td>39.13 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.60 (-4.02%)</td><td>0.52 (+1.73%)</td><td>0.54 (+7.22%)</td><td>0.39 (-7.07%)</td><td>0.08 (+0.36%)</td><td>251.70 (+7.61%)</td><td>191.58 (-1.39%)</td><td>182.00 (-6.71%)</td><td>164.40 (+4.18%)</td><td>35.01 (+15.70%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.62 (n/a)</td><td>0.52 (n/a)</td><td>0.50 (n/a)</td><td>0.42 (n/a)</td><td>0.08 (n/a)</td><td>233.90 (n/a)</td><td>194.28 (n/a)</td><td>195.10 (n/a)</td><td>157.80 (n/a)</td><td>30.26 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.61 <b>(-37.71%)</b></td><td>0.53 (-15.81%)</td><td>0.52 (-6.93%)</td><td>0.43 (-7.36%)</td><td>0.07 <b>(-63.78%)</b></td><td>228.50 (+7.94%)</td><td>189.74 (+13.13%)</td><td>189.40 (+7.43%)</td><td>162.10 <b>(+60.50%)</b></td><td>27.15 <b>(-34.63%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.97 (n/a)</td><td>0.63 (n/a)</td><td>0.56 (n/a)</td><td>0.46 (n/a)</td><td>0.20 (n/a)</td><td>211.70 (n/a)</td><td>167.72 (n/a)</td><td>176.30 (n/a)</td><td>101.00 (n/a)</td><td>41.53 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.60 (+2.04%)</td><td>0.52 (-1.60%)</td><td>0.54 (+0.58%)</td><td>0.43 (-8.77%)</td><td>0.07 <b>(+41.70%)</b></td><td>228.80 (+9.58%)</td><td>193.26 (+2.54%)</td><td>181.00 (-0.60%)</td><td>164.40 (-2.03%)</td><td>28.79 <b>(+51.12%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.59 (n/a)</td><td>0.53 (n/a)</td><td>0.54 (n/a)</td><td>0.47 (n/a)</td><td>0.05 (n/a)</td><td>208.80 (n/a)</td><td>188.48 (n/a)</td><td>182.10 (n/a)</td><td>167.80 (n/a)</td><td>19.05 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.66 (+6.67%)</td><td>0.55 (-0.12%)</td><td>0.51 (-8.50%)</td><td>0.47 (+2.42%)</td><td>0.08 (+19.48%)</td><td>158.00 (-2.41%)</td><td>136.34 (+0.49%)</td><td>143.30 (+9.31%)</td><td>112.00 (-6.20%)</td><td>18.76 (+8.29%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.62 (n/a)</td><td>0.55 (n/a)</td><td>0.56 (n/a)</td><td>0.46 (n/a)</td><td>0.07 (n/a)</td><td>161.90 (n/a)</td><td>135.68 (n/a)</td><td>131.10 (n/a)</td><td>119.40 (n/a)</td><td>17.32 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.57 (+5.17%)</td><td>0.46 (+8.05%)</td><td>0.43 (+4.74%)</td><td>0.34 (+3.49%)</td><td>0.10 (+14.45%)</td><td>213.80 (-3.39%)</td><td>166.08 (-7.00%)</td><td>170.70 (-4.53%)</td><td>129.60 (-4.92%)</td><td>36.31 (+0.50%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.54 (n/a)</td><td>0.43 (n/a)</td><td>0.41 (n/a)</td><td>0.33 (n/a)</td><td>0.09 (n/a)</td><td>221.30 (n/a)</td><td>178.58 (n/a)</td><td>178.80 (n/a)</td><td>136.30 (n/a)</td><td>36.13 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.55 (-11.27%)</td><td>0.38 (-13.55%)</td><td>0.36 (-10.73%)</td><td>0.27 <b>(-20.04%)</b></td><td>0.11 (-8.14%)</td><td>269.90 <b>(+25.07%)</b></td><td>203.60 (+16.53%)</td><td>206.00 (+12.02%)</td><td>133.80 (+12.72%)</td><td>52.95 <b>(+26.22%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.62 (n/a)</td><td>0.44 (n/a)</td><td>0.40 (n/a)</td><td>0.34 (n/a)</td><td>0.12 (n/a)</td><td>215.80 (n/a)</td><td>174.72 (n/a)</td><td>183.90 (n/a)</td><td>118.70 (n/a)</td><td>41.95 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.62 <b>(+29.55%)</b></td><td>0.39 (-2.12%)</td><td>0.36 (-15.15%)</td><td>0.24 (-4.00%)</td><td>0.14 <b>(+50.89%)</b></td><td>306.10 (+4.15%)</td><td>207.92 (+6.31%)</td><td>203.70 (+17.81%)</td><td>119.30 <b>(-22.78%)</b></td><td>69.16 (+18.86%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.48 (n/a)</td><td>0.40 (n/a)</td><td>0.43 (n/a)</td><td>0.25 (n/a)</td><td>0.09 (n/a)</td><td>293.90 (n/a)</td><td>195.58 (n/a)</td><td>172.90 (n/a)</td><td>154.50 (n/a)</td><td>58.19 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.29 (+17.46%)</td><td>0.24 (+17.03%)</td><td>0.21 (+3.05%)</td><td>0.20 (+16.58%)</td><td>0.04 <b>(+34.96%)</b></td><td>185.10 (-14.23%)</td><td>160.28 (-14.03%)</td><td>177.70 (-2.95%)</td><td>125.50 (-14.92%)</td><td>28.41 (-3.75%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>215.80 (n/a)</td><td>186.44 (n/a)</td><td>183.10 (n/a)</td><td>147.50 (n/a)</td><td>29.52 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.29 (-19.73%)</td><td>0.23 (+1.29%)</td><td>0.24 <b>(+26.30%)</b></td><td>0.16 (-11.39%)</td><td>0.05 <b>(-27.04%)</b></td><td>232.40 (+12.82%)</td><td>170.94 (-2.72%)</td><td>151.90 <b>(-20.80%)</b></td><td>129.00 <b>(+24.64%)</b></td><td>44.61 (+5.65%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.36 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.07 (n/a)</td><td>206.00 (n/a)</td><td>175.72 (n/a)</td><td>191.80 (n/a)</td><td>103.50 (n/a)</td><td>42.22 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.25 (-6.53%)</td><td>0.20 (-1.73%)</td><td>0.21 (-0.07%)</td><td>0.15 (-12.84%)</td><td>0.04 (-10.42%)</td><td>253.10 (+14.73%)</td><td>185.84 (+1.73%)</td><td>174.60 (+0.06%)</td><td>149.50 (+7.02%)</td><td>39.41 (+11.01%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>220.60 (n/a)</td><td>182.68 (n/a)</td><td>174.50 (n/a)</td><td>139.70 (n/a)</td><td>35.50 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.29 (-13.17%)</td><td>0.23 (+6.56%)</td><td>0.23 (+18.84%)</td><td>0.17 <b>(+21.39%)</b></td><td>0.05 <b>(-31.73%)</b></td><td>214.60 (-17.62%)</td><td>167.92 (-10.87%)</td><td>157.20 (-15.85%)</td><td>125.40 (+15.15%)</td><td>40.54 <b>(-34.15%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.34 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>260.50 (n/a)</td><td>188.40 (n/a)</td><td>186.80 (n/a)</td><td>108.90 (n/a)</td><td>61.56 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.31 <b>(+32.70%)</b></td><td>0.22 (+14.18%)</td><td>0.20 (-3.65%)</td><td>0.17 <b>(+35.85%)</b></td><td>0.06 <b>(+39.55%)</b></td><td>213.50 <b>(-26.40%)</b></td><td>172.86 (-12.19%)</td><td>186.90 (+3.78%)</td><td>119.30 <b>(-24.68%)</b></td><td>40.74 <b>(-24.29%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>290.10 (n/a)</td><td>196.86 (n/a)</td><td>180.10 (n/a)</td><td>158.40 (n/a)</td><td>53.81 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.27 (+11.79%)</td><td>0.25 <b>(+23.11%)</b></td><td>0.25 (+19.63%)</td><td>0.22 <b>(+38.40%)</b></td><td>0.02 <b>(-44.01%)</b></td><td>167.70 <b>(-27.75%)</b></td><td>147.42 <b>(-20.18%)</b></td><td>144.70 (-16.41%)</td><td>138.20 (-10.55%)</td><td>11.66 <b>(-63.32%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>232.10 (n/a)</td><td>184.68 (n/a)</td><td>173.10 (n/a)</td><td>154.50 (n/a)</td><td>31.79 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.27 (+7.14%)</td><td>0.22 (-6.45%)</td><td>0.21 (-14.09%)</td><td>0.19 (-9.52%)</td><td>0.03 <b>(+77.60%)</b></td><td>194.10 (+10.54%)</td><td>169.88 (+7.96%)</td><td>175.90 (+16.41%)</td><td>136.80 (-6.68%)</td><td>21.78 <b>(+80.12%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.02 (n/a)</td><td>175.60 (n/a)</td><td>157.36 (n/a)</td><td>151.10 (n/a)</td><td>146.60 (n/a)</td><td>12.09 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.24 (-0.26%)</td><td>0.22 (+5.14%)</td><td>0.23 (+10.57%)</td><td>0.16 (-12.47%)</td><td>0.03 <b>(+41.63%)</b></td><td>236.40 (+14.20%)</td><td>175.56 (-3.46%)</td><td>163.10 (-9.54%)</td><td>151.60 (+0.26%)</td><td>34.74 <b>(+68.37%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>207.00 (n/a)</td><td>181.86 (n/a)</td><td>180.30 (n/a)</td><td>151.20 (n/a)</td><td>20.64 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.34 <b>(+38.85%)</b></td><td>0.27 (+14.31%)</td><td>0.27 (+11.05%)</td><td>0.22 (-3.26%)</td><td>0.06 <b>(+514.88%)</b></td><td>190.10 (+3.37%)</td><td>155.80 (-9.38%)</td><td>153.40 (-9.92%)</td><td>119.30 <b>(-28.00%)</b></td><td>33.02 <b>(+363.91%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.01 (n/a)</td><td>183.90 (n/a)</td><td>171.92 (n/a)</td><td>170.30 (n/a)</td><td>165.70 (n/a)</td><td>7.12 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.34 <b>(+23.32%)</b></td><td>0.25 (+5.72%)</td><td>0.23 (+5.59%)</td><td>0.20 (-4.56%)</td><td>0.05 <b>(+93.23%)</b></td><td>202.90 (+4.75%)</td><td>170.60 (-3.42%)</td><td>177.20 (-5.29%)</td><td>120.70 (-18.88%)</td><td>30.82 <b>(+56.79%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>193.70 (n/a)</td><td>176.64 (n/a)</td><td>187.10 (n/a)</td><td>148.80 (n/a)</td><td>19.66 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.31 (+0.47%)</td><td>0.26 (+4.21%)</td><td>0.27 (+18.52%)</td><td>0.21 (-0.10%)</td><td>0.05 (+13.30%)</td><td>197.20 (+0.10%)</td><td>161.36 (-3.41%)</td><td>151.50 (-15.60%)</td><td>132.10 (-0.45%)</td><td>30.51 (+14.80%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>197.00 (n/a)</td><td>167.06 (n/a)</td><td>179.50 (n/a)</td><td>132.70 (n/a)</td><td>26.58 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.32 (+7.60%)</td><td>0.24 (-3.09%)</td><td>0.23 (-5.07%)</td><td>0.19 (-5.98%)</td><td>0.05 <b>(+26.73%)</b></td><td>211.30 (+6.34%)</td><td>177.08 (+4.25%)</td><td>175.70 (+5.34%)</td><td>126.60 (-7.12%)</td><td>32.32 (+19.86%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>198.70 (n/a)</td><td>169.86 (n/a)</td><td>166.80 (n/a)</td><td>136.30 (n/a)</td><td>26.97 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.32 (-8.61%)</td><td>0.27 (+3.65%)</td><td>0.27 <b>(+23.03%)</b></td><td>0.22 (+6.34%)</td><td>0.05 <b>(-35.17%)</b></td><td>190.20 (-5.93%)</td><td>153.92 (-6.52%)</td><td>154.50 (-18.73%)</td><td>127.10 (+9.47%)</td><td>26.71 <b>(-34.55%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.35 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.07 (n/a)</td><td>202.20 (n/a)</td><td>164.66 (n/a)</td><td>190.10 (n/a)</td><td>116.10 (n/a)</td><td>40.82 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.32 (+2.83%)</td><td>0.27 (+6.71%)</td><td>0.26 (+2.46%)</td><td>0.21 (+6.88%)</td><td>0.05 (+17.43%)</td><td>194.70 (-6.44%)</td><td>159.28 (-5.71%)</td><td>155.40 (-2.39%)</td><td>127.60 (-2.74%)</td><td>31.65 (+5.68%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>208.10 (n/a)</td><td>168.92 (n/a)</td><td>159.20 (n/a)</td><td>131.20 (n/a)</td><td>29.95 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.27 (-16.82%)</td><td>0.25 (-2.32%)</td><td>0.27 (+12.37%)</td><td>0.18 (-8.57%)</td><td>0.04 <b>(-25.88%)</b></td><td>225.20 (+9.37%)</td><td>167.44 (+1.54%)</td><td>152.20 (-11.05%)</td><td>150.60 <b>(+20.19%)</b></td><td>32.42 (-0.24%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>205.90 (n/a)</td><td>164.90 (n/a)</td><td>171.10 (n/a)</td><td>125.30 (n/a)</td><td>32.50 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.27 (+0.28%)</td><td>0.25 (+6.49%)</td><td>0.26 (+15.94%)</td><td>0.21 (-0.11%)</td><td>0.03 (-9.17%)</td><td>198.60 (+0.10%)</td><td>164.20 (-6.27%)</td><td>156.30 (-13.74%)</td><td>150.70 (-0.26%)</td><td>19.86 (-7.18%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>198.40 (n/a)</td><td>175.18 (n/a)</td><td>181.20 (n/a)</td><td>151.10 (n/a)</td><td>21.40 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.26 (+5.87%)</td><td>0.23 (+15.29%)</td><td>0.24 <b>(+20.99%)</b></td><td>0.20 (+12.81%)</td><td>0.02 (-14.62%)</td><td>171.00 (-11.35%)</td><td>150.58 (-13.62%)</td><td>145.60 (-17.37%)</td><td>135.10 (-5.52%)</td><td>14.01 <b>(-26.72%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>192.90 (n/a)</td><td>174.32 (n/a)</td><td>176.20 (n/a)</td><td>143.00 (n/a)</td><td>19.12 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.30 (+10.89%)</td><td>0.20 (-2.22%)</td><td>0.22 (+6.69%)</td><td>0.09 <b>(-48.51%)</b></td><td>0.08 <b>(+113.37%)</b></td><td>388.30 <b>(+94.25%)</b></td><td>200.56 (+17.88%)</td><td>159.90 (-6.27%)</td><td>117.50 (-9.75%)</td><td>107.70 <b>(+318.42%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>199.90 (n/a)</td><td>170.14 (n/a)</td><td>170.60 (n/a)</td><td>130.20 (n/a)</td><td>25.74 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.27 <b>(+22.13%)</b></td><td>0.20 (+8.47%)</td><td>0.19 (+3.57%)</td><td>0.16 (+8.28%)</td><td>0.04 <b>(+41.06%)</b></td><td>219.70 (-7.65%)</td><td>180.30 (-6.92%)</td><td>182.30 (-3.44%)</td><td>127.50 (-18.11%)</td><td>33.49 (+1.94%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>237.90 (n/a)</td><td>193.70 (n/a)</td><td>188.80 (n/a)</td><td>155.70 (n/a)</td><td>32.85 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.28 <b>(+20.35%)</b></td><td>0.19 (+9.46%)</td><td>0.18 (+11.15%)</td><td>0.10 <b>(-35.21%)</b></td><td>0.07 <b>(+106.91%)</b></td><td>350.10 <b>(+54.37%)</b></td><td>202.48 (+1.11%)</td><td>193.80 (-10.03%)</td><td>123.00 (-16.89%)</td><td>88.53 <b>(+176.38%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>226.80 (n/a)</td><td>200.26 (n/a)</td><td>215.40 (n/a)</td><td>148.00 (n/a)</td><td>32.03 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.27 (+2.38%)</td><td>0.22 (+14.41%)</td><td>0.23 <b>(+26.80%)</b></td><td>0.18 (+16.35%)</td><td>0.04 (-15.80%)</td><td>192.60 (-14.06%)</td><td>159.60 (-13.92%)</td><td>149.70 <b>(-21.17%)</b></td><td>128.40 (-2.36%)</td><td>27.52 <b>(-28.48%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>224.10 (n/a)</td><td>185.40 (n/a)</td><td>189.90 (n/a)</td><td>131.50 (n/a)</td><td>38.48 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.19 (-15.48%)</td><td>0.17 (-18.29%)</td><td>0.17 <b>(-23.45%)</b></td><td>0.16 (-11.20%)</td><td>0.01 <b>(-23.79%)</b></td><td>219.80 (+12.60%)</td><td>204.60 <b>(+22.16%)</b></td><td>209.20 <b>(+30.67%)</b></td><td>180.70 (+18.26%)</td><td>16.86 (+1.03%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>195.20 (n/a)</td><td>167.48 (n/a)</td><td>160.10 (n/a)</td><td>152.80 (n/a)</td><td>16.69 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.27 (+18.39%)</td><td>0.21 (+3.70%)</td><td>0.20 (-1.05%)</td><td>0.16 (-13.84%)</td><td>0.04 <b>(+151.69%)</b></td><td>220.70 (+16.10%)</td><td>172.42 (-0.81%)</td><td>175.70 (+1.09%)</td><td>129.90 (-15.54%)</td><td>35.18 <b>(+144.56%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>190.10 (n/a)</td><td>173.82 (n/a)</td><td>173.80 (n/a)</td><td>153.80 (n/a)</td><td>14.39 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.26 (+10.81%)</td><td>0.22 (+10.96%)</td><td>0.22 (+14.67%)</td><td>0.19 <b>(+42.07%)</b></td><td>0.03 <b>(-25.94%)</b></td><td>187.70 <b>(-29.62%)</b></td><td>161.36 (-12.49%)</td><td>156.10 (-12.79%)</td><td>133.50 (-9.80%)</td><td>23.30 <b>(-52.09%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>266.70 (n/a)</td><td>184.40 (n/a)</td><td>179.00 (n/a)</td><td>148.00 (n/a)</td><td>48.64 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>1.11 <b>(+68.29%)</b></td><td>0.79 <b>(+24.44%)</b></td><td>0.65 (+1.50%)</td><td>0.64 (+7.40%)</td><td>0.21 <b>(+581.61%)</b></td><td>205.90 (-6.92%)</td><td>175.20 (-15.76%)</td><td>200.70 (-1.47%)</td><td>118.00 <b>(-40.58%)</b></td><td>39.90 <b>(+288.28%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.66 (n/a)</td><td>0.63 (n/a)</td><td>0.64 (n/a)</td><td>0.59 (n/a)</td><td>0.03 (n/a)</td><td>221.20 (n/a)</td><td>207.98 (n/a)</td><td>203.70 (n/a)</td><td>198.60 (n/a)</td><td>10.27 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.99 (+9.81%)</td><td>0.78 (+8.75%)</td><td>0.78 (+9.56%)</td><td>0.59 (-4.09%)</td><td>0.16 <b>(+43.94%)</b></td><td>221.50 (+4.28%)</td><td>173.92 (-6.49%)</td><td>167.80 (-8.75%)</td><td>132.80 (-8.92%)</td><td>35.84 <b>(+39.05%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.90 (n/a)</td><td>0.72 (n/a)</td><td>0.71 (n/a)</td><td>0.62 (n/a)</td><td>0.11 (n/a)</td><td>212.40 (n/a)</td><td>186.00 (n/a)</td><td>183.90 (n/a)</td><td>145.80 (n/a)</td><td>25.78 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.84 (+12.05%)</td><td>0.74 (+4.50%)</td><td>0.72 (-2.33%)</td><td>0.69 (+15.84%)</td><td>0.06 (-3.56%)</td><td>190.00 (-13.68%)</td><td>178.90 (-4.53%)</td><td>182.90 (+2.35%)</td><td>155.80 (-10.77%)</td><td>13.63 <b>(-27.31%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.75 (n/a)</td><td>0.70 (n/a)</td><td>0.73 (n/a)</td><td>0.60 (n/a)</td><td>0.06 (n/a)</td><td>220.10 (n/a)</td><td>187.38 (n/a)</td><td>178.70 (n/a)</td><td>174.60 (n/a)</td><td>18.76 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.02 <b>(-30.03%)</b></td><td>0.02 (-8.74%)</td><td>0.02 (+0.19%)</td><td>0.02 (+12.21%)</td><td>0.00 <b>(-90.79%)</b></td><td>182.70 (-10.92%)</td><td>177.40 (+6.13%)</td><td>176.90 (-0.17%)</td><td>172.70 <b>(+42.96%)</b></td><td>3.78 <b>(-88.07%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>205.10 (n/a)</td><td>167.16 (n/a)</td><td>177.20 (n/a)</td><td>120.80 (n/a)</td><td>31.73 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (-1.03%)</td><td>0.02 (-8.38%)</td><td>0.02 (-10.68%)</td><td>0.02 (-10.99%)</td><td>0.00 (+12.25%)</td><td>211.50 (+12.38%)</td><td>182.74 (+9.67%)</td><td>182.70 (+12.02%)</td><td>144.40 (+0.98%)</td><td>25.83 <b>(+23.98%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>188.20 (n/a)</td><td>166.62 (n/a)</td><td>163.10 (n/a)</td><td>143.00 (n/a)</td><td>20.83 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (-18.17%)</td><td>0.02 (-9.60%)</td><td>0.02 (+3.88%)</td><td>0.02 (-10.23%)</td><td>0.00 <b>(-46.38%)</b></td><td>231.40 (+11.41%)</td><td>191.78 (+8.34%)</td><td>190.70 (-3.74%)</td><td>162.50 <b>(+22.18%)</b></td><td>25.58 <b>(-26.78%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>207.70 (n/a)</td><td>177.02 (n/a)</td><td>198.10 (n/a)</td><td>133.00 (n/a)</td><td>34.94 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>15.64 (+2.29%)</td><td>13.36 (-2.70%)</td><td>14.94 (+3.56%)</td><td>9.68 (-12.30%)</td><td>2.70 <b>(+46.56%)</b></td><td>216.80 (+14.05%)</td><td>162.90 (+4.97%)</td><td>140.40 (-3.44%)</td><td>134.10 (-2.26%)</td><td>36.73 <b>(+62.45%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>15.29 (n/a)</td><td>13.73 (n/a)</td><td>14.43 (n/a)</td><td>11.04 (n/a)</td><td>1.84 (n/a)</td><td>190.10 (n/a)</td><td>155.18 (n/a)</td><td>145.40 (n/a)</td><td>137.20 (n/a)</td><td>22.61 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.78 <b>(-29.49%)</b></td><td>0.67 <b>(-28.35%)</b></td><td>0.71 <b>(-30.55%)</b></td><td>0.53 (-8.62%)</td><td>0.10 <b>(-50.09%)</b></td><td>247.90 (+9.45%)</td><td>202.30 <b>(+35.06%)</b></td><td>186.80 <b>(+44.02%)</b></td><td>168.40 <b>(+41.87%)</b></td><td>33.14 <b>(-24.74%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>1.11 (n/a)</td><td>0.93 (n/a)</td><td>1.02 (n/a)</td><td>0.58 (n/a)</td><td>0.21 (n/a)</td><td>226.50 (n/a)</td><td>149.78 (n/a)</td><td>129.70 (n/a)</td><td>118.70 (n/a)</td><td>44.03 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.79 <b>(-26.66%)</b></td><td>0.72 (-7.22%)</td><td>0.73 (+7.31%)</td><td>0.60 (+7.44%)</td><td>0.07 <b>(-66.11%)</b></td><td>220.10 (-6.93%)</td><td>186.20 (+2.57%)</td><td>181.90 (-6.81%)</td><td>166.50 <b>(+36.25%)</b></td><td>20.64 <b>(-55.76%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>1.08 (n/a)</td><td>0.77 (n/a)</td><td>0.68 (n/a)</td><td>0.56 (n/a)</td><td>0.22 (n/a)</td><td>236.50 (n/a)</td><td>181.54 (n/a)</td><td>195.20 (n/a)</td><td>122.20 (n/a)</td><td>46.65 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.83 (-8.92%)</td><td>0.65 (-14.23%)</td><td>0.60 (-18.51%)</td><td>0.52 <b>(-24.78%)</b></td><td>0.14 <b>(+46.50%)</b></td><td>255.80 <b>(+32.95%)</b></td><td>209.80 (+19.33%)</td><td>220.20 <b>(+22.74%)</b></td><td>158.40 (+9.77%)</td><td>42.08 <b>(+112.66%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.92 (n/a)</td><td>0.76 (n/a)</td><td>0.74 (n/a)</td><td>0.69 (n/a)</td><td>0.09 (n/a)</td><td>192.40 (n/a)</td><td>175.82 (n/a)</td><td>179.40 (n/a)</td><td>144.30 (n/a)</td><td>19.79 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.82 (-5.98%)</td><td>0.75 (-3.83%)</td><td>0.78 (+0.45%)</td><td>0.61 (-4.86%)</td><td>0.08 (-8.38%)</td><td>215.40 (+5.07%)</td><td>177.88 (+3.91%)</td><td>170.10 (-0.47%)</td><td>160.50 (+6.36%)</td><td>21.54 (+3.78%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.88 (n/a)</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.64 (n/a)</td><td>0.09 (n/a)</td><td>205.00 (n/a)</td><td>171.18 (n/a)</td><td>170.90 (n/a)</td><td>150.90 (n/a)</td><td>20.76 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.82 (-13.55%)</td><td>0.67 (-15.71%)</td><td>0.63 <b>(-20.74%)</b></td><td>0.56 (+0.72%)</td><td>0.12 <b>(-20.85%)</b></td><td>233.90 (-0.72%)</td><td>202.08 (+17.54%)</td><td>209.70 <b>(+26.17%)</b></td><td>160.70 (+15.69%)</td><td>33.57 (-10.79%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.95 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.56 (n/a)</td><td>0.15 (n/a)</td><td>235.60 (n/a)</td><td>171.92 (n/a)</td><td>166.20 (n/a)</td><td>138.90 (n/a)</td><td>37.63 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (+13.51%)</td><td>0.02 (-9.21%)</td><td>0.02 (-13.29%)</td><td>0.02 <b>(-20.19%)</b></td><td>0.01 <b>(+121.42%)</b></td><td>227.00 <b>(+25.28%)</b></td><td>191.48 (+14.84%)</td><td>200.90 (+15.33%)</td><td>120.80 (-11.89%)</td><td>42.17 <b>(+139.90%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>181.20 (n/a)</td><td>166.74 (n/a)</td><td>174.20 (n/a)</td><td>137.10 (n/a)</td><td>17.58 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.03 (+10.96%)</td><td>0.02 (+6.53%)</td><td>0.02 (+6.84%)</td><td>0.02 (+9.82%)</td><td>0.00 <b>(+27.31%)</b></td><td>209.00 (-8.97%)</td><td>177.52 (-5.50%)</td><td>172.80 (-6.39%)</td><td>136.70 (-9.89%)</td><td>30.80 (+7.02%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>229.60 (n/a)</td><td>187.86 (n/a)</td><td>184.60 (n/a)</td><td>151.70 (n/a)</td><td>28.78 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.00 (-2.22%)</td><td>0.00 (-0.94%)</td><td>0.00 (+0.00%)</td><td>0.00 (-2.50%)</td><td>0.00 (+19.34%)</td><td>1059.09 (+3.60%)</td><td>972.42 (+0.77%)</td><td>945.86 (-1.67%)</td><td>925.17 (+1.83%)</td><td>54.18 <b>(+34.06%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1022.30 (n/a)</td><td>965.03 (n/a)</td><td>961.91 (n/a)</td><td>908.56 (n/a)</td><td>40.41 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.01 (+1.20%)</td><td>0.01 (-1.24%)</td><td>0.01 (-2.47%)</td><td>0.01 (-6.33%)</td><td>0.00 <b>(+167.14%)</b></td><td>1104.59 (+7.02%)</td><td>1027.06 (+1.32%)</td><td>1031.70 (+1.44%)</td><td>980.46 (-0.44%)</td><td>50.84 <b>(+168.65%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1032.11 (n/a)</td><td>1013.67 (n/a)</td><td>1017.03 (n/a)</td><td>984.75 (n/a)</td><td>18.92 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.97 (-1.17%)</td><td>0.95 (-1.68%)</td><td>0.95 (-1.75%)</td><td>0.93 (-2.31%)</td><td>0.02 <b>(+21.25%)</b></td><td>2263.62 (+2.37%)</td><td>2212.11 (+1.72%)</td><td>2214.51 (+1.78%)</td><td>2155.49 (+1.18%)</td><td>38.40 <b>(+25.76%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.98 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.01 (n/a)</td><td>2211.25 (n/a)</td><td>2174.79 (n/a)</td><td>2175.75 (n/a)</td><td>2130.37 (n/a)</td><td>30.53 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.39 (-6.86%)</td><td>0.38 (-2.55%)</td><td>0.38 (-0.62%)</td><td>0.38 (+0.83%)</td><td>0.00 <b>(-79.71%)</b></td><td>1389.32 (-0.81%)</td><td>1368.19 (+2.48%)</td><td>1362.24 (+0.63%)</td><td>1359.12 (+7.38%)</td><td>12.34 <b>(-78.32%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.41 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.37 (n/a)</td><td>0.02 (n/a)</td><td>1400.71 (n/a)</td><td>1335.02 (n/a)</td><td>1353.72 (n/a)</td><td>1265.71 (n/a)</td><td>56.89 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.26 (-0.64%)</td><td>0.25 (+2.22%)</td><td>0.26 (+5.62%)</td><td>0.25 (+2.59%)</td><td>0.01 <b>(-29.49%)</b></td><td>2137.08 (-2.56%)</td><td>2059.43 (-2.26%)</td><td>2037.66 (-5.32%)</td><td>1983.32 (+0.63%)</td><td>62.63 <b>(-30.61%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.01 (n/a)</td><td>2193.20 (n/a)</td><td>2107.08 (n/a)</td><td>2152.16 (n/a)</td><td>1970.94 (n/a)</td><td>90.26 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.38 (+2.27%)</td><td>0.37 (+1.29%)</td><td>0.37 (+1.28%)</td><td>0.36 (+0.34%)</td><td>0.01 <b>(+40.95%)</b></td><td>1463.44 (-0.32%)</td><td>1419.09 (-1.26%)</td><td>1410.92 (-1.26%)</td><td>1385.54 (-2.21%)</td><td>30.04 <b>(+37.75%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.01 (n/a)</td><td>1468.11 (n/a)</td><td>1437.17 (n/a)</td><td>1428.91 (n/a)</td><td>1416.92 (n/a)</td><td>21.81 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>5.88 (+4.31%)</td><td>4.81 (-4.85%)</td><td>4.72 (-7.81%)</td><td>3.76 (-9.35%)</td><td>0.97 <b>(+61.57%)</b></td><td>279.10 (+10.32%)</td><td>225.56 (+7.31%)</td><td>222.00 (+8.45%)</td><td>178.40 (-4.14%)</td><td>45.64 <b>(+69.34%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>5.64 (n/a)</td><td>5.05 (n/a)</td><td>5.12 (n/a)</td><td>4.14 (n/a)</td><td>0.60 (n/a)</td><td>253.00 (n/a)</td><td>210.20 (n/a)</td><td>204.70 (n/a)</td><td>186.10 (n/a)</td><td>26.95 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>5.52 (-3.25%)</td><td>4.88 (+6.63%)</td><td>4.76 <b>(+21.86%)</b></td><td>4.57 <b>(+21.40%)</b></td><td>0.37 <b>(-63.20%)</b></td><td>229.40 (-17.63%)</td><td>215.64 (-9.21%)</td><td>220.30 (-17.95%)</td><td>190.10 (+3.37%)</td><td>15.24 <b>(-68.60%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>5.70 (n/a)</td><td>4.58 (n/a)</td><td>3.91 (n/a)</td><td>3.77 (n/a)</td><td>1.01 (n/a)</td><td>278.50 (n/a)</td><td>237.52 (n/a)</td><td>268.50 (n/a)</td><td>183.90 (n/a)</td><td>48.54 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>5.67 (+0.92%)</td><td>4.49 (-8.62%)</td><td>4.23 (-11.62%)</td><td>3.29 <b>(-20.20%)</b></td><td>1.01 <b>(+76.39%)</b></td><td>318.90 <b>(+25.30%)</b></td><td>243.28 (+12.80%)</td><td>247.90 (+13.14%)</td><td>185.00 (-0.91%)</td><td>55.48 <b>(+113.01%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>5.62 (n/a)</td><td>4.92 (n/a)</td><td>4.79 (n/a)</td><td>4.12 (n/a)</td><td>0.58 (n/a)</td><td>254.50 (n/a)</td><td>215.68 (n/a)</td><td>219.10 (n/a)</td><td>186.70 (n/a)</td><td>26.04 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>6.95 <b>(+22.53%)</b></td><td>4.93 (-5.55%)</td><td>4.67 (-10.06%)</td><td>3.90 (-16.27%)</td><td>1.18 <b>(+191.30%)</b></td><td>268.60 (+19.43%)</td><td>221.04 (+9.44%)</td><td>224.60 (+11.19%)</td><td>150.80 (-18.40%)</td><td>43.59 <b>(+172.25%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>5.68 (n/a)</td><td>5.22 (n/a)</td><td>5.19 (n/a)</td><td>4.66 (n/a)</td><td>0.41 (n/a)</td><td>224.90 (n/a)</td><td>201.98 (n/a)</td><td>202.00 (n/a)</td><td>184.80 (n/a)</td><td>16.01 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>8.42 (-12.07%)</td><td>7.97 (-6.03%)</td><td>7.85 (-4.52%)</td><td>7.66 (+0.76%)</td><td>0.34 <b>(-58.44%)</b></td><td>273.80 (-0.76%)</td><td>263.66 (+5.81%)</td><td>267.30 (+4.74%)</td><td>249.20 (+13.74%)</td><td>11.00 <b>(-52.82%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>9.57 (n/a)</td><td>8.48 (n/a)</td><td>8.22 (n/a)</td><td>7.60 (n/a)</td><td>0.81 (n/a)</td><td>275.90 (n/a)</td><td>249.18 (n/a)</td><td>255.20 (n/a)</td><td>219.10 (n/a)</td><td>23.31 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>7.84 <b>(-21.25%)</b></td><td>7.32 (-13.40%)</td><td>7.45 (-4.82%)</td><td>6.47 (-13.25%)</td><td>0.52 <b>(-53.77%)</b></td><td>324.00 (+15.26%)</td><td>287.74 (+14.40%)</td><td>281.50 (+5.04%)</td><td>267.60 <b>(+26.94%)</b></td><td>21.69 <b>(-31.44%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>9.95 (n/a)</td><td>8.45 (n/a)</td><td>7.83 (n/a)</td><td>7.46 (n/a)</td><td>1.12 (n/a)</td><td>281.10 (n/a)</td><td>251.52 (n/a)</td><td>268.00 (n/a)</td><td>210.80 (n/a)</td><td>31.64 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>8.17 (-12.58%)</td><td>7.30 (-6.43%)</td><td>7.07 (-1.86%)</td><td>6.38 (-4.68%)</td><td>0.77 <b>(-32.68%)</b></td><td>328.70 (+4.92%)</td><td>289.66 (+6.07%)</td><td>296.50 (+1.89%)</td><td>256.80 (+14.39%)</td><td>30.37 (-19.96%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>9.34 (n/a)</td><td>7.81 (n/a)</td><td>7.21 (n/a)</td><td>6.69 (n/a)</td><td>1.14 (n/a)</td><td>313.30 (n/a)</td><td>273.08 (n/a)</td><td>291.00 (n/a)</td><td>224.50 (n/a)</td><td>37.95 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>9.93 (+19.56%)</td><td>8.01 (+1.68%)</td><td>7.90 (-2.80%)</td><td>7.04 (-4.48%)</td><td>1.16 <b>(+158.06%)</b></td><td>298.00 (+4.71%)</td><td>265.74 (-0.42%)</td><td>265.60 (+2.87%)</td><td>211.20 (-16.36%)</td><td>34.46 <b>(+123.25%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>8.30 (n/a)</td><td>7.88 (n/a)</td><td>8.12 (n/a)</td><td>7.37 (n/a)</td><td>0.45 (n/a)</td><td>284.60 (n/a)</td><td>266.86 (n/a)</td><td>258.20 (n/a)</td><td>252.50 (n/a)</td><td>15.44 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>8.69 (-4.35%)</td><td>8.10 (+2.55%)</td><td>8.07 (+4.75%)</td><td>7.58 (+5.16%)</td><td>0.41 <b>(-42.73%)</b></td><td>276.70 (-4.88%)</td><td>259.50 (-2.88%)</td><td>260.00 (-4.55%)</td><td>241.40 (+4.55%)</td><td>12.92 <b>(-42.16%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>9.08 (n/a)</td><td>7.90 (n/a)</td><td>7.70 (n/a)</td><td>7.21 (n/a)</td><td>0.71 (n/a)</td><td>290.90 (n/a)</td><td>267.20 (n/a)</td><td>272.40 (n/a)</td><td>230.90 (n/a)</td><td>22.34 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>9.24 (-12.97%)</td><td>8.27 (-4.66%)</td><td>7.80 (-12.24%)</td><td>7.59 (+10.65%)</td><td>0.78 <b>(-43.07%)</b></td><td>276.10 (-9.62%)</td><td>255.38 (+3.49%)</td><td>268.80 (+13.95%)</td><td>227.00 (+14.94%)</td><td>23.33 <b>(-41.35%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>10.62 (n/a)</td><td>8.67 (n/a)</td><td>8.89 (n/a)</td><td>6.86 (n/a)</td><td>1.37 (n/a)</td><td>305.50 (n/a)</td><td>246.76 (n/a)</td><td>235.90 (n/a)</td><td>197.50 (n/a)</td><td>39.77 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>11.41 (-4.70%)</td><td>10.30 (-9.75%)</td><td>10.49 (-10.33%)</td><td>8.64 (-19.13%)</td><td>1.11 <b>(+72.25%)</b></td><td>485.60 <b>(+23.66%)</b></td><td>411.22 (+11.62%)</td><td>399.90 (+11.52%)</td><td>367.50 (+4.94%)</td><td>47.21 <b>(+123.95%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>11.98 (n/a)</td><td>11.41 (n/a)</td><td>11.70 (n/a)</td><td>10.68 (n/a)</td><td>0.64 (n/a)</td><td>392.70 (n/a)</td><td>368.42 (n/a)</td><td>358.60 (n/a)</td><td>350.20 (n/a)</td><td>21.08 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>12.94 (-2.47%)</td><td>12.21 (-1.86%)</td><td>12.57 (-2.73%)</td><td>11.09 (+2.82%)</td><td>0.74 <b>(-29.92%)</b></td><td>378.40 (-2.72%)</td><td>344.72 (+1.59%)</td><td>333.80 (+2.83%)</td><td>324.20 (+2.53%)</td><td>21.66 <b>(-29.55%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>13.26 (n/a)</td><td>12.44 (n/a)</td><td>12.92 (n/a)</td><td>10.78 (n/a)</td><td>1.05 (n/a)</td><td>389.00 (n/a)</td><td>339.32 (n/a)</td><td>324.60 (n/a)</td><td>316.20 (n/a)</td><td>30.75 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>13.05 (+11.51%)</td><td>11.08 (+0.59%)</td><td>10.91 (-2.21%)</td><td>9.35 (-7.84%)</td><td>1.34 <b>(+115.56%)</b></td><td>448.80 (+8.51%)</td><td>382.82 (+0.31%)</td><td>384.60 (+2.26%)</td><td>321.30 (-10.33%)</td><td>45.80 <b>(+108.93%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>11.71 (n/a)</td><td>11.02 (n/a)</td><td>11.15 (n/a)</td><td>10.14 (n/a)</td><td>0.62 (n/a)</td><td>413.60 (n/a)</td><td>381.62 (n/a)</td><td>376.10 (n/a)</td><td>358.30 (n/a)</td><td>21.92 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>14.25 (-0.87%)</td><td>12.39 (-4.83%)</td><td>12.22 (-4.70%)</td><td>11.58 (-5.56%)</td><td>1.08 <b>(+22.32%)</b></td><td>362.10 (+5.88%)</td><td>340.34 (+5.28%)</td><td>343.10 (+4.92%)</td><td>294.40 (+0.86%)</td><td>27.21 <b>(+28.76%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>14.37 (n/a)</td><td>13.02 (n/a)</td><td>12.83 (n/a)</td><td>12.27 (n/a)</td><td>0.88 (n/a)</td><td>342.00 (n/a)</td><td>323.26 (n/a)</td><td>327.00 (n/a)</td><td>291.90 (n/a)</td><td>21.13 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>14.66 (-1.96%)</td><td>12.63 (-2.22%)</td><td>12.69 (-7.65%)</td><td>11.37 (+19.00%)</td><td>1.29 <b>(-38.06%)</b></td><td>368.80 (-15.95%)</td><td>334.74 (+0.60%)</td><td>330.60 (+8.29%)</td><td>286.20 (+2.00%)</td><td>32.39 <b>(-48.34%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>14.95 (n/a)</td><td>12.92 (n/a)</td><td>13.74 (n/a)</td><td>9.56 (n/a)</td><td>2.08 (n/a)</td><td>438.80 (n/a)</td><td>332.76 (n/a)</td><td>305.30 (n/a)</td><td>280.60 (n/a)</td><td>62.70 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>15.32 (-0.01%)</td><td>13.07 (-4.15%)</td><td>12.88 (-5.05%)</td><td>11.94 (+0.53%)</td><td>1.36 (+10.86%)</td><td>351.30 (-0.54%)</td><td>323.54 (+4.47%)</td><td>325.70 (+5.34%)</td><td>273.70 (+0.00%)</td><td>31.16 (+9.20%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>15.32 (n/a)</td><td>13.63 (n/a)</td><td>13.56 (n/a)</td><td>11.88 (n/a)</td><td>1.23 (n/a)</td><td>353.20 (n/a)</td><td>309.70 (n/a)</td><td>309.20 (n/a)</td><td>273.70 (n/a)</td><td>28.54 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>14.71 (-5.35%)</td><td>13.99 (+3.59%)</td><td>13.97 (+7.21%)</td><td>12.76 (+5.17%)</td><td>0.77 <b>(-43.89%)</b></td><td>328.70 (-4.92%)</td><td>300.62 (-3.97%)</td><td>300.20 (-6.71%)</td><td>285.20 (+5.67%)</td><td>17.20 <b>(-43.24%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>15.54 (n/a)</td><td>13.50 (n/a)</td><td>13.03 (n/a)</td><td>12.13 (n/a)</td><td>1.37 (n/a)</td><td>345.70 (n/a)</td><td>313.06 (n/a)</td><td>321.80 (n/a)</td><td>269.90 (n/a)</td><td>30.30 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>14.06 (+3.29%)</td><td>12.12 (-2.11%)</td><td>12.33 (-4.13%)</td><td>8.94 (-14.72%)</td><td>2.02 <b>(+62.79%)</b></td><td>469.10 (+17.28%)</td><td>355.22 (+3.92%)</td><td>340.30 (+4.32%)</td><td>298.40 (-3.18%)</td><td>68.27 <b>(+85.91%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>13.61 (n/a)</td><td>12.38 (n/a)</td><td>12.86 (n/a)</td><td>10.49 (n/a)</td><td>1.24 (n/a)</td><td>400.00 (n/a)</td><td>341.82 (n/a)</td><td>326.20 (n/a)</td><td>308.20 (n/a)</td><td>36.72 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>3.38 (+15.84%)</td><td>2.85 (+6.59%)</td><td>2.60 (-0.37%)</td><td>2.41 (-4.01%)</td><td>0.45 <b>(+172.50%)</b></td><td>217.80 (+4.16%)</td><td>187.56 (-4.68%)</td><td>201.70 (+0.35%)</td><td>154.90 (-13.70%)</td><td>28.21 <b>(+141.60%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>2.92 (n/a)</td><td>2.67 (n/a)</td><td>2.61 (n/a)</td><td>2.51 (n/a)</td><td>0.16 (n/a)</td><td>209.10 (n/a)</td><td>196.76 (n/a)</td><td>201.00 (n/a)</td><td>179.50 (n/a)</td><td>11.68 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>5.63 (-7.96%)</td><td>4.74 (+7.30%)</td><td>4.74 (+10.15%)</td><td>4.04 <b>(+22.43%)</b></td><td>0.62 <b>(-43.39%)</b></td><td>259.70 (-18.33%)</td><td>224.00 (-9.68%)</td><td>221.10 (-9.24%)</td><td>186.10 (+8.64%)</td><td>28.35 <b>(-49.28%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>6.12 (n/a)</td><td>4.42 (n/a)</td><td>4.31 (n/a)</td><td>3.30 (n/a)</td><td>1.09 (n/a)</td><td>318.00 (n/a)</td><td>248.02 (n/a)</td><td>243.60 (n/a)</td><td>171.30 (n/a)</td><td>55.90 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>8.15 (-0.65%)</td><td>7.15 (+2.57%)</td><td>7.20 (+1.83%)</td><td>6.16 (+4.89%)</td><td>0.75 <b>(-22.46%)</b></td><td>340.60 (-4.67%)</td><td>295.94 (-3.15%)</td><td>291.20 (-1.82%)</td><td>257.30 (+0.67%)</td><td>31.61 <b>(-26.20%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>8.20 (n/a)</td><td>6.97 (n/a)</td><td>7.07 (n/a)</td><td>5.87 (n/a)</td><td>0.97 (n/a)</td><td>357.30 (n/a)</td><td>305.58 (n/a)</td><td>296.60 (n/a)</td><td>255.60 (n/a)</td><td>42.84 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>3.90 <b>(+36.25%)</b></td><td>2.58 (-3.55%)</td><td>2.54 (-10.35%)</td><td>1.50 <b>(-34.52%)</b></td><td>0.87 <b>(+243.04%)</b></td><td>349.50 <b>(+52.69%)</b></td><td>223.26 (+13.07%)</td><td>206.10 (+11.53%)</td><td>134.60 <b>(-26.61%)</b></td><td>79.20 <b>(+294.94%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>2.86 (n/a)</td><td>2.68 (n/a)</td><td>2.84 (n/a)</td><td>2.29 (n/a)</td><td>0.25 (n/a)</td><td>228.90 (n/a)</td><td>197.46 (n/a)</td><td>184.80 (n/a)</td><td>183.40 (n/a)</td><td>20.05 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.24 (-5.83%)</td><td>0.18 (-12.82%)</td><td>0.16 <b>(-25.61%)</b></td><td>0.15 (-9.41%)</td><td>0.04 (+8.37%)</td><td>218.10 (+10.37%)</td><td>183.80 (+15.85%)</td><td>202.50 <b>(+34.37%)</b></td><td>136.00 (+6.17%)</td><td>37.46 <b>(+27.37%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>197.60 (n/a)</td><td>158.66 (n/a)</td><td>150.70 (n/a)</td><td>128.10 (n/a)</td><td>29.41 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.23 (-6.94%)</td><td>0.18 (-3.97%)</td><td>0.18 (-1.42%)</td><td>0.15 (-2.96%)</td><td>0.03 (-14.02%)</td><td>217.50 (+3.08%)</td><td>187.42 (+3.59%)</td><td>182.50 (+1.45%)</td><td>141.10 (+7.46%)</td><td>31.50 (-4.46%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>211.00 (n/a)</td><td>180.92 (n/a)</td><td>179.90 (n/a)</td><td>131.30 (n/a)</td><td>32.97 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.44 (-10.32%)</td><td>0.38 (-1.01%)</td><td>0.39 (-4.42%)</td><td>0.31 (+3.81%)</td><td>0.05 <b>(-38.34%)</b></td><td>212.50 (-3.67%)</td><td>176.26 (-1.17%)</td><td>170.20 (+4.61%)</td><td>149.90 (+11.53%)</td><td>24.41 <b>(-36.06%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.49 (n/a)</td><td>0.38 (n/a)</td><td>0.40 (n/a)</td><td>0.30 (n/a)</td><td>0.08 (n/a)</td><td>220.60 (n/a)</td><td>178.34 (n/a)</td><td>162.70 (n/a)</td><td>134.40 (n/a)</td><td>38.17 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.55 <b>(+26.29%)</b></td><td>0.41 (+14.10%)</td><td>0.37 (+6.10%)</td><td>0.32 (+5.79%)</td><td>0.09 <b>(+80.99%)</b></td><td>207.20 (-5.47%)</td><td>165.58 (-10.57%)</td><td>174.90 (-5.77%)</td><td>118.70 <b>(-20.87%)</b></td><td>32.92 <b>(+34.35%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.44 (n/a)</td><td>0.36 (n/a)</td><td>0.35 (n/a)</td><td>0.30 (n/a)</td><td>0.05 (n/a)</td><td>219.20 (n/a)</td><td>185.16 (n/a)</td><td>185.60 (n/a)</td><td>150.00 (n/a)</td><td>24.50 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.53 <b>(+45.46%)</b></td><td>0.41 <b>(+22.99%)</b></td><td>0.40 (+16.25%)</td><td>0.30 (+5.55%)</td><td>0.09 <b>(+133.77%)</b></td><td>220.30 (-5.25%)</td><td>167.44 (-16.51%)</td><td>163.70 (-13.98%)</td><td>124.10 <b>(-31.25%)</b></td><td>36.32 <b>(+54.15%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.36 (n/a)</td><td>0.33 (n/a)</td><td>0.34 (n/a)</td><td>0.28 (n/a)</td><td>0.04 (n/a)</td><td>232.50 (n/a)</td><td>200.54 (n/a)</td><td>190.30 (n/a)</td><td>180.50 (n/a)</td><td>23.56 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.85 <b>(-24.96%)</b></td><td>0.67 (-16.25%)</td><td>0.61 (-16.77%)</td><td>0.59 (+2.22%)</td><td>0.11 <b>(-53.25%)</b></td><td>223.20 (-2.15%)</td><td>198.30 (+13.74%)</td><td>215.10 <b>(+20.17%)</b></td><td>153.80 <b>(+33.28%)</b></td><td>29.85 <b>(-39.03%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>1.14 (n/a)</td><td>0.81 (n/a)</td><td>0.73 (n/a)</td><td>0.57 (n/a)</td><td>0.24 (n/a)</td><td>228.10 (n/a)</td><td>174.34 (n/a)</td><td>179.00 (n/a)</td><td>115.40 (n/a)</td><td>48.95 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>1.03 (-0.47%)</td><td>0.77 (-0.04%)</td><td>0.71 (+3.17%)</td><td>0.53 (-15.05%)</td><td>0.23 <b>(+27.15%)</b></td><td>247.60 (+17.74%)</td><td>181.76 (+3.12%)</td><td>183.80 (-3.06%)</td><td>127.20 (+0.47%)</td><td>52.28 <b>(+43.83%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>1.04 (n/a)</td><td>0.77 (n/a)</td><td>0.69 (n/a)</td><td>0.62 (n/a)</td><td>0.18 (n/a)</td><td>210.30 (n/a)</td><td>176.26 (n/a)</td><td>189.60 (n/a)</td><td>126.60 (n/a)</td><td>36.35 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>1.00 <b>(+24.74%)</b></td><td>0.71 (-5.25%)</td><td>0.63 (-18.07%)</td><td>0.47 <b>(-28.04%)</b></td><td>0.25 <b>(+358.94%)</b></td><td>277.80 <b>(+38.97%)</b></td><td>203.78 (+16.05%)</td><td>208.20 <b>(+22.04%)</b></td><td>131.50 (-19.82%)</td><td>68.85 <b>(+392.13%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.80 (n/a)</td><td>0.75 (n/a)</td><td>0.77 (n/a)</td><td>0.66 (n/a)</td><td>0.05 (n/a)</td><td>199.90 (n/a)</td><td>175.60 (n/a)</td><td>170.60 (n/a)</td><td>164.00 (n/a)</td><td>13.99 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.80 <b>(-24.01%)</b></td><td>0.72 (-6.75%)</td><td>0.73 (+0.72%)</td><td>0.58 (-10.03%)</td><td>0.09 <b>(-48.40%)</b></td><td>225.90 (+11.17%)</td><td>183.76 (+5.35%)</td><td>178.70 (-0.72%)</td><td>163.20 <b>(+31.61%)</b></td><td>24.54 <b>(-20.56%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>1.06 (n/a)</td><td>0.77 (n/a)</td><td>0.73 (n/a)</td><td>0.64 (n/a)</td><td>0.16 (n/a)</td><td>203.20 (n/a)</td><td>174.42 (n/a)</td><td>180.00 (n/a)</td><td>124.00 (n/a)</td><td>30.89 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:38:02</td><td>0.12 <b>(+20.91%)</b></td><td>0.10 <b>(+26.76%)</b></td><td>0.10 <b>(+39.74%)</b></td><td>0.09 <b>(+42.26%)</b></td><td>0.02 (-9.87%)</td><td>191.70 <b>(-29.73%)</b></td><td>165.64 <b>(-22.63%)</b></td><td>160.90 <b>(-28.43%)</b></td><td>131.60 (-17.34%)</td><td>24.99 <b>(-45.65%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:22:55</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>272.80 (n/a)</td><td>214.10 (n/a)</td><td>224.80 (n/a)</td><td>159.20 (n/a)</td><td>45.99 (n/a)</td>
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
