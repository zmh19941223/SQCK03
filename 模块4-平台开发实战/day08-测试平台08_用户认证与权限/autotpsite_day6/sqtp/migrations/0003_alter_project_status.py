# Generated by Django 3.2.7 on 2021-11-02 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqtp', '0002_auto_20211030_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.SmallIntegerField(choices=[(0, '开发中'), (1, '维护中'), (2, '稳定运行')], default=2, max_length=32, verbose_name='项目状态'),
        ),
    ]
