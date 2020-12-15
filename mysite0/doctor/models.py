from django.db import models


# Create your models here.

class Hospital_department(models.Model):
    dname = models.CharField('科室名称', max_length=20)
    #insert into doctor_hospital_department values('冲击部')

class Doctor(models.Model):
    doctorname = models.CharField("医生姓名", max_length=20)
    age = models.IntegerField('年龄')
    gender = models.CharField('性别', max_length=1)
    phone = models.CharField('手机号', max_length=11)

    password = models.CharField("密码", max_length=32)
    title = models.CharField('职称', max_length=20)

    d_space = models.CharField('医生介绍', max_length=500)
    # surgery_weekday = models.CharField('出诊时间',max_length=100)
    limit_visits = models.CharField('就诊人数上限', max_length=100)
    # created_time = models.DateTimeField('创建时间', auto_now_add=True)
    # updated_time = models.DateTimeField('更新时间', auto_now=True)
    # active = models.BooleanField('是否活跃', default=1)
    workday = models.CharField('排班安排', max_length=100)
    dept = models.ForeignKey(Hospital_department, on_delete=models.CASCADE, default=1)

    #insert into doctor_doctor values (1,'亚索',28,'男','17717771864','1234','无','无','00000000000000','0101010',1);