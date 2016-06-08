#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
78. 5分割交差検定
76-77の実験では，学習に用いた事例を評価にも用いたため，正当な評価とは言えない．すなわち，分類器が訓練事例を丸暗記する際の性能を評価しており，モデルの汎化性能を測定していない．そこで，5分割交差検定により，極性分類の正解率，適合率，再現率，F1スコアを求めよ．
"""

from n73 import sigmoid, logreg
from n77 import evaluate
import sys
import numpy as np
import pandas as pd


def cross_validate(X, y, n_folds):
    n = len(X)
    fold_sizes = (n // n_folds) * np.ones(n_folds, dtype=np.int)
    fold_sizes[:n % n_folds] += 1
    current = 0
    for k, fold_size in enumerate(fold_sizes):
        start, end = current, current + fold_size
        current = end
        X_train = np.r_[X[:start], X[end:]]
        X_test = X[start:end]
        y_train = np.r_[y[:start], y[end:]]
        y_test = y[start:end]
        yield X_train, y_train, X_test, y_test


def execute(filename, iter=100, n_folds=5, thresholds=(0.5,), random=False):
    df = pd.read_csv(filename, delimiter="\t", quoting=3)
    data = df.as_matrix()
    X = data[:, 1:]
    y = np.c_[data[:, 0]]

    n_folds = 5

    results = [{
        'threshold': threshold,
        'acc': np.zeros(n_folds),
        'pre': np.zeros(n_folds),
        'rec': np.zeros(n_folds),
        'f': np.zeros(n_folds),
    } for threshold in thresholds]

    if random:
        np.random.shuffle(X)

    k = 0
    for X_train, y_train, X_test, y_test in cross_validate(X, y, n_folds=n_folds):
        print("Cross Validation {:d}/{:d}".format(k + 1, n_folds))
        weight = logreg(X_train, y_train, iter=100)
        X_test = np.c_[np.ones((X_test.shape[0], 1)), X_test]  # add bias
        y_test = y_test.reshape(y_test.size)
        h = sigmoid(X_test.dot(weight))
        for r in results:
            pred = np.array([1 if v >= r['threshold'] else 0 for v in h])
            r['acc'][k], r['pre'][k], r['rec'][k], r['f'][k] = evaluate(y_test, pred)
        k += 1

    for r in results:
        r['acc'] = r['acc'].mean()
        r['pre'] = r['pre'].mean()
        r['rec'] = r['rec'].mean()
        r['f'] = r['f'].mean()

    return results


if __name__ == "__main__":
    results = execute(sys.argv[1], iter=100, n_folds=5, thresholds=(0.5,), random=True)
    for r in results:
        print("Threshold %f, Accuracy %f, precision %f, recall %f, F1 %f" % (r['threshold'], r['acc'], r['pre'], r['rec'], r['f']))
