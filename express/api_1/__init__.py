# encoding: utf-8
'''
@author: Chenxiantao
@file: __init__.py.py
@time: 2019/3/29 22:24
@desc:
'''

from flask.blueprints import Blueprint

#需求url:127.0.0.1/api/1.0
api = Blueprint("api_1.0",__name__,url_prefix="api/1.0")

#调用蓝图视图层
