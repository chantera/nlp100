#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
96. 国名に関するベクトルの抽出
word2vecの学習結果から，国名に関するベクトルのみを抜き出せ．
"""

from n81 import get_country_list
from n90 import load_model
import sys


def get_country_vector(model):
    vector = {}
    for country in get_country_list():
        if country in model.vocab:
            vector[country] = model[country]
        # else:
        #     vector[country] = None
    return vector


if __name__ == "__main__":
    model = load_model(sys.argv[1])
    print(get_country_vector(model))
