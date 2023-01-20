from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"fleetmanagement/dashboard.html")

#driver 
def drivers_view(request):
    return render(request,"fleetmanagement/drivers_view.html")

def driver_add(request):
    return render(request,"fleetmanagement/driver_add.html")

def driver_edit(request):
    return render(request,"fleetmanagement/driver_edit.html")