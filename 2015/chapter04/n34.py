#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
34. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．
"""

import n30


def NofN_extractor(sentences):
    NofNs = []
    for sentence in sentences:
        for k in range(len(sentence) - 3):
            triple = sentence[k:k + 3]
            a = triple[0]['pos'] == "名詞"
            of = triple[1]['surface'] == "の"
            b = triple[2]['pos'] == "名詞"
            if a and of and b:
                NofNs.append((i['surface'] for i in triple))

    return NofNs


def main():
    sentences = n30.main()
    return NofN_extractor(sentences)


if __name__ == '__main__':
    NofNs = main()
    for NofN in NofNs:
        print("".join(NofN))
