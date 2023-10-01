from rest_framework import serializers
from django.db import models
from .models import Contact, Department, Employee

class ContactSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length=50)

    class Meta:
        model = Contact
        fields = ["id", "phone", "address"]

class DepartmentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()

    class Meta:
        model = Department
        fields = ["id", "name", "description"]

class EmployeeSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField()
    
    contact = models.OneToOneField(
            Contact,
            on_delete=models.CASCADE,
            null=True
        )

    department = models.ForeignKey(
            Department,
            on_delete=models.CASCADE,
            default=None
        )
    
    class Meta:
        model = Employee
        fields = ["id", "first_name", "last_name", "contact", "department"]

