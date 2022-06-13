"""
@author: haiwen
@date: 2021/11/9
@file: hr3.py
"""
from httprunner.cli import main_run
from rest_framework import status
from rest_framework.decorators import  action
from rest_framework.response import Response

from sqtp.models import Request, Case, Step
from sqtp.serializers import RequestSerializer, CaseSerializer, StepSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from django.utils.decorators import method_decorator


# 优化3：视图集--增删改查
@method_decorator(name='list',
                  decorator=swagger_auto_schema(operation_summary='列出数据', operation_description='列出请求数据...'))
@method_decorator(name='create',
                  decorator=swagger_auto_schema(operation_summary='增加数据', operation_description='增加请求数据...'))
@method_decorator(name='retrieve',
                  decorator=swagger_auto_schema(operation_summary='查看详情', operation_description='查看单个请求数据...'))
@method_decorator(name='destroy',
                  decorator=swagger_auto_schema(operation_summary='删除数据', operation_description='删除请求数据...'))
@method_decorator(name='update',
                  decorator=swagger_auto_schema(operation_summary='更新数据', operation_description='更新请求数据...'))
class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()  # 数据的查询集
    serializer_class = RequestSerializer


class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    # 同步创建用户
    def perform_create(self, serializer):
        serializer.save(create_by=self.request.user)
    # 同步更新用户
    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    @action(methods=['GET'],detail=True,url_path='run',url_name='run_case')
    # 完整的url等于/cases/<int:case_id>/run
    def run_case(self,request,pk):
        # 获取序列化器
        case = Case.objects.get(pk=pk) #根据ID获取当前用例
        serializer = self.get_serializer(instance=case)
        path = serializer.to_json_file()
        # subprocess.Popen(f'hrun {path}',shell=True)  #命令行执行法
        # HR3 API执行法
        exit_code=main_run([path])
        # 根据推出代码判断是否执行成功
        if exit_code !=0:
            return Response(data={'error':'failed run case','retcode':exit_code},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data={'msg':'run success','retcode':200})


class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer