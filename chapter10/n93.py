#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
93. アナロジータスクの正解率の計算
92で作ったデータを用い，各モデルのアナロジータスクの正解率を求めよ．
"""

import sys


num = 0
correct = 0
for line in open(sys.argv[1]):
    num += 1
    values = line.strip().split()
    if values[3] == values[4]:
        correct += 1

print('Accuracy %f (%d/%d)' % (correct / num, correct, num))
