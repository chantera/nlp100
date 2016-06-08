#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
"""

import sys

N = int(sys.argv[1])
f = open(sys.argv[2])
f.seek(0, 0)

fileno = 0
count = 0
out = None
for line in f:
    if count == 0:
        count = N
        if out:
            out.close()
        fileno += 1
        out = open("splitted_{0:02d}.txt".format(fileno), "w")
    out.write(line)
    count -= 1
if out:
    out.close()
f.close()

# split -l line_number hightemp.txt
