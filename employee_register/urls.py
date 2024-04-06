from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.fronpage, name='frontpage'),
    path('<int:id>/', views.employeeform, name='employee_update'),
    path('list/', views.employeeList, name='employee_list'),
    path('delete/<int:id>/', views.delete, name='employee_delete'),
    path('form/', views.employeeform, name='employee_form'),
]