from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerizlizer
from rest_framework.response import Response
from .models import Student
from rest_framework import status
# Create your views here.

class TestViewSet(viewsets.ViewSet):

    def list(self, request):
        std = Student.objects.all()
        serializer = StudentSerizlizer(std, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = StudentSerizlizer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Student Register'})
        else:
            return Response(serializer.errors)

    def retrieve(self, request, pk):
        try:
            std = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerizlizer(std)
        return Response(serializer.data)


    def update(self,request,pk):
        std = Student.objects.get(pk=pk)
        serializer = StudentSerizlizer(std, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'update com[pleted'})
        else:
            return Response(serializer.errors)


    def destroy(self, request, pk):
        id=pk
        std = Student.objects.get(pk=id)
        std.delete()
        return Response({'msg':'Data deleted'})





