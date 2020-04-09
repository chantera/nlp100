#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
95. WordSimilarity-353での評価
94で作ったデータを用い，各モデルが出力する類似度のランキングと，人間の類似度判定のランキングの間のスピアマン相関係数を計算せよ．
"""

import sys


ranking_hum = {}
ranking_n94 = {}

data = {}
for line in open(sys.argv[1]):
    cols = line.strip().split("\t")
    data[(cols[0], cols[1])] = (float(cols[2]), float(cols[3]))

for rank, (key, value) in enumerate(sorted(data.items(), key=lambda x: -x[1][0])):
    ranking_hum[key] = rank + 1

for rank, (key, value) in enumerate(sorted(data.items(), key=lambda x: -x[1][1])):
    ranking_n94[key] = rank + 1

N = len(data)
correlation = 1 - (6.0 * sum([(ranking_hum[key] - ranking_n94[key]) ** 2 for key in data.keys()]) / (N ** 3 - N))
print(correlation)
