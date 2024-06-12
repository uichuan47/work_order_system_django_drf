# from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from api import models
import uuid


class AuthSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)
    phone = serializers.CharField(required=True)

    def validate_confirm_password(self, value):
        password = self.initial_data.get('password')
        if password != value:
            raise exceptions.ValidationError("密码不一致")
        return value


class AuthView(APIView):
    authentication_classes = []

    def post(self, request):
        # username = request.data.get('username')
        # password =request.data.get('password')

        ser = AuthSerializer(data=request.data)
        if not ser.is_valid():
            return Response({"code": 400, "msg": "fail", "detail": ser.errors})

        user_object = models.UserInfo.objects.filter(**ser.data).first()
        if not user_object:
            return Response({"code": 401, "msg": "fail", "detail": "not exists in database"})
        token = str(uuid.uuid4())
        user_object.token = token
        user_object.save()

        return Response({
            "code": 0,
            "status": "success",
            "data": {
                "id": user_object.id,
                "name": user_object.username,
                "token": user_object.token
            }
        })


class RegisterView(APIView):
    authentication_classes = []

    def post(self, request):
        ser = RegisterSerializer(data=request.data)
        if not ser.is_valid():
            return Response({"code": 401, "msg": "fail", "detail": ser.errors})
        ser.validated_data.pop('confirm_password')
        user_obj = models.UserInfo.objects.create(**ser.validated_data)
        user_obj.save()
        print(ser.validated_data)
        return Response({
            "code": 0,
            "status": "success",
            "data": ser.validated_data
        })


class DemoSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class DemoView(APIView):

    def get(self, request):
        return Response({"code": 1, "detail": "test"})

    def post(self, request):
        ser = DemoSerializer(data=request.data)
        if not ser.is_valid():
            return Response({"code": 401, "msg": "fail", "detail": ser.errors})

        return Response({"code": 1, "detail": "test"})

