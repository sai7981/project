from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.empdetails , name='empdetails'),
    path('result1', views.Employee_1, name='sweet_emp'),
    path('output', views.fetchData),
]