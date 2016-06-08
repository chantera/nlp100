#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
70. データの入手・整形
文に関する極性分析の正解データを用い，以下の要領で正解データ（sentiment.txt）を作成せよ．

rt-polarity.posの各行の先頭に"+1 "という文字列を追加する（極性ラベル"+1"とスペースに続けて肯定的な文の内容が続く）
rt-polarity.negの各行の先頭に"-1 "という文字列を追加する（極性ラベル"-1"とスペースに続けて否定的な文の内容が続く）
上述1と2の内容を結合（concatenate）し，行をランダムに並び替える
sentiment.txtを作成したら，正例（肯定的な文）の数と負例（否定的な文）の数を確認せよ．
"""

import io
import random

file1 = io.open("rt-polaritydata/rt-polarity.neg", "r", encoding='latin-1')
file2 = io.open("rt-polaritydata/rt-polarity.pos", "r", encoding='latin-1')

list1 = ["-1" + " " + line for line in file1.readlines()]
list2 = ["+1" + " " + line for line in file2.readlines()]

data = list1 + list2
random.shuffle(data)

for value in data:
    print(value.strip())
