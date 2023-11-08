"""
@author shuijing
@date 2023-10-20 10:34
@version 1.0
@description
"""

from flask import Flask

from modules.index.index import index_blue

app = Flask(__name__)
# 导入蓝图

app.register_blueprint(blueprint=index_blue)


if __name__ == '__main__':
    app.run(port=9000, host="0.0.0.0")
