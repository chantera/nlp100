#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
62. KVS内の反復処理
60で構築したデータベースを用い，活動場所が「Japan」となっているアーティスト数を求めよ．
"""

import redis

area = "Japan"
r = redis.Redis(host='127.0.0.1', port=6379, db=0)
names = []

keys = r.keys('*')
for key in keys:
    if r.type(key) == "KV" and r.get(key) == area:
        names.append(key)

print(len(key))
