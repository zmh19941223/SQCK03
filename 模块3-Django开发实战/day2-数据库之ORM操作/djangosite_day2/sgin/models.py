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


