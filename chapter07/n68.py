#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
68. ソート
"dance"というタグを付与されたアーティストの中でレーティングの投票数が多いアーティスト・トップ10を求めよ．
"""

from pymongo import MongoClient, DESCENDING

conn = MongoClient('localhost', 27017)
db = conn.test
coll = db.artist

c = 0
for doc in coll.find({'tags.value': 'dance'}).sort('rating.count', DESCENDING):
    print(doc)
    c += 1
    if c == 10:
        break
