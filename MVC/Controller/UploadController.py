"""
@author shuijing
@date 2023-11-11 11:35
@version 1.0 
@description 
"""
import random
from datetime import datetime

from flask import Blueprint, render_template, request, session, jsonify
from MVC.Dao.UserFileDao import UserFile
from exps import db

# 记得去app.py注册蓝图
upload_blue = Blueprint('upload', __name__, url_prefix='/upload')


@upload_blue.route('/', methods=['POST'])
def upload():
    # 检查是否有文件被上传
    if 'file' not in request.files:
        return '没有文件上传'

    file = request.files['file']
    # 先去读取数据库的所有的四位fileId
    fileId_List = UserFile.query.with_entities(UserFile.fileId).all()
    print(fileId_List)
    random_number = 0000
    for i in range(0, 1000):
        random_number = random.randint(1000, 9999)
        if random_number not in fileId_List:
            break
    saveFileName = str(random_number) + '_' + file.filename
    print(saveFileName)
    # 添加一个数据
    try:
        uf = UserFile()
        uf.fileId = random_number
        uf.FileName = saveFileName
        uf.userName = session['userName']
        uf.downTimes = 0
        uf.delStatus = False
        # 创建时间
        uf.createTime = datetime.now()
        db.session.add(uf)
        db.session.commit()
    except Exception as e:
        print(f"添加失败，错误信息: {str(e)}")
        db.session.rollback()
        db.session.flush()
        response_data = {'status': 300, 'message': '添加到数据库错误！'}
        return jsonify(response_data)

    # 保存文件到 "/upload" 文件夹
    file.save('uploads/' + saveFileName)
    response_data = {'status': 200, 'message': '上传成功，您的取件码：{}'.format(random_number)}
    return jsonify(response_data)
