"""
@author shuijing
@date 2023-10-20 10:34
@version 1.0
@description
"""
import datetime

from flask import Flask
from MVC.Controller.FlashTransController import flashTrans_blue
from MVC.Controller.IndexController import index_blue
from MVC.Controller.UploadController import upload_blue
from exps import init_Exps

app = Flask(__name__)
# 导入蓝图
app.register_blueprint(blueprint=index_blue)
app.register_blueprint(blueprint=upload_blue)
app.register_blueprint(blueprint=flashTrans_blue)
#配置Https证书
context = ('证书/amaa.cn.pem', '证书/amaa.cn.key')
#配置session的Key
app.config['SECRET_KEY'] = 'abc123'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=7)

# 配置数据库连接字符串
db_uri = 'mysql+pymysql://root:Lhf2001@10.11.2.231:3306/FlashTrans'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化插件
init_Exps(app=app)

if __name__ == '__main__':
    app.run(port=9000, host="0.0.0.0", debug=True, ssl_context=context)
