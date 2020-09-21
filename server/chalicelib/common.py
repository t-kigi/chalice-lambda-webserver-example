#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from urllib import parse

from chalice import Chalice

# 複数ファイルで共有される Chalice オブジェクト
app = Chalice(app_name='server')

# プロジェクトが配置されているディレクトリのパス
chalicelib_dir = os.path.dirname(__file__)
project_dir = os.path.dirname(chalicelib_dir)

# よく使う固定値
post_content_types = [
    'application/x-www-form-urlencoded',
    'multipart/form-data'
]


def post_params():
    ''' post メソッドに送られたパラメータを dict で返します '''
    def to_s(s):
        try:
            return s.decode()
        except Exception:
            return s
    # str 型に変換して返す
    body = app.current_request.raw_body
    parsed = dict(parse.parse_qsl(body))
    return {to_s(k): to_s(v) for (k, v) in parsed.items()}
