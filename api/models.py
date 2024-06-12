from django.db import models


# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    token = models.CharField(verbose_name="token", max_length=64, null=True, blank=True)
    email = models.EmailField(verbose_name="邮件", max_length=64, null=True, blank=True)
    phone = models.CharField(verbose_name="电话", max_length=32, null=True, blank=True)
    balance = models.IntegerField(verbose_name="余额", null=True, blank=True,default=0)


class Order(models.Model):
    user = models.ForeignKey(verbose_name="用户", to="UserInfo", on_delete=models.CASCADE)
    category_choices = ((1, "微博数据"), (2, "微博媒体"), (3, "微博新闻"))
    category = models.IntegerField(verbose_name="分类", choices=category_choices, default=1)
    OrderNumber = models.CharField(verbose_name="订单号", max_length=32)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    cost = models.IntegerField(verbose_name="订单费用", null=True, blank=True)
    item_number = models.CharField(verbose_name="采集数量", null=True, blank=True, max_length=32)
    weibo_id = models.CharField(verbose_name="微博id", max_length=64, null=True, blank=True)
