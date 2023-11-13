"""
@author shuijing
@date 2023-11-11 10:14
@version 1.0 
@description 
"""

# 1.导入第三方插件
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# 2.初始化
db = SQLAlchemy() #ORM
migrate = Migrate()


# 3.和app对象绑定
def init_Exps(app):
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)