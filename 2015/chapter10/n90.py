#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
90. word2vecによる学習
81で作成したコーパスに対してword2vecを適用し，単語ベクトルを学習せよ．さらに，学習した単語ベクトルの形式を変換し，86-89のプログラムを動かせ．
"""

from gensim.models import word2vec
import sys


def train(in_file, out_file, size=300):
    data = word2vec.Text8Corpus(in_file)
    model = word2vec.Word2Vec(data, size=size)
    model.save_word2vec_format(out_file, binary=True)


def load_model(filename):
    return word2vec.Word2Vec.load_word2vec_format(filename, binary=True)


def main(argv):
    if len(argv) <= 1:
        print("Usage:")
        print("\ttrain <input> <output>")
        print("\tn86 <model>")
        print("\tn87 <model>")
        print("\tn88 <model>")
        print("\tn89 <model>")
        return
    if argv[1] == "train":
        train(argv[2], argv[3], size=300)
    elif argv[1] == "n86":
        model = load_model(argv[2])
        print(model["United_States"])
    elif argv[1] == "n87":
        model = load_model(argv[2])
        print(model.similarity("United_States", "U.S"))
    elif argv[1] == "n88":
        model = load_model(argv[2])
        for w, s in model.most_similar("England"):
            print(w, s)
    elif argv[1] == "n89":
        model = load_model(argv[2])
        for w, s in model.most_similar(["Spain", "Athens"], ["Madrid"]):
            print(w, s)
    else:
        print("ERROR: unknown command \"%s\"" % argv[1])

if __name__ == "__main__":
    main(sys.argv)
