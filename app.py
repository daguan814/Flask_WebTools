"""
@author shuijing
@date 2023-10-20 10:34
@version 1.0
@description
"""

from flask import Flask
from modules.index.IndexViews import index_blue
from modules.learn.LearnViews import learn_blue

app = Flask(__name__)
# 导入蓝图
app.register_blueprint(blueprint=index_blue)
app.register_blueprint(blueprint=learn_blue)

if __name__ == '__main__':
    app.run()
