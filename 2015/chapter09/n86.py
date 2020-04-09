#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
86. 単語ベクトルの表示
85で得た単語の意味ベクトルを読み込み，"United States"のベクトルを表示せよ．ただし，"United States"は内部的には"United_States"と表現されていることに注意せよ．
"""

from scipy import io
import sys


def load(matrix_file, key_file):
    matrix = io.loadmat(matrix_file)["context"]
    keys = {}
    with open(key_file, 'r') as f:
        for line in f:
            values = line.strip().split("\t")
            keys[values[0]] = int(values[1])
        sorted(keys)
    return matrix, keys


def get_vector(matrix, keys, keyword):
    index = keys.get(keyword, None)
    if index is not None:
        return matrix[index]
    else:
        return None


if __name__ == "__main__":
    matrix, keys = load(sys.argv[1], sys.argv[2])
    keyword = "United_States"
    vector = get_vector(matrix, keys, keyword)
    if vector is not None:
        print(vector)
    else:
        print("key=%s not found" % keyword)
