#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
60. KVSの構築
Key-Value-Store (KVS) を用い，アーティスト名（name）から活動場所（area）を検索するためのデータベースを構築せよ
"""

import json
import redis
import sys

with open(sys.argv[1], 'r') as f:
    r = redis.Redis(host='127.0.0.1', port=6379, db=0)
    for line in f:
        data = json.loads(line)
        r.set(data['name'], data['area'] if 'area' in data else None)
