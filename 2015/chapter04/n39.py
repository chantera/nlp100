#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
39. Zipfの法則
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
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
    plt.figure()
    plt.xscale('log')
    plt.yscale('log')
    plt.plot(sorted(list(counter.values()), reverse=True), range(1, len(list(counter)) + 1))
    plt.savefig('fig39.png')

if __name__ == '__main__':
    main()
