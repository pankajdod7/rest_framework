from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
import io
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class StudentDetails(APIView):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        bobj = io.BytesIO(json_data)
        data = JSONParser().parse(bobj)
        id = data.get('id')
        if id is not None:
            try:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Student.DoesNotExist:
                return Response({'msg':'record not found'}, status=status.HTTP_404_NOT_FOUND)
        stu_qs = Student.objects.all()
        serializer = StudentSerializer(stu_qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        json_data = request.body
        bobj = io.BytesIO(json_data)
        data = JSONParser().parse(bobj)
        print(data)
        if data:
            serializer = StudentSerializer(data=data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Resource created successfully'}, status=status.HTTP_201_CREATED)
        return Response({'msg':'plzz send data'}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        json_data = request.body
        bobj = io.BytesIO(json_data)
        data = JSONParser().parse(bobj)
        id = data.get('id')
        try:
            stu = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({'msg':'perticular record does not found'})
        serializer = StudentSerializer(stu, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Resource updated sucessfully'}, status=status.HTTP_205_RESET_CONTENT)
        return Response({'msg':'plzzz send the valid data'})

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        bobj = io.BytesIO(json_data)
        data = JSONParser().parse(bobj)
        id = data.get('id')
        if id is not None:
            try:
                stu = Student.objects.get(id=id)
            except Student.DoesNotExist:
                return Response({'msg':'record not found'}, status=status.HTTP_404_NOT_FOUND)
            stu.delete()
            return Response({'msg':'Resource deleted succesfully'}, status=status.HTTP_200_OK)
        return Response({'msg':'plzz send the id'})





