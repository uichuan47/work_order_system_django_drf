# Generated by Django 5.0.4 on 2024-04-19 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_order_weibo_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='info',
            field=models.TextField(blank=True, default='null', null=True, verbose_name='备注信息'),
        ),
    ]