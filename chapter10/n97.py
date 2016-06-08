#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
97. k-meansクラスタリング
96の単語ベクトルに対して，k-meansクラスタリングをクラスタ数k=5として実行せよ．
"""

from n90 import load_model
from n96 import get_country_vector
import numpy as np
from sklearn.cluster import KMeans
import sys


vector = get_country_vector(load_model(sys.argv[1]))
km_model = KMeans(n_clusters=5).fit(np.array(list(vector.values())))
for label, country in sorted(zip(km_model.labels_, vector.keys()), key=lambda x: x[0]):
    print(label, country)
