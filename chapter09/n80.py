#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
80. コーパスの整形
文を単語列に変換する最も単純な方法は，空白文字で単語に区切ることである． ただ，この方法では文末のピリオドや括弧などの記号が単語に含まれてしまう． そこで，コーパスの各行のテキストを空白文字でトークンのリストに分割した後，各トークンに以下の処理を施し，単語から記号を除去せよ．

トークンの先頭と末尾に出現する次の文字を削除: .,!?;:()[]'"
空文字列となったトークンは削除
以上の処理を適用した後，トークンをスペースで連結してファイルに保存せよ．
"""

import sys
import re


for line in open(sys.argv[1]):
    tokens = []
    for token in line.strip().split():
        token = re.sub(r'^[\.,!\?;:()\[\]\'"]*', '', token)
        token = re.sub(r'[\.,!\?;:()\[\]\'"]*$', '', token)
        tokens.append(token)
    print(' '.join([token for token in tokens if token]))
