from django.db.models import Value
from django.test import TestCase

# Create your tests here.
from sqtp.models import Case,Config,Step,Request

class TestRelatedQuery(TestCase):
    def setUp(self) -> None:
        # 创建用例
        config1 = Config.objects.create(name='case001',base_url='http://localhost')
        config2 = Config.objects.create(name='case002',base_url='http://localhost')
        self.case1 = Case.objects.create(config=config1)
        self.case2 = Case.objects.create(config=config2)

    def test_steps_query(self):
        step1 = Step.objects.create(belong_case=self.case1,name='step1')
        step1.linked_case=self.case2
        step1.save()
        step2 = Step.objects.create(belong_case=self.case2,name='step2')

        # 正向查询
        print('=============正向查询============')
        print(step1.belong_case) #查看step1所属用例
        print(step1.linked_case) #查看step1关联的用例
        # 反向查询
        print('=============反向查询============')
        # related_name代替step_set
        print(self.case1.teststeps.all())  #查询用例1下面由哪些步骤
        print(self.case2.linked_steps.all()) #查询case2被哪些步骤引用


class TestJsonField(TestCase):
    def setUp(self) -> None:
        req1 = Request.objects.create(method=1,url='/mgr/course/',data={"name":"小明","age":16,"address":"nanjing"})

    def test_json01(self):
        req = Request.objects.all().first()
        print(req)
        # 测试修改--整体
        req.data={"name":"小强","age":18,"address":"shanghai","school":{"name":"北大","level":"top1"}}
        req.save()
        print(Request.objects.all().first().data) # 查看修改后的内容

        # 修改局部
        req=Request.objects.all().first()
        print(req.data['name']) # 修改前
        req.data['name'] = '星辰大海'
        req.save()
        print(Request.objects.all().first().data['name']) # 修改后

        # json删除操作
        # 删除整体
        # req.data=Value('null')  设置成json的null
        # req.data=None            设置成sql的null
        # req.save()
        # print(Request.objects.all().first().data)

        # 删除局部
        req.data.pop('name')
        req.save()
        print(Request.objects.all().first().data)

        # 条件查询--根据json字段的某个值来查询，json字段__嵌套字段
        # res=Request.objects.filter(data__age=18)
        res=Request.objects.filter(data__school__name="北大")
        print('======json条件查询=====')
        print(res)