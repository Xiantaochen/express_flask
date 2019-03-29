# encoding: utf-8
'''
@author: Chenxiantao
@file: app.py
@time: 2019/3/29 22:30
@desc:
'''
import logging
from logging.handlers import RotatingFileHandler
import redis
from  flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from config import configs
from express.api_1 import api


#定义能被外部调用的对象
db = SQLAlchemy()
redis_store =None

#为flask创建一个csrf保护
csrf = CSRFProtect()

def setupLogging(level):
    """配置日志"""
    #业务逻辑已开启加载日志
    #设置日志的纪录等级
    logging.basicConfig(level=level) #调试debug等级
    # 创建日志记录器，指明日志保存的路径、每个文件的大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志的纪录格式
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志纪录器设置日志纪录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的） 添加日记录器
    logging.getLogger().addHandler(file_log_handler)

def create_app(config_name):
    """
    app工厂函数
    :param config_name: 传入现在开发的环境名称
    :return: 返回app
    """
    #调用封装的日志
    setupLogging(configs[config_name].LOGGING_LEAVEL)

    #创建app
    app =Flask(__name__)

    #加载配置文件
    config_cls = configs.get(config_name)
    app.config.from_object(config_cls)

    #创建数据库连接对象，赋值给全局db
    db.init_app(app)
    global redis_store
    redis_store = redis.StrictRedis(host=config_cls.REDIS_HOST,port=config_cls.REDIS_PORT)

    #利用flask_session,将session保存到redis中
    Session(app)

    #为flask补充csrf防护
    csrf.init_app(app)

    #注册蓝图
    from express import api_1
    app.register_blueprint(api_1.api,url_prefix = "/api/v1.0")

    return app