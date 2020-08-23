# -*- coding:utf-8 -*-
from django.test import TestCase, Client

from .models import Student

# Create your tests here.


class StudentTestCase(TestCase):
    # setUp：用来初始化环境
    # test_**：方法后面的**可以是任意东西，以test_开头的方法，会被认为是需要测试的方法，跑测试时会被执行，每个需要测试的方法是相互独立的
    # tearDown: 跟setUp相对，用来清理测试环境和测试数据，在django中我们可以不关心这个
    def setUp(self):
        Student.objects.create(
            name='张三test',
            sex=1,
            email='zhangsan@126.com',
            profession='程序猿',
            qq='12341234',
            phone='1234'
        )

    # model层测试
    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='张三test2',
            sex=1,
            email='zhangsan@126.com',
            profession='IT',
            qq='123',
            phone='1234'
        )
        # self.assertEqual(student.sex_show, '男', '性别和展示内容不一致!')
        # 对于配置了choices参数的字段，django提供了get_**_display的方法，增加的sex_show其实可以用get_sex_display来替换
        self.assertEqual(student.get_sex_display(), '男', '性别和展示内容不一致!')

    def test_filter(self):
        student = Student.objects.create(
            name='张三test3',
            sex=1,
            email='zhangsan@126.com',
            profession='IT',
            qq='123',
            phone='1234234'
        )
        name = '张三test3'
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(), 1, '应该只存在一个名称为{0}的记录'.format(name))

    # View层测试
    def test_get_index(self):
        # 测试首页的可用性
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200, 'status code must be 200')

    def test_post_student(self):
        client = Client()
        data = dict(
            name='张三test4',
            sex=1,
            email='zhangsan@126.com',
            profession='IT',
            qq='2222',
            phone='3333'
        )
        response = client.post('/', data)
        self.assertEqual(response.status_code, 200, 'status code must be 302')
        response = client.get('/')
        print(response.content)
        # self.assertTrue(b'test_for_post' in response.content, 'response content must contain "test_for_post"')
        print(Student.objects.all())

