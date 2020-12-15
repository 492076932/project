from django.shortcuts import render
from django.views import  View
from .models import Doctor,Hospital_department
from django.http import HttpResponse, HttpResponseRedirect
from time import sleep
# Create your views here.

def list_view(request,id):
    dept = Hospital_department.objects.get(id=id)

    doctors = Doctor.objects.filter(dept=id)
    if request.method == 'GET':
        return render(request,'doctor/demo01.html',locals())
    elif request.method == 'POST':
        KeyWord = request.POST['KeyWord']
        if not KeyWord:
            return HttpResponse('no KeyWord ')
        if KeyWord:
            # return HttpResponse(KeyWord)
            try:
                doctor = Doctor.objects.get(doctorname=KeyWord)
            except Exception as e:
                return HttpResponse('no doctors %s'% e)

            return HttpResponseRedirect('/doctorsInfo/%s/'% doctor.doctorname)


        # return render(request, 'doctor/demo2.html', locals())



def doctor_view(request,docname):
    doctor = Doctor.objects.get(doctorname=docname)
    dept = Hospital_department.objects.get(id=doctor.dept_id)

    if request.method == 'GET':
        return render(request, 'doctor/demo2.html', locals())
    elif request.method == 'POST':
        return render(request, 'doctor/demo2.html', locals())

















