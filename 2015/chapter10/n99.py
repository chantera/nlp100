#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
99. t-SNEによる可視化
96の単語ベクトルに対して，ベクトル空間をt-SNEで可視化せよ．
"""

from n90 import load_model
from n96 import get_country_vector
import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import sys


vector = get_country_vector(load_model(sys.argv[1]))
tsne = TSNE(n_components=2).fit_transform(np.array(list(vector.values())))
plt.plot(tsne[:,0], tsne[:,1], '.')
plt.show()
