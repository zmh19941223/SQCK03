"""
@author: haiwen
@date: 2021/10/19
@file: debugtalk.py
"""

# 定义脚本，函数可以被用例文件引用
import json

import requests


def login_variables():
    # 读取数据库或者EXCEL或其他文件...
    return {'account':'auto','psw':'sdfsdfsdf','code':0}

def add_course_variables():
    return {"name":"中学数学","desc":"微积分", "idx":"4"}


def hook_setup():
    with open('setup.txt','w',encoding='utf-8') as f:
        f.write('执行初始化步骤')

def hook_teardown():
    with open('teardown.txt','w',encoding='utf-8') as f:
        f.write('执行清除步骤')

def before_add_course(request):
    print('####$$$$$$$##########$$$$$$$$$$$########')
    print(request)
    data= request['data']['data']  #从原请求信息获取入参
    # data['name']='计算机课程_steup'
    # data['desc']='steup_test'
    # data['display_idx']='100'

    request['data']['data']= json.dumps(data) #覆盖掉原请求数据


def after_add_course(response):
    print(response.json)
    course_id = response.json['id']
    # 完成以后根据id取删除该课程
    requests.delete('http://localhost/api/mgr/sq_mgr/',data={'action':'delete_course','id':course_id})