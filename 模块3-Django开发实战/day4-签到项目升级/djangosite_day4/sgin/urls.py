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
    path('events/<int:event_id>',views.event_detail), #events/8

    path('guests/',views.guests), #嘉宾管理页面
    path('guests/<int:guest_id>',views.guest_detail),

    #签到路由
    path('do_sgin/<int:event_id>',views.do_sgin),
    # 签到成功页
    path('sgin_success/<int:phone>',views.sgin_success_page),

    # 添加发布会表单页面
    path('add_event_page/',views.add_event_page),
    path('add_event/',views.add_event),

    path('add_guest/',views.add_guest),
    path('add_guest_page/',views.add_guest),
]