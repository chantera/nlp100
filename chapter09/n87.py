#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
87. 単語の類似度
85で得た単語の意味ベクトルを読み込み，"United States"と"U.S."のコサイン類似度を計算せよ．ただし，"U.S."は内部的に"U.S"と表現されていることに注意せよ．
"""

from n86 import load, get_vector
import numpy
import sys


def cos_sim(x, y):
    return numpy.dot(x, y) / (numpy.linalg.norm(x) * numpy.linalg.norm(y))


if __name__ == '__main__':
    matrix, keys = load(sys.argv[1], sys.argv[2])
    keyword1, keyword2 = "United_States", "U.S"
    x, y = get_vector(matrix, keys, keyword1), get_vector(matrix, keys, keyword2)
    print(cos_sim(x, y))
