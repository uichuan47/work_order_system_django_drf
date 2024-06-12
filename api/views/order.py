from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from api import models
from utils.order_number import generate_order_number
import os
import json

class OrderSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='get_category_display', read_only=True)
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M', required=False, read_only=True)
    user_name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = models.Order
        fields = '__all__'


class OrderView(APIView):
    def get(self, request):
        token = request.query_params.get('token')
        user_obj = models.UserInfo.objects.get(token=token)
        uid = user_obj.id
        order_obj = models.Order.objects.filter(user_id=uid)
        ser = OrderSerializer(instance=order_obj, many=True)
        return Response({"code": 200, "data": ser.data})

    def post(self, request):
        token = request.query_params.get('token')
        user_obj = models.UserInfo.objects.get(token=token)
        ser = OrderSerializer(data=request.data)
        if not ser.is_valid():
            return Response({"code": -1, "error": ser.errors})
        ser.save(user_id=user_obj.id)
        return Response({"code": 0, "data": ser.data})


class OrderPurchaseSerializer(serializers.ModelSerializer):
    OrderNumber = serializers.CharField(required=False)
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M', required=False, read_only=True)
    cost = serializers.IntegerField(required=True)
    item_number = serializers.IntegerField(required=True)
    weibo_id = serializers.CharField(required=True)

    class Meta:
        model = models.Order
        fields = ['item_number', 'weibo_id', 'cost', 'create_time', 'OrderNumber']


class OrderPurchaseView(APIView):
    def post(self, request):
        token = request.query_params.get('token')
        user_obj = models.UserInfo.objects.get(token=token)
        ser = OrderPurchaseSerializer(data=request.data)
        ser.is_valid()
        od_number = generate_order_number()
        ser.save(user_id=user_obj.id, OrderNumber=str(od_number))
        cost = int(request.data.get("cost"))
        balance = user_obj.balance - cost
        user_obj.balance -= cost
        user_obj.save()
        weibo_id = request.data.get("weibo_id")
        item_number = request.data.get("item_number")

        with open('/Users/kento/Documents/graduation/project/django_codes/drf01/config.json', 'r') as file:
            data = json.load(file)

        # 修改"user_id_list"字段
        data["user_id_list"] = [weibo_id]
        data['since_date'] = int(item_number)
        # 保存修改后的JSON文件
        with open('/Users/kento/Documents/graduation/project/django_codes/drf01/config.json', 'w') as file:
            json.dump(data, file, indent=2)
        os.system("python3 -m weibo_spider")
        return Response({"code": 200, "balance": balance, "data": ser.data})
