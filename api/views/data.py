from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from rest_framework import serializers
from api import models
from utils.order_number import generate_order_number

import json


class FileDownloadView(APIView):
    def get(self, request):
        weibo_id = request.query_params.get('OrderNumber')
        file_path = '/Users/kento/Documents/graduation/project/django_codes/drf01/weibo/{}/{}.csv'.format(weibo_id,
                                                                                                            weibo_id)
        print(file_path)
        try:
            with open(file_path, 'rb') as file:
                response = HttpResponse(FileWrapper(file), content_type='application/octet-stream')
                response['Content-Disposition'] = 'attachment; filename="file.csv"'  # 设置下载文件的文件名
                return response
        except FileNotFoundError:
            return Response(status=404)


class DataView(APIView):
    def post(self, request):
        OrderNumber = request.data.get("OrderNumber")
        file_path = '/Users/kento/Documents/graduation/project/django_codes/drf01/weibo/{}/{}.json'.format(OrderNumber,
                                                                                                           OrderNumber)
        with open(file_path, 'r') as file:
            json_data = json.loads(file.read())
        print(json_data)
        return Response({"code": 100, "data": json_data.get("weibo")})
