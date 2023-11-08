"""
@author shuijing
@date 2023-11-08 15:28
@version 1.0 
@description 
"""

from flask import Blueprint, render_template, request

# 蓝图
index_blue = Blueprint('index', __name__)


@index_blue.route('/')
def index():
    visitor_ip = request.remote_addr
    print(visitor_ip)
    ins = {
        'nat_env': '校园网环境，您的ip是：{}'.format(visitor_ip),
        'nas_url': 'http://10.11.2.231:5000',
        'movie_url': 'http://10.11.2.231:8096',
        'movie_name': 'jellyfin影音系统'
    }

    if visitor_ip == '111.46.163.21':  # 外网访问
        ins.nat_env = '没有连接校园网，您的ip是：'.format(visitor_ip)
        ins.nas_url = 'https://ammaa.cn:61389'
        ins.movie_url = '#'
        ins.movie_name = '不在内网，无法访问'
    return render_template('index.html', ins=ins)

