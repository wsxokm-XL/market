from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth
from ..register.models import User
from django import http

class LoginView(View):

    def get(self, request):
        """登录"""
        return render(request, 'login.html')

    def post(self,request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        login = auth.authenticate(username=username, password=password)

        if login is not None:
            auth.login(request, login)
            return redirect('/home/home')
        else:
            return render(request, 'login.html', {'register_errmsg': '用户名或密码错误'})
