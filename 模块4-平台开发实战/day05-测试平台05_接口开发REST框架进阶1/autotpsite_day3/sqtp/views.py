from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from sqtp.models import Request
from sqtp.serializers import RequestSerializer

@api_view(['GET','POST']) #列表中是允许的请求方法
def request_list(request,format=None):
    if request.method=='GET':  # 处理查询请求
        # 获取序列化器--针对当前数据模型的所有数据
        serializer = RequestSerializer(Request.objects.all(),many=True)
        print(request.data)
        # 返回Json格式响应
        return Response(serializer.data) #使用REST框架的响应对象，自动为你分配返回格式
    elif request.method == 'POST': # 处理新增请求
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def request_detail(request,_id,format=None):
    try:
        req_obj = Request.objects.get(id=_id)
    except Exception:
        return Response(status=404) #返回错误状态码

    if request.method == 'GET':
        # 序列化
        serializer = RequestSerializer(req_obj)
        return Response(serializer.data)

    elif request.method=='PUT': # 处理修改
        # 采用序列化器实现修改动作
        serializer = RequestSerializer(req_obj,data=request.data)
        if serializer.is_valid(): # 判断data中的数据是否符合要求
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE': #处理删除
        req_obj.delete() #
        return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework.views import APIView

# 改写   request_list视图方法
# class RequestList(APIView):
#     '''
#     查询所有数据和新增单个数据的功能
#     '''
#     def get(self,request,format=None):  # 处理查询请求
#         # 获取序列化器--针对当前数据模型的所有数据
#         serializer = RequestSerializer(Request.objects.all(),many=True)
#         # 返回Json格式响应
#         return Response(serializer.data) #使用REST框架的响应对象，自动为你分配返回格式
#     def post(self,request,format=None): # 处理新增请求
#         serializer = RequestSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
# # 改写request_detail视图方法
# class RequestDetail(APIView):
#     # 覆盖父类的get_object方法实现
#     def get_object(self,_id):
#         try:
#             req_obj = Request.objects.get(id=_id)
#             return req_obj
#         except Exception:
#             return Response({"error":"data not found"},status=404) #返回错误状态码
#
#     def get(self,request,_id,format=None):
#         req_obj = self.get_object(_id)
#         #如果是异常响应，直接返回
#         if isinstance(req_obj,Response):
#             return req_obj
#         serializer = RequestSerializer(req_obj)
#         return Response(serializer.data)
#
#     def put(self,request,_id,format=None):
#         req_obj = self.get_object(_id)
#         #如果是异常响应，直接返回
#         if isinstance(req_obj,Response):
#             return req_obj
#         serializer = RequestSerializer(req_obj,data=request.data)
#         if serializer.is_valid(): # 判断data中的数据是否符合要求
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,rquest,_id,format=None):
#         req_obj = self.get_object(_id)
#         #如果是异常响应，直接返回
#         if isinstance(req_obj,Response):
#             return req_obj
#         req_obj.delete() #
#         return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

class RequestList(ListCreateAPIView):
    '''
    查询所有数据和新增单个数据的功能
    '''
    queryset = Request.objects.all()  # 数据的查询集
    serializer_class = RequestSerializer

class RequestDetail(RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.all()  # 数据的查询集
    serializer_class = RequestSerializer

from rest_framework import viewsets


# 优化3：视图集--增删改查
class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()  # 数据的查询集
    serializer_class = RequestSerializer