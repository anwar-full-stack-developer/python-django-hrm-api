from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Contact, Department, Employee
from .serializers import ContactSerializer

class ContactListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Contact items for given requested user
        '''
        contacts = Contact.objects.filter()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Contact with given contact data
        '''
        data = {
            'phone': request.data.get('phone'), 
            'address': request.data.get('address')
        }
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ContactDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, contact_id):
        '''
        Helper method to get the object with given contact_id
        '''
        try:
            return Contact.objects.get(id=contact_id)
        except Contact.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, contact_id, *args, **kwargs):
        '''
        Retrieves the Contact with given contact_id
        '''
        contact_instance = self.get_object(contact_id)
        if not contact_instance:
            return Response(
                {"res": "Object with contact id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ContactSerializer(contact_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, contact_id, *args, **kwargs):
        '''
        Updates the contact item with given contact_id if exists
        '''
        contact_instance = self.get_object(contact_id)
        if not contact_instance:
            return Response(
                {"res": "Object with contact id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        data = {
            'phone': request.data.get('phone'), 
            'address': request.data.get('address')
        }
        serializer = ContactSerializer(instance = contact_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, contact_id, *args, **kwargs):
        '''
        Deletes the contact item with given contact_id if exists
        '''
        contact_instance = self.get_object(contact_id)
        if not contact_instance:
            return Response(
                {"res": "Object with contact id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        contact_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )