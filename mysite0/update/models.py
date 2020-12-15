from django.db import models

# Create your models here.
# class Doctor(models.Model):
#     name = models.CharField('姓名', null=False, max_length=20)
#     age = models.IntegerField('年龄', default=1)
#     gender = models.CharField('性别', max_length=30)
#     dname = models.CharField('科室',max_length=30)
#     title = models.CharField('职称', max_length=20)
#     phone = models.CharField('手机号', max_length=11, )
#     likes = models.CharField('喜好',max_length=50)
#     email = models.EmailField('邮箱', null=True)
#     intro = models.CharField('简介',max_length=100)
#     limit_visits = models.CharField('就诊人数上限', max_length=10,default=20)
#
#
# class Schedule(models.Model):
#     workday = models.CharField('排班',max_length=100,default='每天都要')
#     doctor = models.OneToOneField(Doctor,on_delete=models.CASCADE)