from django.db import models
from department.models import Hospital_department

# Create your models here.
class Diseases(models.Model):
    dis_name=models.CharField('疾病名称',max_length=40)
    dis_id=models.IntegerField('疾病编号')
    dept_id=models.IntegerField('科室编号')
    # 导入科室类做关联
    department=models.ManyToManyField(Hospital_department)

    def __str__(self):
        return "%s,%s,%s"%(self.dis_name,self.dept_id,self.dis_id)
