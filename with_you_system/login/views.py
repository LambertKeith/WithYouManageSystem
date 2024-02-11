from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from login.models import Teacher
from django.contrib.auth.hashers import make_password



def user_login(request):
    """用户登录
    """    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "index.html")
        else:
            return HttpResponse("Invalid login.")
    else:
        # 显示登录表单
        return render(request, "login.html")


def user_logout(request):
    """用户退出登录
    """    
    logout(request)
    # 重定向到登录表单
    return HttpResponseRedirect('/account/login/')