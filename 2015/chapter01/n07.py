#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
07. テンプレートによる文生成
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
"""

from string import Template


def weather(x, y, z):
    s = Template('$x時の$yは$z')
    return s.substitute(x=str(x), y=str(y), z=str(z))

print(weather(12, "気温", 22.4))
