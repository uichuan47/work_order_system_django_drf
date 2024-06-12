from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from api import models
import uuid


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserInfo
        fields = "__all__"


class UserInfoView(APIView):
    def get(self, request):
        token = request.query_params.get('token')
        user_obj = models.UserInfo.objects.get(token=token)
        ser = UserInfoSerializer(instance=user_obj)

        return Response({"code": 100, "data": ser.data})


class ChargeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True)
    balance = serializers.IntegerField(read_only=True)
    # class Meta:
    #     model = models.UserInfo
    #     fields = ["id", "username", "balance"]


class ChargeInfoView(APIView):
    def post(self, request):
        # user_id = request.data.get("user_id")
        money = request.data.get('money')
        token = request.query_params.get('token')
        print(money)
        print(token)
        user_obj = models.UserInfo.objects.get(token=token)
        print(user_obj.username)
        user_obj.balance += money
        user_obj.save()
        ser = ChargeSerializer(user_obj)
        return Response({"code": 100, "data": ser.data})
