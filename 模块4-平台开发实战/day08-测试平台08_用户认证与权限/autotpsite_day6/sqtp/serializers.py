"""
@author: haiwen
@date: 2021/10/23
@file: serializers.py
"""
# 序列化器作用是 转化json为模型对象数据，或者转化模型对象数据为Json
# 序列化器是针对数据模型，一个序列化器对应一个模型
from django.conf import settings
from django.contrib import auth
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from sqtp.models import Step, Request, Case, Config, Project, Environment, User


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

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = '__all__'

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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


#注册序列化器
class RegisterSerializer(serializers.ModelSerializer):
    admin_code = serializers.CharField(default='')

    class Meta:
        model = User
        fields=['username','password','email','phone','realname','admin_code']

    # 校验器-自定义校验规则
    def validate(self, attrs): # attrs为入参的字典形式
        #检测admin_code是否正确，
        if attrs.get('admin_code') and attrs['admin_code'] != 'sqtp':
            raise ValidationError('错误的admin_code')
        return attrs #需要返回attrs

    # 创建用户数据
    def register(self):
        #获取入参
        in_param = self.data
        if 'admin_code' in in_param: #创建管理员
            in_param.pop('admin_code') # 用户模型没有admin_code字段，硬传会报错
            user=User.objects.create_superuser(**in_param)
        else:
            user=User.objects.create_user(**in_param)
        return user

#登录序列化器
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

    def validate(self, attrs):
        #验证用户名和密码
        user = auth.authenticate(**attrs)
        if not user:
            raise ValidationError('用户名或密码错误')
        return user
