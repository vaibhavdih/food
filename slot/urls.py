
from django.urls import path
from . import views

urlpatterns = [

    path('',views.show_index,name="show_index"),
    path('reg/register/',views.register_booking,name="register_booking"),
    path('reg/',views.start_register,name="start_register"),

]
