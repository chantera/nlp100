#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．


import sys


def count_line(file):
    count = 0
    for line in file:
        count += 1
    return count


def main():
    f = open(sys.argv[1])
    print(count_line(f))
    f.close()


if __name__ == '__main__':
    main()

# wc hightemp.txt
