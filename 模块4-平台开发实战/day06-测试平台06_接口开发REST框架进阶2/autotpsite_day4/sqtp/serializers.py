"""
@author: haiwen
@date: 2021/10/23
@file: serializers.py
"""
# 序列化器作用是 转化json为模型对象数据，或者转化模型对象数据为Json
# 序列化器是针对数据模型，一个序列化器对应一个模型

from rest_framework import serializers
from sqtp.models import Step, Request, Case, Config


#命名规范：模型名+Serializer
class RequestSerializer(serializers.ModelSerializer):
    method = serializers.SerializerMethodField() # 指定该字段通过get_method方法获取
    def get_method(self,obj): #
        return obj.get_method_display()

    class Meta:
        model = Request #指定序列器对应的模型
        # fields =['step','method','url','params','headers'] # 指定序列化模型中的字段
        fields = '__all__' #序列化所有字段


class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = '__all__'

class CaseSerializer(serializers.ModelSerializer):
    config = ConfigSerializer()  # config字段就对应其序列化器返回的内容
    class Meta:
        model = Case
        fields = '__all__'