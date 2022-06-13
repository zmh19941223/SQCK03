from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def events(request):
    event_list = [
        '自动化发布会',
        '测试开发布会',
        '性能发布会'
    ]
    # 简单的返回字符串
    # return HttpResponse([f'<li>{event}</li>' for event in event_list])
    # 返回一个模板内容
    return render(request,'events.html',{'event_list':event_list})

#发布会详情页
def event_detail(request):
    return render(request,'event_detail.html')