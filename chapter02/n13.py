#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
"""

col1 = open("col1.txt", "r")
col2 = open("col2.txt", "r")
o = open("resurrection.txt", "w")

for l1 in col1:
    o.write(l1.rstrip("\n") + '\t' + col2.readline())

col1.close()
col2.close()
o.close()

# paste col1.txt col2.txt
