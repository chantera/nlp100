#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
32. 動詞の原形
動詞の原形をすべて抽出せよ．
"""

import n30


def verb_base_extractor(sentences):
    verb_bases = []
    for sentence in sentences:
        for morpheme in sentence:
            if morpheme['pos'] == "動詞":
                verb_bases.append(morpheme['base'])

    return verb_bases


def main():
    sentences = n30.main()
    return verb_base_extractor(sentences)


if __name__ == '__main__':
    verb_bases = main()
    for verb_base in verb_bases:
        print(verb_base)
