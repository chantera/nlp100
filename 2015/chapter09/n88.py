#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
88. 類似度の高い単語10件
85で得た単語の意味ベクトルを読み込み，"England"とコサイン類似度が高い10語と，その類似度を出力せよ．
"""

from n86 import load, get_vector
from n87 import cos_sim
import sys


def get_similar_words(vector, matrix, keys, n=10):
    words = []
    sims = {}
    for key, index in keys.items():
        sims[key] = cos_sim(vector, matrix[index])
    for i, (k, v) in enumerate(sorted(sims.items(), key=lambda x:x[1], reverse=True)):
        if i == n:
            break
        words.append((k,v))
        i += 1
    return words


if __name__ == '__main__':
    matrix, keys = load(sys.argv[1], sys.argv[2])
    keyword = "England"
    vector = get_vector(matrix, keys, keyword)
    words = get_similar_words(vector, matrix, keys, n=10)
    for word in words:
        print(word[0], word[1])
