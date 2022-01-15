from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout
from ..register.models import User


class HomeView(View):

    def get(self, request):
        """访问用户主页"""
        if not request.user.is_authenticated:
            return redirect('/login/login')
        else:
            username = request.user.username
            money = request.user.money
            #print(dir(request.user))
            #print(request.user.id)
            dict = {"username": username, "money": money}
            return render(request, 'home.html', dict)

    def post(self, request):
        """退出登录"""
        logout(request)
        return redirect('/home/home')




