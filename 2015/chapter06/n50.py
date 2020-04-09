#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
50. 文区切り
(. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，入力された文書を1行1文の形式で出力せよ．
"""

import re
import sys

END_PAT = re.compile(r"(?P<punct>[\.;:\?\!]) (?P<head>[A-Z])")

with open(sys.argv[1], 'r') as textfile:
    for line in textfile:
        stripped = line.strip()
        if END_PAT.search(stripped):
            print(END_PAT.sub(r"\g<punct>\n\g<head>", stripped))
