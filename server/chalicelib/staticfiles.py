#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
chalice local で動作する static file を返す実装です。
本番では CloudFront -> S3 へのパスで対処する内容となるため、
開発時にのみ利用することを想定しています。
'''

import os

from chalice import Response
from chalice import NotFoundError
from chalicelib.common import app, project_dir


def static_filepath(directory, file, subdirs=[]):
    ''' ローカルサーバーで static file のパスを生成して返す '''
    pathes = [f for f in ([directory] + subdirs + [file]) if f is not None]
    filepath = os.path.join(*pathes)
    localpath = os.path.join(project_dir, 'static', filepath)
    return (f'/{filepath}', localpath)


def static_content_type(filepath):
    ''' static file 用の Content-Type を返す '''
    (_, suffix) = os.path.splitext(filepath.lower())
    if suffix in ['.png', '.ico']:
        return 'image/png'
    if suffix in ['.jpg', '.jpeg']:
        return 'image/jpeg'
    if suffix in ['.css']:
        return 'text/css'
    if suffix in ['.js']:
        return 'text/javascript'
    return 'application/json'


def load_static(access, filepath, binary=False):
    ''' static file の読み込み '''
    try:
        with open(filepath, 'rb' if binary else 'r') as fp:
            data = fp.read()
        return Response(
            body=data, status_code=200,
            headers={'Content-Type': static_content_type(filepath)})
    except Exception:
        raise NotFoundError(access)


@app.route('/favicon.ico', content_types=["*/*"])
def favicon():
    (access, filepath) = static_filepath(None, 'favicon.ico')
    return load_static(access, filepath, binary=True)


@app.route('/images/{file}', content_types=["*/*"])
@app.route('/images/{dir1}/{file}', content_types=["*/*"])
def images(dir1=None, file=None):
    '''
    ローカル環境用画像ファイルレスポンス
    (Lambdaにデプロイするとパスの都合で動かないのでCloudFrontでS3に流す)
    '''
    (access, filepath) = static_filepath('images', file, [dir1])
    return load_static(access, filepath, binary=True)


@app.route('/css/{file}', content_types=["*/*"])
@app.route('/css/{dir1}/{file}', content_types=["*/*"])
def css(dir1=None, file=None):
    '''
    ローカル環境用CSSファイルレスポンス
    (Lambdaにデプロイするとパスの都合で動かないのでCloudFrontでS3に流す)
    '''
    (access, filepath) = static_filepath('css', file, [dir1])
    return load_static(access, filepath)


@app.route('/js/{file}', content_types=["*/*"])
@app.route('/js/{dir1}/{file}', content_types=["*/*"])
def js(dir1=None, file=None):
    '''
    ローカル環境用JSファイルレスポンス
    (Lambdaにデプロイするとパスの都合で動かないのでCloudFrontでS3に流す)
    '''
    (access, filepath) = static_filepath('js', file, [dir1])
    return load_static(access, filepath)
