"""
@author shuijing
@date 2023-11-11 10:22
@version 1.0 
@description 
"""
import datetime

from flask import request


def get_tomorrow_expiry_time():
    # 获取当前时间
    current_time = datetime.datetime.utcnow()

    # 获取明天凌晨的时间
    tomorrow = current_time + datetime.timedelta(days=1)
    expiry_time = datetime.datetime(tomorrow.year, tomorrow.month, tomorrow.day, 0, 0, 0)

    return expiry_time


def qiandao_judge(ins):
    # 查看cookie，看看是否签到了，没签到渲染没签到
    qiandao_cookie = request.cookies.get("qiandao", "no")
    print(qiandao_cookie)
    # 签到了，渲染签到了
    if qiandao_cookie == 'yes':
        ins["qiandao"] = "今天已经签到了"

