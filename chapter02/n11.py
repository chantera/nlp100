#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

import sys


def tab2space(file):
    out = open("tab2spaced_" + sys.argv[1], "w")
    for line in file:
        out.write(line.replace(" ", "\t"))
    out.close()


def main():
    with open(sys.argv[1], "r") as f:
        tab2space(f)


if __name__ == '__main__':
    main()

# sed -e "s/\t/ /g" hightemp.txt > hightemp_t2s_sed.txt
# cat hightemp.txt | tr "\t" " " > hightemp_t2s_tr.txt
# expand -t 1 hightemp.txt > hightemp_t2s_expand.txt
