#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""

import n05

X = set(n05.make_n_gram("paraparaparadise", 2, unit="char"))
Y = set(n05.make_n_gram("paragraph", 2, unit="char"))

print(X | Y)
print(X & Y)
print(X - Y)

print("check containment of 'se'")
print(('s', 'e') in X)
print(('s', 'e') in Y)
