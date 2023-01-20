from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="home"),
    path("/drivers",views.drivers_view,name="drivers"),
    path("/driver_add",views.driver_add,name="driver_add"),
    path("/driver_edit",views.driver_edit,name="driver_edit"),
]