# 登录认证的装饰器
from django.http import JsonResponse
import jwt
from django.conf import settings
from user.models import User


def login_check(func):
    def wrap(request, *args, **kwargs):
        # 获取token,验证是否已经登录
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            result = {'code': 10403, 'error': 'Please login !!!'}
            return JsonResponse(result)
        # 存在token时进行校验
        try:
            res = jwt.decode(token,
                             settings.JWT_TOKEN_KEY,  # 在settings.py设置值
                             algorithm='HS256')
        except Exception as e:
            print('check login error %s' % e)
            result = {'code': 10403, 'error': 'Please login !!!'}
            return JsonResponse(result)
        print(res)
        phone = res['phone']
        request.myself = User.objects.get(phone=phone)

        return func(request, *args, **kwargs)

    return wrap


def get_user_by_request(request):
    token = request.META.get('HTTP_AUTHORIZATION')
    if not token:
        return None
    try:
        payload = jwt.decode(token, settings.JWT_TOKEN_KEY)
    except Exception as e:
        print('get user is error %s' % e)
        return None
    username = payload['username']
    return username
