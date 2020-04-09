#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
65. MongoDBの検索
MongoDBのインタラクティブシェルを用いて，"Queen"というアーティストに関する情報を取得せよ．さらに，これと同様の処理を行うプログラムを実装せよ．
"""

from pymongo import MongoClient

conn = MongoClient('localhost', 27017)
db = conn.test
coll = db.artist

for doc in coll.find({'name': 'Queen'}):
    print(doc)
