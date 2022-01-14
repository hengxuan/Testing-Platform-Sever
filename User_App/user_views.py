import hashlib

from django.contrib import auth
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.settings import api_settings
from User_App.user_serializers import *
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class Api_register(APIView):
    def post(self,request):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Api_login(APIView):
    def post(self, request):
        msg = {'code': status.HTTP_200_OK, 'message': '操作成功', 'data': ''}
        username = request.data.get('username')
        password = request.data.get('password')
        user_obj = auth.authenticate(username=username, password=password)
        if user_obj:
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user_obj)
            token = jwt_encode_handler(payload)
            user_data = {'username': user_obj.username, 'token': token, }
            msg['data'] = user_data
        else:
            msg['code'] = status.HTTP_400_BAD_REQUEST
            msg['message'] = '账号或密码错误'
        return Response(msg)

class Api_resetpassword(APIView):
    def post(self,request):
        msg = {'code': status.HTTP_200_OK, 'message': '密码修改成功', 'data': ''}
        try:
            user = User.objects.get(username=request.data["username"])
            serializer = UserSerializers(instance=user,data=request.data)
            if  serializer.is_valid():
                serializer.save()
                msg['data'] = serializer.data
                return Response(msg)
            else:
                msg['data'] = serializer.errors
                msg['code'] = status.HTTP_400_BAD_REQUEST
                msg['message'] = ''
                return Response(msg)
        except:
            msg['code'] = status.HTTP_400_BAD_REQUEST
            msg['message'] = '用户不存在'
            return Response(msg)

class Api_del(APIView):
    def post(self,request):
        msg = {'code': status.HTTP_200_OK, 'message': '注销成功', 'data': ''}
        username = request.data.get("username")
        pasword = request.data.get("password")
        user = auth.authenticate(username=username,pasword=pasword)
        if user:
            User.objects.get(username=username).delete()
            return Response(msg)
        else:
            msg['message'] = '用户名或密码错误'
            msg['code'] = status.HTTP_400_BAD_REQUEST
            return Response(msg)



class Api_test(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        return Response({"test":"test"})

