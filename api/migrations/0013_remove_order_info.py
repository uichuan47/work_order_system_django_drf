# Generated by Django 5.0.4 on 2024-04-19 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_order_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='info',
        ),
    ]