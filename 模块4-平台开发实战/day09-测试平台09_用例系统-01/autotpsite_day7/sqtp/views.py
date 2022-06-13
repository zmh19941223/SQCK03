from django.contrib import auth

# Create your views here.
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from sqtp.models import Request, Case, Step, Project, Environment, User
from sqtp.permissions import IsOwnerOrReadOnly
from sqtp.serializers import RequestSerializer, CaseSerializer, StepSerializer, ProjectSerializer, \
    EnvironmentSerializer, UserSerializer, RegisterSerializer, LoginSerializer
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


class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    #权限
    permission_classes = (IsOwnerOrReadOnly,)


class EnvironmentViewSet(viewsets.ModelViewSet):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer
    #权限
    #authentication_classes = (()) #传入空元组表示禁用全局认证
    permission_classes = (())


@api_view(['GET'])
@authentication_classes((BasicAuthentication,SessionAuthentication))
@permission_classes((IsAuthenticated,))
def user_list(request):
    query_set = User.objects.all()
    serializer = UserSerializer(query_set, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user_detail(request, _id):
    try:
        user = User.objects.get(pk=_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(instance=user)
    return Response(serializer.data)

#注册用户
@api_view(['POST'])
@permission_classes(())
def register(request):
    # 获取序列化器
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid(): #根据序列器和模型字段综合检查数据是否合法
        user = serializer.register() #创建用户数据
        auth.login(request,user) # 完成用户登录状态设置
        return Response(data={'msg':'register success','is_admin':user.is_superuser,'retcode':status.HTTP_201_CREATED},status=status.HTTP_201_CREATED)
    return Response(data={'msg':'error','retcode':status.HTTP_400_BAD_REQUEST,'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes(())
def login(request):
    # 获取登录信息--序列化器
    serializer = LoginSerializer(data=request.data)
    user = serializer.validate(request.data)
    if user:
        auth.login(request,user) #登录存储session信息
        return Response(data={'msg':'login success','to':'index.html'},status=status.HTTP_302_FOUND)
    return Response(data={'msg':'error','retcode':status.HTTP_400_BAD_REQUEST,'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def logout(request):
    if request.user.is_authenticated: #如果当前用户处于登录状态
        auth.logout(request) #登出，清除session
    return Response(data={'msg':'logout success','to':'login.html'},status=status.HTTP_302_FOUND)

#当前用户信息
@api_view(['GET'])
@permission_classes(())
def current_user(request):
    if request.user.is_authenticated: #如果当前用户处于登录状态
        # 返回当前用户信息
        serializer = UserSerializer(request.user)
        return Response(data=serializer.data)
    else:
        return Response(data={'retcode':403,'msg':'未登录','to':'login.html'},status=403)
