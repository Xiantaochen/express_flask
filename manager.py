# encoding: utf-8
'''
@author: Chenxiantao
@file: manager.py
@time: 2019/3/29 22:34
@desc:
'''
from flask_script import  Manager
from flask_migrate import MigrateCommand,Migrate
from express import create_app,db

app = create_app('develop')
#迁移数据是，app和数据库关联
Migrate(app,db)
#创建脚本管理器
manager = Manager(app)
#增加db脚本命令
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    print(app.url_map)
    manager.run()
