#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
69. Webアプリケーションの作成
ユーザから入力された検索条件に合致するアーティストの情報を表示するWebアプリケーションを作成せよ．アーティスト名，アーティストの別名，タグ等で検索条件を指定し，アーティスト情報のリストをレーティングの高い順などで整列して表示せよ．

"""

from bottle import route, run, template
from pymongo import MongoClient

conn = MongoClient('localhost', 27017)
db = conn.test
coll = db.artist


def find_by_name(name):
    result = []
    for doc in coll.find({'name': name}):
        result.append(doc)
    return result


@route('/artist/<name>')
def index(name):
    return template('<b>{{data}}</b>!', data=find_by_name(name))

run(host='localhost', port=8080)
