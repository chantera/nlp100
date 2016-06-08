#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
66. 検索件数の取得
MongoDBのインタラクティブシェルを用いて，活動場所が「Japan」となっているアーティスト数を求めよ．
"""

from pymongo import MongoClient

conn = MongoClient('localhost', 27017)
db = conn.test
coll = db.artist

print(coll.find({'area': 'Japan'}).count())
