from django.shortcuts import render, redirect
from django.views import View
from .check import RegisterCheck
from .models import User
from django import http


class RegisterView(View):

    def get(self, request):
        """注册"""
        return render(request, 'register.html')

    def post(self, request):
        register_form = RegisterCheck(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            User.objects.create_user(username=username, password=password)
        except Exception as e:
            return render(request, 'register.html', {'register_errmsg': '用户名重复'})

        return redirect('/login/login')
        # return http.HttpResponse('注册成功')

        # 校验
        #register_form = RegisterCheck(request.POST)

        # if register_form.is_valid():
        #     username = register_form.clean().get('username')
        #     password = register_form.clean().get('password')
        #
        #     # 保存用户名和密码到数据库中
        #     try:
        #         User.objects.create(username=username, password=password)
        #     except Exception as e:
        #         return render(request, 'register.html', {'register_errmsg': '注册失败'})
        #
        #     return http.HttpResponse('注册成功')
        # else:
        #     print(register_form.errors.get_json_data())
        #     context = {
        #         'forms_error': register_form.errors
        #     }
        #     return render(request, 'register.html', context=context)
        #     ###


class RuleView(View):

    def get(self, request):
        """用户守则"""
        return render(request, '用户守则.html')
