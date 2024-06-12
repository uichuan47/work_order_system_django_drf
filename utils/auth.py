from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from api import models


class MyAuthenticationFailed(AuthenticationFailed):
    status_code = status.HTTP_200_OK

class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token')
        if not token:
            raise MyAuthenticationFailed({"code":-1,"detail":"token is required"})
        user_obj = models.UserInfo.objects.filter(token=token).first()
        if not user_obj:
            raise MyAuthenticationFailed({"code":-2,"detail":"user not exist"})
        return user_obj, token

    def authenticate_header(self, request):
        return 'Token'
