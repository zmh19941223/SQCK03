# Generated by Django 3.2.7 on 2021-11-06 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sqtp', '0005_config_project'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='step',
            options={'ordering': ['id', 'sorted_no'], 'verbose_name': '测试步骤表'},
        ),
        migrations.AddField(
            model_name='step',
            name='sorted_no',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='步骤顺序'),
        ),
        migrations.AlterField(
            model_name='config',
            name='name',
            field=models.CharField(max_length=128, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='request',
            name='step',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='request', to='sqtp.step'),
        ),
        migrations.AlterUniqueTogether(
            name='step',
            unique_together={('belong_case', 'sorted_no')},
        ),
    ]
