# Generated by Django 3.2.7 on 2021-11-09 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sqtp', '0006_auto_20211106_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('status', models.SmallIntegerField(choices=[(0, '未运行'), (1, '执行中'), (2, '中断'), (3, '已执行')], default=0, verbose_name='执行状态')),
                ('exec_count', models.PositiveSmallIntegerField(default=0, verbose_name='执行次数')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='计划名称')),
                ('case', models.ManyToManyField(blank=True, to='sqtp.Case', verbose_name='测试用例')),
                ('create_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='plan_create_by', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
                ('environment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sqtp.environment', verbose_name='测试环境')),
                ('executor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='执行者')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='plan_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='更新者')),
            ],
            options={
                'ordering': ['id'],
                'abstract': False,
            },
        ),
    ]
