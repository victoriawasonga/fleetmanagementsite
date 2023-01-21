from django.shortcuts import render
from django.views import View
from .forms import DriverForm
from .models import Driver
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
import json
from django.http import JsonResponse

def index(request):
    return render(request,"fleetmanagement/dashboard.html")

class LicenseValidationView(View):
    def post(self,request):
        data=json.loads(request.body)
        license_no=data['license_no'] 
        if not str(license_no).isalnum():
            return JsonResponse({
                "license_no_error": "License Number is invalid  it should only contain alpanumeric characters ",
            })


def licence_validation(request):
    if request.method=="POST":
        data=json.loads(request.body)
        license_no=data['license_no'] 
        if not str(license_no).isalnum():
            return JsonResponse({
                "license_no_error": "License Number is invalid  it should only contain alpanumeric characters "},status=400)
        if Driver.objects.filter(license_no=license_no).exists():
            return JsonResponse({
                "license_no_error": "License Number is already in our database "},status=409)
        
        return JsonResponse({
            "license_valid":True
        })
        
######################################################## Driver ####################################################################################
def drivers_view(request):
    drivers=Driver.objects.all()
    drivers_count=drivers.count()
    drivers_active_count=drivers.filter(status="Active").count()
    drivers_inactive_count=drivers.filter(status="Inactive").count()

    context={
        'drivers':drivers,
        'drivers_count':drivers_count,
        'drivers_active_count':drivers_active_count,
        'drivers_inactive_count':drivers_inactive_count
    }
    return render(request,"fleetmanagement/driver/drivers_view.html",context)

def driver_add(request):
    form=DriverForm()
    context={
        "form":form
    }
    if request.method=="POST":
        First_name=request.POST.get('First_name')
        Last_name=request.POST.get('Last_name')
        Other_names=request.POST.get('Other_names')
        national_ID=request.POST.get('national_ID')
        address=request.POST.get('address')
        Email=request.POST.get('Email')
        Phone_number=request.POST.get('Phone_number')
        license_no=request.POST.get('license_no')
        license_expiry_date=request.POST.get('license_expiry_date')
        status=request.POST.get('status')

        driver=Driver()
        driver.First_name=First_name
        driver.Last_name=Last_name
        driver.Other_names=Other_names
        driver.national_ID=national_ID
        driver.address=address
        driver.Email=Email
        driver.Phone_number=Phone_number
        driver.license_no=license_no
        driver.license_expiry_date=license_expiry_date
        driver.status=status
        driver.save()
        messages.add_message(request,messages.SUCCESS,"Driver Added Successfully")
        return HttpResponseRedirect(reverse("drivers_view"))
    return render(request,"fleetmanagement/driver/driver_add.html",context)

def driver_detail(request,id):
    driver=get_object_or_404(Driver,pk=id)
    context={
        'driver':driver
    }
    return render(request,"fleetmanagement/driver/driver_view.html",context)

def driver_delete(request,id):
    driver=get_object_or_404(Driver,pk=id)
    context={
        'driver':driver
    }
    if request.method=='POST':
        driver.delete()
        messages.add_message(request,messages.SUCCESS,"Driver deleted Successfully")
        return HttpResponseRedirect(reverse('drivers_view'))
    return render(request,"fleetmanagement/driver/driver_delete.html",context)

def driver_edit(request,id):
    driver=get_object_or_404(Driver,pk=id)
    form=DriverForm(instance=driver)
    context={
        'driver':driver,
        'form':form,
    }
    if request.method=='POST':
        First_name=request.POST.get('First_name')
        Last_name=request.POST.get('Last_name')
        Other_names=request.POST.get('Other_names')
        national_ID=request.POST.get('national_ID')
        address=request.POST.get('address')
        Email=request.POST.get('Email')
        Phone_number=request.POST.get('Phone_number')
        license_no=request.POST.get('license_no')
        license_expiry_date=request.POST.get('license_expiry_date')
        status=request.POST.get('status')

        driver.First_name=First_name
        driver.Last_name=Last_name
        driver.Other_names=Other_names
        driver.national_ID=national_ID
        driver.address=address
        driver.Email=Email
        driver.Phone_number=Phone_number
        driver.license_no=license_no
        driver.license_expiry_date=license_expiry_date
        driver.status=status
        driver.save()
        messages.add_message(request,messages.SUCCESS,"Driver Edited Successfully")
        return HttpResponseRedirect(reverse("driver_detail",kwargs={'id':driver.pk}))
    return render(request,"fleetmanagement/driver/driver_edit.html",context)
########################################################End Driver ####################################################################################