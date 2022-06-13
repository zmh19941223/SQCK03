"""
@author: haiwen
@date: 2021/10/23
@file: urls.py
"""


from django.urls import path, include
from sqtp import views
from rest_framework.urlpatterns import format_suffix_patterns
#使用rest框架自带的路由器生成路由列表
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'requests',views.RequestViewSet)

urlpatterns = [
    # path('requests/',views.RequestList.as_view()), #视图类需要调用as_view转化
    # path('requests/<int:pk>',views.RequestDetail.as_view()),
    path('',include(router.urls))
]
# urlpatterns = format_suffix_patterns(urlpatterns) #重写路由