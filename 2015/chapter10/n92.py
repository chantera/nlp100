#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
92. アナロジーデータへの適用
91で作成した評価データの各事例に対して，vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算し，そのベクトルと類似度が最も高い単語と，その類似度を求めよ．求めた単語と類似度は，各事例の末尾に追記せよ．このプログラムを85で作成した単語ベクトル，90で作成した単語ベクトルに対して適用せよ．
"""

from n86 import load, get_vector
from n88 import get_similar_words
from n90 import load_model
import sys


def main(argv):
    if len(argv) <= 1:
        print("Usage:")
        print("\tn85 <matrix> <keys> <input>")
        print("\tn90 <model> <input>")
        return
    if argv[1] == "n85":
        matrix, keys = load(sys.argv[2], sys.argv[3])
        with open(sys.argv[4], 'r') as f:
            for line in f:
                words = line.strip().split()
                v1 = get_vector(matrix, keys, words[0])
                v2 = get_vector(matrix, keys, words[1])
                v3 = get_vector(matrix, keys, words[2])
                if v1 is None or v2 is None or v3 is None:
                    # print(" ".join(words + ["None", "None"]))
                    continue
                else:
                    vector = v2 - v1 + v3
                    sim_word_k, sim_word_v = get_similar_words(vector, matrix, keys, n=1)[0]
                    print(" ".join(words + [sim_word_k, str(sim_word_v)]))
    elif argv[1] == "n90":
        model = load_model(argv[2])
        with open(sys.argv[3], 'r') as f:
            for line in f:
                words = line.strip().split()
                if words[0] not in model.vocab or words[1] not in model.vocab or words[2] not in model.vocab:
                    # print(" ".join(words + ["None", "None"]))
                    continue
                else:
                    sim_word_k, sim_word_v = model.most_similar([words[1], words[2]], [words[0]], topn=1)[0]
                    print(" ".join(words + [sim_word_k, str(sim_word_v)]))
    else:
        print("ERROR: unknown command \"%s\"" % argv[1])


if __name__ == "__main__":
    main(sys.argv)
