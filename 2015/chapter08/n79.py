#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
79. 適合率-再現率グラフの描画
ロジスティック回帰モデルの分類の閾値を変化させることで，適合率-再現率グラフを描画せよ．
"""

from n78 import execute
import sys
import matplotlib.pyplot as plt


def draw_graph(results):
    threshold = []
    pre = []
    rec = []
    for result in results:
        threshold.append(result['threshold'])
        pre.append(result['pre'])
        rec.append(result['rec'])
    plt.plot(threshold, pre, label="precision", color="red")
    plt.plot(threshold, rec, label="recall", color="blue")
    plt.xlabel("threshold")
    plt.ylabel("rate")
    plt.xlim(-0.05, 1.00)
    plt.ylim(0, 1)
    plt.title("logistic regresssion")
    plt.legend(loc=3)
    plt.show()


if __name__ == '__main__':
    results = execute(sys.argv[1], iter=100, n_folds=5, thresholds=(0.05 * i for i in range(1, 20)), random=True)
    for r in results:
        print("Threshold %f, Accuracy %f, precision %f, recall %f, F1 %f" % (r['threshold'], r['acc'], r['pre'], r['rec'], r['f']))
    draw_graph(results)
