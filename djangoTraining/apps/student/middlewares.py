# -*- coding:utf-8 -*-
from __future__ import unicode_literals

import time

from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class TimeItMiddleware(MiddlewareMixin):
    # 请求到middleware中进入的第一个方法，一般可以在这里做一些校验，比如用户登录或者http中是否有认证头之类的验证
    # 用到的MiddlewareMixin是django目前版本中用来兼容老版本代码的错事，新版本，django建议自己处理process_request和process_response
    def process_request(self, request):
        self.start_time = time.time()
        return

    # 执行完process_request之后执行的
    def process_view(self, request, func, *args, **kwargs):
        if request.path != reverse('index'):
            return None
        start = time.time()
        response = func(request)
        cost_time = time.time() - start
        print('process view: {:.2f}s'.format(cost_time))
        return response

    # 执行完上面两个，并且执行完view，拿到最终response后，如果使用了模板的response返回方式，就会来到这
    def process_template_response(self, request):
        pass

    # 所有流程执行完就会来到这里，上面的针对带有模板的response
    def process_response(self, request, response):
        cost_time = time.time() - self.start_time
        print('request to response cost: {0:.2f}s {1}'.format(cost_time, 'test'))
        return response

    # 发生异常才会来到这里
    def process_exception(self, request, exception):
        print('failed {0}'.format(str(exception)))


