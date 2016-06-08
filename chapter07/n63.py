#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
63. オブジェクトを値に格納したKVS
KVSを用い，アーティスト名（name）からタグと被タグ数（タグ付けされた回数）のリストを検索するためのデータベースを構築せよ．さらに，ここで構築したデータベースを用い，アーティスト名からタグと被タグ数を検索せよ．
"""

import json
import redis
import sys

with open(sys.argv[1], 'r') as f:
    r = redis.Redis(host='127.0.0.1', port=6379, db=0)
    for line in f:
        data = json.loads(line)
        r.set(data['name'], data['tags'] if 'tags' in data else None)

# 省略
