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

@api_view(['GET']) #列表中是允许的请求方法
def request_list(request,format=None):
    # if request.method=='GET':
    # 获取序列化器--针对当前数据模型的所有数据
    serializer = RequestSerializer(Request.objects.all(),many=True)
    print(request.data)
    # 返回Json格式响应
    # return JsonResponse(data=serializer.data,safe=False) #safe=False是为了支持字典以外的python对象转化成json
    return Response(serializer.data) #使用REST框架的响应对象，自动为你分配返回格式

@api_view(['GET'])
def request_detail(request,_id,format=None):
    try:
        req_obj = Request.objects.get(id=_id)
        # 序列化
        serializer = RequestSerializer(req_obj)
        return Response(serializer.data)
    except Exception:
        return Response(status=404) #返回错误状态码

