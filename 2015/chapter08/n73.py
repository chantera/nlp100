#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
73. 学習
72で抽出した素性を用いて，ロジスティック回帰モデルを学習せよ．
"""

import numpy as np
import pandas as pd


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def compute(theta, X, y, lmda):
    m = y.size
    h = sigmoid(X.dot(theta))
    J = (1 / m) * np.sum(-1 * y * np.log(h) - (1 - y) * np.log(1 - h))
    penalty = (lmda / (2 * m)) * np.sum(np.power(theta[2:], 2))
    J += penalty
    grad = ((1 / m) * (h - y).T.dot(X)).T
    return J, grad


def logreg(X, y, iter=100):
    m, n = X.shape
    X = np.c_[np.ones((m, 1)), X]
    theta = np.zeros((n + 1, 1))
    lmda = 1.0
    eta = 0.1
    cost = 0
    for i in range(1, iter + 1):
        cost, grad = compute(theta, X, y, lmda)
        theta -= eta * grad
        # eta *= 0.9
        print("Iteration {:d}: cost={:f}".format(i, cost))
    return theta


if __name__ == "__main__":
    df = pd.read_csv("features.tsv", delimiter="\t", quoting=3)
    data = df.as_matrix()
    X = data[:, 1:]
    y = np.c_[data[:, 0]]
    weight = logreg(X, y, iter=500)
    new_df = pd.DataFrame(data=weight.T, columns=df.columns)
    new_df.rename(columns={"<LABEL>": "<BIAS>"}, inplace=True)
    # print(new_df)
    new_df.to_csv('weight.tsv', sep="\t")
