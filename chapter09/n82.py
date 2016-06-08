#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
82. 文脈の抽出
81で作成したコーパス中に出現するすべての単語tに関して，単語tと文脈語cのペアをタブ区切り形式ですべて書き出せ．ただし，文脈語の定義は次の通りとする．

・ある単語tの前後d単語を文脈語cとして抽出する（ただし，文脈語に単語tそのものは含まない）
・単語tを選ぶ度に，文脈幅dは{1,2,3,4,5}の範囲でランダムに決める．
"""

import sys
import random

for line in open(sys.argv[1]):
    tokens = line.strip().split()
    for i, t in enumerate(tokens):
        d = random.randint(1, 5)
        c = [t]
        c += tokens[i-d:i] if i-d >= 0 else tokens[0:i]
        c += tokens[i+1:i+d+1]
        if len(c) > 1:
            print("\t".join(c))
