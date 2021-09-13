from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.parsers import JSONParser
import io
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def employeedetail(request):
    if request.method == 'GET':
        json_data = request.body
        bobj = io.BytesIO(json_data)
        data = JSONParser().parse(bobj)
        id = data.get('id')
        if id is not None:
            emp = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(emp)
            return Response(serializer.data)
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    elif request.method == 'POST':
        json_data = request.body
        bobj = io.BytesIO(json_data)
        data = JSONParser().parse(bobj)
        if data:
            serializer = EmployeeSerializer(data=data)
            if serializer.is_valid():    
                serializer.save()
                return Response({'msg':'resource created'})
            return Response({'msg':'plzz send correct data'})
        return Response({'msg':'plzz send data'})

    elif request.method == 'PUT':
        json_data = request.body
        bobj = io.BytesIO(json_data)
        data = JSONParser().parse(bobj)
        id = data.get('id')
        emp = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(emp, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'updated'})
        return Response({'msg':'send valid data'})

    elif request.method == 'DELETE':
        json_data = request.body
        bobj = io.BytesIO(json_data)
        data = JSONParser().parse(bobj)
        id = data.get('id')
        emp = Employee.objects.get(id=id)
        emp.delete()
        return Response({'msg':'deleted'})


