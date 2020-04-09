#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
37. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
"""

import n36
import matplotlib.pyplot as plt

from matplotlib.font_manager import FontProperties
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = 14, 10

fp = FontProperties(fname="/Library/Fonts/Osaka.ttf")
plt.rcParams['font.family'] = fp.get_name()


def main():
    counter = n36.main()
    word10 = []
    count10 = []
    for word, count in counter.most_common(10):
        word10.append(word)
        count10.append(count)

    plt.bar(range(10), count10, align='center')
    plt.xticks(range(0, 10), word10)
    plt.savefig('fig37.png')


if __name__ == '__main__':
    main()
