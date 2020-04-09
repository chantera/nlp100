#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
89. 加法構成性によるアナロジー
85で得た単語の意味ベクトルを読み込み，vec("Spain") - vec("Madrid") + vec("Athens")を計算し，そのベクトルと類似度の高い10語とその類似度を出力せよ．
"""

from n86 import load, get_vector
from n88 import get_similar_words
import sys


if __name__ == '__main__':
    matrix, keys = load(sys.argv[1], sys.argv[2])
    v1 = get_vector(matrix, keys, "Spain")
    v2 = get_vector(matrix, keys, "Madrid")
    v3 = get_vector(matrix, keys, "Athens")
    vector = v1 - v2 + v3
    words = get_similar_words(vector, matrix, keys, n=10)
    for word in words:
        print(word[0], word[1])
