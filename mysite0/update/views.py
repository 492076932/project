import json

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from doctor.models import Doctor,Hospital_department


# Create your views here.
def update_doc(request):
    if request.method == 'POST':
        # 1.获取ajax请求提交的数据
        json_str = request.body
        # 2.将json串反序列化为对象
        json_obj = json.loads(json_str)
        print(json_obj)
        # 3. 获取数据
        id = json_obj['id']
        # 尝试从数据库获取对象
        try:
            doctor = Doctor.objects.get(id=id)
        except Exception as e:
            return JsonResponse({'code': 405, 'error': 'id有误'})
        # 保存获取到的数据
        try:
            doctorname = json_obj['doctorname']
            age = json_obj['age']
            dname = json_obj['dname']
            gender = json_obj['gender']
            d_space = json_obj['d_space']
            title = json_obj['title']
            phone = json_obj['phone']
            limit_visits = json_obj['limit_visits']
        except Exception as e:
            return JsonResponse({'code': 404, 'error': '数据有误'})
        # 数据写入到数据库
        doctor.doctorname = doctorname
        doctor.age = age
        doctor.dept.dname = dname
        doctor.gender = gender
        doctor.d_space = d_space
        doctor.title = title
        doctor.phone = phone
        doctor.limit_visits = limit_visits

        doctor.save()
        # 重定向到医生列表
        return JsonResponse({'code': 200})


def all_doc(request):
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        doctors_res = []
        result = {'code': 200, 'data': {}}
        for doc in doctors:
            d = {}
            d['id'] = doc.id
            d['name'] = doc.doctorname
            d['age'] = doc.age
            d['gender'] = doc.gender
            d['dname'] = doc.dept.dname
            d['title'] = doc.d_space
            d['phone'] = doc.phone
            d['d_space'] = doc.d_space
            d['limit_visits'] = doc.limit_visits
            doctors_res.append(d)
        result['data'] = doctors_res
        return JsonResponse(result)


def delete_doc(request):
    did = request.GET.get('did')
    try:
        doctor = Doctor.objects.get(id=did)
        doctor.delete()
    except Exception as e:
        print('did is error')
        return HttpResponse('删除失败')
    return HttpResponseRedirect('/update/all_doc')


def schedule(request):
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        print(doctors)
        doctors_res = []
        result = {'code': 200, 'data': {}}
        for doc in doctors:
            d = {}
            d['id'] = doc.id
            d['name'] = doc.doctorname
            d['dname'] = doc.dept.dname
            d['workday'] = doc.workday
            doctors_res.append(d)
        result['data'] = doctors_res
        print(result)

        return JsonResponse(result)
    if request.method == 'POST':
        json_str = request.body
        # 2.将json串反序列化为对象
        json_obj = json.loads(json_str)
        print(json_obj)
        # 3. 获取数据
        d_id = json_obj['id']
        time = json_obj['time']
        # 尝试从数据库获取对象
        try:
            doctor = Doctor.objects.get(id=d_id)
        except Exception as e:
            return JsonResponse({'code': 405, 'error': 'id有误'})
        doctor.workday = time
        doctor.save()
        return JsonResponse({'code': 200})


def add_doc(request):
    if request.method == 'POST':
        # 1.获取ajax请求提交的数据
        json_str = request.body
        # 2.将json串反序列化为对象
        json_obj = json.loads(json_str)
        print(json_obj)
        # 3. 获取数据
        try:
            doctorname = json_obj['doctorname']
            age = json_obj['age']
            dname = json_obj['dname']
            gender = json_obj['gender']
            # email = json_obj['email']
            d_space = json_obj['d_space']
            title = json_obj['title']
            phone = json_obj['phone']
            limit_visits = json_obj['limit_visits']
        except Exception as e:
            return JsonResponse({'code': 404, 'error': '数据有误'})
        # 数据写入到数据库
        d_id = Hospital_department.objects.get(dname=dname).id
        Doctor.objects.create(
            doctorname = doctorname,age = age,gender = gender,d_space = d_space,
            title = title,phone = phone,limit_visits = limit_visits,dept_id=d_id
        )

        # 重定向到医生列表
        return JsonResponse({'code': 200})