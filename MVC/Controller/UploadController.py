"""
@author shuijing
@date 2023-11-11 11:35
@version 1.0 
@description 
"""
from flask import Blueprint, render_template, request

# 记得去app.py注册蓝图
upload_blue = Blueprint('upload', __name__, url_prefix='/upload')


@upload_blue.route('/')
def upload():
    # 检查是否有文件被上传
    if 'file' not in request.files:
        return '没有文件上传'

    file = request.files['file']

    # 保存文件到 "/upload" 文件夹
    file.save('upload/' + file.filename)

    return '上传成功'
