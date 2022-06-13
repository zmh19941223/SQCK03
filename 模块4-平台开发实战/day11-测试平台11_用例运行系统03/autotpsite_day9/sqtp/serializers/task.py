"""
@author: haiwen
@date: 2021/11/9
@file: task.py
"""

from rest_framework import serializers
from sqtp.models import Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields='__all__'

