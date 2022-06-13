"""
@author: haiwen
@date: 2021/10/9
@file: urls.py
"""
from django.urls import path
from sgin import views
#子路由列表
urlpatterns=[
    path('events/',views.events),  #发布会管理页面
    path('events/<int:_id>',views.event_detail), #events/8
]