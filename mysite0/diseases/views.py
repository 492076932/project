from django.http import JsonResponse
from django.shortcuts import render
from department.models import Hospital_department
from diseases.models import Diseases

# Create your views here.

def diseases_index(request):
    if request.method=="GET":
        dept = Hospital_department.objects.values('id', 'dname')
        dept_list = list(dept)
        for dept in dept_list:
            dis = Diseases.objects.filter(dept_id=dept['id']).values_list('dis_name')
            dis_list = list(dis)
            dept['dis_name'] = dis_list

        return JsonResponse(dept_list, safe=False)
        # return render(request,'diseases_index.html')


# def all_diseases(request):
#     # if request.method=="GET":
#     dept = Hospital_department.objects.values('id', 'dname')
#     dept_list = list(dept)
#     for dept in dept_list:
#         dis = Diseases.objects.filter(dept_id=dept['id']).values_list('dis_name')
#         dis_list = list(dis)
#         dept['dis_name']=dis_list
#
#     return JsonResponse(dept_list,safe=False)