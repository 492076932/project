# Generated by Django 2.2.12 on 2020-11-16 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diseases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dis_name', models.CharField(max_length=40, verbose_name='疾病名称')),
                ('dis_id', models.IntegerField(verbose_name='疾病编号')),
                ('dept_id', models.IntegerField(verbose_name='科室编号')),
                ('department', models.ManyToManyField(to='department.Hospital_department')),
            ],
        ),
    ]
