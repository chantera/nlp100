#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
75. 素性の重み
73で学習したロジスティック回帰モデルの中で，重みの高い素性トップ10と，重みの低い素性トップ10を確認せよ．
"""

import pandas as pd


if __name__ == "__main__":
    df = pd.read_csv("weight.tsv", delimiter="\t", quoting=3)
    df.drop('<BIAS>', axis=1, inplace=True)
    ranking = df.T.sort(columns=0, ascending=False)
    print("重みの高い素性トップ10")
    print(ranking.head(10))
    print("重みの低い素性トップ10")
    print(ranking.tail(10))
