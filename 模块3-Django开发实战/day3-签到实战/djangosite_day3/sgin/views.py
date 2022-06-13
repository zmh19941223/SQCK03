from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from sgin.models import Event,Guest


def events(request):
    # 从数据库获取实时的数据
    event_list = Event.objects.all()
    # 简单的返回字符串
    # return HttpResponse([f'<li>{event}</li>' for event in event_list])
    # 返回一个模板内容
    return render(request,'events.html',{'event_list':event_list})

#发布会详情页
def event_detail(request,event_id):
    # 从某处获取到当前页面的发布会数据对象
    try:
        event = Event.objects.get(id=event_id)
    except:
        return render(request,'404.html')

    return render(request,'event_detail.html',{'event':event})


#嘉宾
def guests(request):
    # 从数据库获取嘉宾数据
    guest_list = Guest.objects.all()
    # 返回模板页面展示嘉宾数据
    return render(request,'guests.html',{'guest_list':guest_list})


#嘉宾详情
def guest_detail(request,guest_id):
    # 获取单个嘉宾数据
    try:
        guest = Guest.objects.get(id=guest_id)
    except:
        return render(request,'404.html')

    return render(request,'guest_detail.html',{'guest':guest})

# 处理签到
@csrf_exempt
def do_sgin(request,event_id):
    # 拿到待签到的发布会
    event =Event.objects.get(pk=event_id)
    # 拿到手机号，获取签到的嘉宾
    if request.method =='POST': # 请求方法是POST并且是表单格式的数据
        phone = request.POST['phone']
        # 判断手机号是否正确
        res=Guest.objects.filter(phone=phone)
        if not res:
            #手机号错误
            return render(request,'event_detail.html',{'error':'手机号错误','event':event})
        guest = res[0]
        # 是否是当前发布会的嘉宾
        if guest.event.id != event_id:
            return render(request,'event_detail.html',{'error':'非当前发布会嘉宾','event':event})

        # 是否已经签到
        if guest.is_sgin:
            return render(request,'event_detail.html',{'error':'已签到，不要重复提交','event':event})

        # 执行签到
        try:
            guest.is_sgin=True
            guest.save()
        except:
            return render(request,'event_detail.html',{'error':'签到失败，服务器异常','event':event})

        # 重定向到另一个路由
        return redirect(f'/sgin/sgin_success/{phone}')


def sgin_success_page(request,phone):
    return render(request,'sgin_success.html',{'phone':phone})


def add_event_page(request):
    return render(request,'event_add.html')


def add_event(request):
    #获取发布会数据
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        limits = request.POST['limits']
        if request.POST.get('status',False):
            status=True
        else:
            status=False
        start_time = request.POST['start_time']

        #创建发布会
        try:
            event = Event.objects.create(name=name,address=address,limits=limits,status=status,start_time=start_time)
        except Exception as e:
            return render(request,'event_add.html',{'error':repr(e)}) # repr获取异常的精简信息

        #保存成功
        return redirect('/sgin/events/')