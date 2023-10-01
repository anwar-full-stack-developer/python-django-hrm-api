from django.urls import path, include
from .views import ContactListApiView, ContactDetailApiView
from .department_views import DepartmentApiView
from .employee_views import EmployeeListApiView, EmployeeDetailApiView

urlpatterns = [
    path('contact/api/', ContactListApiView.as_view()),
    path('contact/api/<int:contact_id>/', ContactDetailApiView.as_view()),
    path('department/api/', DepartmentApiView.as_view()),
    path('department/api/<int:id>/', DepartmentApiView.as_view()),
    path('employee/api/', EmployeeListApiView.as_view()),
    path('employee/api/<int:id>/', EmployeeDetailApiView.as_view()),
]