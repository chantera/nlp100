#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
71. ストップワード
英語のストップワードのリスト（ストップリスト）を適当に作成せよ．さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，それ以外は偽を返す関数を実装せよ．さらに，その関数に対するテストを記述せよ．
"""

f_sw = open("/usr/local/share/nltk_data/corpora/stopwords/english", "r")
stopwords = [w.strip() for w in f_sw.readlines()]
stopwords += [",", ".", "(", ")", "'", "-", "[", "]"]


def is_stopword(word):
    if word in stopwords:
        return True
    else:
        return False


def test():
    c = 0
    if is_stopword("run"):
        print("error")
    else:
        print("pass")
        c += 1
    if is_stopword("have"):
        print("pass")
        c += 1
    else:
        print("error")
    if c == 2:
        print("pass all")

if __name__ == "__main__":
    test()
