# middleware.py

from with_you_system.settings import AUTHENTICATION_EXCLUDED_PATHS
from django.shortcuts import redirect
from django.urls import reverse

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        response = self.get_response(request)
        # 检查请求的路径是否在排除列表中
        excluded_paths = AUTHENTICATION_EXCLUDED_PATHS
        if request.path not in excluded_paths and not request.user.is_authenticated and not request.path.startswith('/admin/') :
            # 如果未认证且路径不在排除列表中，则重定向到登录页面
            return redirect("/account/login/")
        return response