"""
@author shuijing
@date 2023-11-13 08:53
@version 1.0 
@description 
"""
from datetime import datetime

from exps import db


class User(db.Model):
    # 表名
    __tablename__ = 'User'
    # 字段
    userId = db.Column(db.String(30), primary_key=True)
    userName = db.Column(db.String(20), nullable=False)
    userPwd = db.Column(db.String(50), nullable=False)
    createTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
