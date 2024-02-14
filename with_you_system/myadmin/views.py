from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def myadmin(request):

    return HttpResponse("myadmin")


def myadmin_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "myadmin.html", {"user": username})
        else:
            return HttpResponse("Invalid login.")
    else:
        # 显示登录表单
        return render(request, "myadmin_login.html")    
