#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
"""


def make_n_gram(seq, n, unit="word"):
    if unit == "word":
        seq = seq.split()
    elif unit == "char":
        seq = seq
    return [tuple(seq[i:i + n]) for i in range(len(seq) - n + 1)]

if __name__ == "__main__":
    str = "I am an NLPer"
    print("word bi-gram: ", make_n_gram(str, 2, "word"))
    print("character bi-gram: ", make_n_gram(str, 2, "char"))
