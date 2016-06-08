#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
94. WordSimilarity-353での類似度計算
The WordSimilarity-353 Test Collectionの評価データを入力とし，1列目と2列目の単語の類似度を計算し，各行の末尾に類似度の値を追加するプログラムを作成せよ．このプログラムを85で作成した単語ベクトル，90で作成した単語ベクトルに対して適用せよ．
"""

from n86 import load, get_vector
from n87 import cos_sim
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
            lines = f.readlines()
            # print(lines[0].strip() + "\tCosine Similarity")  # header
            for line in lines[1:]:
                cols = line.strip().split("\t")
                v1 = get_vector(matrix, keys, cols[0])
                v2 = get_vector(matrix, keys, cols[1])
                if v1 is None or v2 is None:
                    # print("\t".join(cols + ["None"]))
                    continue
                else:
                    print("\t".join(cols + [str(cos_sim(v1, v2))]))
    elif argv[1] == "n90":
        model = load_model(argv[2])
        with open(sys.argv[3], 'r') as f:
            lines = f.readlines()
            # print(lines[0].strip() + "\tCosine Similarity")  # header
            for line in lines[1:]:
                cols = line.strip().split("\t")
                if cols[0] not in model.vocab or cols[1] not in model.vocab:
                    # print("\t".join(cols + ["None"]))
                    continue
                else:
                    print("\t".join(cols + [str(cos_sim(model[cols[0]], model[cols[1]]))]))
    else:
        print("ERROR: unknown command \"%s\"" % argv[1])


if __name__ == "__main__":
    main(sys.argv)
