"""
@author shuijing
@date 2023-11-13 09:02
@version 1.0 
@description 
"""
from datetime import datetime

from exps import db


class UserFile(db.Model):
    __tablename__ = 'UserFile'
    # 字段
    userName = db.Column(db.String(255), primary_key=True)
    fileId = db.Column(db.Integer, nullable=False)
    FileName = db.Column(db.Text, nullable=False)
    downTimes = db.Column(db.Integer, nullable=False)
    createTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    delStatus = db.Column(db.Boolean, nullable=False)
