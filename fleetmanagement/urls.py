from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="home"),
    path("/drivers",views.drivers_view,name="drivers"),
    path("/driver/<id>/",views.driver_detail,name="driver_detail"),
    path("/driver_delete/<id>/",views.driver_delete,name="driver_delete"),
    path("/driver_add/",views.driver_add,name="driver_add"),
    path("/driver_edit/<id>/",views.driver_edit,name="driver_edit"),
]