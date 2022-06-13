from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from sgin.models import Event


def events(request):
    # 从数据库获取实时的数据
    event_list = Event.objects.all()
    # 简单的返回字符串
    # return HttpResponse([f'<li>{event}</li>' for event in event_list])
    # 返回一个模板内容
    return render(request,'events.html',{'event_list':event_list})

#发布会详情页
def event_detail(request,_id):
    # 从某处获取到当前页面的发布会数据对象
    event = Event.objects.get(id=_id)
    return render(request,'event_detail.html',{'event':event})