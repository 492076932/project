from django.db import models

# Create your models here.
class Ord_list(models.Model):
    uname=models.CharField('患者姓名',max_length=20,null=False)
    dname=models.CharField('医生姓名或者id',max_length=50)
    curedate=models.CharField(null=False,max_length=50)
    cost=models.DecimalField(max_digits=3,decimal_places=1,default=25.0)


    class Meta():
        db_table = 'ord_list'
    #insert into ord_list values (1,'亚索','关爱孤儿科','提莫','0100110',25)