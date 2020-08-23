# -*- coding:utf-8 -*-
from __future__ import unicode_literals   # 加上coding和这一行为了兼容python2.7
from django.db import models

# Create your models here.


class Student(models.Model):
    SEX_ITEMS = [
        (1, '男'),
        (2, '女'),
        (0, '未知'),
    ]
    STATUS_ITEMS = [
        (0, '申请'),
        (1, '通过'),
        (2, '拒绝'),
    ]
    name = models.CharField(max_length=128, verbose_name='姓名')  # verbose_name:页面上展示用，相当于我们对字段的描述
    sex = models.IntegerField(choices=SEX_ITEMS, verbose_name='性别')
    profession = models.CharField(max_length=128, verbose_name='职业')
    email = models.EmailField(verbose_name='Email')
    qq = models.CharField(max_length=128, verbose_name='qq')
    phone = models.CharField(max_length=128, verbose_name='电话')
    status = models.IntegerField(choices=STATUS_ITEMS, default=0, verbose_name='审核状态')
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='创建时间', auto_created=True)

    # 调用时返回自身的属性，不然都是显示xx object
    def __str__(self):
        return '<Student: {}'.format(self.name)

    # 配置model属性
    class Meta:
        # verbose_name指定在admin管理界面中显示中文；
        # verbose_name表示单数形式的显示，verbose_name_plural表示复数形式的显示；中文的单数和复数一般不作区别。
        verbose_name = verbose_name_plural = '学员信息'
        # db_table = 'student'

    # 把数据获取逻辑封装到Model层中，对上暴露更语义化接口，同时修改views.py中代码，后期再需要修改时，只需要修改get_all这个函数即可
    @classmethod
    def get_all(cls):
        return cls.objects.all()

    @property
    def sex_show(self):
        return dict(self.SEX_ITEMS)[self.sex]
