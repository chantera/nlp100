#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
"""

import sys
import n18


def main():
    with open(sys.argv[1], "r") as file:
        file_ary = n18.split_col2ary(file)
        col1 = [line[0] for line in file_ary]
        result = {}
        for row in col1:
            if row in result:
                result[row] += 1
            else:
                result[row] = 1
        result = sorted(result.items(), key=lambda x: -x[1])
        print(result)


if __name__ == '__main__':
    main()

# sort col1.txt | uniq -c | sort -n -r | less > freq_ranking.txt
