import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Api_action(APIView):
    def post(self,request):
        header = request.data['header']
        print(header)
        url = request.data['url']
        param = request.data['param']
        method = request.data['method']
        if method == "get":
            res = requests.get(url=url,params=param,header=header)
            return Response(res)
        elif method == "post":
            res = requests.post(url=url,data=param)
            return  Response(res)
        elif method == "put":
            res = requests.put(url=url,data=param,header=header)
            return Response(res)
        else:
            res = requests.delete(url=url,header=header,data=param)
            return Response(res)
