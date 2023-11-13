"""
@author shuijing
@date 2023-11-11 11:46
@version 1.0 
@description 
"""
import uuid
import bcrypt
from flask import Blueprint, render_template, request
from MVC.Dao.UserDao import User
from MVC.Dao.UserFileDao import UserFile
from exps import db

# 记得去app.py注册蓝图
flashTrans_blue = Blueprint('flashTrans', __name__, url_prefix='/flashTrans')


@flashTrans_blue.route('/')
def flashTrans():
    return render_template('flashTrans.html')


@flashTrans_blue.route('/userAdd', methods=['POST'])
def addUser():
    # 用户加密
    userPwd = request.form.get('userPwd')
    # 添加一个数据
    try:
        u = User()
        u.userId = str(uuid.uuid4())[:20]
        u.userName = request.form.get('userName')
        u.userPwd = request.form.get('userPwd')
        #创建时间自动填写
        db.session.add(u)
        db.session.commit()
    except:
        db.session.rollback()  # 回滚，只要上面的东西有问题就会回复到没更改的时候
        db.session.flush()  #
        return '有这个用户了'

    return '创建用户成功'
