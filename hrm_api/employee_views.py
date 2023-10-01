from django.shortcuts import render  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .models import Contact, Department, Employee
from .serializers import EmployeeSerializer
from django.shortcuts import get_object_or_404  
  
class EmployeeListApiView(APIView):  
    
    def get(self, request, id=None):  
        if id:  
            result = Employee.objects.get(id=id)  
            serializers = EmployeeSerializer(result)  
            return Response({'success': 'success', "data":serializers.data}, status=200)  
  
        result = Employee.objects.all()  
        serializers = EmployeeSerializer(result, many=True)  
        return Response({'status': 'success', "data":serializers.data}, status=200)  
  
    def post(self, request):  
        serializer = EmployeeSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  
  
  
class EmployeeDetailApiView(APIView):  
    def get(self, request, id=None):  
        if id:  
            result = Employee.objects.get(id=id)  
            serializers = EmployeeSerializer(result)  
            return Response({'success': 'success', "data":serializers.data}, status=200)  
  
    def put(self, request, id):  
        result = Employee.objects.get(id=id)  
        serializer = EmployeeSerializer(result, data = request.data, partial=True)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data})  
        else:  
            return Response({"status": "error", "data": serializer.errors})  
  
    def delete(self, request, id=None):  
        result = get_object_or_404(Employee, id=id)  
        result.delete()  
        return Response({"status": "success", "data": "Record Deleted"})  