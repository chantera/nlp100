#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
84. 単語文脈行列の作成
83の出力を利用し，単語文脈行列Xを作成せよ．ただし，行列Xの各要素X_tcは次のように定義する．

・f(t,c)≥10ならば，X_tc=PPMI(t,c)=max{logN×f(t,c)/f(t,∗)×f(∗,c),0}
・f(t,c)<10fならば，X_tc=0
ここで，PPMI(t,c)はPositive Pointwise Mutual Information（正の相互情報量）と呼ばれる統計量である．なお，行列Xの行数・列数は数百万オーダとなり，行列のすべての要素を主記憶上に載せることは無理なので注意すること．幸い，行列Xのほとんどの要素は0になるので，非0の要素だけを書き出せばよい．
"""

from n83 import Context
from collections import defaultdict
import math
import pickle
import sys
import os
from scipy import io, sparse


def generate_context_matrix(context, threshold=10):
    keys = defaultdict(None)
    matrix = sparse.lil_matrix((len(context.t_occ), len(context.c_occ)))

    for i, t in enumerate(context.t_occ):
        for j, c in enumerate(context.c_occ):
            keys[(t, c)] = (i, j)
            if context.co_occ[(t, c)] >= threshold:
                print((t, c), context.co_occ[(t, c)])
                # pmi = math.log((context.N * context.co_occ[(t, c)]) / (context.t_occ[t] * context.c_occ[c]), 2)
                pmi = math.log(Context.N, 2) + math.log(context.co_occ[(t, c)], 2) - math.log(context.t_occ[t], 2) - math.log(context.c_occ[c], 2)
                matrix[i, j] = max(pmi, 0)
    return matrix, keys


def main(in_file, out_file):
    context = None
    with open(in_file, 'rb') as f:
        context = pickle.load(f)
    matrix, keys = generate_context_matrix(context)
    # print("key=(%s, %s), value=%d" % ("fiction", "science", matrix[keys[("fiction", "science")]]))
    basename = os.path.basename(out_file).split('.')[0]
    index = [k[0] + "\t" + str(v[0]) + "\n" for k, v in keys.items()]
    io.savemat(basename, {"context": matrix})
    with open(basename + '-keys.txt', 'w') as f:
        f.writelines(index)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
