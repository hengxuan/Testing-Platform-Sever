import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Api_action(APIView):
    def post(self,request):
        header = request.data['header']
        url = request.data['url']
        param = request.data['param']
        method = request.data['method']
        