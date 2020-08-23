# Generated by Django 3.1 on 2020-08-23 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.IntegerField(choices=[(0, '申请'), (1, '通过'), (2, '拒绝')], default=0, verbose_name='审核状态'),
        ),
        migrations.AlterModelTable(
            name='student',
            table='student',
        ),
    ]