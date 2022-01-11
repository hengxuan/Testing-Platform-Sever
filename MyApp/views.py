import hashlib

from django.contrib import auth
from django.shortcuts import render
from MyApp.serializers import *
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_jwt.serializers import jwt_decode_handler,jwt_get_username_from_payload,jwt_payload_handler,jwt_encode_handler
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.hashers import check_password,make_password
# Create your views here.

class Api_register(APIView):
    def post(self,request):
        serializer = UserSerializers(data=request.data)
        username = request.data["username"]
        password = request.data["password"]
        if serializer.is_valid():
            # user = User.objects.create_user(username,password)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Api_login(APIView):
    def post(self, request):
        msg = {'code': status.HTTP_200_OK, 'message': '操作成功', 'data': ''}

        username = request.data.get('username')
        password = request.data.get('password')
        if User.objects.get(username=username):
            password_re = UserSerializers(User.objects.get(username=username)).data["password"]
            if password == password_re:
                return Response(msg)
            else:
                msg['code'] = status.HTTP_400_BAD_REQUEST
                msg['message'] = '账号或密码错误'
            return Response(msg)
        else:
            msg['message'] = '用户不存在'
            return Response(msg)


        # user_obj = auth.authenticate(username=username, password=password)
        # if user_obj:
        #     payload = jwt_payload_handler(user_obj)
        #     token = jwt_encode_handler(payload)
        #     user_data = {'username': user_obj.username, 'token': token, }
        #     msg['data'] = user_data
        # else:
        #     msg['code'] = status.HTTP_400_BAD_REQUEST
        #     msg['message'] = '账号或密码错误'
        # return Response(msg)

