#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
"""

import random


def shuffle_word(str):
    words = str.split()
    result = []
    for word in words:
        if len(word) > 4:
            head = word[0]
            content = list(word[1:-1])
            tail = word[-1]

            random.shuffle(content)
            result.append(head + ''.join(content) + tail)
        else:
            result.append(word)
    return " ".join(result)

string = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind."
print(shuffle_word(string))
