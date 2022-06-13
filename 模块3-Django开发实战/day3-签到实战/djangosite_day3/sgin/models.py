from django.db import models

# Create your models here.

# 发布会模型--需要继承django自带的模型基类
class Event(models.Model):
    # 名称--字符串 最大长度256
    name = models.CharField(max_length=256,null=False)
    # 地点
    address = models.CharField(max_length=256)
    # 人数
    limits = models.IntegerField(default=100)
    # 状态
    status = models.BooleanField(default=True)
    # 开始时间--允许为空
    start_time = models.DateTimeField(null=True)

    # 覆盖对象对外的字符串表现形式
    def __str__(self):
        return self.name

#嘉宾
class Guest(models.Model):
    #关联发布会,外键字段定义在多方
    event = models.ForeignKey(Event,on_delete=models.CASCADE) #如果删除了该发布会，关联的嘉宾也会被删除
    # 姓名 唯一 最大长度64
    name = models.CharField(max_length=64,unique=True)
    # 手机号 长度11 唯一
    phone = models.CharField(max_length=11,unique=True)
    # 邮箱 -- 邮箱格式xx@yy.zz
    email = models.EmailField()
    # 加入时间 -- 自动获取创建嘉宾数据的时间
    join_time = models.DateTimeField(auto_now_add=True) # auto_now_add 创建的适合自动获取当前时间
    # 签到状态
    is_sgin = models.BooleanField(default=False)

    def __str__(self):
        return self.name
