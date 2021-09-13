from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User 
from .serializers import UserSerializer
import io
from rest_framework.response import Response

# Create your views here.


class UserCBV(APIView):
    def get(self,request,*args,**kwargs):
        json_data = request.body
        bobj = io.BytesIO(json_data)
        data = JSONParser().parse(bobj)
        id = data.get('id')
        if id is not None:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        qs = User.objects.all()
        serializer = UserSerializer(qs,many=True)
        return Response(serializer.data)

    # def post(self, request, *args, **kwargs):
    #     json_data = request.body
    #     bobj = io.BytesIO(json_data)
    #     data = JSONParser().parse(bobj)
    #     serializer = UserSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)

    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            result = serializer.save()
            return Response({
                result:{result.is_staff}
            })
        return Response(serializer.errors) 

    def put(self, request, *args, **kwargs):
        json_data = request.body
        bobj = io.BytesIO(json_data)
        data = JSONParser().parse(bobj)
        id = data.get('id')
        if id:
            user =User.objects.get(id=id)
            serializer =UserSerializer(user, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        bobj = io.BytesIO(json_data)
        data = JSONParser().parse(bobj)
        id = data.get('id')
        if id:
            try:
                user = User.objects.get(id=id)
                user.delete()
                return Response({'msg':'Resource deleted successfully'})
            except Employee.DoesNotExist:
                return Response({'msg':'record not found'})
        return Response({'msg':'plzz provide the id'})
