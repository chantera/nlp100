#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""


def mix(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    str = ""
    min_len = min(len1, len2)
    i = 0
    while i < min_len:
        str = str + str1[i] + str2[i]
        i += 1
    if len1 < len2:
        str += str2[len1:]
    elif len1 > len2:
        str += str1[len2:]
    return str

str1 = "パトカー"
str2 = "タクシー"
print(mix(str1, str2))
