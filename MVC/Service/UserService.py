"""
@author shuijing
@date 2023-11-13 16:45
@version 1.0 
@description 
"""

import bcrypt


# 哈希盐值加密
def jiami(yuandata):
    plain_password = yuandata
    # 生成盐值，可以存储在数据库中
    salt = bcrypt.gensalt()

    # 使用bcrypt进行密码哈希
    hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'), salt)

    # 返回加密结果
    return hashed_password


# 验证密码
def verifyPwd(login_password, dbpwd):
    if bcrypt.checkpw(login_password.encode('utf-8'), dbpwd):
        # 密码匹配，允许登录
        return True
    else:  # 密码不匹配，拒绝登录
        return False
