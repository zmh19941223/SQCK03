"""
@author: haiwen
@date: 2021/10/23
@file: serializers.py
"""
# 序列化器作用是 转化json为模型对象数据，或者转化模型对象数据为Json
# 序列化器是针对数据模型，一个序列化器对应一个模型

from rest_framework import serializers
from sqtp.models import Step,Request
#命名规范：模型名+Serializer
class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request #指定序列器对应的模型
        # fields =['step','method','url','params','headers'] # 指定序列化模型中的字段
        fields = '__all__' #序列化所有字段

