#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
64. MongoDBの構築
アーティスト情報（artist.json.gz）をデータベースに登録せよ．さらに，次のフィールドでインデックスを作成せよ: name, aliases.name, tags.value, rating.value
"""

from pymongo import MongoClient
import json

conn = MongoClient('localhost', 27017)
db = conn.test
coll = db.artist

for line in open('artist.json', 'r'):
    dic = json.loads(line)
    coll.insert(dic)

from pymongo import ASCENDING

coll.create_index([('name', ASCENDING)])
coll.create_index([('aliases.name', ASCENDING)])
coll.create_index([('tags.value', ASCENDING)])
coll.create_index([('rating.value', ASCENDING)])
