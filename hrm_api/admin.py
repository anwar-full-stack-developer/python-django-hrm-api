from django.contrib import admin
from .models import Contact, Department, Employee
# Register your models here.
admin.site.register(Contact);
admin.site.register(Department);
admin.site.register(Employee);