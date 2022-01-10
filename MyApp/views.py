from django.shortcuts import render
from MyApp.serializers import *
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class Api_register(APIView):
    def post(self,request):
        serializer = UserSerializers(data=request.data)
        print(serializer,type(serializer))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
