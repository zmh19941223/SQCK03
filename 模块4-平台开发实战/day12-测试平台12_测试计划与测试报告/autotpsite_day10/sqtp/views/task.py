"""
@author: haiwen
@date: 2021/11/9
@file: task.py
"""
from httprunner.cli import main_run
from rest_framework.decorators import action
from rest_framework.response import Response

from sqtp.models import Plan, Report
from sqtp.serializers import PlanSerializer, CaseSerializer
from rest_framework import viewsets

from sqtp.serializers.task import ReportSerialzier
from sqtp.utils import setup_case_dir


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

    # 同步创建者
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    # 同步更新者
    def perform_update(self, serializer):
        serializer.save(updater=self.request.user)

    # 定义运行测试计划方法,批量运行测试用例并生成测试报告
    @action(methods=['GET'],detail=True,url_path='run',url_name='run_plan')
    def run_plan(self,request,pk):
        # 获取测试计划
        plan = Plan.objects.get(pk=pk)
        # 更新计划状态--执行中
        plan.status=1
        plan.save()
        setup_case_dir('testcase') # 执行前清空用例目录
        # 取出关联的测试用例，执行这些测试用例
        case_list=[] #用例路径
        for case in plan.cases.all(): # 生成测试用例文件，再收集用例路径
            cs = CaseSerializer(instance=case)
            path = cs.to_json_file()
            case_list.append(path)
        # hr3执行用例路径列表
        # pytest入参列表规则 路径1，路径2，路径3....参数1,参数2...
        exit_code=main_run([*case_list,'--alluredir=report/tmp'])
        # 更新测试计划执行状态和执行次数
        plan.status = 3
        plan.exec_counts += 1 #执行次数+1
        plan.save()
        # 保存报告数据
        Report.objects.create(plan=plan,path='report/html/index.html',trigger=request.user)

        # 根据推出代码判断是否执行成功
        if exit_code !=0:
            return Response(data={'error':'failed run plan','retcode':exit_code},status=500)
        return Response(data={'msg':'run success','retcode':200})


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerialzier

    # 报告只提供查询功能
    def create(self, request, *args, **kwargs):
        return Response(data={'msg':'error','retcode':404,'error':'创建功能只针对测试计划开放'},status=404)

    def update(self, request, *args, **kwargs):
        return Response(data={'msg':'error','retcode':404,'error':'更新功能只针对测试计划开放'},status=404)


