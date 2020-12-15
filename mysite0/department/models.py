from django.db import models

# Create your models here.
class Doctor(models.Model):
    LIKE_CHOICES = (
        ('5','excellent'),
        ('4','great'),
        ('3','good'),
        ('2','normal'),
        ('1','bad'),
    )
    GENDER_CHOICES = (
        ('男', 'Male'),
        ('女', 'Female'),
    )
    doctorname = models.CharField("医生姓名", max_length=30)
    age = models.IntegerField('年龄')
    gender = models.CharField('性别',max_length=1,choices=GENDER_CHOICES)
    phone = models.CharField('手机号',max_length=11)
    email = models.EmailField('邮箱')
    password = models.CharField("密码",max_length=32)
    title = models.CharField('职称',max_length=30)
    d_space = models.CharField('医生介绍',max_length=500)
    surgery_weekday = models.CharField('出诊时间',max_length=100) #连接排版表
    limit_visits = models.CharField('就诊人数上限',max_length=20)
    dept = models.CharField('科室',max_length=20) #连接科室表
    likes = models.CharField('喜爱',max_length=1,choices=LIKE_CHOICES)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)
    active = models.BooleanField('是否活跃',default=1)


class Hospital_department(models.Model):
    dname = models.CharField('科室名称',max_length=20)
    # doctors = models.ManyToManyField(Doctor)

    def __str__(self):
        return self.dname