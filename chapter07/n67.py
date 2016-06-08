#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
67. 複数のドキュメントの取得
特定の（指定した）別名を持つアーティストを検索せよ
"""

import sys
from pymongo import MongoClient

conn = MongoClient('localhost', 27017)
db = conn.test
coll = db.artist

for doc in coll.find({'aliases.name': sys.argv[1]}):
    print(doc)
