# -*- coding:utf-8 -*-
# 告诉PEP8规范检测工具，NOQA这里不需要检测
from .base import *  # NOQA

DEBUG = True

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangoTraining',
        'HOST': '120.25.247.92',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': 'Aly_mysql_891125'
    }
}
print('develop settings...........')
