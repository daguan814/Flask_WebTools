"""
@author shuijing
@date 2023-11-08 15:28
@version 1.0 
@description 
"""
from datetime import timedelta

from flask import Blueprint, render_template, make_response, redirect, request

from MVC.Service.IndexService import qiandao_judge, get_tomorrow_expiry_time

# 蓝图
index_blue = Blueprint('index', __name__)


@index_blue.route('/')
def index():
    nowIp = request.remote_addr
    print(nowIp)
    if "10.11.2" not in nowIp:
        ins = {
            'nat_env': '欢迎进入外网环境',
            'nas_url': 'https://amaa.cn:61389',
            'movie_url': '#',
            'movie_name': '外网不可访问影音系统',
            "qiandao": '今天没有签到，去签到',
            "flash": 'https://amaa.cn:14250/flashTrans'
        }
    else:
        # 模版渲染
        ins = {
            'nat_env': '欢迎进入校园网环境,您的ip：{}'.format(nowIp),
            'nas_url': 'http://10.11.2.231:5000',
            'movie_url': 'http://10.11.2.231:8096',
            'movie_name': 'jellyfin影音系统',
            "qiandao": '今天没有签到，去签到',
            "flash": '/flashTrans'  # 自己的路由，直接写就行了
        }
    # 查看cookie，看看是否签到了，没签到渲染没签到
    qiandao_judge(ins=ins)
    return render_template('index.html', ins=ins)


@index_blue.route('/sakuraSign')
def sakuraSign():
    # 去签到，在签到之前设置cookie
    # 创建响应对象

    response = make_response(redirect('https://www.natfrp.com/user/'))
    # 设置名为 'your_cookie_name' 的 Cookie，并设置其值为 'Your Cookie Value'

    response.set_cookie('qiandao', 'yes', expires=get_tomorrow_expiry_time() - timedelta(hours=8))

    # 创建一个重定向到另一个页面的对象
    return response
