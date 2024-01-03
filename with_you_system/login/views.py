from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login
# Create your views here.
from login.models import Teacher
from django.contrib.auth.hashers import make_password


def create_user():
    '''
    新建示例用户
    '''
    # 创建一个新用户
    new_teacher = Teacher.objects.create_user(
        username='example_user',
        password='your_password',
        email='example@email.com',
        teacher_id='1234567890',
        classroom='101',
        is_admin=False
    )


def check_user(request):
    '''
    检测示例用户密码
    '''
    user = authenticate(username='example_user', password='your_password')
    if user is not None:
        login(request, user)
        # 用户认证成功，继续后续流程
        return HttpResponse("success")
    else:
        return HttpResponse("fail")
        # 认证失败