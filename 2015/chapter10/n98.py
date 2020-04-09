#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
98. Ward法によるクラスタリング
96の単語ベクトルに対して，Ward法による階層型クラスタリングを実行せよ．さらに，クラスタリング結果をデンドログラムとして可視化せよ．
"""

from n90 import load_model
from n96 import get_country_vector
import numpy as np
from scipy.cluster.hierarchy import ward, dendrogram
import matplotlib.pyplot as plt
import sys


vector = get_country_vector(load_model(sys.argv[1]))
dendrogram(ward(np.array(list(vector.values()))), labels=list(vector.keys()))
plt.show()
