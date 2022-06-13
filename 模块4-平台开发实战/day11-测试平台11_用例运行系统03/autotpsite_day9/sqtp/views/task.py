"""
@author: haiwen
@date: 2021/11/9
@file: task.py
"""
from sqtp.models import Plan
from sqtp.serializers import PlanSerializer
from rest_framework import viewsets


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    # 定义运行测试计划方法,批量运行测试用例并生成测试报告
    def run_plan(self):
        pass
