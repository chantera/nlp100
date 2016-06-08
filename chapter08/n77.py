#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
77. 正解率の計測
76の出力を受け取り，予測の正解率，正例に関する適合率，再現率，F1スコアを求めるプログラムを作成せよ．
"""

import sys


def evaluate(golds, predictions):
    tp = .0
    fp = .0
    tn = .0
    fn = .0

    for gold, pred in zip(golds, predictions):
        gold = int(gold)
        pred = int(pred)
        if gold != pred and pred == 1:
            fp += 1
        elif gold != pred:
            fn += 1
        elif gold == pred and pred == 1:
            tp += 1
        elif gold == pred:
            tn += 1
        else:
            raise

    acc = (tp + tn) / (tp + tn + fn + fp)
    pre = (tp / (tp + fp)) if tp + fp > 0 else 0
    rec = (tp / (tp + fn)) if tp + fn > 0 else 0
    f = ((2 * rec * pre) / (rec + pre)) if rec + pre > 0 else 0
    return acc, pre, rec, f


if __name__ == "__main__":
    golds = []
    preds = []
    for line in open(sys.argv[1]):
        gold, pred, p = line.strip().split("\t")
        golds.append(gold)
        preds.append(pred)

    acc, pre, rec, f = evaluate(golds, preds)
    print("Accuracy %f, precision %f, recall %f, F1 %f" % (acc, pre, rec, f))
