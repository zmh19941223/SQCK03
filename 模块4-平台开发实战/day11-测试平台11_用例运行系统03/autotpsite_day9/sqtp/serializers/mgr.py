"""
@author: haiwen
@date: 2021/11/4
@file: mgr.py
"""
from rest_framework import serializers

from sqtp.models import  Project, Environment

# 项目
from sqtp.serializers import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)
    admin_id = serializers.IntegerField(write_only=True)
    admin = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ['id','admin','admin_id','name','status','version','desc','create_time','update_time',]


# 环境
class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = '__all__'