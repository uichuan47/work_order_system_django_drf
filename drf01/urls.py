"""
URL configuration for drf01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import account, userinfo, data, order

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', account.AuthView.as_view()),
    path('api/register/', account.RegisterView.as_view()),
    path('api/demo/', account.DemoView.as_view()),
    path('api/userinfo/', userinfo.UserInfoView.as_view()),
    path('api/charge/', userinfo.ChargeInfoView.as_view()),
    path('api/order_list/', order.OrderView.as_view()),
    path('api/order_purchase/', order.OrderPurchaseView.as_view()),
    path('api/file_download/', data.FileDownloadView.as_view()),
    path('api/get_data/', data.DataView.as_view()),
]
