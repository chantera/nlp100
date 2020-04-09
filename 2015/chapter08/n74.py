#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
74. 予測
73で学習したロジスティック回帰モデルを用い，与えられた文の極性ラベル（正例なら"+1"，負例なら"-1"）と，その予測確率を計算するプログラムを実装せよ．
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

    while True:
        print("分析したい文章を入力してください.\n>>")
        input_str = input()
        if input_str == "q":
            break
        doc = Document(input_str)
        words = {stem: count for stem, count in doc.stems.items() if not is_stopword(stem)}
        feature = np.zeros(len(columns))
        feature[columns.get_loc("<BIAS>")] = 1
        for word, count in words.items():
            if word in columns:
                index = columns.get_loc(word)
                feature[index] = count
        h = sigmoid(feature.dot(weight))[0]
        label = "+1" if h >= 0.5 else "-1"
        p = h if h >= 0.5 else 1 - h
        print("PREDICT: label='{:s}' with a probability {:.2%}".format(label, p))
