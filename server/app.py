#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import json

from chalice import Response
from chalicelib import common, template
from chalicelib.common import app

stage = os.environ.get('STAGE', 'dev')
if stage == 'local':
    # ローカル時のみ活用
    from chalicelib import staticfiles # noqa


def html_render(template_path, **params):
    ''' HTMLのレンダリングレスポンスを返します '''
    tpl = template.get(template_path)
    return Response(
        status_code=200,
        headers={'Content-Type': 'text/html'},
        body=tpl.render(**params))


@app.route('/')
def index():
    ''' トップページを返す '''
    req = json.dumps(app.current_request.to_dict(), indent=4)
    return html_render('index.tpl', req=req)


def _search(database, keyword):
    ''' 検索の実体 '''
    if keyword:
        # 入力あり
        return [e for e in database if keyword in e]
    else:
        # 入力なし
        return database


@app.route('/search', methods=['POST'],
           content_types=common.post_content_types)
def search():
    ''' 検索する '''
    # database はサンプル
    database = ['C', 'C++', 'Java', 'Perl', 'PHP', 'Ruby', 'Python']
    params = common.post_params()
    results = _search(database, params.get('keyword'))
    return html_render('search.tpl', results=results)
