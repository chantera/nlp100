#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
85. 主成分分析による次元圧縮
84で得られた単語文脈行列に対して，主成分分析を適用し，単語の意味ベクトルを300次元に圧縮せよ．
"""

import sklearn.decomposition
import sys
import os
from scipy import io


filename = sys.argv[1]
matrix = io.loadmat(filename)["context"]
pca = sklearn.decomposition.PCA(300)
decom_matrix = pca.fit_transform(matrix.todense())
basename = os.path.basename(filename).split('.')[0]
io.savemat(basename + "-decom", {"context": decom_matrix})
