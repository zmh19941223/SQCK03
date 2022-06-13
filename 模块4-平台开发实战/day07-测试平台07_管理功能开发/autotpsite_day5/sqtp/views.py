from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from sqtp.models import Request, Case,Step,Project,Environment,User
from sqtp.serializers import RequestSerializer, CaseSerializer, StepSerializer, ProjectSerializer, \
    EnvironmentSerializer, UserSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from django.utils.decorators import method_decorator

# 优化3：视图集--增删改查
@method_decorator(name='list',decorator=swagger_auto_schema(operation_summary='列出数据',operation_description='列出请求数据...'))
@method_decorator(name='create',decorator=swagger_auto_schema(operation_summary='增加数据',operation_description='增加请求数据...'))
@method_decorator(name='retrieve',decorator=swagger_auto_schema(operation_summary='查看详情',operation_description='查看单个请求数据...'))
@method_decorator(name='destroy',decorator=swagger_auto_schema(operation_summary='删除数据',operation_description='删除请求数据...'))
@method_decorator(name='update',decorator=swagger_auto_schema(operation_summary='更新数据',operation_description='更新请求数据...'))
class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()  # 数据的查询集
    serializer_class = RequestSerializer

class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class EnvironmentViewSet(viewsets.ModelViewSet):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer

@api_view(['GET'])
def user_list(request):
    query_set = User.objects.all()
    serializer = UserSerializer(query_set,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def user_detail(request,_id):
    try:
        user = User.objects.get(pk=_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(instance=user)
    return Response(serializer.data)

# 用户定制接口
@swagger_auto_schema(method='POST',operation_summary='用户定制化摘要',operation_description='用户定制化详情信息...')
@api_view(['POST'])
def customer_api(request):
    return Response(data={"retcode":status.HTTP_200_OK,"msg":"testing..."})
