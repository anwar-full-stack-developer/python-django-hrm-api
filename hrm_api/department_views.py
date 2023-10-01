from django.shortcuts import render  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .models import Contact, Department, Employee
from .serializers import DepartmentSerializer
from django.shortcuts import get_object_or_404  
  
class DepartmentApiView(APIView):  
  
    def get(self, request, id=None):  
        if id:  
            result = Department.objects.get(id=id)  
            serializers = DepartmentSerializer(result)  
            return Response({'success': 'success', "data":serializers.data}, status=200)  
  
        result = Department.objects.all()  
        serializers = DepartmentSerializer(result, many=True)  
        return Response({'status': 'success', "data":serializers.data}, status=200)  
  
    def post(self, request):  
        serializer = DepartmentSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  
  
    def put(self, request, id):  
        result = Department.objects.get(id=id)  
        serializer = DepartmentSerializer(result, data = request.data, partial=True)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data})  
        else:  
            return Response({"status": "error", "data": serializer.errors})  
  
    def delete(self, request, id=None):  
        result = get_object_or_404(Department, id=id)  
        result.delete()  
        return Response({"status": "success", "data": "Record Deleted"})  