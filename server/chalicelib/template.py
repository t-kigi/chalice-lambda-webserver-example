#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
テンプレート処理を行うモジュール
'''

import os
from jinja2 import Environment, FileSystemLoader, select_autoescape
from chalicelib.common import project_dir

template_path = os.path.join(project_dir, 'chalicelib/templates')
loader = FileSystemLoader([template_path])
jinja2_env = Environment(
    loader=loader,
    autoescape=select_autoescape(['html', 'xml']))


def env():
    ''' テンプレートをロードするための Environment を取得 '''
    return jinja2_env


def get(template_path):
    ''' テンプレートを取得します '''
    return jinja2_env.get_template(template_path)
