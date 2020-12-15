import datetime
import json
from django.views import View
from .models import Ord_list
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from doctor.models import Doctor
import re

# Create your views here.
# def home_view(request):
#     #
#     #提取医生id,患者id
#     did=Ord_list.objects.get(d_id=1)
#     #循环创建 变量day_i=当前日期   变量week_i=当前周几
#     for i in range(0, 7):
#         now = datetime.datetime.now()
#         delta = datetime.timedelta(days=i)
#         n_days = now + delta
#         dayOfWeek = n_days.isoweekday()
#         weekStr = "一二三四五六日"
#         week='星期'+weekStr[dayOfWeek-1]
#         locals()['day_' + str(i)] = n_days.strftime('%m-%d')
#         locals()['week_'+str(i)]= week
#     return render(request,'yuyue.html',locals())

class home_view(View):
    def get(self,requests):
        # json_str=request.body
        # json_obj=json.loads(json_str)
        # did=json_obj['did']
        #获取医生对象
        try:
            d = Doctor.objects.get(id=2)
        except Exception as e:
            result={'code':10400,'error':'获取医生信息失败%s'%e}
            return JsonResponse(result)
        #创建返回字典
        res = {}
        #获取医生排班信息
        day=d.workday
        #遍历day字符串,如果为1表示当天工作,0表示当天不工作(工作排表只会显示从当前时间起七天的工作状态)
        for index,j in  enumerate(day):
            if j=='1':
                res['wday_' + str(index)] = index
        #获取列表日期信息
        for i in range(0, 7):
            now = datetime.datetime.now()
            delta = datetime.timedelta(days=i)
            n_days = now + delta
            dayOfWeek = n_days.isoweekday()
            weekStr = "一二三四五六日"
            week='星期'+weekStr[dayOfWeek-1]
            #循环创建变量,并加入字典
            res['day_' + str(i)]= n_days.strftime('%m-%d')
            res['week_'+str(i) ] = week

        result={'code':200,'data':res}
        return JsonResponse(result)


def yuyue(request):
    ainfo=request.get_full_path()
    #good/yuyue/yuyue?d=3&u=TEDU2&day=2
    info=ainfo.split("?")[1]#info='d=3&u=TEDU2&day=2'
    pattern = 'd=(.*?)&u=(.*?)&day=(.*)'
    #拿到匹配的列表
    all=re.findall(pattern, info)[0]
    #拿到预约医生ID
    did= all[0]
    #拿到预约患者name
    uname = all[1]
    #拿到预约时间
    day= int(all[2])
    now = datetime.datetime.now()
    delta = datetime.timedelta(day-1)
    #得到预约时间并格式化为2020-11-19
    days=(now+delta).strftime("%Y-%m-%d")
    cost=25
    #提取医生医生对象
    docter = Doctor.objects.get(id=did)
    #提取对象中的预约数量
    #docter['预约人数']='00010000000000'
    b=docter.limit_visits
    #将字符串利用正则改为列表,提取当前天数的人数
    rlist=re.findall('\d{2}',b)
    a=int(rlist[day-1])
    if  a< 20:
        # 预约未满,可以增加一条新纪录
        # Ord_list.objects.create(患者ID,医生id,就诊时间,花费)
        try:
            user=Ord_list.objects.get(uname=uname,dname=did,curedate=days)
            result = {'code': 10400, 'error': '您已经预约当天治疗'}
            return JsonResponse(result)
        except Exception as e:
            pass
        Ord_list.objects.create(uname=uname,dname=did,curedate=days,cost=cost)
        #更改医生当天预约的人数
        a+=1
        #判断a是否为2位数,不为两位数,需添加字符0 在前保证字段长度
        if a<10:
            rlist[day-1]='0'+str(a)
        else:
            rlist[day-1]=str(a)
        num=''.join(rlist)
        docter.limit_visits =num
        docter.save()
        result = {'code': 10500, 'error': '预约成功'}
        return JsonResponse(result)
    else:
        result = {'code': 10400, 'error': '预约已满'}
        return JsonResponse(result)
