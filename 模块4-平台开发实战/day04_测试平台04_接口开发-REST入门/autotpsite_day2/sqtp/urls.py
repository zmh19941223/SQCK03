"""
@author: haiwen
@date: 2021/10/23
@file: urls.py
"""


from django.urls import path
from sqtp import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('requests/',views.request_list),
    path('requests/<int:_id>',views.request_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns) #重写路由