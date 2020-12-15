from django.db import models

class User(models.Model):
    # 患者个人信息数据表
    phone = models.CharField('手机号', max_length=11, unique=True)
    username = models.CharField('姓名', max_length=20)
    nickname = models.CharField('昵称', max_length=10, default=username)
    password = models.CharField('密码', max_length=32)
    gender = models.CharField('性别', max_length=2, default="")
    age = models.SmallIntegerField('年龄', default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    id_number = models.CharField('身份证号', max_length=18, unique=True, null=True)
