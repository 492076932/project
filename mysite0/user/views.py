import hashlib
import json
import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core.cache import cache
from django.utils.decorators import method_decorator
# Create your views here.
from user.models import User
from tools.sms import YunTongXin
from django.conf import settings
from django.views import View
from tools.check_login import login_check


class UserView(View):

    # 个人界面显示
    def get(self, request, username=None):
        if username:
            # 获取指定用户信息
            try:
                user = User.objects.get(username=username)
            except Exception as e:
                print('get user error %s' % e)
                result = {'code': 10104, 'error': 'username is wrong!'}
                return JsonResponse(result)

            result = {'code': 200, 'username': username,
                      'data': {'phone': user.phone,
                               'nickname': user.nickname,
                               'age': user.age,
                               'gender': user.gender,
                               }
                      }

            return JsonResponse(result)

    # 注册
    def post(self, request):
        json_str = request.body
        json_obj = json.loads(json_str)
        print(json_obj)
        username = json_obj['username']
        phone = json_obj['phone']
        sms_num = json_obj['sms_num']
        password = json_obj['password']

        # 为空检查
        if not username or not phone or not password or not password:
            return JsonResponse({'code': 10100, 'error': '姓名电话不允许为空'})
        cache_key = 'sms_%s' % phone
        # if not sms_num:
        #     return JsonResponse({'code': 10200, 'error': '验证码为空'})
        # old_code = cache.get(cache_key)
        # if not old_code:
        #     return JsonResponse({'code': 10201, 'error': '验证码错误'})
        # if type(int(sms_num)) != int:
        #     return JsonResponse({'code': 10202, 'error': '验证码错误'})
        # if int(sms_num) != old_code:
        #     return JsonResponse({'code': 10203, 'error': '验证码错误'})
        # # 3,用户名是否已存在
        old_user = User.objects.filter(username=username)
        print(old_user)
        if old_user:
            return JsonResponse({'code': 10203, 'error': '用户已存在'})
        # 4,是否会直接保存输入的’密码‘呢？
        md5 = hashlib.md5()
        md5.update(password.encode())
        # 口令的Hash值
        password_h = md5.hexdigest()
        # 5.数据库中添加数据
        try:
            User.objects.create(username=username, nickname=username,
                                phone=phone, password=password_h)
        except Exception as e:
            print(e)
            return JsonResponse({'code': 10101, 'error': '用户名已占用'})
        return JsonResponse({'code': 200})

        # 个人信息修改

    @method_decorator(login_check)
    def put(self, request, username):
        # 获取数据
        json_str = request.body
        json_obj = json.loads(json_str)
        # 修改对象
        request.myself.nickname = json_obj['nickname']
        request.myself.age = json_obj['age']
        request.myself.gender = json_obj['gender']

        # 保存至数据库
        request.myself.save()
        result = {'code': 200,
                  'username': request.myself.username}
        return JsonResponse(result)


# 获取注册页面
def reg_view(request):
    if request.method == "GET":
        return render(request, 'user/register.html')


# 获取登录页面


def login_view(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')


# 发送短信


def sms_view(request):
    json_str = request.body
    json_obj = json.loads(json_str)
    phone = json_obj['phone']
    # regex = "^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\\d{8}$"
    # if phone not in regex:
    #     result = {'code': 10111, 'error': '请输入正确的手机号'}
    #     return JsonResponse(result)
    if not phone:
        result = {'code': 10111, 'error': '手机号不能为空'}
        return JsonResponse(result)
    cache_key = 'sms_%s' % phone
    old_code = cache.get(cache_key)
    if old_code:
        result = {'code': 10112, 'error': '请稍后再发送'}
        return JsonResponse(result)
    code = random.randint(1000, 9999)
    print('-----code is %s-------------' % code)
    cache.set(cache_key, code, 65)
    # x = YunTongXin(settings.SMS_ACCOUNT_ID,
    #                settings.SMS_ACCOUNT_TOKEN,
    #                settings.SMS_APP_ID,
    #                settings.SMS_TEMPLATE_ID)
    # res = x.run(phone, code)
    # print('-send sms result is %s-' % res)
    return JsonResponse({'code': 200})


def logout_view(request):
    if 'uname' in request.session:
        del request.session['uname']
    if 'uid' in request.session:
        del request.session['uid']
    resp = HttpResponse('注销用户成功')
    resp.delete_cookie('uname')
    resp.delete_cookie('uid')
    return resp
