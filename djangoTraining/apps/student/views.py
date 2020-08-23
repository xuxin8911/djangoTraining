from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views import View

from .models import Student
from .forms import StudentForm
# Create your views here.

"""
# 采用函数方式实现 function view

def index(request):
    # 查询单个值
    # words = 'Word!'
    # return render(request, 'index.html', context={'words': words})

    # 根据表做查询
    # students = Student.objects.all()
    # return render(request, 'index.html', context={'students': students})

    # students = Student.objects.all()
    students = Student.get_all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():

            # 手动构建Student对象的方法来保存student数据
            # cleaned_data = form.cleaned_data    # cleaned_data:form根据字段类型对用户提交的数据做完转换后的结果
            # student = Student()
            # student.name = cleaned_data['name']
            # student.sex = cleaned_data['sex']
            # student.email = cleaned_data['email']
            # student.profession = cleaned_data['profession']
            # student.qq = cleaned_data['qq']
            # student.phone = cleaned_data['phone']
            # student.save()

            # 因为有了Model的定义，手动构建Student的步骤可以省略，代码如下
            form.save()

            # 在urls.py中定义了index时，声明了name='index'，所以这里可以通过reverse来拿到对应的url，这样做的好处是，
            # 不需要硬编码url到代码中，这意味着如果以后有修改url的需求，只要index的名称不变，这个地方代码就不用修改
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()

    context = {
        'students': students,
        'form': form
    }
    return render(request, 'index.html', context=context)

"""


# 采用类方式实现
class IndexView(View):
    template_name = 'index.html'

    @staticmethod
    def get_context():
        students = Student.get_all()
        context = dict(students=students)
        return context

    def get(self, request):
        context = self.get_context()
        form = StudentForm()
        context.update(dict(form=form))
        return render(request, template_name=self.template_name, context=context)

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        else:  # 参数校验不通过，走以下分支
            context = self.get_context()
            context.update(dict(form=form))
            return render(request, template_name=self.template_name, context=context)