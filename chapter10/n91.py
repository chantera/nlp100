#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
91. アナロジーデータの準備
単語アナロジーの評価データをダウンロードせよ．このデータ中で": "で始まる行はセクション名を表す．例えば，": capital-common-countries"という行は，"capital-common-countries"というセクションの開始を表している．ダウンロードした評価データの中で，"family"というセクションに含まれる評価事例を抜き出してファイルに保存せよ．
"""

import sys


flag = False
for line in open(sys.argv[1]):
    if line.startswith(': family'):
        flag = True
    elif flag:
        if line.startswith(':'):
            flag = False
        else:
            print(line.strip())
