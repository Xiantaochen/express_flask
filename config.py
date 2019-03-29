# encoding: utf-8
'''
@author: Chenxiantao
@file: config.py
@time: 2019/3/29 22:34
@desc:
'''

import logging
from redis import StrictRedis
import base64
import os

class Config:
    """应用程序环境配置"""

    #logging 登记
    LOGGING_LEAVEL = logging.DEBUG

    #配置secret key
    SECRET_KEY = base64.b64encode(os.urandom(48))

    #配置SQLALCHEMY连接
    HOST = "127.0.0.1"
    PORT = '3306'
    USERNAME = "root"
    PASSWORD = '302811'
    DATABASE = "express_mysql"
    DB_URL = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOST,PORT,DATABASE)
    SQLALCHEMY_DATABASE_URI = DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置Redis数据库
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    REDIS_DB = 1

    #配置redis数据库,保存session的数据
    REDIS_TYPE = 'redis'
    #指定存储session数据库的redis位置
    SESSION_REDIS =StrictRedis(host=REDIS_HOST,port=REDIS_PORT,db=REDIS_DB)
    #开启session的数据签名，意思session数据不以明文的方式展现
    SESSION_USE_SINGER =True
    #设置session的回话的超时时长：一天，全局指定
    PERMANENT_SESSION_LIFETIME = 3600 * 24

class DevelopmentConfig(Config):
    """开发阶段下的配置子类"""
    #开启调试模式
    DEBUG = True

class ProductionConfig(Config):
    """生产环境下的配置子类"""
    pass


#工厂函数原材料
configs = {
    'default':Config,
    "develop":DevelopmentConfig,
    'production':ProductionConfig
}

