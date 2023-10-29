"""
@author shuijing
@date 2023-10-20 10:33
@version 1.0 
@description 
"""
from flask import Blueprint, render_template

# 蓝图
index_blue = Blueprint('index', __name__)


@index_blue.route('/')
def index():
    return render_template('index.html')


@index_blue.route('/list')
def index_list():
    return 'index_list'

