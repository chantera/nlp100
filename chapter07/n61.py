#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
61. KVSの検索
60で構築したデータベースを用い，特定の（指定された）アーティストの活動場所を取得せよ．
"""

import redis
# import sys

# artist = sys.argv[1]
artist = "The Wanderers"
r = redis.Redis(host='127.0.0.1', port=6379, db=0)
area = r.get(artist)
print(area)
