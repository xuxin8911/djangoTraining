# -*- coding=utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Link(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    WEIGHT_ITEMS = (
        (1, '第一级'),
        (2, '第二级'),
        (3, '第三级'),
        (4, '第四级'),
        (5, '第五级')
    )
    title = models.CharField(max_length=64, verbose_name='标题')
    href = models.URLField(verbose_name='链接')  # 默认长度200
    status = models.PositiveIntegerField(choices=STATUS_ITEMS, default=STATUS_NORMAL, verbose_name='状态')
    weight = models.PositiveIntegerField(choices=WEIGHT_ITEMS, default=1, verbose_name='权重',
                                         help_text='权重高展示顺序靠前')
    owner = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '友链'
        # db_table = 'link'


class SideBar(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    SIDE_TYPE = (
        (1, 'HTML'),
        (2, '最新文章'),
        (3, '最热文章'),
        (4, '最近评论'),
    )
    title = models.CharField(max_length=64, verbose_name='标题')
    display_type = models.PositiveIntegerField(choices=SIDE_TYPE, default=1, verbose_name='展示类型')
    content = models.CharField(max_length=500, blank=True, verbose_name='内容', help_text='如果设置的不是HTML类型，可以为空')
    status = models.PositiveIntegerField(choices=STATUS_ITEMS, default=1, verbose_name='状态')
    owner = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '侧边栏'
