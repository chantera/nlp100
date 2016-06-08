#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
76. ラベル付け
学習データに対してロジスティック回帰モデルを適用し，正解のラベル，予測されたラベル，予測確率をタブ区切り形式で出力せよ．
"""

from n71 import is_stopword
from n72 import Document
import numpy as np
import pandas as pd


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


if __name__ == "__main__":
    df = pd.read_csv("weight.tsv", delimiter="\t", quoting=3)
    weight = np.c_[df.T.as_matrix()]
    columns = df.columns

    with open("sentiment.txt", "r") as train_f:
        for line in train_f:
            gold = line[0:2]
            doc = Document(line[3:])
            words = {stem: count for stem, count in doc.stems.items() if not is_stopword(stem)}
            feature = np.zeros(len(columns))
            feature[columns.get_loc("<BIAS>")] = 1
            for word, count in words.items():
                if word in columns:
                    index = columns.get_loc(word)
                    feature[index] = count
            h = sigmoid(feature.dot(weight))[0]
            predict = "+1" if h >= 0.5 else "-1"
            p = h if h >= 0.5 else 1 - h
            print("\t".join([gold, predict, str(p)]))
