"""
@author shuijing
@date 2023-11-11 11:46
@version 1.0 
@description 
"""

import uuid
from datetime import datetime

import bcrypt
from flask import Blueprint, render_template, request, session, redirect, jsonify
from MVC.Dao.UserDao import User
from MVC.Dao.UserFileDao import UserFile
from MVC.Service.FlashTransService import jiami, verifyPwd
from exps import db

# 记得去app.py注册蓝图
flashTrans_blue = Blueprint('flashTrans', __name__, url_prefix='/flashTrans')


@flashTrans_blue.route('/')
def flashTrans():
    # 先获取session里面的用户名，没有就直接设置session为other
    userName = session.get('userName', None)  # 使用 get 方法获取键值，如果键不存在，返回默认值 None
    print(userName)
    if userName is None:  # 没有登陆
        session['userName'] = 'other'  # 默认给个other用户
        userName = '登录'
    else:
        userName = userName + "已登陆"
    return render_template('flashTrans.html', userName=userName)


@flashTrans_blue.route('/loginPage')
def loginPage():
    return render_template('FTloginPage.html')


# 用户登陆
@flashTrans_blue.route('/login', methods=['POST'])
def userLogin():
    # 获取前端发送的JSON数据
    data = request.json

    # 从JSON数据中获取用户名和密码
    username = data.get('username')
    password = data.get('password')

    # 将结果以JSON格式返回给前端
    # 查找这个用户存不存在
    user_by_username = User.query.filter(User.userName == username).first()
    print(user_by_username)
    if user_by_username is None:  # 用户不存在
        response_data = {'status': '300', 'message': '用户不存在'}
    # 判断这个用户的密码是否正确（解密）
    elif not verifyPwd(password, user_by_username.userPwd):
        response_data = {'status': '100', 'message': '用户名或密码不正确'}
    else:
        # 登陆成功添加一个session
        response_data = {'status': '200', 'message': '登陆成功'}
        session['userName'] = username

    return jsonify(response_data)


@flashTrans_blue.route('/userAdd', methods=['POST'])
def addUser():
    # 用户加密
    userPwd = request.form.get('userPwd')
    # 先查询一下这个用户有没有注册过
    # 或者使用通用的 filter 方法
    formUserName = request.form.get('userName')
    user_by_username = User.query.filter(User.userName == formUserName).first()
    if user_by_username:  # 如果有这个用户，直接返回，不创建
        return '这个用户已经创建过了'

    # 添加一个数据
    try:
        u = User()
        u.userId = uuid.uuid4()
        u.userName = request.form.get('userName')
        u.userPwd = jiami(userPwd)  # 存储加密后的密码
        # 创建时间
        u.createTime = datetime.now()
        db.session.add(u)
        db.session.commit()
    except:
        db.session.rollback()  # 回滚，只要上面的东西有问题就会回复到没更改的时候
        db.session.flush()  #
        print(jiami(userPwd))
        return '添加失败'

    return '创建用户成功'
