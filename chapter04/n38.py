#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
38. ヒストグラム
単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
"""

import n36
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.font_manager import FontProperties
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = 14, 10

fp = FontProperties(fname="/Library/Fonts/Osaka.ttf")
plt.rcParams['font.family'] = fp.get_name()


def main():
    counter = n36.main()
    freq = pd.Series(list(counter.values()), index=list(counter.keys()))

    plot = freq.hist()
    fig = plot.get_figure()
    fig.savefig('fig38.png')

if __name__ == '__main__':
    main()
