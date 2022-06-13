"""
@author: haiwen
@date: 2021/11/4
@file: mgr.py
"""
from rest_framework import serializers

from sqtp.models import  Project, Environment

# 项目
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id','admin','name','status','version','desc']


# 环境
class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = '__all__'