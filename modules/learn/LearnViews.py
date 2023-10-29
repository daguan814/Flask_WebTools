"""
@author shuijing
@date 2023-10-20 16:43
@version 1.0 
@description 
"""
from flask import Blueprint, request, render_template, jsonify, make_response, redirect, url_for

# prefix是加上去的，index不需要加，加了会导致没有根路由
learn_blue = Blueprint('learn', __name__, url_prefix='/learn')


@learn_blue.route('/')
def user():
    return 'user'


'''# <int:name> 还可以是<path:name>,这样就可以接受///将斜杠作为参数'''


@learn_blue.route('/<name>', )
def get_name(name):
    print(name)
    return name


'''方法，可以是单个或者多个的'''


@learn_blue.route('/req_methods', methods=['GET', 'POST'])
def method():
    return 'post method'


"""
# 请求与响应
# 重要属性：
# url 完整清求
# base_url  去掉GET参数的URL
# host_url  只有主机和端口号的URL
# path 路由中的路径
# method 请求方法
# remote_addr 请求的客户端地址
# args GET请求参数
# form PosT请求参数
# files 文件上传
# headers 请求头
# cookies  请求中的cookie
"""


# 如果是get请求则在URL中带参数，如果是post则是用form表单传输数据
# 推荐使用request.args.get请求来获取
@learn_blue.route('/req', methods=['GET', 'POST'])
def req():
    # get请求
    # res = requests.get('http://127.0.0.1:9000/learn/req?name=lisi&age=33')
    print(request.args)  # ImmutableMultiDict([('name', 'lisi'), ('age', '33')])
    print(request.args.get('name'))
    print(request.args.getlist('name'))

    # post请求
    # res = requests.post('http://127.0.0.1:9000/learn/req', data={'name': '12412', 'age': '14'})
    print(request.form)
    print(request.form.get('name'))
    return 'request ok'


# 响应
@learn_blue.route('/rep')
def get_response():
    # 响应的几种方式

    # 1.字符串
    # return '123'

    # 2. 模版渲染(用于前后端不分离)
    # return render_template('learn.html', name='zhangsan', age='23')

    # 3.返回json数据（前后端分离）
    # data = {'name': 'lisi', 'age': 44}
    # return   data
    # return jsonify(data)

    # 4.自定义响应对象
    html = render_template('learn.html', name='zhangsan', age='23')
    res = make_response(html, 200)
    return res


'''重定向'''


@learn_blue.route('/redi')
def make_redirect():
    # 正常解析
    # return redirect('https://baidu.com')
    # return redirect('/learn/user')

    # url_for传参  蓝图名称.视图函数名 反向解析
    ret = url_for('learn.user', name='xigua', age=12)
    return redirect(ret)


'''cookie'''
