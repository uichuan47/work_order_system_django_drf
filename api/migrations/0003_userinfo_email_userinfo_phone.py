# Generated by Django 5.0.4 on 2024-04-17 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_userinfo_create_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(blank=True, max_length=64, null=True, verbose_name='邮件'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='phone',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='电话'),
        ),
    ]
