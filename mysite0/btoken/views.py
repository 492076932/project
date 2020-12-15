import hashlib
import json
import time
import jwt
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings

# Create your views here.
from django.views import View

from user.models import User


class TokensView(View):
    def post(self, request):
        json_str = request.body
        json_obj = json.loads(json_str)
        phone = json_obj['phone']
        password = json_obj['password']
        print(type(phone))
        print(phone)
        if not phone or not password:
            return JsonResponse({'code': 10010, 'error': '手机号密码不允许为空'})
        try:
            old_user = User.objects.get(phone=phone)
        except Exception as e:
            print('the error is %s' % e)
            return JsonResponse({'code': 10011, 'error': '手机号密码错误'})
        md5 = hashlib.md5()
        md5.update(password.encode())
        # 口令的Hash值
        # password_h = md5.hexdigest()
        print(md5.hexdigest())
        print(old_user.password)
        if md5.hexdigest() != old_user.password or phone != old_user.phone:
            return JsonResponse({'code': 10012, 'error': '手机号密码错误'})
        phone = json_obj['phone']
        if phone == '15323766372':
            return JsonResponse({'code': 2001, 'username': old_user.username,
                                 })
        else:
            # 生成token并返回
            token = make_token(old_user.phone, settings.JWT_TOKEN_KEY, 5000)
            return JsonResponse({'code': 200, 'username': old_user.username,
                                 'data': {'token': token.decode()}})


# 生成token
def make_token(phone, key, expire):
    print(expire)
    now = time.time()
    print(now)
    payload = {'phone': phone, 'exp': now + expire}
    print(payload)
    return jwt.encode(payload, key)
