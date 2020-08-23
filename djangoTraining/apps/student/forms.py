# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    # 写法1：自己定义form字段
    # name = forms.CharField(label='姓名', max_length=128)
    # sex = forms.ChoiceField(label='性别', choices=Student.SEX_ITEMS)
    # profession = forms.CharField(label='职业', max_length=128)
    # email = forms.EmailField(label='邮箱', max_length=128)
    # qq = forms.CharField(label='QQ', max_length=128)
    # phone = forms.CharField(label='手机', max_length=128)

    # 写法2：复用Model的代码
    # 如果有修改字段类型需求，比如把qq改成IntegerField来做数字校验，也可以声明出来，如下通过clean_方法来实现
    # clean_是Form会自动调用来处理每个字段的方法
    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字')
        return int(cleaned_data)

    class Meta:
        model = Student
        fields = (
            'name', 'sex', 'profession', 'email', 'qq', 'phone', 'status'
        )