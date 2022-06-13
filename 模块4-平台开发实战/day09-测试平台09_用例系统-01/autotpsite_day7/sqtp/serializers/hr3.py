"""
@author: haiwen
@date: 2021/11/4
@file: hr3.py
"""
from rest_framework.exceptions import ValidationError

from sqtp.models import Step, Request, Case, Config, Project
from rest_framework import serializers

#命名规范：模型名+Serializer
from .mgr import ProjectSerializer


class RequestSerializer(serializers.ModelSerializer):
    method = serializers.SerializerMethodField() # 指定该字段通过get_method方法获取
    def get_method(self,obj): #
        return obj.get_method_display()

    class Meta:
        model = Request #指定序列器对应的模型
        # fields =['step','method','url','params','headers'] # 指定序列化模型中的字段
        fields = '__all__' #序列化所有字段


class ConfigSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(required=False,read_only=True)

    class Meta:
        model = Config
        fields = ['project','name','base_url','variables','parameters','export','verify']

class StepSerializer(serializers.ModelSerializer):
    request = RequestSerializer()
    belong_case = serializers.IntegerField(write_only=True,required=False)
    def create(self, validated_data):
        #构造请求
        req_kws = validated_data.pop('request')
        req_serializer=RequestSerializer(data=req_kws)
        if req_serializer.is_valid(raise_exception=True):
            req_obj = req_serializer.save()
        # else:
        #     raise ValidationError(req_serializer.errors)
        #构造步骤
        step_obj = Step.objects.create(testrequest=req_obj,**validated_data)
        return step_obj

    class Meta:
        model = Step
        fields = '__all__'

class CaseSerializer(serializers.ModelSerializer):
    config = ConfigSerializer()  # config字段就对应其序列化器返回的内容
    teststeps = StepSerializer(required=False,many=True) # read_only=True为只读参数，required=False 表示非必填，就不会校验入参 many=True展示为列表形式
    project_id = serializers.CharField(write_only=True) # 只做为入参

    # 覆盖父类新增反方法
    def create(self, validated_data):
        '''
        validated_data: 校验后的入参--字典形式
        '''
        # 创建config
        config_kws = validated_data.pop('config') # 取出config参数
        project = Project.objects.get(pk=validated_data['project_id'])
        config =Config.objects.create(project=project,**config_kws) #关联project
        # 创建用例
        file_path = f'{project.name}_{config.name}.json' # 项目名+用例名.json
        case = Case.objects.create(config=config,file_path=file_path,desc=validated_data['desc'])
        return case

    # 修改用例
    def update(self, instance, validated_data):
        '''
        instance 当前被修改的数据对象
        validated_data 校验后的入参--字典形式
        '''
        config_kws = validated_data.pop('config')  # config入参
        project = Project.objects.get(pk=validated_data.pop('project_id'))
        # 把project数据传递到config入参中
        config_kws['project']=project.id
        conf_serializer = ConfigSerializer(instance=instance.config,data=config_kws)
        # 通过序列化器更新数据
        if conf_serializer.is_valid():
            conf_serializer.save()#调用save方法之前必须调用检查参数动作
        else:
            raise ValidationError(conf_serializer.errors) # 发生错误后，信息保存在序列化器的error字段中
        # 更新case数据
        # instance.file_path = validated_data['file_path']
        # instance.desc = validated_data['desc']

        # teststeps更新
        teststeps=validated_data.pop('teststeps')
        for step in teststeps:
            # 取出步骤关联的用例ID
            step['belong_case']=self.instance.id
            ss=StepSerializer(data=step)
            if ss.is_valid():
                ss.save()
            else:
                raise ValidationError(ss.errors)
        ...
        # 利用python反射自动赋值
        for k,v in validated_data.items():
            # 注意validated_data不要包含instance数据对象没有的字段参数
            setattr(instance,k,v)
        return instance


    class Meta:
        model = Case
        fields = ['config','teststeps','project_id','desc','id','file_path'] #序列化器定义的字段必须再此展示